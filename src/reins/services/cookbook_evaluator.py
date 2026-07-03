import os
import json
import subprocess
import time
import threading
from typing import Any
from reins.services.logger import get_logger

logger = get_logger("cookbook_evaluator")

class CookbookEvaluator:
    """
    Evaluates Ollama models by benchmarking them against the Cookbook Test Suite.
    Checks logical parsing and speed to ensure a performance score of >= 85.
    """
    def __init__(self, mqtt_client: Any) -> None:
        self.mqtt = mqtt_client
        self.registry_path = os.path.expanduser("~/data_rein/data-oby/TrainingData/model_registry.json")
        self.mqtt.subscribe("data_rein/cookbook/trigger")
        self.mqtt.message_callback_add("data_rein/cookbook/trigger", self.on_trigger)
        logger.info("Cookbook Evaluator online. Ready to benchmark.")

    def on_trigger(self, client: Any, userdata: Any, msg: Any) -> None:
        threading.Thread(target=self.run_evaluations, daemon=True).start()

    def evaluate_model(self, model: str, host: str = None) -> int:
        """Runs the Cookbook Math/Logic test against the model."""
        prompt = "Answer exactly 'SUCCESS' if 5 * 5 is 25. Say nothing else."
        cmd = ["ollama", "run", model]
        if host and host != "amdy":
            cmd = ["ssh", "-o", "BatchMode=yes", host, "ollama", "run", model]
            
        try:
            start_time = time.time()
            res = subprocess.run(cmd, input=prompt.encode("utf-8"), capture_output=True, timeout=20)
            elapsed = time.time() - start_time
            
            if res.returncode != 0:
                return 0
                
            output = res.stdout.decode("utf-8").strip().upper()
            
            score = 100
            if "SUCCESS" not in output:
                score -= 30 # Logic failure
                
            if elapsed > 10.0:
                score -= 20 # Too slow
                
            return score
        except Exception as e:
            logger.error(f"Failed to evaluate {model} on {host}: {e}")
            return 0

    def run_evaluations(self) -> None:
        if not os.path.exists(self.registry_path):
            logger.error("Registry not found. Run sys_profiler first.")
            return
            
        with open(self.registry_path, "r") as f:
            registry = json.load(f)
            
        results = {"amdy": {}, "tell": {}}
        
        for node in ["amdy", "tell"]:
            models = registry.get(node, {}).get("models", [])
            for m in models:
                name = m["model"]
                logger.info(f"Evaluating {name} on {node}...")
                score = self.evaluate_model(name, node)
                
                if score >= 85:
                    logger.info(f"{name} PASSED Cookbook Test (Score: {score})")
                    results[node][name] = score
                else:
                    logger.warning(f"{name} FAILED Cookbook Test (Score: {score})")
                    
        self.mqtt.publish("data_rein/cookbook/result", json.dumps({"status": "success", "evaluations": results}))
