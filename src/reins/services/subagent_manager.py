import json
import threading
from typing import Any, Dict
from reins.services.logger import get_logger
from reins.services.data_nexus.reasoning_engine import UniversalModelRouter

logger = get_logger("subagent_manager")

class SubagentManager:
    """
    PON-compliant Subagent Orchestrator.
    Listens for instigations to spawn subagents and routes them using the Universal Model Harness.
    """
    def __init__(self, mqtt_client: Any) -> None:
        self.mqtt = mqtt_client
        self.router = UniversalModelRouter()
        
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
        
        # Route through the universal harness
        result = self.router.route_inference(task_type, prompt, target_node=node)
        
        # Publish result back
        if result:
            self.mqtt.publish(reply_topic, json.dumps({
                "status": "success",
                "task_type": task_type,
                "node": node,
                "output": result
            }))
            logger.info(f"Subagent '{task_type}' completed successfully.")
        else:
            self.mqtt.publish(reply_topic, json.dumps({
                "status": "error",
                "task_type": task_type,
                "node": node,
                "output": "Inference failed or degraded gracefully."
            }))
