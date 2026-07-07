from reins.harness import handoff
from reins.services.task_trail import TaskTrail


def _isolate(monkeypatch, tmp_path):
    monkeypatch.setenv("DATA_REIN_STATE_DIR", str(tmp_path / "state"))


def test_queue_chunked_task_writes_chunks_to_trail(monkeypatch, tmp_path):
    _isolate(monkeypatch, tmp_path)
    task_id = handoff.queue_chunked_task("generic", "do the thing", ["ctx one", "ctx two"])
    assert task_id is not None

    task = TaskTrail().get_task(task_id)
    assert task["status"] == "queued"
    assert task["target_node"] == "amdy"
    assert task["chunk_cursor"] == 0
    assert len(task["chunks"]) >= 1


def test_pickup_next_returns_none_when_nothing_queued(monkeypatch, tmp_path):
    _isolate(monkeypatch, tmp_path)
    assert handoff.pickup_next() is None


def test_pickup_next_uses_maestro_fast_path_via_local_generate(monkeypatch, tmp_path):
    _isolate(monkeypatch, tmp_path)
    task_id = handoff.queue_chunked_task("generic", "goal", ["only chunk"])

    from reins.harness import local as local_mod

    calls = []

    def _fake_generate(model, prompt, **kwargs):
        calls.append(model)
        assert model == handoff.MAESTRO_MODEL
        assert "only chunk" in prompt
        assert "Step 1 of 1" in prompt
        return "did the step\nSUMMARY: finished step one"

    monkeypatch.setattr(local_mod, "generate", _fake_generate)

    result = handoff.pickup_next()
    assert result["status"] == "done"
    assert result["summary"] == "SUMMARY: finished step one"
    assert calls == [handoff.MAESTRO_MODEL]

    task = TaskTrail().get_task(task_id)
    assert task["status"] == "done"
    assert task["chunk_cursor"] == 1
    assert task["chunk_summaries"] == ["SUMMARY: finished step one"]
    assert task["last_model"] == handoff.MAESTRO_MODEL


def test_pickup_next_falls_back_to_router_when_maestro_fails(monkeypatch, tmp_path):
    _isolate(monkeypatch, tmp_path)
    task_id = handoff.queue_chunked_task("generic", "goal", ["only chunk"])

    from reins.harness import local as local_mod
    from reins.harness import models as models_mod

    def _boom(model, prompt, **kwargs):
        raise RuntimeError("ollama down")

    def _fake_route(self, category, prompt, node="amdy", **kwargs):
        return models_mod.RouteResult(
            text="did the step\nSUMMARY: via fallback", model="fallback-model",
            provider="ollama", node=node, ok=True,
        )

    monkeypatch.setattr(local_mod, "generate", _boom)
    monkeypatch.setattr(models_mod.ModelRouter, "route", _fake_route)

    result = handoff.pickup_next()
    assert result["status"] == "done"
    assert result["summary"] == "SUMMARY: via fallback"

    task = TaskTrail().get_task(task_id)
    assert task["last_model"] == "fallback-model"


def test_pickup_next_marks_failed_on_route_failure(monkeypatch, tmp_path):
    _isolate(monkeypatch, tmp_path)
    task_id = handoff.queue_chunked_task("generic", "goal", ["ctx"])

    from reins.harness import local as local_mod
    from reins.harness import models as models_mod

    def _boom(model, prompt, **kwargs):
        raise RuntimeError("ollama down")

    def _fake_route(self, category, prompt, node="amdy", **kwargs):
        return models_mod.RouteResult(text=None, model="none", provider="none",
                                       node=node, ok=False, error="all candidates down")

    monkeypatch.setattr(local_mod, "generate", _boom)
    monkeypatch.setattr(models_mod.ModelRouter, "route", _fake_route)

    result = handoff.pickup_next()
    assert result["status"] == "failed"

    task = TaskTrail().get_task(task_id)
    assert task["status"] == "failed"


def test_pickup_next_never_raises_on_internal_error(monkeypatch, tmp_path):
    _isolate(monkeypatch, tmp_path)

    def _boom(*a, **k):
        raise RuntimeError("trail corrupted")

    monkeypatch.setattr(TaskTrail, "by_status", _boom)
    assert handoff.pickup_next() is None
