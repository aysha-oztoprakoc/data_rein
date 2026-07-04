"""
The Universal Task Trail — the single shared state machine every data_rein agent
reads/writes to know what the others are doing (see PRIME_DIRECTIVE §5).

Hardened for the converged agent fleet:
* Path comes from ``reins.harness.paths`` (one canonical location, env-overridable).
* Mutations are serialized with an ``fcntl`` advisory lock and persisted with an
  atomic temp-file ``os.replace`` — concurrent agents can no longer corrupt the JSON.
* Services use the public API (``upsert_task`` / ``set_status`` / ``by_status`` /
  ``all_tasks``) instead of reaching into ``_load`` / ``_save``.
"""

import os
import json
import uuid
import time
import fcntl
from contextlib import contextmanager
from typing import Dict, Any, List, Optional

from reins.services.logger import get_logger
from reins.harness import paths

logger = get_logger("task_trail")


class TaskTrail:
    """Persistent, lock-protected task ledger for graceful-degradation handoff."""

    def __init__(self) -> None:
        paths.ensure_state_dir()
        self.trail_path = str(paths.task_trail())
        self._lock_path = self.trail_path + ".lock"
        if not os.path.exists(self.trail_path):
            self._atomic_write([])

    # -- low-level (private) --------------------------------------------------
    @contextmanager
    def _flock(self):
        """Exclusive advisory lock held on a sidecar file for the mutation window."""
        f = open(self._lock_path, "w")
        try:
            fcntl.flock(f, fcntl.LOCK_EX)
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()

    def _load(self) -> List[Dict[str, Any]]:
        try:
            with open(self.trail_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _atomic_write(self, data: List[Dict[str, Any]]) -> None:
        tmp = f"{self.trail_path}.{os.getpid()}.tmp"
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, self.trail_path)  # atomic on POSIX
        except Exception as e:
            logger.error(f"Failed to persist task trail: {e}")
            try:
                os.path.exists(tmp) and os.remove(tmp)
            except Exception:
                pass

    @contextmanager
    def _mutate(self):
        """Lock, load, yield the list for in-place edits, then persist atomically."""
        with self._flock():
            trail = self._load()
            yield trail
            self._atomic_write(trail)

    # -- public read API ------------------------------------------------------
    def all_tasks(self) -> List[Dict[str, Any]]:
        return self._load()

    def by_status(self, *statuses: str) -> List[Dict[str, Any]]:
        want = set(statuses)
        return [t for t in self._load() if t.get("status") in want]

    def get_task(self, task_id: str) -> Optional[Dict[str, Any]]:
        return next((t for t in self._load() if t.get("task_id") == task_id), None)

    def get_failed_tasks(self) -> List[Dict[str, Any]]:
        return self.by_status("failed")

    # -- public write API -----------------------------------------------------
    def create_task(self, task_type: str, prompt: str, target_node: str) -> str:
        task_id = str(uuid.uuid4())
        with self._mutate() as trail:
            trail.append({
                "task_id": task_id,
                "task_type": task_type,
                "prompt": prompt,
                "target_node": target_node,
                "status": "pending",
                "timestamp": time.time(),
                "attempts": 0,
            })
        return task_id

    def update_task(self, task_id: str, status: str) -> None:
        self.set_status(task_id, status)

    def set_status(self, task_id: str, status: str) -> None:
        with self._mutate() as trail:
            for t in trail:
                if t.get("task_id") == task_id:
                    t["status"] = status
                    if status in ("running", "running_fallback"):
                        t["attempts"] = t.get("attempts", 0) + 1
                    break

    def upsert_task(self, task_id: str, **fields: Any) -> str:
        """Insert a task by an explicit (often deterministic) id, or update it in place.

        Used by producers like the AGY bridge that derive stable ids and re-sync
        idempotently. Unknown fields are stored; sensible defaults fill the rest.
        """
        with self._mutate() as trail:
            for t in trail:
                if t.get("task_id") == task_id:
                    t.update(fields)
                    t.setdefault("timestamp", time.time())
                    break
            else:
                record = {
                    "task_id": task_id,
                    "task_type": fields.pop("task_type", "generic"),
                    "prompt": fields.pop("prompt", ""),
                    "target_node": fields.pop("target_node", "amdy"),
                    "status": fields.pop("status", "pending"),
                    "timestamp": time.time(),
                    "attempts": 0,
                }
                record.update(fields)
                trail.append(record)
        return task_id

    def clear(self) -> None:
        with self._mutate() as trail:
            trail.clear()
