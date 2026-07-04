import subprocess
from typing import Any, List, Dict

from reins.services.logger import get_logger
from reins.services.task_trail import TaskTrail
from reins.services.harness_bootstrapper import HarnessBootstrapper

logger = get_logger("odysseus_agent")

TRAIL_EVENT_TOPIC = "data_rein/trail/updated"


class OdysseusAgent:
    """
    Local Odysseus AI persona daemon.

    Runs under the Data Harness and reacts to TaskTrail changes for tasks assigned
    to 'data-ody', gracefully taking over 'pending'/'running' tasks when the cloud
    API fails.

    PON-compliant: it does NOT poll. It drains any backlog once on startup, then
    blocks on the MQTT event loop (epoll-based, ~0% idle CPU) and reacts to trail
    notifications via callback. There is no `while True` / `time.sleep` spin-wait.
    """

    def __init__(self, model_name: str = "qwen2.5-coder:7b"):
        self.model_name = model_name
        self.trail = TaskTrail()
        self.bootstrapper = HarnessBootstrapper()

    def query_ollama(self, prompt: str) -> str:
        """Queries the local Ollama instance. Degrades to an error string, never raises."""
        try:
            logger.info(f"Querying local model {self.model_name}...")
            result = subprocess.run(
                ["ollama", "run", self.model_name, prompt],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout
        except Exception as e:  # graceful degradation
            stderr = getattr(e, "stderr", "") or str(e)
            logger.error(f"Local LLM failed: {stderr}")
            return f"Error: {stderr}"

    def process_pending(self) -> List[Dict[str, Any]]:
        """
        Reactive handler: execute every pending/running task once and return the
        list of tasks acted upon. Each task is wrapped so one failure degrades that
        task (marked 'failed') without aborting the drain or crashing the daemon.
        """
        acted: List[Dict[str, Any]] = []
        tasks = self.trail._load()
        pending = [t for t in tasks if t.get("status") in ("pending", "running")]

        for task in pending:
            task_id = task.get("task_id")
            try:
                self.trail.update_task(task_id, "running")
                logger.info(f"[Odysseus] Processing task {task_id}: {task.get('prompt', '')[:50]}...")
                result = self.query_ollama(task.get("prompt", ""))

                if not result.startswith("Error"):
                    logger.info(f"[Odysseus] Task {task_id} completed successfully.")
                    self.trail.update_task(task_id, "success_fallback")
                else:
                    logger.error(f"[Odysseus] Task {task_id} failed.")
                    self.trail.update_task(task_id, "failed")
            except Exception as e:  # graceful degradation: never abort the whole drain
                logger.error(f"[Odysseus] Task {task_id} crashed, degrading to failed: {e}")
                try:
                    self.trail.update_task(task_id, "failed")
                except Exception:
                    pass
            acted.append(task)
        return acted

    def _on_trail_event(self, client: Any, userdata: Any, msg: Any) -> None:
        try:
            self.process_pending()
        except Exception as e:  # a callback must never take the loop down
            logger.error(f"[Odysseus] Trail event handler degraded: {e}")

    def run_daemon(self) -> None:
        """
        Start the reactive daemon. Drains the current backlog, then blocks on the
        MQTT event loop. If no broker is reachable, it degrades gracefully to the
        one-shot drain it already performed and exits (no busy-wait).
        """
        logger.info("Starting Data-Odysseus Daemon under the Universal Harness...")
        self.bootstrapper.bootstrap()

        # Drain anything already waiting (reactive catch-up, not polling).
        self.process_pending()

        logger.info("Odysseus is now reacting to Task Trail events...")
        try:
            import paho.mqtt.client as mqtt

            client = mqtt.Client()
            client.on_connect = lambda c, u, f, rc: c.subscribe(TRAIL_EVENT_TOPIC)
            client.message_callback_add(TRAIL_EVENT_TOPIC, self._on_trail_event)
            client.connect("localhost", 1883, 60)
            client.loop_forever()  # blocking, epoll-based — PON-compliant, 0% idle CPU
        except KeyboardInterrupt:
            logger.info("Odysseus daemon shutting down gracefully.")
        except Exception as e:
            # Graceful degradation: broker absent -> we already drained the backlog.
            logger.error(f"MQTT event loop unavailable ({e}); backlog drained, exiting cleanly.")
