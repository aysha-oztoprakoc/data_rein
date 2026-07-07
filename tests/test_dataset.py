"""
Tests for `reins.harness.dataset`: exporting wiki content to JSONL training
sets. The wiki DB stays the single knowledge store; JSONL is a derived,
disposable artifact.
"""

import json

from reins.harness import dataset


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
