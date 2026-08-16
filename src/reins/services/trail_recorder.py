"""TrailRecorder — canonical helper for making the Task Trail the authoritative
record of every plan and execution step agents perform on the harness.

Why this exists: agents previously made changes without recording them, so the
Trail degraded to session/breaker noise and sessions lost continuity (crashed
into a dead end). This service gives every client (CLI, OpenCode plugin, MCP,
or direct call) one consistent way to:
  * record_plan: open a plan record with optional full plan text,
  * append_step: append an executed step (with its commits + files changed),
  * finish_plan: mark the plan done.

It is a thin, graceful wrapper over TaskTrail.upsert_task; it never creates a
second database. All writes are idempotent keyed by a stable task id.
"""

from __future__ import annotations

import time
from typing import Any

from reins.services.logger import get_logger
from reins.services.task_trail import TaskTrail

logger = get_logger(__name__)


class TrailRecorder:
    def __init__(self, trail: TaskTrail | None = None) -> None:
        self._trail = trail or TaskTrail()

    @staticmethod
    def _now() -> float:
        return time.time()

    def record_plan(
        self,
        *,
        task_id: str,
        task_type: str = "plan",
        prompt: str = "",
        target_node: str = "amdy",
        plan_md: str = "",
        author: str = "",
        extra: dict[str, Any] | None = None,
    ) -> str:
        """Open (or update) a plan record. task_id must be stable so later
        steps can be appended across sessions. Returns the task_id."""
        fields: dict[str, Any] = {
            "status": "active",
            "kind": "plan",
            "author": author,
        }
        if plan_md:
            fields["plan_md"] = plan_md
        if extra:
            fields.update(extra)
        return self._trail.upsert_task(
            task_id,
            task_type=task_type,
            prompt=prompt,
            target_node=target_node,
            **fields,
        )

    def append_step(
        self,
        task_id: str,
        summary: str,
        *,
        status: str = "success",
        commits: list[str] | None = None,
        files: list[str] | None = None,
        detail: str = "",
        target_node: str = "amdy",
    ) -> None:
        """Append one executable step to a plan record. Leaves the plan active
        so follow-up sessions can keep appending; set finish_plan to close it."""
        record = self._trail.get_task(task_id)
        if record is None:
            logger.warning("append_step: unknown plan id %s; creating stub", task_id)
            self.record_plan(task_id=task_id, prompt=summary, target_node=target_node)
            record = self._trail.get_task(task_id)
            if record is None:
                logger.warning("append_step: could not (re)create %s", task_id)
                return
        steps = list(record.get("steps") or [])
        step = {
            "index": len(steps) + 1,
            "ts": self._now(),
            "summary": summary,
            "status": status,
            "commits": list(commits or []),
            "files": list(files or []),
            "detail": detail,
        }
        steps.append(step)
        fields: dict[str, Any] = {"steps": steps, "steps_count": len(steps)}
        # keep the plan record alive unless the step itself is terminal/failed
        if status in ("failed", "failed_fallback"):
            fields["status"] = "failed" if status == "failed" else "running"
        self._trail.upsert_task(task_id, target_node=target_node, **fields)

    def finish_plan(self, task_id: str, status: str = "success") -> None:
        """Mark a plan complete. Preserves the recorded steps/plan text."""
        if self._trail.get_task(task_id) is None:
            logger.warning("finish_plan: unknown plan id %s", task_id)
            return
        self._trail.upsert_task(task_id, status=status, kind="plan", finished_at=time.time())