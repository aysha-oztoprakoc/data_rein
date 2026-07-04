import os
import json
from reins.services.logger import get_logger
from reins.services.task_trail import TaskTrail

logger = get_logger("harness_bootstrapper")

class HarnessBootstrapper:
    def __init__(self):
        self.knowledge_dir = os.path.expanduser("~/data_rein/knowledge_base")
        self.trail = TaskTrail()

    def cache_knowledge_base(self):
        """Reads and caches the knowledge database."""
        logger.info("Initializing knowledge base cache...")
        if not os.path.exists(self.knowledge_dir):
            logger.warning(f"Knowledge base directory not found at {self.knowledge_dir}")
            return

        cache = {}
        for root, dirs, files in os.walk(self.knowledge_dir):
            for file in files:
                if file.endswith(".md") or file.endswith(".xml"):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            cache[filepath] = f.read()
                    except Exception as e:
                        logger.error(f"Failed to cache {filepath}: {e}")
        
        logger.info(f"Cached {len(cache)} knowledge documents in memory.")
        # Store in a global attribute if needed by other components
        self.memory_cache = cache
        return cache

    def resume_pending_tasks(self):
        """Picks up from where it left off, independently of remote/local agent."""
        logger.info("Checking task trail for pending or interrupted tasks...")
        tasks = self.trail._load()
        pending_tasks = [t for t in tasks if t["status"] in ["pending", "running"]]
        
        if not pending_tasks:
            logger.info("No pending tasks found. System is caught up.")
            return

        logger.info(f"Found {len(pending_tasks)} pending/running task(s). Resuming...")
        for task in pending_tasks:
            logger.info(f"Resuming Task [{task['task_id']}] - Node: {task['target_node']} - Prompt: {task['prompt'][:50]}...")
            # We mark as running to signify it has been picked up
            self.trail.update_task(task["task_id"], "running")
            # In a full implementation, we dispatch to fallback_agent or remote node here.

    def bootstrap(self):
        self.cache_knowledge_base()
        self.resume_pending_tasks()
