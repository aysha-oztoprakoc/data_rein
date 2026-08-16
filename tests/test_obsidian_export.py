from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from reins.harness.wiki import WikiDB
from scripts.export_to_obsidian import ExportError, MANIFEST_NAME, export_vault


def _snapshot(directory: Path) -> dict[str, str]:
    return {
        path.relative_to(directory).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


def test_obsidian_export_is_deterministic_and_manifest_owned(tmp_path: Path) -> None:
    # Given
    database_path = tmp_path / "wiki.db"
    output = tmp_path / "vault"
    with WikiDB(database_path) as database:
        database.upsert_page(title="Page / One", content="stable page", slug="page-one")
        database.add_memory("stable fact", category="facts")

    # When
    first = export_vault(database_path, output, "revision-123")
    first_snapshot = _snapshot(output)
    second = export_vault(database_path, output, "revision-123")
    second_snapshot = _snapshot(output)

    # Then
    assert first == second
    assert first_snapshot == second_snapshot
    assert first["counts"] == {"pages": 1, "memories": 1, "files": 2}
    assert (output / MANIFEST_NAME).is_file()


def test_secret_scan_failure_leaves_prior_vault_unchanged(tmp_path: Path) -> None:
    # Given
    database_path = tmp_path / "wiki.db"
    output = tmp_path / "vault"
    with WikiDB(database_path) as database:
        database.upsert_page(title="Safe", content="safe body", slug="safe")
    export_vault(database_path, output, "safe-revision")
    prior = _snapshot(output)
    with WikiDB(database_path) as database:
        database.upsert_page(
            title="Unsafe",
            slug="unsafe",
            content="AWS_ACCESS_KEY_ID = AKIAIOSFODNN7EXAMPLE",
        )

    # When
    with pytest.raises(ExportError, match="Secret scan blocked"):
        export_vault(database_path, output, "unsafe-revision")

    # Then
    assert _snapshot(output) == prior
