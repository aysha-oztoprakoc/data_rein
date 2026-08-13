"""
Tests for the tool dispatch registry (`reins.harness.dispatch`): the real
functions an accepted, judge-approved leaf action is allowed to invoke.
Node targeting always defaults to amdy - tell is unreachable and out of
scope until a live hardware scan brings it back online.
"""

from __future__ import annotations


def test_dispatch_local_generate_defaults_to_amdy_and_never_cloud(monkeypatch):
    # Given a local provider result and a cloud path that must remain unreachable.
    from reins.harness import dispatch

    seen: dict[str, object] = {}

    def _fake_route(self, category, prompt, node="amdy", *, allow_fallback=True):
        seen["node"] = node
        from reins.harness.models import RouteResult

        return RouteResult("ok", "qwen2.5-coder:7b", "ollama", node, ok=True)

    def _fail_cloud(*_args, **_kwargs):
        raise AssertionError("local dispatch must never call route_cloud")

    monkeypatch.setattr(dispatch.ModelRouter, "route", _fake_route)
    monkeypatch.setattr(dispatch.ModelRouter, "route_cloud", _fail_cloud)

    # When the public local dispatcher generates a result.
    result = dispatch.dispatch_local_generate({"prompt": "summarize this"})

    # Then its neutral result envelope preserves both execution node and provider.
    assert seen["node"] == "amdy"
    assert result["ok"] is True
    assert result["provider"] == "ollama"


def test_dispatch_read_file_reads_within_repo_root():
    from reins.harness import dispatch

    result = dispatch.dispatch_read_file({"path": "blueprint.yaml"})
    assert result["ok"] is True
    text = result["text"]
    assert isinstance(text, str)
    assert "local_model_rules" in text


def test_dispatch_read_file_degrades_gracefully_on_missing_file():
    from reins.harness import dispatch

    result = dispatch.dispatch_read_file({"path": "does/not/exist.txt"})
    assert result["ok"] is False
    assert result["error"]


def test_dispatch_cloud_generate_logs_trail(trail, monkeypatch):
    from reins.harness import dispatch

    monkeypatch.setattr(
        dispatch.ModelRouter,
        "route_cloud",
        lambda self, prompt, provider=None: __import__(
            "reins.harness.models", fromlist=["RouteResult"]
        ).RouteResult("ok", "claude-sonnet-5", provider or "claude", "cloud", ok=True),
    )
    result = dispatch.dispatch_cloud_generate({"prompt": "use claude for this"})
    assert result["ok"] is True
    assert result["task_id"]

    from reins.services.task_trail import TaskTrail

    task_id = result["task_id"]
    assert isinstance(task_id, str)
    logged = TaskTrail().get_task(task_id)
    assert logged is not None
    assert logged["status"] == "success"
