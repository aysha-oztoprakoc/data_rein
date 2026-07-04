import os
import json
import time
import subprocess
import threading
from typing import Any, Optional

from reins.services.logger import get_logger
from reins.harness import paths, local

logger = get_logger("cookbook_evaluator")


class CookbookEvaluator:
    """
    Benchmarks the installed Ollama models (the Odysseus cookbook suite): a quick
    logic + speed probe, gated at score >= 85. Converged onto the harness planes —
    local models run through ``reins.harness.local`` (clean HTTP, auto-started
    server), remote (``tell``) models over SSH — instead of raw ``ollama`` shells.
    Results feed back into the model registry / router tiers.
    """

    PASS_SCORE = 85

    def __init__(self, mqtt_client: Any = None) -> None:
        self.mqtt = mqtt_client
        self.registry_path = str(paths.model_registry())
        if self.mqtt is not None:
            self.mqtt.subscribe("data_rein/cookbook/trigger")
            self.mqtt.message_callback_add("data_rein/cookbook/trigger", self.on_trigger)
        logger.info("Cookbook Evaluator online. Ready to benchmark.")

    def on_trigger(self, client: Any, userdata: Any, msg: Any) -> None:
        threading.Thread(target=self.run_evaluations, daemon=True).start()

    def evaluate_model(self, model: str, node: str = "amdy") -> int:
        """Run the cookbook logic+speed probe against one model on one node."""
        prompt = "Answer exactly 'SUCCESS' if 5 * 5 is 25. Say nothing else."
        try:
            start = time.time()
            if node == "amdy":
                local.ensure_server()
                output = local.generate(model, prompt)  # raises on failure
            else:
                res = subprocess.run(
                    ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=3", node, "ollama", "run", model],
                    input=prompt.encode("utf-8"), capture_output=True, timeout=25,
                )
                if res.returncode != 0:
                    return 0
                output = res.stdout.decode("utf-8")
            elapsed = time.time() - start

            score = 100
            if "SUCCESS" not in output.strip().upper():
                score -= 30  # logic failure
            if elapsed > 10.0:
                score -= 20  # too slow on this hardware
            return score
        except Exception as e:  # graceful degradation
            logger.error(f"Failed to evaluate {model} on {node}: {e}")
            return 0

    def _models_for(self, registry: dict, node: str) -> list:
        node_data = registry.get(node, {})
        # New getinfo format: models_fit=[{model,...}]; tolerate the legacy `models` key.
        entries = node_data.get("models_fit") or node_data.get("models") or []
        return [e["model"] for e in entries if isinstance(e, dict) and e.get("model")]

    def run_evaluations(self) -> Optional[dict]:
        if not os.path.exists(self.registry_path):
            logger.error("Model registry not found. Run getinfo (sys_profiler) first.")
            return None
        with open(self.registry_path, "r") as f:
            registry = json.load(f)

        results: dict = {"amdy": {}, "tell": {}}
        for node in ("amdy", "tell"):
            for name in self._models_for(registry, node):
                logger.info(f"Evaluating {name} on {node}...")
                score = self.evaluate_model(name, node)
                results[node][name] = score
                if score >= self.PASS_SCORE:
                    logger.info(f"{name} PASSED cookbook (score {score}).")
                else:
                    logger.warning(f"{name} FAILED cookbook (score {score}).")

        if self.mqtt is not None:
            self.mqtt.publish("data_rein/cookbook/result", json.dumps({"status": "success", "evaluations": results}))
        return results
