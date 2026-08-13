from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest
from cryptography.fernet import Fernet

sys.path.insert(0, str(Path(__file__).parents[1]))
from scripts import get_secrets  # noqa: E402


def _isolated_vault(tmp_path: Path, plaintext: str) -> get_secrets.VaultPaths:
    paths = get_secrets.VaultPaths(
        key=tmp_path / ".secrets.key",
        encrypted=tmp_path / ".secrets.enc",
    )
    key = Fernet.generate_key()
    _ = paths.key.write_bytes(key)
    _ = paths.key.chmod(0o400)
    _ = paths.encrypted.write_bytes(Fernet(key).encrypt(plaintext.encode()))
    _ = paths.encrypted.chmod(0o600)
    return paths


def test_http_token_is_provisioned_atomically_without_plaintext_artifact(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    # Given
    paths = _isolated_vault(tmp_path, "EXISTING=value\n")

    # When
    token = get_secrets.get_or_create_secret(
        "REINS_MCP_HTTP_TOKEN",
        paths=paths,
        generator=lambda: "isolated-generated-token",
    )

    # Then
    decrypted = Fernet(paths.key.read_bytes()).decrypt(paths.encrypted.read_bytes()).decode()
    assert token == "isolated-generated-token"
    assert "REINS_MCP_HTTP_TOKEN=isolated-generated-token" in decrypted.splitlines()
    assert paths.encrypted.stat().st_mode & 0o777 == 0o600
    assert {path.name for path in tmp_path.iterdir()} == {
        paths.key.name,
        paths.encrypted.name,
        f"{paths.encrypted.name}.bak",
    }
    captured = capsys.readouterr()
    assert "isolated-generated-token" not in captured.out + captured.err


def test_existing_http_token_is_returned_without_rewrite(tmp_path: Path) -> None:
    # Given
    paths = _isolated_vault(tmp_path, "REINS_MCP_HTTP_TOKEN=existing-token\n")
    ciphertext = paths.encrypted.read_bytes()

    def unexpected_generation() -> str:
        raise AssertionError("existing token was regenerated")

    # When
    token = get_secrets.get_or_create_secret(
        "REINS_MCP_HTTP_TOKEN",
        paths=paths,
        generator=unexpected_generation,
    )

    # Then
    assert token == "existing-token"
    assert paths.encrypted.read_bytes() == ciphertext


def test_empty_http_token_entry_is_replaced_exactly_once(tmp_path: Path) -> None:
    # Given
    paths = _isolated_vault(tmp_path, "REINS_MCP_HTTP_TOKEN=\nEXISTING=value\n")

    # When
    token = get_secrets.get_or_create_secret(
        "REINS_MCP_HTTP_TOKEN",
        paths=paths,
        generator=lambda: "isolated-generated-token",
    )

    # Then
    decrypted = Fernet(paths.key.read_bytes()).decrypt(paths.encrypted.read_bytes()).decode()
    token_lines = [
        line for line in decrypted.splitlines() if line.startswith("REINS_MCP_HTTP_TOKEN=")
    ]
    assert token == "isolated-generated-token"
    assert token_lines == ["REINS_MCP_HTTP_TOKEN=isolated-generated-token"]


def test_http_token_provision_failure_preserves_ciphertext(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given
    paths = _isolated_vault(tmp_path, "EXISTING=value\n")
    ciphertext = paths.encrypted.read_bytes()

    def reject_replace(
        _source: str | bytes | os.PathLike[str],
        _target: str | bytes | os.PathLike[str],
    ) -> None:
        raise OSError("replace refused")

    monkeypatch.setattr(get_secrets, "replace_file", reject_replace)

    # When / Then
    with pytest.raises(get_secrets.VaultWriteError, match="atomic vault replacement failed"):
        _ = get_secrets.get_or_create_secret(
            "REINS_MCP_HTTP_TOKEN",
            paths=paths,
            generator=lambda: "isolated-generated-token",
        )
    assert paths.encrypted.read_bytes() == ciphertext
    assert {path.name for path in tmp_path.iterdir()} == {paths.key.name, paths.encrypted.name}


def test_http_token_provision_rejects_insecure_permissions(tmp_path: Path) -> None:
    # Given
    paths = _isolated_vault(tmp_path, "EXISTING=value\n")
    paths.encrypted.chmod(0o644)
    ciphertext = paths.encrypted.read_bytes()

    # When / Then
    with pytest.raises(get_secrets.VaultPermissionError):
        _ = get_secrets.get_or_create_secret(
            "REINS_MCP_HTTP_TOKEN",
            paths=paths,
            generator=lambda: "isolated-generated-token",
        )
    assert paths.encrypted.read_bytes() == ciphertext


def test_http_token_provision_fails_closed_when_vault_is_missing(tmp_path: Path) -> None:
    # Given
    paths = get_secrets.VaultPaths(
        key=tmp_path / ".secrets.key",
        encrypted=tmp_path / ".secrets.enc",
    )

    # When / Then
    with pytest.raises(get_secrets.VaultError, match="unavailable"):
        _ = get_secrets.get_or_create_secret("REINS_MCP_HTTP_TOKEN", paths=paths)
    assert tuple(tmp_path.iterdir()) == ()


def test_http_token_provision_decrypt_failure_preserves_vault(tmp_path: Path) -> None:
    # Given
    paths = _isolated_vault(tmp_path, "EXISTING=value\n")
    _ = paths.encrypted.write_bytes(b"invalid-ciphertext")
    ciphertext = paths.encrypted.read_bytes()

    # When / Then
    with pytest.raises(get_secrets.VaultError, match="decrypted"):
        _ = get_secrets.get_or_create_secret("REINS_MCP_HTTP_TOKEN", paths=paths)
    assert paths.encrypted.read_bytes() == ciphertext
    assert {path.name for path in tmp_path.iterdir()} == {paths.key.name, paths.encrypted.name}


def test_vault_update_creates_durable_encrypted_backup(tmp_path: Path) -> None:
    # Given
    plaintext = "EXISTING=value\n"
    paths = _isolated_vault(tmp_path, plaintext)
    original_ciphertext = paths.encrypted.read_bytes()
    backup = paths.encrypted.with_name(f"{paths.encrypted.name}.bak")

    # When
    _ = get_secrets.get_or_create_secret(
        "REINS_MCP_HTTP_TOKEN",
        paths=paths,
        generator=lambda: "isolated-generated-token",
    )

    # Then
    cipher = Fernet(paths.key.read_bytes())
    assert backup.read_bytes() == original_ciphertext
    assert cipher.decrypt(backup.read_bytes()).decode() == plaintext
    assert paths.encrypted.read_bytes() != original_ciphertext
    assert backup.stat().st_mode & 0o777 == 0o600
    assert paths.encrypted.stat().st_mode & 0o777 == 0o600
    assert {path.name for path in tmp_path.iterdir()} == {
        paths.key.name,
        paths.encrypted.name,
        backup.name,
    }


def test_vault_update_failure_restores_previous_ciphertext(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given
    paths = _isolated_vault(tmp_path, "EXISTING=value\n")
    original_ciphertext = paths.encrypted.read_bytes()
    backup = paths.encrypted.with_name(f"{paths.encrypted.name}.bak")
    real_replace = get_secrets.replace_file
    active_replacements = 0

    def fail_after_active_replace(
        source: str | os.PathLike[str],
        target: str | os.PathLike[str],
    ) -> None:
        nonlocal active_replacements
        if Path(target) == paths.encrypted:
            active_replacements += 1
            if active_replacements == 1:
                real_replace(source, target)
                raise OSError("durability signal refused")
        real_replace(source, target)

    monkeypatch.setattr(get_secrets, "replace_file", fail_after_active_replace)

    # When / Then
    with pytest.raises(get_secrets.VaultWriteError, match="previous ciphertext restored"):
        _ = get_secrets.get_or_create_secret(
            "REINS_MCP_HTTP_TOKEN",
            paths=paths,
            generator=lambda: "isolated-generated-token",
        )
    assert paths.encrypted.read_bytes() == original_ciphertext
    assert backup.read_bytes() == original_ciphertext
    assert backup.stat().st_mode & 0o777 == 0o600
    assert active_replacements == 2


def test_vault_update_and_rollback_failure_retains_encrypted_backup(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given
    paths = _isolated_vault(tmp_path, "EXISTING=value\n")
    original_ciphertext = paths.encrypted.read_bytes()
    backup = paths.encrypted.with_name(f"{paths.encrypted.name}.bak")
    real_replace = get_secrets.replace_file
    active_replacements = 0

    def reject_rollback(
        source: str | os.PathLike[str],
        target: str | os.PathLike[str],
    ) -> None:
        nonlocal active_replacements
        if Path(target) == paths.encrypted:
            active_replacements += 1
            if active_replacements == 1:
                real_replace(source, target)
                raise OSError("durability signal refused")
            raise OSError("rollback refused")
        real_replace(source, target)

    monkeypatch.setattr(get_secrets, "replace_file", reject_rollback)

    # When / Then
    with pytest.raises(get_secrets.VaultWriteError, match="rollback failed; encrypted backup retained"):
        _ = get_secrets.get_or_create_secret(
            "REINS_MCP_HTTP_TOKEN",
            paths=paths,
            generator=lambda: "isolated-generated-token",
        )
    assert backup.read_bytes() == original_ciphertext
    assert backup.stat().st_mode & 0o777 == 0o600
    assert active_replacements == 2
