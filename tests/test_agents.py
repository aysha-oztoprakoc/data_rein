"""
Tests for the shared agent spine (``reins.harness.agents.HarnessAgent``) — the one
identity every data_rein service (data-agy / data-hermes / data-ody) inherits after
the convergence. Enforces the contract: one router, one wiki for recall/remember,
graceful degradation (never raises), and PON-passive construction (no threads/polling).
"""


from reins.harness.agents import HarnessAgent
from reins.harness.models import RouteResult


def test_agent_has_router_and_role():
    a = HarnessAgent()
    assert a.role == "agent"
    assert a.router is not None  # every agent shares the model-agnostic plane


def test_infer_delegates_to_workflow(monkeypatch):
    """infer() must route through the single workflow/router gateway, forwarding args."""
    captured = {}

    def fake_run(category, prompt, node="amdy", rag=False, router=None):
        captured.update(category=category, prompt=prompt, node=node, rag=rag)
        return RouteResult(text="ok", model="m", provider="ollama", node=node, ok=True)

    monkeypatch.setattr("reins.harness.workflow.run", fake_run)
    res = HarnessAgent().infer("deep search", "q", node="tell", rag=True)
    assert res.ok and res.text == "ok"
    assert captured == {"category": "deep search", "prompt": "q", "node": "tell", "rag": True}


def test_remember_then_recall_roundtrip(wiki):
    """remember() persists to the shared wiki; recall() reads it back (FTS)."""
    a = HarnessAgent()
    a.remember("amdy GPU is 8GB VRAM", category="system")
    hits = a.recall("VRAM")
    # search_memories returns rows with a highlighted `snippet` column.
    assert any("VRAM" in row["snippet"] for row in hits["memories"])


def test_recall_degrades_to_empty(monkeypatch):
    """If the wiki is unavailable, recall() degrades to empty results, never raises."""
    import reins.harness.wiki as wikimod

    def boom(*_a, **_k):
        raise RuntimeError("wiki down")

    monkeypatch.setattr(wikimod, "WikiDB", boom)
    assert HarnessAgent().recall("anything") == {"pages": [], "memories": []}


def test_remember_is_best_effort(monkeypatch):
    """remember() must swallow failures (graceful degradation), never raise."""
    import reins.harness.wiki as wikimod

    def boom(*_a, **_k):
        raise RuntimeError("wiki down")

    monkeypatch.setattr(wikimod, "WikiDB", boom)
    HarnessAgent().remember("x")  # must not raise
