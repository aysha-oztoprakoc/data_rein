"""
Model residency coordinator for the amdy model plane.

Enforces the hardware budget law (8GB VRAM RX 9060 XT) against Ollama's model
store: which models are loaded, how much VRAM each estimated to cost, and what
to evict when a new model needs room. This is a state machine over HTTP calls
to Ollama, not a daemon — every public method is a bounded call (blocking I/O
with timeouts, PON-legal) that returns; there is no background poll loop.

On any failure (Ollama down, OOM, unknown model) methods degrade instead of
raising: they mark the offending slot ERROR, log to the Task Trail, and — for
`generate()` — fall through to `ModelRouter().route()` so a caller always gets
a `RouteResult`, never an exception.
"""

from __future__ import annotations
from reins.services.logger import log_degradation

import json
import time
from dataclasses import dataclass
from enum import Enum
from typing import Optional, TypedDict

from reins.harness import local, paths


class ModelState(Enum):
    UNLOADED = "unloaded"
    LOADING = "loading"
    READY = "ready"
    BUSY = "busy"
    UNLOADING = "unloading"
    ERROR = "error"


@dataclass
class ModelSlot:
    name: str
    state: ModelState = ModelState.UNLOADED
    est_gb: float = 0.0
    last_used: float = 0.0
    error: Optional[str] = None


class SlotStatus(TypedDict):
    state: str
    est_gb: float
    last_used: float
    error: str | None


class CoordinatorStatus(TypedDict):
    vram_budget_gb: float
    used_gb: float
    slots: dict[str, SlotStatus]


# Name-based fallback estimate (GB) when /api/tags doesn't expose a size yet
# (model not pulled) — rough parameter-count heuristic, q4_K_M-ish.
_SIZE_FALLBACK_GB = {
    "3b": 2.2, "7b": 4.5, "8b": 5.0, "13b": 8.5, "14b": 9.0, "34b": 20.0,
}


def _config() -> dict:
    try:
        return json.loads(paths.coordinator_config().read_text())
    except Exception:
        log_degradation(__name__)
        return {}


class ModelCoordinator:
    """Admission control + LRU eviction over the local Ollama plane."""

    def __init__(self, host: str = None) -> None:
        self.host = host or local.DEFAULT_HOST
        self._slots: dict[str, ModelSlot] = {}
        cfg = _config()
        self.vram_budget_gb: float = cfg.get("vram_budget_gb", 7.2)
        self.kv_overhead_gb: float = cfg.get("kv_overhead_gb", 0.6)
        self.load_headroom_factor: float = cfg.get("load_headroom_factor", 1.10)
        self.keep_alive: str = cfg.get("keep_alive", "10m")
        self.model_overrides: dict = cfg.get("model_overrides", {})
        self.defaults: dict = cfg.get("defaults", {"num_ctx": 2048, "num_thread": 8})

    # -- introspection --------------------------------------------------
    def status(self) -> CoordinatorStatus:
        self._sync_from_ollama()
        return {
            "vram_budget_gb": self.vram_budget_gb,
            "used_gb": round(sum(s.est_gb for s in self._slots.values()
                                  if s.state in (ModelState.READY, ModelState.BUSY)), 2),
            "slots": {
                name: {
                    "state": s.state.value, "est_gb": s.est_gb,
                    "last_used": s.last_used, "error": s.error,
                }
                for name, s in self._slots.items()
            },
        }

    def estimate_gb(self, model: str) -> float:
        for m in local.list_models_detailed(self.host):
            if m["name"] == model and m.get("size"):
                base_gb = m["size"] / (1024 ** 3)
                return round(base_gb * self.load_headroom_factor + self.kv_overhead_gb, 2)
        for key, gb in _SIZE_FALLBACK_GB.items():
            if key in model.lower():
                return round(gb * self.load_headroom_factor + self.kv_overhead_gb, 2)
        return round(4.5 * self.load_headroom_factor + self.kv_overhead_gb, 2)  # unknown-model default

    def fits(self, model: str) -> bool:
        self._sync_from_ollama()
        need = self.estimate_gb(model)
        used = sum(s.est_gb for s in self._slots.values()
                   if s.state in (ModelState.READY, ModelState.BUSY) and s.name != model)
        return used + need <= self.vram_budget_gb

    def options_for(self, model: str) -> dict:
        return {**self.defaults, **self.model_overrides.get(model, {})}

    # -- lifecycle --------------------------------------------------------
    def load(self, model: str) -> ModelSlot:
        if not local.ensure_server(self.host):
            slot = self._slot(model)
            slot.state, slot.error = ModelState.ERROR, "ollama server unreachable"
            self._publish_state()
            return slot

        self._sync_from_ollama()
        need = self.estimate_gb(model)
        if need > self.vram_budget_gb:
            slot = self._slot(model)
            slot.state = ModelState.ERROR
            slot.error = f"does not fit {self.vram_budget_gb}GB budget even empty ({need}GB)"
            self._publish_state()
            return slot

        if not self.fits(model):
            self.evict_lru(need)

        slot = self._slot(model)
        slot.state = ModelState.LOADING
        self._publish_state()
        ok = local.load_model(model, host=self.host, keep_alive=self.keep_alive)
        slot.state = ModelState.READY if ok else ModelState.ERROR
        slot.est_gb = need
        slot.last_used = time.time()
        slot.error = None if ok else "load_model failed"
        self._publish_state()
        return slot

    def unload(self, model: str) -> ModelSlot:
        slot = self._slot(model)
        slot.state = ModelState.UNLOADING
        self._publish_state()
        local.unload_model(model, host=self.host)
        slot.state = ModelState.UNLOADED
        slot.est_gb = 0.0
        self._publish_state()
        return slot

    def evict_lru(self, need_gb: float) -> list[str]:
        self._sync_from_ollama()
        resident = sorted(
            (s for s in self._slots.values() if s.state in (ModelState.READY, ModelState.BUSY)),
            key=lambda s: s.last_used,
        )
        evicted = []
        freed = 0.0
        used = sum(s.est_gb for s in resident)
        for slot in resident:
            if used - freed + need_gb <= self.vram_budget_gb:
                break
            slot_gb = slot.est_gb
            self.unload(slot.name)
            evicted.append(slot.name)
            freed += slot_gb
        return evicted

    # -- generation with OOM defense -------------------------------------
    def generate(self, model: str, prompt: str, options: Optional[dict] = None,
                 timeout: float = 300.0):
        from reins.harness.models import ModelRouter, RouteResult

        slot = self._slot(model)
        slot.state = ModelState.BUSY
        self._publish_state()
        merged_options = {**self.options_for(model), **(options or {})}

        for attempt in range(2):
            try:
                text = local.generate(model, prompt, host=self.host,
                                       timeout=timeout, options=merged_options)
                slot.state = ModelState.READY
                slot.last_used = time.time()
                self._publish_state()
                return RouteResult(text, model, "ollama", "amdy", ok=True)
            except Exception as e:
                log_degradation(__name__)
                slot.state, slot.error = ModelState.ERROR, str(e)
                self._publish_state()
                self.evict_lru(self.estimate_gb(model))
                if attempt == 0:
                    continue
                self._log_trail_failure(model, str(e))
                return ModelRouter().route("general chatting", prompt)

    def generate_category(self, category: str, prompt: str):
        from reins.harness.models import ModelRouter

        spec = ModelRouter().optimal(category, "amdy")
        return self.generate(spec.model, prompt)

    # -- internals ----------------------------------------------------------
    def _slot(self, model: str) -> ModelSlot:
        if model not in self._slots:
            self._slots[model] = ModelSlot(name=model)
        return self._slots[model]

    def _sync_from_ollama(self) -> None:
        try:
            resident = {m["name"]: m for m in local.loaded_models(self.host)}
        except Exception:
            log_degradation(__name__)
            return
        for name, info in resident.items():
            slot = self._slot(name)
            if slot.state not in (ModelState.LOADING, ModelState.UNLOADING):
                slot.state = ModelState.READY if slot.state != ModelState.BUSY else slot.state
            size_vram = info.get("size_vram")
            if size_vram:
                slot.est_gb = round(size_vram / (1024 ** 3), 2)
            slot.last_used = slot.last_used or time.time()
        for name, slot in self._slots.items():
            if name not in resident and slot.state in (ModelState.READY,):
                slot.state = ModelState.UNLOADED
                slot.est_gb = 0.0

    def _publish_state(self) -> None:
        """FBE: every transition fires the notification. Best-effort — a
        SharedState write failure never blocks the coordinator's caller."""
        try:
            from reins.harness.ipc import SharedState

            SharedState().write({
                "ts": time.time(),
                "slots": {n: {"state": s.state.value, "est_gb": s.est_gb} for n, s in self._slots.items()},
            })
        except Exception:
            log_degradation(__name__)
            pass

    def _log_trail_failure(self, model: str, error: str) -> None:
        try:
            from reins.services.task_trail import TaskTrail
            import uuid

            TaskTrail().upsert_task(
                str(uuid.uuid4()), task_type="coordinator_generate", status="failed",
                model=model, error=error, target_node="amdy",
            )
        except Exception:
            log_degradation(__name__)
            pass  # honest-failure logging is best-effort; never crash on it


_coordinator: Optional[ModelCoordinator] = None


def get_coordinator() -> ModelCoordinator:
    global _coordinator
    if _coordinator is None:
        _coordinator = ModelCoordinator()
    return _coordinator
