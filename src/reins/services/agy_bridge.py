import os
import glob
import re

from reins.services.logger import get_logger
from reins.harness import paths
from reins.harness.agents import HarnessAgent

logger = get_logger("agy_bridge")


class AGYBridge(HarnessAgent):
    """
    The data-agy bridge: synchronizes Antigravity's internal Markdown task
    checklists (task.md) into the shared Universal Task Trail.

    Converged onto the harness spine: it is a ``HarnessAgent`` (role ``data-agy``)
    and mutates the trail only through its public, lock-safe API — never the
    private ``_load`` / ``_save`` internals.
    """

    role = "data-agy"

    def __init__(self) -> None:
        super().__init__()
        # Canonical location of Antigravity conversation brain artifacts.
        self.agy_brains_dir = str(paths.agy_brain_dir())

    def scan_and_sync(self) -> None:
        """Find all task.md files, parse checkboxes, upsert them into the trail."""
        if self.trail is None:
            logger.error("Task trail unavailable; cannot sync AGY tasks.")
            return

        task_files = glob.glob(os.path.join(self.agy_brains_dir, "*", "task.md"))
        if not task_files:
            logger.info("No AGY task files found to sync.")
            return

        synced_count = 0
        for filepath in task_files:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.readlines()
            except Exception as e:
                logger.error(f"Failed to read {filepath}: {e}")
                continue

            conv_id = os.path.basename(os.path.dirname(filepath))
            for i, line in enumerate(content):
                match = re.match(r"- \[( |x|/)\] (.*)", line.strip())
                if not match:
                    continue
                state_char, task_desc = match.group(1), match.group(2)
                status = {"x": "success", "/": "running"}.get(state_char, "pending")

                # Deterministic id -> idempotent upsert (safe to re-run any time).
                task_id = f"AGY-{conv_id}-L{i}"
                is_new = self.trail.get_task(task_id) is None
                self.trail.upsert_task(
                    task_id,
                    task_type="AGY Checkbox",
                    prompt=task_desc,
                    target_node="AGY-Frontend",
                    status=status,
                )
                if is_new:
                    synced_count += 1

        logger.info(f"AGY Bridge sync complete. {synced_count} new task(s) added.")
