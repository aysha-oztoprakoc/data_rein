import os
import socket

from reins.services.logger import get_logger
from reins.services.task_trail import TaskTrail
from reins.harness import paths

logger = get_logger("harness_bootstrapper")

TRAIL_EVENT_TOPIC = "data_rein/trail/updated"


class HarnessBootstrapper:
    def __init__(self):
        self.knowledge_dir = str(paths.knowledge_base())
        self.trail = TaskTrail()
        self.memory_cache: dict = {}

    def cache_knowledge_base(self):
        """Reads and caches the knowledge base markdown/xml sources."""
        logger.info("Initializing knowledge base cache...")
        if not os.path.exists(self.knowledge_dir):
            logger.warning(f"Knowledge base directory not found at {self.knowledge_dir}")
            return {}

        cache = {}
        for root, _dirs, files in os.walk(self.knowledge_dir):
            for file in files:
                if file.endswith((".md", ".xml")):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            cache[filepath] = f.read()
                    except Exception as e:
                        logger.error(f"Failed to cache {filepath}: {e}")

        logger.info(f"Cached {len(cache)} knowledge documents in memory.")
        self.memory_cache = cache
        return cache

    @staticmethod
    def _broker_up(host: str = "localhost", port: int = 1883) -> bool:
        """Fast, non-blocking check so CLI startup never hangs on a dead broker."""
        try:
            with socket.create_connection((host, port), timeout=0.3):
                return True
        except Exception:
            return False

    def resume_pending_tasks(self):
        """Notify the fleet (PON) so the reactive data-ody fallback drains any backlog.

        We do NOT pre-mark tasks 'running' — that used to make them look picked up
        while nothing dispatched them. Instead we emit one trail-updated notification;
        ``OdysseusAgent`` (subscribed to it) claims and executes pending/running work.
        Degrades cleanly to a no-op when no broker is present.
        """
        pending = self.trail.by_status("pending", "running")
        if not pending:
            logger.info("No pending tasks found. System is caught up.")
            return

        logger.info(f"Found {len(pending)} pending/running task(s); notifying the fleet to resume.")
        if not self._broker_up():
            logger.info("No MQTT broker reachable; data-ody will drain the backlog on its next startup.")
            return
        try:
            import paho.mqtt.publish as publish
            publish.single(TRAIL_EVENT_TOPIC, payload="resume", hostname="localhost", port=1883)
            logger.info("Resume notification published to the fleet.")
        except Exception as e:  # graceful degradation
            logger.info(f"Could not notify broker ({e}); daemons will pick up on next event.")

    def bootstrap(self):
        self.cache_knowledge_base()
        self.resume_pending_tasks()
