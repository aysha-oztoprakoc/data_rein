"""
Tests for the local-model workflow integration (reins.harness.local + workflow).

Hermetic: no live Ollama server required. They assert the routing/degradation
contract so low-effort offload and batch automation stay correct.
"""

import pytest

from reins.harness import local, workflow
from reins.harness.models import ModelRouter, RouteResult


# --- local plane -----------------------------------------------------------
def test_model_store_env_override(monkeypatch, tmp_path):
    monkeypatch.setenv("OLLAMA_MODELS", str(tmp_path / "store"))
    assert local.model_store() == tmp_path / "store"


def test_model_store_default_under_home(monkeypatch):
    monkeypatch.delenv("OLLAMA_MODELS", raising=False)
    assert local.model_store().name == "models"
    assert "ai_models" in str(local.model_store())


def test_server_up_false_when_unreachable(monkeypatch):
    monkeypatch.setattr(local.urllib.request, "urlopen",
                        lambda *a, **k: (_ for _ in ()).throw(OSError("no server")))
    assert local.server_up(host="127.0.0.1:9") is False


# --- workflow routing ------------------------------------------------------
class _StubRouter(ModelRouter):
    def __init__(self, result):
        self._result = result

    def route(self, category, prompt, node="amdy", allow_fallback=True):
        self._last = (category, prompt, node)
        return self._result


def test_run_routes_and_returns(monkeypatch):
    stub = _StubRouter(RouteResult("hi", "llama3.1:8b", "ollama", "amdy", ok=True))
    res = workflow.run("general chatting", "hello", router=stub)
    assert res.ok and res.text == "hi"
    assert stub._last[0] == "general chatting"


def test_run_rag_prepends_context(monkeypatch):
    monkeypatch.setattr(workflow, "_rag_context", lambda p, **k: "CTX\n")
    stub = _StubRouter(RouteResult("x", "m", "ollama", "amdy", ok=True))
    workflow.run("deep search", "q", rag=True, router=stub)
    assert stub._last[1].startswith("CTX\n")


def test_rag_context_degrades_to_empty(monkeypatch):
    # If the wiki blows up, RAG must degrade to no-context, never raise.
    import reins.harness.wiki as wiki_mod

    def _boom(*a, **k):
        raise RuntimeError("wiki unavailable")

    monkeypatch.setattr(wiki_mod, "WikiDB", _boom)
    assert workflow._rag_context("anything") == ""


def test_low_effort_maps_categories():
    assert workflow.LOW_EFFORT["ask"][0] == "general chatting"
    with pytest.raises(ValueError):
        workflow.low_effort("nonsense", "x")


# --- batch automation ------------------------------------------------------
def test_batch_isolates_failures(monkeypatch):
    # Router returns ok for evens, failure for odds -> batch must not abort.
    calls = {"n": 0}

    def fake_run(category, prompt, node="amdy", rag=False, router=None):
        i = calls["n"]
        calls["n"] += 1
        if i % 2 == 0:
            return RouteResult(f"ok{i}", "m", "ollama", node, ok=True)
        return RouteResult(None, "m", "none", node, ok=False, error="boom")

    monkeypatch.setattr(workflow, "run", fake_run)
    items = workflow.batch("general chatting", ["a", "b", "c"], log_trail=False)
    assert len(items) == 3
    assert [i.ok for i in items] == [True, False, True]


def test_batch_skips_blank_lines(monkeypatch):
    monkeypatch.setattr(workflow, "run",
                        lambda *a, **k: RouteResult("x", "m", "ollama", "amdy", ok=True))
    items = workflow.batch("general chatting", ["a", "", "  ", "b"], log_trail=False)
    assert len(items) == 2
