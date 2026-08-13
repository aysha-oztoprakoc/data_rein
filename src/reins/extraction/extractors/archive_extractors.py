from __future__ import annotations

import stat
import zipfile
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import ClassVar, Final
from subprocess import TimeoutExpired
from typing_extensions import override

from reins.extraction.extractors.base import BaseExtractor, ExtractionResult
from reins.extraction.registry import registry
from reins.extraction.serialization import save_as_xml
from reins.harness import external_io
from reins.services.logger import log_degradation

MAX_ARCHIVE_MEMBERS: Final = 512
MAX_MEMBER_BYTES: Final = 8 * 1024 * 1024
MAX_TOTAL_UNCOMPRESSED_BYTES: Final = 64 * 1024 * 1024
MAX_TEXT_BYTES: Final = 16 * 1024 * 1024
READ_CHUNK_BYTES: Final = 64 * 1024
SEVEN_ZIP_TIMEOUT_SECONDS: Final = 30
TEXT_EXTENSIONS: Final = frozenset({".txt", ".md", ".json", ".xml", ".csv", ".html"})


class ArchiveSecurityError(Exception):
    pass


@dataclass(frozen=True, slots=True)
class ArchiveMember:
    name: str
    size: int
    is_directory: bool = False


def _validate_member_names(members: list[ArchiveMember]) -> list[ArchiveMember]:
    if len(members) > MAX_ARCHIVE_MEMBERS:
        raise ArchiveSecurityError("archive member limit exceeded")
    approved: list[ArchiveMember] = []
    seen: set[str] = set()
    total = 0
    file_names: set[str] = set()
    directory_names: set[str] = set()
    for member in members:
        name = member.name.replace("\\", "/")
        path = PurePosixPath(name)
        has_drive_prefix = bool(path.parts) and path.parts[0].endswith(":")
        if (
            "\x00" in name
            or path.is_absolute()
            or ".." in path.parts
            or has_drive_prefix
            or not name
        ):
            raise ArchiveSecurityError(f"unsafe archive member path: {member.name}")
        normalized = path.as_posix().rstrip("/")
        folded = normalized.casefold()
        if folded in seen:
            raise ArchiveSecurityError(f"duplicate archive member: {member.name}")
        seen.add(folded)
        if member.is_directory:
            directory_names.add(folded)
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            raise ArchiveSecurityError(f"non-text archive member: {member.name}")
        if member.size < 0 or member.size > MAX_MEMBER_BYTES:
            raise ArchiveSecurityError(f"archive member size limit exceeded: {member.name}")
        total += member.size
        if total > MAX_TOTAL_UNCOMPRESSED_BYTES:
            raise ArchiveSecurityError("archive aggregate size limit exceeded")
        file_names.add(folded)
        approved.append(ArchiveMember(normalized, member.size))
    for filename in file_names:
        parts = PurePosixPath(filename).parts
        parents = {PurePosixPath(*parts[:index]).as_posix() for index in range(1, len(parts))}
        if filename in directory_names or parents & file_names:
            raise ArchiveSecurityError(f"archive file/directory conflict: {filename}")
    return approved


def _zip_members(handle: zipfile.ZipFile) -> list[ArchiveMember]:
    members: list[ArchiveMember] = []
    for info in handle.infolist():
        mode = info.external_attr >> 16
        kind = stat.S_IFMT(mode)
        if kind == stat.S_IFLNK:
            raise ArchiveSecurityError(f"archive link rejected: {info.filename}")
        if kind not in {0, stat.S_IFREG, stat.S_IFDIR}:
            raise ArchiveSecurityError(f"archive special file rejected: {info.filename}")
        if info.flag_bits & 0x1:
            raise ArchiveSecurityError(f"encrypted archive member rejected: {info.filename}")
        members.append(ArchiveMember(info.filename, info.file_size, info.is_dir()))
    return _validate_member_names(members)


def _bounded_zip_text(handle: zipfile.ZipFile, members: list[ArchiveMember]) -> str:
    output = bytearray()
    for member in members:
        header = f"\n--- {member.name} ---\n".encode()
        if len(output) + len(header) > MAX_TEXT_BYTES:
            raise ArchiveSecurityError("archive text output limit exceeded")
        output.extend(header)
        read_bytes = 0
        with handle.open(member.name) as stream:
            while chunk := stream.read(min(READ_CHUNK_BYTES, member.size - read_bytes + 1)):
                read_bytes += len(chunk)
                if read_bytes > member.size or len(output) + len(chunk) > MAX_TEXT_BYTES:
                    raise ArchiveSecurityError("archive text output limit exceeded")
                output.extend(chunk)
        if read_bytes != member.size:
            raise ArchiveSecurityError(f"archive member size mismatch: {member.name}")
    return output.decode("utf-8", errors="replace")


def _parse_7z_listing(listing: str) -> list[ArchiveMember]:
    members: list[ArchiveMember] = []
    for block in listing.split("\n\n"):
        fields: dict[str, str] = {}
        for line in block.splitlines():
            key, separator, value = line.partition(" = ")
            if separator:
                fields[key] = value
        name = fields.get("Path")
        if name is None:
            continue
        if fields.get("Symbolic Link") or fields.get("Hard Link"):
            raise ArchiveSecurityError(f"archive link rejected: {name}")
        if fields.get("Encrypted") == "+" or fields.get("Anti") == "+":
            raise ArchiveSecurityError(f"unsupported archive member: {name}")
        mode_text = fields.get("Mode")
        if mode_text is not None:
            try:
                kind = stat.S_IFMT(int(mode_text, 8))
            except ValueError as error:
                raise ArchiveSecurityError(f"invalid archive member mode: {name}") from error
            if kind not in {0, stat.S_IFREG, stat.S_IFDIR}:
                raise ArchiveSecurityError(f"archive special file rejected: {name}")
        is_directory = fields.get("Folder") == "+" or fields.get("Attributes", "").startswith("D")
        try:
            size = int(fields.get("Size", "0"))
        except ValueError as error:
            raise ArchiveSecurityError(f"invalid archive member size: {name}") from error
        members.append(ArchiveMember(name, size, is_directory))
    return _validate_member_names(members)


def _seven_zip_members(filepath: str) -> list[ArchiveMember]:
    result = external_io.run(
        ["7z", "l", "-slt", "-ba", "--", filepath],
        capture_output=True,
        text=True,
        timeout=SEVEN_ZIP_TIMEOUT_SECONDS,
    )
    if result.returncode != 0:
        raise ArchiveSecurityError(f"7z preflight failed: {result.stderr.strip()}")
    return _parse_7z_listing(result.stdout)


def _seven_zip_text(filepath: str, members: list[ArchiveMember]) -> str:
    output = bytearray()
    for member in members:
        result = external_io.run(
            ["7z", "x", "-so", "--", filepath, member.name],
            capture_output=True,
            timeout=SEVEN_ZIP_TIMEOUT_SECONDS,
        )
        if result.returncode != 0:
            raise ArchiveSecurityError(f"7z member extraction failed: {member.name}")
        payload = result.stdout
        header = f"\n--- {member.name} ---\n".encode()
        if (
            len(payload) != member.size
            or len(output) + len(header) + len(payload) > MAX_TEXT_BYTES
        ):
            raise ArchiveSecurityError(f"7z member size limit violated: {member.name}")
        output.extend(header)
        output.extend(payload)
    return output.decode("utf-8", errors="replace")


class ZIPExtractor(BaseExtractor):
    SUPPORTED_FORMATS: ClassVar[list[str]] = [".zip"]
    NODE: ClassVar[str] = "amdy"

    @override
    def extract(self, filepath: str, output_dir: str) -> ExtractionResult:
        try:
            with zipfile.ZipFile(filepath, "r") as handle:
                text = _bounded_zip_text(handle, _zip_members(handle))
            output = save_as_xml(text, filepath, output_dir)
            return {"status": "success", "output_path": output, "metadata": {"format": "zip"}}
        except (ArchiveSecurityError, OSError, zipfile.BadZipFile, RuntimeError) as error:
            log_degradation(__name__)
            return {"status": "error", "error": str(error)}


class RARExtractor(BaseExtractor):
    SUPPORTED_FORMATS: ClassVar[list[str]] = [".rar"]
    NODE: ClassVar[str] = "amdy"

    @override
    def extract(self, filepath: str, output_dir: str) -> ExtractionResult:
        try:
            members = _seven_zip_members(filepath)
            output = save_as_xml(_seven_zip_text(filepath, members), filepath, output_dir)
            return {"status": "success", "output_path": output, "metadata": {"format": "rar"}}
        except (ArchiveSecurityError, OSError, TimeoutExpired) as error:
            log_degradation(__name__)
            return {"status": "error", "error": str(error)}


registry.register(ZIPExtractor)
registry.register(RARExtractor)
