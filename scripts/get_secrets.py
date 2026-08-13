from __future__ import annotations

import fcntl
import os
import secrets
import stat
import tempfile
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Final

from cryptography.fernet import Fernet, InvalidToken
from typing_extensions import override

_DEFAULT_CONFIG: Final = Path("/home/amdy/data_rein/config")
replace_file: Final = os.replace


@dataclass(frozen=True, slots=True)
class VaultPaths:
    key: Path = _DEFAULT_CONFIG / ".secrets.key"
    encrypted: Path = _DEFAULT_CONFIG / ".secrets.enc"


@dataclass(frozen=True, slots=True)
class VaultError(RuntimeError):
    message: str

    @override
    def __str__(self) -> str:
        return self.message


class VaultPermissionError(VaultError):
    pass


class VaultWriteError(VaultError):
    pass


def _validate_vault_file(path: Path) -> None:
    try:
        metadata = path.stat(follow_symlinks=False)
    except OSError as error:
        raise VaultError(message=f"encrypted secrets vault unavailable: {path.name}") from error
    if (
        not stat.S_ISREG(metadata.st_mode)
        or metadata.st_uid != os.getuid()
        or metadata.st_mode & 0o077
    ):
        raise VaultPermissionError(message=f"insecure encrypted vault permissions: {path.name}")


def _secret_value(plaintext: str, key_name: str) -> str | None:
    prefix = f"{key_name}="
    for line in plaintext.splitlines():
        if line.startswith(prefix):
            value = line.split("=", 1)[1].strip()
            if value.startswith('"') and value.endswith('"'):
                return value[1:-1]
            return value
    return None


def _upsert_secret(plaintext: str, key_name: str, value: str) -> str:
    prefix = f"{key_name}="
    lines = plaintext.splitlines()
    updated: list[str] = []
    replaced = False
    for line in lines:
        if line.startswith(prefix):
            if not replaced:
                updated.append(f"{prefix}{value}")
                replaced = True
        else:
            updated.append(line)
    if not replaced:
        updated.append(f"{prefix}{value}")
    return "\n".join(updated) + "\n"


def _decrypt(paths: VaultPaths) -> tuple[Fernet, str, bytes]:
    _validate_vault_file(paths.key)
    _validate_vault_file(paths.encrypted)
    try:
        cipher = Fernet(paths.key.read_bytes())
        ciphertext = paths.encrypted.read_bytes()
        plaintext = cipher.decrypt(ciphertext).decode("utf-8")
    except (InvalidToken, UnicodeDecodeError, ValueError, OSError) as error:
        raise VaultError(message="encrypted secrets vault could not be decrypted") from error
    return cipher, plaintext, ciphertext


def _atomic_replace(target: Path, ciphertext: bytes) -> None:
    descriptor = -1
    temporary_path: Path | None = None
    try:
        descriptor, raw_path = tempfile.mkstemp(
            prefix=f".{target.name}.",
            dir=target.parent,
        )
        temporary_path = Path(raw_path)
        os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "wb", closefd=True) as destination:
            descriptor = -1
            _ = destination.write(ciphertext)
            destination.flush()
            os.fsync(destination.fileno())
        replace_file(temporary_path, target)
        temporary_path = None
        directory = os.open(target.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except OSError as error:
        raise VaultWriteError(message="atomic vault replacement failed") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError as error:
                raise VaultWriteError(message="temporary vault cleanup failed") from error


def _replace_vault(paths: VaultPaths, ciphertext: bytes, previous: bytes) -> None:
    backup = paths.encrypted.with_name(f"{paths.encrypted.name}.bak")
    _atomic_replace(backup, previous)
    try:
        _atomic_replace(paths.encrypted, ciphertext)
    except VaultWriteError as update_error:
        try:
            _atomic_replace(paths.encrypted, previous)
        except VaultWriteError as rollback_error:
            raise VaultWriteError(
                message="encrypted vault update failed and rollback failed; encrypted backup retained"
            ) from rollback_error
        raise VaultWriteError(
            message="encrypted vault update failed; previous ciphertext restored"
        ) from update_error


def get_secret(key_name: str, *, paths: VaultPaths | None = None) -> str | None:
    paths = paths or VaultPaths()
    _validate_vault_file(paths.key)
    try:
        with paths.key.open("rb") as lock_file:
            fcntl.flock(lock_file, fcntl.LOCK_SH)
            _, plaintext, _ = _decrypt(paths)
    except OSError as error:
        raise VaultError(message="encrypted secrets vault could not be read") from error
    return _secret_value(plaintext, key_name)


def get_or_create_secret(
    key_name: str,
    *,
    paths: VaultPaths | None = None,
    generator: Callable[[], str] | None = None,
) -> str:
    paths = paths or VaultPaths()
    generator = generator or _generate_token
    _validate_vault_file(paths.key)
    try:
        with paths.key.open("rb") as lock_file:
            fcntl.flock(lock_file, fcntl.LOCK_EX)
            cipher, plaintext, previous = _decrypt(paths)
            existing = _secret_value(plaintext, key_name)
            if existing:
                return existing
            generated = generator()
            if not generated:
                raise VaultWriteError(message="generated vault secret was empty")
            updated = _upsert_secret(plaintext, key_name, generated)
            _replace_vault(paths, cipher.encrypt(updated.encode("utf-8")), previous)
            return generated
    except VaultError:
        raise
    except OSError as error:
        raise VaultWriteError(message="encrypted secrets vault update failed") from error


def _generate_token() -> str:
    return secrets.token_urlsafe(32)
