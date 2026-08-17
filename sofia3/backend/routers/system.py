"""System/panel endpoints (SOFIA³ Tasks view — read-only).

All backing reads go through the same reins functions the MCP bridge uses, so
the dashboard can never diverge from what agents see. Slow probes (hardware,
train) are TTL-cached to keep the UI responsive.
"""

from __future__ import annotations

import time
from dataclasses import asdict
from typing import Any, Optional

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api", tags=["system"])

# -----------------------------------------------------------------------------
# Small TTL cache for expensive probes (hardware scan / train capability).
# -----------------------------------------------------------------------------
_TTL_CACHE: dict[str, tuple[float, dict[str, Any]]] = {}
_HARDWARE_TTL = 300.0   # 5 minutes
_TRAIN_TTL = 300.0


def _cached(key: str, ttl: float, producer: Any) -> dict[str, Any]:
    now = time.time()
    hit = _TTL_CACHE.get(key)
    if hit and now - hit[0] < ttl:
        return hit[1]
    try:
        value = producer()
    except Exception as exc:
        return {"degraded": True, "error": str(exc)}
    _TTL_CACHE[key] = (now, value)
    return value


# -----------------------------------------------------------------------------
# Agent activity + budgets
# -----------------------------------------------------------------------------
@router.get("/agents/status")
def agent_status() -> dict[str, Any]:
    """Summarize what every agent identity has been doing (Rule of Awareness)."""
    try:
        from reins.services.task_trail import TaskTrail

        trail = TaskTrail()
        tasks = trail.all_tasks()
        by_owner: dict[str, dict[str, int]] = {}
        for task in tasks:
            owner = str(task.get("task_type", "generic")).split(":", 1)[0]
            status = str(task.get("status", "unknown"))
            bucket = by_owner.setdefault(owner, {})
            bucket[status] = bucket.get(status, 0) + 1
        return {
            "by_owner": by_owner,
            "failed_tasks": trail.get_failed_tasks()[-10:],
            "total_tasks": len(tasks),
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/agents/budgets")
def agent_budgets() -> dict[str, Any]:
    """Every known agent's CPU%/GPU-VRAM-GB resource budget."""
    try:
        from reins.services.resource_budgets import load_budgets

        return {"budgets": load_budgets()}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# -----------------------------------------------------------------------------
# Coordinator / models / combos
# -----------------------------------------------------------------------------
@router.get("/coord")
def coordinator_status() -> dict[str, Any]:
    """Local model-residency coordinator slot state (loaded/busy, VRAM budget)."""
    try:
        from reins.harness.coordinator import get_coordinator

        return {"coordinator": get_coordinator().status()}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/models")
def models_show() -> dict[str, Any]:
    """All archetype categories and their mapped model combo IDs."""
    try:
        from reins.harness.combo_registry import ComboRegistry

        registry = ComboRegistry()
        cats: dict[str, dict[str, Any]] = {}
        for cat_name, cat_obj in registry.config.categories.items():
            cats[cat_name] = {
                "description": cat_obj.description,
                "amdy": list(cat_obj.amdy),
                "tell": list(cat_obj.tell),
                "cloud": list(cat_obj.cloud),
            }
        return {"categories": cats}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/combos")
def combo_list() -> dict[str, Any]:
    """Every combo and its current health/cooldown status."""
    try:
        from reins.harness.combo_registry import ComboRegistry

        registry = ComboRegistry()
        combos = []
        for combo in registry.all_combos():
            combos.append(
                {
                    "id": combo.id,
                    "provider": combo.provider,
                    "model": combo.model,
                    "tier": getattr(combo, "tier", "free"),
                    "node": getattr(combo, "node", "amdy"),
                }
            )
        return {"combos": combos}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# -----------------------------------------------------------------------------
# Token usage
# -----------------------------------------------------------------------------
@router.get("/tokens")
def token_usage() -> dict[str, Any]:
    """Self-tracked cloud usage and configured rolling-window budgets."""
    try:
        from reins.services.token_ledger import budget_report

        return {"report": budget_report()}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# -----------------------------------------------------------------------------
# Hardware + training (TTL-cached probes)
# -----------------------------------------------------------------------------
@router.get("/hardware")
def hardware_scan() -> dict[str, Any]:
    """Cluster profile (VRAM/RAM/CPU, model fit scoring) — cached 5 min."""
    def _probe() -> dict[str, Any]:
        from reins.services.sys_profiler import SysProfiler

        return {"profile": SysProfiler().profile_cluster(publish=False)}

    return _cached("hardware", _HARDWARE_TTL, _probe)


@router.get("/hardware/gaps")
def hardware_gaps() -> dict[str, Any]:
    """Capability gaps (quantization/ROCm) against harness needs — cached 5 min."""
    def _probe() -> dict[str, Any]:
        from reins.services.sys_profiler import SysProfiler

        return {"gaps": SysProfiler().gap_report()}

    return _cached("hardware_gaps", _HARDWARE_TTL, _probe)


@router.get("/train")
def train_status() -> dict[str, Any]:
    """QLoRA/LoRA capability probe (NF4/fp16/CPU chain) — cached 5 min."""
    def _probe() -> dict[str, Any]:
        from reins.training import capability

        return {"train": asdict(capability.probe())}

    return _cached("train", _TRAIN_TTL, _probe)


@router.get("/skills")
def skills_list() -> dict[str, Any]:
    """Canonical harness skills inventory."""
    try:
        from reins.harness.skill_registry import canonical_skills

        skills = canonical_skills()
        return {"skills": [{"name": s.name, "description": s.description} for s in skills]}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/panel/summary")
def panel_summary() -> dict[str, Any]:
    """One-shot aggregate for the Tasks screen: all panels in a single call."""
    from reins.services.task_trail import TaskTrail

    try:
        trail = TaskTrail()
        tasks = trail.all_tasks()
        by_owner: dict[str, dict[str, int]] = {}
        for task in tasks:
            owner = str(task.get("task_type", "generic")).split(":", 1)[0]
            status = str(task.get("status", "unknown"))
            bucket = by_owner.setdefault(owner, {})
            bucket[status] = bucket.get(status, 0) + 1
        summary: dict[str, int] = {}
        for task in tasks:
            st = str(task.get("status", "pending")).lower()
            summary[st] = summary.get(st, 0) + 1
        return {
            "total_tasks": len(tasks),
            "summary": summary,
            "by_owner": by_owner,
            "failed_tasks": trail.get_failed_tasks()[-10:],
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
