"""
Tests for `reins.harness.dataset`: exporting wiki content to JSONL training
sets. The wiki DB stays the single knowledge store; JSONL is a derived,
disposable artifact.
"""

import json
from pathlib import Path

import pytest

from reins.harness import dataset


@pytest.fixture(autouse=True)
def _export_root(tmp_path, monkeypatch):
    """Confine exports to tmp_path so tests don't depend on the real state dir."""
    monkeypatch.setenv("DATA_REIN_EXPORT_DIR", str(tmp_path))
    yield tmp_path


def test_export_jsonl_filters_by_modality(wiki, tmp_path):
    wiki.upsert_page("a", "x" * 100, slug="a", category="digested/text")
    wiki.upsert_page("b", "y" * 100, slug="b", category="digested/image")

    out = tmp_path / "train.jsonl"
    stats = dataset.export_jsonl(str(out), modality="text")

    lines = out.read_text().splitlines()
    assert stats.written == 1
    assert len(lines) == 1
    record = json.loads(lines[0])
    assert record["meta"]["slug"] == "a"


def test_export_jsonl_skips_short_content(wiki, tmp_path):
    wiki.upsert_page("short", "tiny", slug="short", category="digested/text")
    wiki.upsert_page("long", "z" * 100, slug="long", category="digested/text")

    out = tmp_path / "train.jsonl"
    stats = dataset.export_jsonl(str(out), modality="text", min_chars=64)

    assert stats.written == 1
    assert stats.skipped == 1


def test_export_jsonl_memories_kind(wiki, tmp_path):
    wiki.add_memory("a" * 100, category="digested", source="s")

    out = tmp_path / "mem.jsonl"
    stats = dataset.export_jsonl(str(out), kind="memories")

    assert stats.written == 1
    record = json.loads(out.read_text().splitlines()[0])
    assert record["meta"]["category"] == "digested"


def test_export_jsonl_relative_path_lands_in_export_root(wiki, tmp_path):
    """A bare filename (no directory) resolves inside the export root."""
    wiki.upsert_page("a", "x" * 100, slug="a", category="digested/text")

    stats = dataset.export_jsonl("train.jsonl", modality="text")

    landed = (tmp_path / "train.jsonl").resolve()
    assert Path(stats.out_path).resolve() == landed
    assert landed.read_text()


def test_export_jsonl_rejects_absolute_escape(wiki, tmp_path, monkeypatch):
    """An absolute out_path outside the export root must fail closed."""
    wiki.upsert_page("a", "x" * 100, slug="a", category="digested/text")
    outside = tmp_path.parent / "escape.jsonl"

    with pytest.raises(ValueError, match="export"):
        dataset.export_jsonl(str(outside), modality="text")
    assert not outside.exists()


def test_export_jsonl_rejects_dotdot_escape(wiki, tmp_path):
    """A ../ traversal in a relative path must not leave the export root."""
    wiki.upsert_page("a", "x" * 100, slug="a", category="digested/text")

    with pytest.raises(ValueError, match="export"):
        dataset.export_jsonl("../escape.jsonl", modality="text")
    assert not (tmp_path.parent / "escape.jsonl").exists()
