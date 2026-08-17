"""Read-only Task Trail endpoints (SOFIA³ Tasks view).

Read-only by design (decision #3): no /api/control, no model execution. The
Task Trail in `~/.config/data_nexus/task_trail.sqlite3` is the source of truth;
live updates arrive over the WebSocket bridge (`live.py`).
"""

from __future__ import annotations

from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Query

from reins.services.task_trail import TaskTrail

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


def _summarize(tasks: list[dict[str, Any]]) -> dict[str, int]:
    summary: dict[str, int] = {}
    for task in tasks:
        status = str(task.get("status", "pending")).lower()
        summary[status] = summary.get(status, 0) + 1
    return summary


@router.get("")
def list_tasks(
    status: Optional[str] = Query(None, description="Filter by status (all/success/failed/running/pending)"),
    target: Optional[str] = Query(None, description="Filter by target_node"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
) -> dict[str, Any]:
    """List task trail records with optional filters."""
    try:
        trail = TaskTrail()
        tasks = trail.all_tasks()
        if status and status.lower() not in ("all", ""):
            wanted = status.lower()
            tasks = [t for t in tasks if str(t.get("status", "")).lower() == wanted]
        if target:
            tasks = [t for t in tasks if str(t.get("target_node", "")) == target]
        tasks.sort(key=lambda t: float(t.get("timestamp", 0.0)), reverse=True)
        page = tasks[offset : offset + limit]
        return {"tasks": page, "total": len(tasks), "summary": _summarize(tasks)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/summary")
def task_summary() -> dict[str, Any]:
    """Aggregated task counts by status and target node."""
    try:
        trail = TaskTrail()
        tasks = trail.all_tasks()
        return {
            "summary": _summarize(tasks),
            "total": len(tasks),
            "by_target": _by_target(tasks),
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


def _by_target(tasks: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    by_target: dict[str, dict[str, Any]] = {}
    for task in tasks:
        target = str(task.get("target_node", "unknown"))
        bucket = by_target.setdefault(target, {"total": 0, "status": {}})
        bucket["total"] += 1
        status = str(task.get("status", "pending")).lower()
        bucket["status"][status] = bucket["status"].get(status, 0) + 1
    return by_target


@router.get("/{task_id}")
def get_task(task_id: str) -> dict[str, Any]:
    """Fetch one task record."""
    try:
        trail = TaskTrail()
        task = trail.get_task(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"task": task}
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))