from __future__ import annotations

import os
import re
import secrets
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Final

from reins.harness import paths

MAX_RAW_MEMORY_BYTES: Final = 1_048_576
PRIVATE_DIRECTORY_MODE: Final = stat.S_IRWXU
_MEMORY_ID_PATTERN: Final = re.compile(r"^[A-Za-z0-9_-]{22}$")


@dataclass(frozen=True, slots=True)
class MemoryReference:
    identifier: str


@dataclass(frozen=True, slots=True)
class InvalidMemoryReference(ValueError):
    identifier: str

    def __str__(self) -> str:
        return "invalid raw-memory reference"


@dataclass(frozen=True, slots=True)
class MemoryPayloadTooLargeError(ValueError):
    size_bytes: int
    limit_bytes: int

    def __str__(self) -> str:
        return f"raw memory payload exceeds {self.limit_bytes} byte limit"


@dataclass(frozen=True, slots=True)
class MemoryStorageError(RuntimeError):
    path: Path

    def __str__(self) -> str:
        return "raw-memory storage is not a private directory"


class TencentSymbolicMemory:
    def __init__(self, storage_root: Path | None = None) -> None:
        configured_root = storage_root or (paths.state_dir() / "memories" / "raw_logs")
        configured_root.mkdir(mode=0o700, parents=True, exist_ok=True)
        if configured_root.is_symlink():
            raise MemoryStorageError(path=configured_root)
        self._storage_root = configured_root.resolve(strict=True)
        os.chmod(self._storage_root, PRIVATE_DIRECTORY_MODE)

    def offload_large_memory(self, raw_content: str) -> MemoryReference:
        payload = raw_content.encode("utf-8")
        if len(payload) > MAX_RAW_MEMORY_BYTES:
            raise MemoryPayloadTooLargeError(
                size_bytes=len(payload), limit_bytes=MAX_RAW_MEMORY_BYTES
            )
        reference = MemoryReference(identifier=secrets.token_urlsafe(16))
        path = self._path_for(reference.identifier)
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(descriptor, "wb") as raw_file:
            raw_file.write(payload)
        return reference

    def retrieve_raw_memory(self, reference: MemoryReference | str) -> str:
        identifier = reference.identifier if isinstance(reference, MemoryReference) else reference
        path = self._path_for(identifier)
        try:
            return path.read_text(encoding="utf-8")
        except FileNotFoundError as error:
            raise FileNotFoundError("raw memory reference was not found") from error

    def _path_for(self, identifier: str) -> Path:
        if _MEMORY_ID_PATTERN.fullmatch(identifier) is None:
            raise InvalidMemoryReference(identifier=identifier)
        candidate = (self._storage_root / f"{identifier}.log").resolve()
        if candidate.parent != self._storage_root:
            raise InvalidMemoryReference(identifier=identifier)
        return candidate
