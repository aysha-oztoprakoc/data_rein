from reins.harness import external_io
from reins.services.logger import get_logger
from reins.services.task_trail import TaskTrail

logger = get_logger("harness_bootstrapper")

TRAIL_EVENT_TOPIC = "data_rein/trail/updated"


class HarnessBootstrapper:
    def __init__(self):
        self.trail: TaskTrail = TaskTrail()

    def resume_pending_tasks(self):
        """Notify the fleet (PON) so the reactive data-ody fallback drains any backlog.

        We do NOT pre-mark tasks 'running' — that used to make them look picked up
        while nothing dispatched them. Instead we emit one trail-updated notification;
        ``OdysseusAgent`` (subscribed to it) claims and executes pending/running work.
        Degrades cleanly to a no-op when no broker is present.
        """
        pending = self.trail.fallback_candidates()
        if not pending:
            logger.info("No data-ody fallback tasks found.")
            return

        logger.info(f"Found {len(pending)} data-ody fallback task(s); notifying the fleet.")
        try:
            external_io.mqtt_publish_single(TRAIL_EVENT_TOPIC, payload="resume")
            logger.info("Resume notification published to the fleet.")
        except Exception as e:  # graceful degradation
            logger.info(f"Could not notify broker ({e}); daemons will pick up on next event.")

    def bootstrap(self):
        self.resume_pending_tasks()
