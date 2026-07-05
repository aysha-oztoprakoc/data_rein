import json
import threading
from typing import Any, Dict
from reins.services.logger import get_logger
from reins.harness.agents import HarnessAgent

logger = get_logger("subagent_manager")

class SubagentManager(HarnessAgent):
    """
    PON-compliant Subagent Orchestrator (the data-hermes routing service).
    Listens for instigations to spawn subagents and routes them through the single
    model-agnostic harness router (local-first, graceful amdy<->tell failover).
    """
    role = "data-hermes"

    def __init__(self, mqtt_client: Any) -> None:
        super().__init__()
        self.mqtt = mqtt_client

        # Subscribe to spawn events
        self.mqtt.subscribe("data_rein/subagents/spawn")
        self.mqtt.message_callback_add("data_rein/subagents/spawn", self.on_spawn_request)
        logger.info("Subagent Manager online. Waiting for instigations (Zero Polling).")

    def on_spawn_request(self, client: Any, userdata: Any, msg: Any) -> None:
        """
        Event handler for spawning a new subagent.
        Spawns a daemon thread to prevent blocking the MQTT loop (Graceful Degradation/PON Rule).
        """
        try:
            payload = json.loads(msg.payload.decode("utf-8"))
            thread = threading.Thread(
                target=self._execute_subagent,
                args=(payload,),
                daemon=True
            )
            thread.start()
        except Exception as e:
            logger.error(f"Failed to process subagent spawn request: {e}")

    def _execute_subagent(self, payload: Dict[str, Any]) -> None:
        """
        Executes the subagent logic completely asynchronously.
        """
        task_type = payload.get("task_type", "General Chatting")
        prompt = payload.get("prompt", "")
        node = payload.get("node", "amdy")
        reply_topic = payload.get("reply_topic", "data_rein/subagents/result")
        
        if not prompt:
            logger.error("Subagent spawned with empty prompt.")
            return

        logger.info(f"Spawning '{task_type}' subagent on node '{node}'...")

        # Log to the shared Task Trail so this ephemeral subagent is visible
        # to `agent_status()`/`trail_list()` and the Sofia dashboard, under
        # owner `self.role` (data-hermes). Never blocks/raises - trail may be
        # unavailable (HarnessAgent sets it to None on init failure).
        task_id = None
        if self.trail is not None:
            try:
                task_id = self.trail.create_task(f"{self.role}:subagent:{task_type}", prompt, node)
                self.trail.set_status(task_id, "running")
            except Exception:
                task_id = None

        # Route through the single model-agnostic harness router.
        res = self.infer(task_type, prompt, node=node)

        if task_id is not None:
            try:
                self.trail.set_status(task_id, "success" if res.ok else "failed")
            except Exception:
                pass

        # Publish result back
        if res.ok:
            self.mqtt.publish(reply_topic, json.dumps({
                "status": "success",
                "task_type": task_type,
                "node": res.node,
                "model": res.model,
                "output": res.text
            }))
            logger.info(f"Subagent '{task_type}' completed on {res.model}.")
        else:
            self.mqtt.publish(reply_topic, json.dumps({
                "status": "error",
                "task_type": task_type,
                "node": node,
                "output": f"Inference degraded gracefully: {res.error}"
            }))
