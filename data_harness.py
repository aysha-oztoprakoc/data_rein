import json
import subprocess
import threading
import os
try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

REQUEST_TOPIC = "data_harness/request"
RESPONSE_TOPIC = "data_harness/response"
VSCODE_TOPIC = "data_harness/vscode/request"

REGISTRY_PATH = os.path.expanduser("~/DATA/data_harness/model_registry.json")

def load_registry():
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "r") as f:
            return json.load(f)
    return {"amdy": {"models": []}, "tell": {"models": []}}

def route_query(client, payload):
    registry = load_registry()
    model = payload.get("model", "deepseek-r1:14b")
    prompt = payload.get("prompt", "")
    request_id = payload.get("request_id", "unknown")
    
    node = "amdy"
    if model in registry.get("tell", {}).get("models", []):
        node = "tell"
    elif model in registry.get("amdy", {}).get("models", []):
        node = "amdy"
    else:
        # Fallback to local
        node = "amdy"
    
    response_payload = {
        "request_id": request_id,
        "model": model,
        "node": node,
        "status": "processing"
    }
    client.publish(RESPONSE_TOPIC, json.dumps(response_payload))
    
    cmd = ["ollama", "run", model, prompt]
    if node == "tell":
        cmd = ["ssh", "-o", "BatchMode=yes", "tell@192.168.0.2", "ollama", "run", model, prompt]
    
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if res.returncode == 0:
            result = res.stdout.strip()
        else:
            result = f"Error: {res.stderr.strip()}"
    except Exception as e:
        result = f"Exception: {str(e)}"
        
    final_payload = {
        "request_id": request_id,
        "result": result
    }
    client.publish(RESPONSE_TOPIC, json.dumps(final_payload))

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe(REQUEST_TOPIC)
        client.subscribe(VSCODE_TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
    except json.JSONDecodeError:
        return
        
    if msg.topic in (REQUEST_TOPIC, VSCODE_TOPIC):
        threading.Thread(target=route_query, args=(client, payload), daemon=True).start()

def main():
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="data_harness")
    else:
        client = mqtt.Client(client_id="data_harness")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect("localhost", 1883, 300)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    main()
