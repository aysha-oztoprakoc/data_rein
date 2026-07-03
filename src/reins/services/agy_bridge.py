import os
import glob
import re
import time
from reins.services.task_trail import TaskTrail
from reins.services.logger import get_logger

logger = get_logger("agy_bridge")

class AGYBridge:
    """
    Synchronizes Antigravity's internal Markdown task checklists (task.md)
    into the Hermes Universal Task Trail (task_trail.json).
    """
    def __init__(self) -> None:
        self.trail = TaskTrail()
        # Path where Antigravity stores conversation brain artifacts
        self.agy_brains_dir = os.path.expanduser("~/.gemini/antigravity-cli/brain")

    def scan_and_sync(self) -> None:
        """Finds all task.md files, parses checkboxes, and pushes to Hermes JSON."""
        task_files = glob.glob(os.path.join(self.agy_brains_dir, "*", "task.md"))
        
        if not task_files:
            logger.info("No AGY task files found to sync.")
            return

        hermes_tasks = self.trail._load()
        existing_ids = {t.get("task_id") for t in hermes_tasks}
        
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
                line = line.strip()
                match = re.match(r'- \[( |x|/)\] (.*)', line)
                if match:
                    state_char = match.group(1)
                    task_desc = match.group(2)
                    
                    # Generate a deterministic ID based on conv_id and line number
                    task_id = f"AGY-{conv_id}-L{i}"
                    
                    status = "pending"
                    if state_char == "x":
                        status = "success"
                    elif state_char == "/":
                        status = "running"
                        
                    # If exists, update
                    if task_id in existing_ids:
                        for t in hermes_tasks:
                            if t["task_id"] == task_id:
                                t["status"] = status
                                break
                    else:
                        # Create new
                        hermes_tasks.append({
                            "task_id": task_id,
                            "task_type": "AGY Checkbox",
                            "prompt": task_desc,
                            "target_node": "AGY-Frontend",
                            "status": status,
                            "timestamp": time.time(),
                            "attempts": 1
                        })
                        existing_ids.add(task_id)
                        synced_count += 1

        self.trail._save(hermes_tasks)
        logger.info(f"AGY Bridge Sync Complete. Synced {synced_count} new tasks.")
