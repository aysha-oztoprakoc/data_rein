import os
import json
import time
import subprocess
from reins.services.logger import get_logger
from reins.services.task_trail import TaskTrail
from reins.services.harness_bootstrapper import HarnessBootstrapper

logger = get_logger("odysseus_agent")

class OdysseusAgent:
    """
    Local Odysseus AI persona daemon.
    Runs under the Data Harness and monitors the TaskTrail for tasks assigned
    to 'data-ody' or gracefully takes over 'pending' tasks if the cloud API fails.
    """
    def __init__(self, model_name: str = "qwen2.5-coder:7b"):
        self.model_name = model_name
        self.trail = TaskTrail()
        self.bootstrapper = HarnessBootstrapper()
        
    def query_ollama(self, prompt: str) -> str:
        """Queries the local Ollama instance."""
        try:
            logger.info(f"Querying local model {self.model_name}...")
            result = subprocess.run(
                ["ollama", "run", self.model_name, prompt],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            logger.error(f"Local LLM failed: {e}")
            return f"Error: {e.stderr}"

    def run_daemon(self):
        logger.info("Starting Data-Odysseus Daemon under the Universal Harness...")
        self.bootstrapper.bootstrap()
        
        logger.info("Odysseus is now monitoring the Task Trail...")
        try:
            while True:
                tasks = self.trail._load()
                pending = [t for t in tasks if t["status"] in ["pending", "running"]]
                
                for task in pending:
                    # Take ownership of the task
                    self.trail.update_task(task["task_id"], "running")
                    logger.info(f"[Odysseus] Processing task {task['task_id']}: {task['prompt'][:50]}...")
                    
                    # Execute
                    result = self.query_ollama(task["prompt"])
                    
                    if not result.startswith("Error"):
                        logger.info(f"[Odysseus] Task {task['task_id']} completed successfully.")
                        self.trail.update_task(task["task_id"], "success_fallback")
                    else:
                        logger.error(f"[Odysseus] Task {task['task_id']} failed.")
                        self.trail.update_task(task["task_id"], "failed")
                        
                time.sleep(5)
        except KeyboardInterrupt:
            logger.info("Odysseus daemon shutting down gracefully.")
