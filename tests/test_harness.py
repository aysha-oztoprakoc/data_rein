"""
Tests for the data_rein universal harness core: paths, monolith wiki DB, and the
model-agnostic router. These enforce the Prime Directive's load-bearing promises:
one rebuildable knowledge store, idempotent ingestion, FTS search, and
model-agnostic routing that never crashes (graceful degradation).
"""

import json

import pytest

from reins.harness import paths
from reins.harness.wiki import slugify
from reins.harness.models import ModelSpec, ModelRouter

# The isolated `wiki` DB fixture is shared from conftest.py. These tests alias it
# as `db` to keep their bodies focused.


@pytest.fixture()
def db(wiki):
    return wiki


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
    assert "cloud/" in res.error  # proves Tier-1 remote fallback was attempted, not skipped


def test_router_remote_fallback_engages_after_local_exhausted(monkeypatch):
    """Both nodes exhausted, but a vault key is present -> Tier 1 is tried and used."""
    r = ModelRouter()
    r.table = {"x": {"amdy": [{"model": "ollama-nope"}], "tell": [{"model": "ollama-nope2"}]}}
    r.remote_fallback = [ModelSpec(model="claude-sonnet-5-20260514", provider="claude")]

    monkeypatch.setattr("reins.harness.models._get_secret", lambda name: "fake-key")
    monkeypatch.setattr(ModelRouter, "_claude", lambda self, model, prompt: "hello from claude")
    monkeypatch.setattr(
        ModelRouter,
        "_ollama",
        lambda self, model, prompt, node: (_ for _ in ()).throw(RuntimeError("no ollama")),
    )

    res = r.route("x", "hello", "amdy")
    assert res.ok is True
    assert res.provider == "claude"
    assert res.node == "cloud"
    assert res.model == "claude-sonnet-5-20260514"


def test_router_remote_fallback_absent_still_degrades(monkeypatch):
    """No vault keys anywhere -> still ok=False even with remote_fallback configured."""
    r = ModelRouter()
    r.table = {"x": {"amdy": [{"model": "claude-nope"}], "tell": [{"model": "gpt-nope"}]}}
    r.remote_fallback = [
        ModelSpec(model="claude-sonnet-5-20260514", provider="claude"),
        ModelSpec(model="gemini-2.0-pro", provider="gemini"),
    ]
    monkeypatch.setattr("reins.harness.models._get_secret", lambda *_: None)

    res = r.route("x", "hello", "amdy")
    assert res.ok is False
    assert res.error
    assert "cloud/" in res.error  # proves remote tier was actually attempted, not skipped


def test_route_cloud_skips_local_entirely(monkeypatch):
    """route_cloud() must go straight to remote_fallback - it never touches Ollama."""
    r = ModelRouter()
    r.table = {"x": {"amdy": [{"model": "should-never-be-tried"}]}}
    r.remote_fallback = [ModelSpec(model="claude-sonnet-5-20260514", provider="claude")]

    def _boom(*_a, **_k):
        raise AssertionError("route_cloud must not dispatch to ollama")

    monkeypatch.setattr(ModelRouter, "_ollama", _boom)
    monkeypatch.setattr(ModelRouter, "_claude", lambda self, model, prompt: "hi from claude")

    res = r.route_cloud("hello")
    assert res.ok is True
    assert res.node == "cloud"
    assert res.provider == "claude"


def test_route_cloud_filters_by_provider(monkeypatch):
    r = ModelRouter()
    r.remote_fallback = [
        ModelSpec(model="claude-sonnet-5-20260514", provider="claude"),
        ModelSpec(model="gemini-2.0-pro", provider="gemini"),
    ]
    monkeypatch.setattr(ModelRouter, "_gemini", lambda self, model, prompt: "hi from gemini")
    monkeypatch.setattr(
        ModelRouter, "_claude",
        lambda self, model, prompt: (_ for _ in ()).throw(AssertionError("claude should be filtered out")),
    )
    res = r.route_cloud("hello", provider="gemini")
    assert res.ok is True and res.provider == "gemini"


def test_route_cloud_degrades_without_crashing(monkeypatch):
    r = ModelRouter()
    r.remote_fallback = []
    res = r.route_cloud("hello")
    assert res.ok is False
    assert res.error


# --- mcp bridge: wiki/trail tools ------------------------------------------
def test_mcp_wiki_tools_roundtrip(wiki):
    from reins.harness.mcp_server import wiki_add_memory, wiki_search

    wiki_add_memory("qwen2.5-coder-7b runs via lmstudio on amdy", category="system")
    result = json.loads(wiki_search("lmstudio"))
    assert any(m["category"] == "system" for m in result["memories"])


def test_mcp_trail_tools_roundtrip(trail):
    from reins.harness.mcp_server import trail_create, trail_list, trail_update

    task_id = json.loads(trail_create("session", "opencode session started"))["task_id"]
    trail_update(task_id, "success")
    tasks = json.loads(trail_list())
    match = next(t for t in tasks if t["task_id"] == task_id)
    assert match["status"] == "success"
    assert match["task_type"] == "opencode:session"


def test_mcp_route_local_never_reaches_cloud(monkeypatch):
    """route_local must call ModelRouter.route with allow_cloud=False."""
    from reins.harness import mcp_server

    seen = {}

    def _fake_route(self, category, prompt, node="amdy", *, allow_fallback=True, allow_cloud=True):
        seen["allow_cloud"] = allow_cloud
        from reins.harness.models import RouteResult
        return RouteResult("ok", "qwen2.5-coder:7b", "ollama", node, ok=True)

    monkeypatch.setattr(mcp_server.ModelRouter, "route", _fake_route)
    result = json.loads(mcp_server.route_local("data processing", "summarize this"))
    assert seen["allow_cloud"] is False
    assert result["ok"] is True


def test_mcp_escalate_cloud_logs_trail_and_never_raises(trail, monkeypatch):
    """escalate_cloud always logs a trail entry, and degrades gracefully on failure."""
    from reins.harness import mcp_server
    from reins.harness.models import RouteResult

    monkeypatch.setattr(
        mcp_server.ModelRouter, "route_cloud",
        lambda self, prompt, provider=None: RouteResult(None, "none", "none", "cloud", ok=False, error="no key"),
    )
    result = json.loads(mcp_server.escalate_cloud("use claude for this"))
    assert result["ok"] is False
    assert result["task_id"]

    from reins.services.task_trail import TaskTrail
    logged = TaskTrail().get_task(result["task_id"])
    assert logged["status"] == "failed"
    assert logged["task_type"] == "opencode:cloud-escalation"


# --- token usage / budget tracking ------------------------------------------
def test_token_ledger_records_and_aggregates(token_ledger):
    token_ledger.record("claude", "claude-sonnet-5", input_tokens=100, output_tokens=50)
    token_ledger.record("claude", "claude-sonnet-5", input_tokens=10, output_tokens=5)
    token_ledger.record("gemini", "gemini-2.0-pro", input_tokens=1, output_tokens=1)

    claude_5h = token_ledger.usage_in(5 * 3600, provider="claude")
    assert claude_5h["requests"] == 2
    assert claude_5h["total_tokens"] == 165

    windows = token_ledger.window_summary("claude")
    assert set(windows) == {"5h", "day", "week", "month"}
    assert windows["month"]["requests"] == 2  # every window is trailing-from-now, so all still count


def test_token_ledger_old_events_age_out_of_window(token_ledger, monkeypatch):
    import time

    token_ledger.record("claude", "claude-sonnet-5", input_tokens=10, output_tokens=10)
    events = token_ledger._load()
    events[0]["timestamp"] = time.time() - 10 * 3600  # 10h ago: outside the 5h window
    token_ledger._atomic_write(events)

    assert token_ledger.usage_in(5 * 3600, provider="claude")["requests"] == 0
    assert token_ledger.usage_in(24 * 3600, provider="claude")["requests"] == 1


def test_budget_report_computes_percentage_only_when_configured(monkeypatch, token_ledger):
    from reins.harness import paths
    from reins.services import token_ledger as token_ledger_mod

    monkeypatch.setattr(
        paths, "token_budgets",
        lambda: type("P", (), {"read_text": lambda self, **_: __import__("json").dumps({
            "_comment": "ignore me - not a provider",
            "claude": {"5h": {"requests": 10}},
        })})(),
    )
    token_ledger.record("claude", "claude-sonnet-5", input_tokens=1, output_tokens=1)
    token_ledger.record("gemini", "gemini-2.0-pro", input_tokens=1, output_tokens=1)

    report = token_ledger_mod.budget_report()
    assert report["claude"]["5h"]["request_pct"] == 10.0
    assert "request_pct" not in report["claude"]["day"]  # no budget configured for this window
    assert "request_pct" not in report["gemini"]["5h"]  # no budget configured for this provider


def test_router_records_usage_on_successful_cloud_call(monkeypatch, token_ledger):
    r = ModelRouter()
    r.remote_fallback = [ModelSpec(model="claude-sonnet-5-20260514", provider="claude")]

    def _fake_claude(self, model, prompt):
        self._last_usage = {"input_tokens": 42, "output_tokens": 8}
        return "hi from claude"

    monkeypatch.setattr(ModelRouter, "_claude", _fake_claude)
    res = r.route_cloud("hello")
    assert res.ok is True

    usage = token_ledger.usage_in(3600, provider="claude")
    assert usage["requests"] == 1
    assert usage["total_tokens"] == 50


# --- per-agent resource budgets ---------------------------------------------
def test_resource_budgets_default_to_unrestricted(isolated_config_dir):
    from reins.services import resource_budgets as rb

    budgets = rb.load_budgets()
    assert set(budgets) == {"data-agy", "data-hermes", "data-ody", "data-sofia"}
    assert all(b == {"cpu_pct": 100, "gpu_vram_gb": 0.0} for b in budgets.values())


def test_resource_budgets_save_persists_and_clamps(isolated_config_dir):
    from reins.services import resource_budgets as rb

    rb.save_budget("data-hermes", cpu_pct=250, gpu_vram_gb=-3)  # out-of-range input
    budgets = rb.load_budgets()
    assert budgets["data-hermes"]["cpu_pct"] == 100  # clamped to the [1, 100] range
    assert budgets["data-hermes"]["gpu_vram_gb"] == 0.0  # clamped to >= 0

    rb.save_budget("data-hermes", cpu_pct=40, gpu_vram_gb=2.5)
    assert rb.load_budgets()["data-hermes"] == {"cpu_pct": 40, "gpu_vram_gb": 2.5}
    # unrelated agents keep their defaults across the partial update
    assert rb.load_budgets()["data-ody"]["cpu_pct"] == 100


def test_apply_cpu_budget_degrades_without_cgroup_v2(monkeypatch):
    from reins.services import resource_budgets as rb

    monkeypatch.setattr(rb, "cgroup_available", lambda: False)
    ok, msg = rb.apply_cpu_budget("data-hermes", 50, pids=[1234])
    assert ok is False
    assert "cgroup" in msg


def test_apply_cpu_budget_degrades_on_sudo_failure(monkeypatch):
    from reins.services import resource_budgets as rb

    monkeypatch.setattr(rb, "cgroup_available", lambda: True)
    monkeypatch.setattr(
        rb, "run_sudo_cmd",
        lambda cmd: type("R", (), {"returncode": 1, "stderr": "permission denied"})(),
    )
    ok, msg = rb.apply_cpu_budget("data-hermes", 50, pids=[1234])
    assert ok is False
    assert "permission denied" in msg


def test_subagent_manager_logs_spawn_to_trail(monkeypatch, trail):
    from reins.services.subagent_manager import SubagentManager

    mgr = SubagentManager.__new__(SubagentManager)  # skip MQTT subscribe in __init__
    mgr.role = "data-hermes"
    mgr.trail = trail
    mgr.mqtt = type("M", (), {"publish": lambda self, topic, payload: None})()
    monkeypatch.setattr(mgr, "infer", lambda category, prompt, node="amdy": type(
        "Res", (), {"ok": True, "node": node, "model": "llama3.1:8b", "text": "hi", "error": None},
    )())

    mgr._execute_subagent({"task_type": "General Chatting", "prompt": "hello", "node": "amdy"})

    tasks = trail.all_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task_type"] == "data-hermes:subagent:General Chatting"
    assert tasks[0]["status"] == "success"
