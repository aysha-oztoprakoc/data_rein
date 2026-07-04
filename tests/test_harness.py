"""
Tests for the data_rein universal harness core: paths, monolith wiki DB, and the
model-agnostic router. These enforce the Prime Directive's load-bearing promises:
one rebuildable knowledge store, idempotent ingestion, FTS search, and
model-agnostic routing that never crashes (graceful degradation).
"""

import os

import pytest

from reins.harness import paths
from reins.harness.wiki import WikiDB, slugify
from reins.harness.models import ModelSpec, ModelRouter


@pytest.fixture()
def db(tmp_path, monkeypatch):
    dbfile = tmp_path / "wiki.db"
    monkeypatch.setenv("DATA_REIN_WIKI_DB", str(dbfile))
    w = WikiDB()
    yield w
    w.close()


# --- paths -----------------------------------------------------------------
def test_paths_resolve_under_home():
    assert paths.prime_directive().name == "PRIME_DIRECTIVE.md"
    assert paths.wiki_db().name == "wiki.db"
    assert str(paths.knowledge_base()).endswith("knowledge_base")


def test_paths_env_override(monkeypatch, tmp_path):
    monkeypatch.setenv("DATA_REIN_WIKI_DB", str(tmp_path / "x.db"))
    assert paths.wiki_db() == tmp_path / "x.db"


# --- wiki: pages -----------------------------------------------------------
def test_page_upsert_is_idempotent(db):
    db.upsert_page("PON", "no polling ever", slug="pon", category="arch")
    db.upsert_page("PON", "no polling, zero cpu idle", slug="pon", category="arch")
    assert db.stats()["pages"] == 1
    assert "zero cpu" in db.get_page("pon")["content"]


def test_page_fts_search(db):
    db.upsert_page("Resilience", "graceful degradation under chaos", slug="r1")
    hits = db.search_pages("degradation")
    assert hits and hits[0]["slug"] == "r1"


# --- wiki: memories --------------------------------------------------------
def test_memory_dedup_by_content(db):
    db.add_memory("amdy has 16GB VRAM", category="system", source="hw")
    db.add_memory("amdy has 16GB VRAM", category="system", source="hw")
    assert db.stats()["memories"] == 1


def test_memory_search_and_categories(db):
    db.add_memory("tell runs a GTX 1060", category="system")
    db.add_memory("prefer local models", category="policy")
    assert db.search_memories("GTX")[0]["category"] == "system"
    cats = db.categories()
    assert cats.get("system") == 1 and cats.get("policy") == 1


def test_slugify_stable():
    assert slugify("Hello, World!") == "hello-world"
    assert slugify("a///b") == "a-b"


# --- models: agnostic routing ---------------------------------------------
def test_provider_inference():
    assert ModelSpec(model="gemini-2.0-flash").resolved_provider == "gemini"
    assert ModelSpec(model="claude-sonnet-5").resolved_provider == "claude"
    assert ModelSpec(model="gpt-4o").resolved_provider == "openai"
    assert ModelSpec(model="qwen2.5:7b").resolved_provider == "ollama"
    assert ModelSpec(model="comfyui_sdxl_base", backend="comfyui").resolved_provider == "comfyui"


def test_router_reads_real_config():
    r = ModelRouter()
    # The shipped router has 11 categories; at minimum general chatting must route.
    spec = r.optimal("general chatting", "amdy")
    assert spec.model


def test_router_degrades_without_crashing(monkeypatch):
    """A category with only an unreachable provider returns ok=False, not an exception."""
    r = ModelRouter()
    r.table = {"x": {"amdy": [{"model": "claude-nope"}], "tell": [{"model": "gpt-nope"}]}}
    monkeypatch.setattr("reins.harness.models._get_secret", lambda *_: None)
    res = r.route("x", "hello", "amdy")
    assert res.ok is False
    assert res.error  # explains why each candidate failed
