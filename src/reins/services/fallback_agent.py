from typing import Any, List, Dict

from reins.services.logger import get_logger
from reins.services.harness_bootstrapper import HarnessBootstrapper
from reins.harness.agents import HarnessAgent
from reins.harness import external_io

logger = get_logger("odysseus_agent")

TRAIL_EVENT_TOPIC = "data_rein/trail/updated"


class OdysseusAgent(HarnessAgent):
    """
    Local Odysseus AI persona daemon (the data-ody fallback service).

    Reacts to TaskTrail changes for tasks assigned to 'data-ody', gracefully taking
    over 'pending'/'running' tasks when the cloud API fails.

    PON-compliant: it does NOT poll. It drains any backlog once on startup, then
    blocks on the MQTT event loop (epoll-based, ~0% idle CPU) and reacts to trail
    notifications via callback. There is no `while True` / `time.sleep` spin-wait.
    """

    role = "data-ody"

    def __init__(self):
        super().__init__()
        # Tiered fallback chain optimized for hardware (AMD Ryzen 7, 8GB VRAM) & V2 Budget Plan
        self.fallback_chain = [
            {"model": "qwen2.5-coder:1.5b", "type": "local"}, # Fast CPU execution
            {"model": "qwen2.5-coder:7b", "type": "local"},   # Heavy local execution
            {"model": "gpt-4o-mini", "type": "cloud"}         # Supreme Court fallback
        ]
        self.bootstrapper = HarnessBootstrapper()

    def query_tiered_fallback(self, prompt: str) -> str:
        """
        Executes the tiered fallback chain. Degrades gracefully across models
        and planes (local -> cloud) per the V2 architecture.
        """
        from reins.harness import local
        from reins.harness.models import ModelRouter
        
        last_error = ""
        for tier in self.fallback_chain:
            try:
                logger.info(f"Attempting fallback tier: {tier['model']} ({tier['type']})")
                if tier["type"] == "local":
                    local.ensure_server()
                    return local.generate(tier["model"], prompt)
                else:
                    router = ModelRouter()
                    # We pass the provider explicitly via the model string's prefix, or use openai for gpt models.
                    provider = "openai" if "gpt" in tier["model"] else tier["model"].split("-")[0]
                    result = router.route_cloud(prompt, provider=provider)
                    if result.ok and result.text:
                        return result.text
                    last_error = result.error
            except Exception as e:
                logger.warning(f"Tier {tier['model']} failed: {e}")
                last_error = str(e)
                continue
                
        logger.error("All fallback tiers exhausted.")
        return f"Error: Fallback chain completely exhausted. Last error: {last_error}"

    def process_pending(self) -> List[Dict[str, Any]]:
        """
        Reactive handler: execute every pending/running task once and return the
        list of tasks acted upon. Each task is wrapped so one failure degrades that
        task (marked 'failed') without aborting the drain or crashing the daemon.
        """
        acted: List[Dict[str, Any]] = []
        if self.trail is None:
            logger.warning("OdysseusAgent.process_pending: trail unavailable, skipping")
            return acted
        pending = self.trail.fallback_candidates()

        for task in pending:
            task_id = task.get("task_id")
            try:
                self.trail.update_task(task_id, "running_fallback")
                logger.info(f"[Odysseus] Processing task {task_id}: {task.get('prompt', '')[:50]}...")
                result = self.query_tiered_fallback(task.get("prompt", ""))

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
                except Exception as status_error:
                    logger.error(
                        f"[Odysseus] Could not record failed status for task {task_id}: "
                        f"{status_error}"
                    )
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
            client.on_connect = lambda c, u, f, rc: external_io.mqtt_subscribe(
                c, TRAIL_EVENT_TOPIC
            )
            client.message_callback_add(TRAIL_EVENT_TOPIC, self._on_trail_event)
            _ = external_io.mqtt_connect(client, "localhost", 1883, 60)
            client.loop_forever()  # blocking, epoll-based — PON-compliant, 0% idle CPU
        except KeyboardInterrupt:
            logger.info("Odysseus daemon shutting down gracefully.")
        except Exception as e:
            # Graceful degradation: broker absent -> we already drained the backlog.
            logger.error(f"MQTT event loop unavailable ({e}); backlog drained, exiting cleanly.")
