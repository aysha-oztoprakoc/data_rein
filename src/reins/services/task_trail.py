import os
import json
import uuid
import time
from typing import Dict, Any, List
from reins.services.logger import get_logger

logger = get_logger("task_trail")

class TaskTrail:
    """
    Manages the persistent loop-agentic task trail (state machine) for graceful degradation.
    Logs every prompt dispatched by the orchestrator so it can be picked up if it fails.
    """
    def __init__(self) -> None:
        self.trail_path = os.path.expanduser("~/.config/data_nexus/task_trail.json")
        os.makedirs(os.path.dirname(self.trail_path), exist_ok=True)
        
        if not os.path.exists(self.trail_path):
            self._save([])

    def _load(self) -> List[Dict[str, Any]]:
        try:
            with open(self.trail_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _save(self, data: List[Dict[str, Any]]) -> None:
        try:
            with open(self.trail_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save task trail: {e}")

    def create_task(self, task_type: str, prompt: str, target_node: str) -> str:
        task_id = str(uuid.uuid4())
        trail = self._load()
        trail.append({
            "task_id": task_id,
            "task_type": task_type,
            "prompt": prompt,
            "target_node": target_node,
            "status": "pending",
            "timestamp": time.time(),
            "attempts": 0
        })
        self._save(trail)
        return task_id

    def update_task(self, task_id: str, status: str) -> None:
        trail = self._load()
        for t in trail:
            if t["task_id"] == task_id:
                t["status"] = status
                if status == "running":
                    t["attempts"] += 1
                break
        self._save(trail)

    def get_failed_tasks(self) -> List[Dict[str, Any]]:
        trail = self._load()
        return [t for t in trail if t["status"] == "failed"]
