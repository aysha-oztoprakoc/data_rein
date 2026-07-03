import os
import json
import subprocess
import threading
import re
from typing import Any
from reins.services.logger import get_logger

logger = get_logger("sys_profiler")

class SysProfiler:
    """
    Cluster Telemetry Profiler integrated into Data Rein.
    Scans hardware (amdy and tell) to ensure local models meet the minimum score.
    """
    def __init__(self, mqtt_client: Any) -> None:
        self.mqtt = mqtt_client
        self.registry_path = os.path.expanduser("~/data_rein/data-oby/TrainingData/model_registry.json")
        self.min_model_score = 85
        
        self.mqtt.subscribe("data_rein/sys_profiler/trigger")
        self.mqtt.message_callback_add("data_rein/sys_profiler/trigger", self.on_trigger)
        logger.info("SysProfiler online. Ready for cluster telemetry scans.")

    def on_trigger(self, client: Any, userdata: Any, msg: Any) -> None:
        threading.Thread(target=self.profile_cluster, daemon=True).start()

    def get_vram(self, host: str = None) -> float:
        cmd = ["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader,nounits"]
        if host:
            cmd = ["ssh", "-o", "BatchMode=yes", host] + cmd
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            if res.returncode == 0:
                return int(res.stdout.strip().split("\n")[0]) / 1024 # return GB
        except Exception:
            pass
        return 16.0 # fallback

    def get_ollama_models(self, host: str = None) -> list:
        cmd = ["ollama", "list"]
        if host:
            cmd = ["ssh", "-o", "BatchMode=yes", host, "ollama", "list"]
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            models = []
            if res.returncode == 0:
                lines = res.stdout.strip().split("\n")[1:]
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 1:
                        models.append(parts[0])
            return models
        except Exception:
            return []

    def estimate_vram(self, model_name: str) -> float:
        match = re.search(r'(\d+(?:\.\d+)?)[bB]', model_name)
        if match:
            return float(match.group(1)) * 0.7
        return 4.0

    def evaluate_score(self, model_name: str, total_vram_gb: float) -> float:
        required_vram = self.estimate_vram(model_name)
        if required_vram > total_vram_gb:
            return 40 # Instant fail
        
        # Base score out of 100 based on VRAM fit
        ratio = required_vram / total_vram_gb
        score = 100 - (ratio * 30)
        return max(0, min(100, score))

    def process_node(self, node_name: str, host: str = None) -> dict:
        vram = self.get_vram(host)
        models = self.get_ollama_models(host)
        
        profile = {
            "hardware": {"vram_gb": vram},
            "models": []
        }
        
        for m in models:
            score = self.evaluate_score(m, vram)
            if score >= self.min_model_score:
                profile["models"].append({"model": m, "score": round(score, 1)})
            else:
                logger.warning(f"Model {m} on {node_name} rejected (Score {score} < {self.min_model_score})")
                
        return profile

    def profile_cluster(self) -> None:
        try:
            amdy_profile = self.process_node("amdy")
            tell_profile = self.process_node("tell", "tell")
            
            result = {
                "amdy": amdy_profile,
                "tell": tell_profile
            }
            
            os.makedirs(os.path.dirname(self.registry_path), exist_ok=True)
            with open(self.registry_path, "w") as f:
                json.dump(result, f, indent=2)
                
            self.mqtt.publish("data_rein/sys_profiler/result", json.dumps({"status": "success", "registry": result}))
            logger.info("Cluster profile updated successfully.")
        except Exception as e:
            logger.error(f"Failed to profile cluster: {e}")
            self.mqtt.publish("data_rein/sys_profiler/result", json.dumps({"status": "error", "error": str(e)}))
