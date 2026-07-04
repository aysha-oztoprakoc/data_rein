"""
Shared test fixtures and helpers for the data_rein harness suite.

Centralizes what individual test modules used to duplicate: an isolated wiki DB,
the harness source-file set (for the law tests), and a graceful-skip helper so
environment-coupled tests degrade to `skip` instead of `fail` when a live
artifact is absent — the suite itself obeys graceful degradation.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src" / "reins"


@pytest.fixture()
def wiki(tmp_path, monkeypatch):
    """An isolated monolith Wiki DB, pointed away from the real one."""
    monkeypatch.setenv("DATA_REIN_WIKI_DB", str(tmp_path / "wiki.db"))
    from reins.harness.wiki import WikiDB

    db = WikiDB()
    try:
        yield db
    finally:
        db.close()


def harness_source_files() -> list[Path]:
    """Every non-empty Python source file under src/reins (excludes caches/tests)."""
    files: list[Path] = []
    for p in SRC_ROOT.rglob("*.py"):
        if "__pycache__" in p.parts:
            continue
        if p.stat().st_size == 0:  # skip empty package markers / stubs
            continue
        files.append(p)
    return files


def require(path: str, reason: str | None = None):
    """Skip the calling test gracefully when a live/environment artifact is absent."""
    expanded = os.path.expanduser(path)
    if not os.path.exists(expanded):
        pytest.skip(reason or f"environment artifact not present: {path}")
    return expanded
