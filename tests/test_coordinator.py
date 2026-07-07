"""
Tests for `reins.harness.coordinator` (ModelCoordinator): admission control,
LRU eviction, and OOM-defense/degradation over the local Ollama plane.
Entirely monkeypatched against `reins.harness.local` — no live Ollama needed.
"""

from reins.harness import coordinator as coord_mod
from reins.harness.coordinator import ModelCoordinator, ModelState


def _coordinator(monkeypatch, tmp_path, **overrides):
    monkeypatch.setenv("DATA_REIN_CONFIG_DIR", str(tmp_path / "config"))
    c = ModelCoordinator()
    for k, v in overrides.items():
        setattr(c, k, v)
    return c


def test_load_refuses_model_that_never_fits(monkeypatch, tmp_path):
    monkeypatch.setattr(coord_mod.local, "ensure_server", lambda host=None: True)
    monkeypatch.setattr(coord_mod.local, "list_models_detailed", lambda host=None: [])
    c = _coordinator(monkeypatch, tmp_path, vram_budget_gb=7.2)

    slot = c.load("34b-monster")
    assert slot.state == ModelState.ERROR
    assert "does not fit" in slot.error


def test_evict_lru_unloads_oldest_first(monkeypatch, tmp_path):
    c = _coordinator(monkeypatch, tmp_path, vram_budget_gb=7.2)
    c._slots["old"] = coord_mod.ModelSlot("old", ModelState.READY, est_gb=5.0, last_used=1.0)
    c._slots["new"] = coord_mod.ModelSlot("new", ModelState.READY, est_gb=5.0, last_used=2.0)
    monkeypatch.setattr(coord_mod.local, "loaded_models", lambda host=None: [
        {"name": "old", "size_vram": 5.0 * 1024 ** 3},
        {"name": "new", "size_vram": 5.0 * 1024 ** 3},
    ])
    unloaded = []
    monkeypatch.setattr(coord_mod.local, "unload_model", lambda model, host=None: unloaded.append(model) or True)

    evicted = c.evict_lru(need_gb=2.0)
    assert evicted == ["old"]
    assert unloaded == ["old"]


def test_generate_retries_once_then_degrades_to_router(monkeypatch, tmp_path):
    c = _coordinator(monkeypatch, tmp_path)
    monkeypatch.setattr(coord_mod.local, "loaded_models", lambda host=None: [])
    monkeypatch.setattr(coord_mod.local, "unload_model", lambda model, host=None: True)

    def _boom(*a, **k):
        raise RuntimeError("simulated OOM")
    monkeypatch.setattr(coord_mod.local, "generate", _boom)

    from reins.harness import models as models_mod
    sentinel = models_mod.RouteResult("degraded", "fallback-model", "ollama", "amdy", ok=True)
    monkeypatch.setattr(models_mod.ModelRouter, "route", lambda self, category, prompt: sentinel)

    result = c.generate("some-model", "hello")
    assert result is sentinel
    assert c._slots["some-model"].state == ModelState.ERROR


def test_options_for_merges_defaults_and_overrides(monkeypatch, tmp_path):
    c = _coordinator(monkeypatch, tmp_path, defaults={"num_ctx": 2048, "num_thread": 8},
                     model_overrides={"bakllava:latest": {"num_ctx": 1024}})
    assert c.options_for("bakllava:latest") == {"num_ctx": 1024, "num_thread": 8}
    assert c.options_for("llama3.1:8b") == {"num_ctx": 2048, "num_thread": 8}


def test_status_degrades_when_ollama_down(monkeypatch, tmp_path):
    c = _coordinator(monkeypatch, tmp_path)
    monkeypatch.setattr(coord_mod.local, "loaded_models", lambda host=None: (_ for _ in ()).throw(ConnectionError()))
    status = c.status()
    assert status["slots"] == {}
    assert status["used_gb"] == 0


def test_publish_state_lands_in_shared_state(monkeypatch, tmp_path):
    shm = tmp_path / "shared_state.mmap"
    monkeypatch.setenv("DATA_REIN_SHM", str(shm))
    c = _coordinator(monkeypatch, tmp_path)
    c._slots["m"] = coord_mod.ModelSlot("m", ModelState.READY, est_gb=1.0, last_used=1.0)
    c._publish_state()

    from reins.harness.ipc import SharedState
    data = SharedState().read()
    assert data is not None
    assert data["slots"]["m"]["state"] == "ready"
