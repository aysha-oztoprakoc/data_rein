import json
import subprocess
import threading
import os
import re
from concurrent.futures import ThreadPoolExecutor

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

TRIGGER_TOPIC = "data_rein/getinfo/trigger"
RESULT_TOPIC = "data_rein/getinfo/result"
REGISTRY_PATH = os.path.expanduser("~/DATA/data_rein/model_registry.json")
MIN_MODEL_SCORE = 85

# Bounded Executor to prevent SSH spam and thread exhaustion
executor = ThreadPoolExecutor(max_workers=2)

def get_vram(host=None):
    cmd = ["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader,nounits"]
    if host:
        cmd = ["ssh", "-o", "BatchMode=yes", f"tell@{host}"] + cmd
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if res.returncode == 0:
            return int(res.stdout.strip().split("\n")[0]) / 1024 # return GB
    except Exception:
        pass
    return 16.0 # fallback

def get_ollama_models(host=None):
    cmd = ["ollama", "list"]
    if host:
        cmd = ["ssh", "-o", "BatchMode=yes", f"tell@{host}", "ollama", "list"]
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

def estimate_vram(model_name):
    match = re.search(r'(\d+(?:\.\d+)?)[bB]', model_name)
    if match:
        return float(match.group(1)) * 0.7
    return 4.0

def evaluate_score(model_name, total_vram_gb):
    required_vram = estimate_vram(model_name)
    if required_vram > total_vram_gb:
        return 40 # Instant fail
    
    ratio = required_vram / total_vram_gb
    score = 100 - (ratio * 30)
    return max(0, min(100, score))

def categorize_tier(model_name, score):
    params = 4.0
    match = re.search(r'(\d+(?:\.\d+)?)[bB]', model_name)
    if match:
        params = float(match.group(1))
        
    if params >= 7.0 and score >= 85:
        return "KAT_11" 
    elif params >= 3.0 and score >= 85:
        return "KAT_7" 
    elif score >= 85:
        return "KAT_3" 
    return "REJECTED"

def process_node(node_name, host=None):
    vram = get_vram(host)
    models = get_ollama_models(host)
    
    profile = {
        "hardware": {"vram_gb": vram},
        "tiers": {
            "KAT_11": [],
            "KAT_7": [],
            "KAT_3": []
        }
    }
    
    for m in models:
        score = evaluate_score(m, vram)
        if score >= MIN_MODEL_SCORE:
            tier = categorize_tier(m, score)
            if tier != "REJECTED":
                profile["tiers"][tier].append({"model": m, "score": round(score, 1)})
                
    return profile

def profile_cluster(client):
    try:
        amdy_profile = process_node("amdy")
        tell_profile = process_node("tell", "192.168.0.2")
        
        result = {
            "amdy": amdy_profile,
            "tell": tell_profile
        }
        
        os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
        with open(REGISTRY_PATH, "w") as f:
            json.dump(result, f, indent=2)
            
        client.publish(RESULT_TOPIC, json.dumps({"status": "success", "registry": result}))
    except Exception as e:
        client.publish(RESULT_TOPIC, json.dumps({"error": str(e)}))

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe(TRIGGER_TOPIC)

def on_message(client, userdata, msg):
    if msg.topic == TRIGGER_TOPIC:
        # Enforce execution via ThreadPoolExecutor instead of unbound threads
        executor.submit(profile_cluster, client)

def main():
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="sys_profiler")
    else:
        client = mqtt.Client(client_id="sys_profiler")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect("localhost", 1883, 300)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()
        executor.shutdown(wait=False)

if __name__ == "__main__":
    main()
