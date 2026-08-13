from __future__ import annotations

import os
import stat
from pathlib import Path

from reins.harness import paths


class BackupPathError(Exception):
    pass


def _contains(root: Path, candidate: Path) -> bool:
    try:
        _ = candidate.relative_to(root)
    except ValueError:
        return False
    return True


def _reject_symlink_components(path: Path) -> None:
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current /= part
        if current.exists() and current.is_symlink():
            raise BackupPathError(f"backup path contains symlink: {current}")


def validate_source_tree(source: Path) -> Path:
    expanded = source.expanduser().absolute()
    _reject_symlink_components(expanded)
    canonical = expanded.resolve(strict=True)
    allowed_roots = (Path.home().resolve(), paths.home().resolve())
    if not any(_contains(root, canonical) for root in allowed_roots):
        raise BackupPathError(f"backup source is outside home or harness: {source}")
    if canonical.is_symlink():
        raise BackupPathError(f"backup source is a symlink: {source}")
    if canonical.is_dir():
        for root, directories, filenames in os.walk(canonical, followlinks=False):
            for name in (*directories, *filenames):
                entry = Path(root, name)
                mode = entry.lstat().st_mode
                if stat.S_ISLNK(mode):
                    raise BackupPathError(f"backup source contains symlink: {entry}")
                if not stat.S_ISDIR(mode) and not stat.S_ISREG(mode):
                    raise BackupPathError(f"backup source contains special file: {entry}")
    elif not canonical.is_file():
        raise BackupPathError(f"backup source is not a regular file: {source}")
    return canonical


def validate_destination(destination: Path) -> Path:
    expanded = destination.expanduser().absolute()
    private_root = (Path.home() / ".cache/data_rein/backup").absolute()
    _reject_symlink_components(expanded)
    canonical = expanded.resolve(strict=False)
    canonical_root = private_root.resolve(strict=False)
    if not _contains(canonical_root, canonical):
        raise BackupPathError(f"backup destination is outside {private_root}: {destination}")
    return canonical


def create_private_directory(directory: Path) -> None:
    directory.mkdir(mode=0o700, parents=True, exist_ok=True)
    directory.chmod(0o700)
