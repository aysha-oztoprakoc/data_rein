"""
Tests for `reins digest` (``reins.harness.digest``): the single ingestion path that
turns raw files into wiki knowledge, writing only to the monolith wiki DB. Enrichment
and trail logging are disabled to keep these hermetic (no model calls, no ~/.config writes).
"""

from reins.harness import digest
from reins.harness.wiki import slugify


def test_digest_text_file_creates_page(wiki, tmp_path):
    src = tmp_path / "note.txt"
    src.write_text("Graceful degradation keeps the harness alive.")
    items = digest.digest_path(str(src), enrich=False, log_trail=False)
    assert len(items) == 1 and items[0].ok

    page = wiki.get_page(slugify(str(src)))
    assert page is not None
    assert page["title"] == "note.txt"
    assert "degradation" in page["content"]


def test_digest_unsupported_extension_degrades(wiki, tmp_path):
    src = tmp_path / "mystery.zzz"
    src.write_text("x")
    items = digest.digest_path(str(src), enrich=False, log_trail=False)
    assert len(items) == 1 and not items[0].ok
    assert "no extractor" in (items[0].error or "")


def test_digest_directory_non_recursive(wiki, tmp_path):
    (tmp_path / "a.md").write_text("# A\nalpha content")
    (tmp_path / "b.txt").write_text("beta content")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "c.txt").write_text("gamma content")

    items = digest.digest_path(str(tmp_path), recursive=False, enrich=False, log_trail=False)
    ok = [i for i in items if i.ok]
    assert len(ok) == 2  # a.md + b.txt, not the nested sub/c.txt
