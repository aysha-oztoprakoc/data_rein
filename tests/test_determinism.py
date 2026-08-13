from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def test_environment_declarations_and_locks_are_current() -> None:
    # Given the repository is expected to reproduce its Python and system toolchains.
    required_files = ("pyproject.toml", "uv.lock", "flake.nix", "flake.lock")

    # When the declared lock artifacts are inspected.
    missing = [name for name in required_files if not (REPOSITORY_ROOT / name).is_file()]

    # Then every declaration is present and the Python lock matches the project metadata.
    assert missing == []
    uv = shutil.which("uv")
    assert uv is not None, "uv must be available in the development environment"
    result = subprocess.run(
        [uv, "lock", "--check", "--offline"],
        cwd=REPOSITORY_ROOT,
        capture_output=True,
        check=False,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stderr


def test_nix_shell_uses_the_working_checkout_as_data_rein_home(tmp_path: Path) -> None:
    # Given an isolated flake source that cannot absorb runtime model directories.
    nix = shutil.which("nix")
    if nix is None:
        pytest.skip("Nix is not available")
    flake_source = tmp_path / "flake-source"
    flake_source.mkdir()
    for name in ("flake.nix", "flake.lock"):
        shutil.copy2(REPOSITORY_ROOT / name, flake_source / name)

    # When the locked development shell is activated from the working checkout.
    result = subprocess.run(
        [
            nix,
            "--extra-experimental-features",
            "nix-command flakes",
            "develop",
            f"path:{flake_source}",
            "--command",
            "bash",
            "-c",
            'printf "%s" "$DATA_REIN_HOME"',
        ],
        cwd=REPOSITORY_ROOT / "tests",
        capture_output=True,
        check=False,
        text=True,
        timeout=120,
    )

    # Then tools resolve the mutable canonical checkout rather than a Nix-store snapshot.
    assert result.returncode == 0, result.stderr
    assert result.stdout == str(REPOSITORY_ROOT)
