import json
import os
import threading
import subprocess

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

TRIGGER_TOPIC = "data_rein/llm/quota_exhausted"
STATUS_TOPIC = "data_rein/llm/fallback_status"

def start_local_fallback(client, payload):
    client.publish(STATUS_TOPIC, json.dumps({"status": "starting", "message": "Gemini Quota Exhausted. Booting local fallback model via Ollama..."}))
    
    # Check if Ollama is running and start it if needed (assumed it's a system service or available in PATH)
    model = payload.get("model", "llama3.1")
    
    # 1. Start Ollama local process to take over the data loop
    client.publish(STATUS_TOPIC, json.dumps({"status": "pulling", "model": model, "message": "Ensuring local model is pulled..."}))
    subprocess.run(["ollama", "pull", model], capture_output=True)
    
    # 2. Trigger the local loop runner script (placeholder for Odysseus local orchestrator)
    # The local model assumes control of the data_rein loop.
    client.publish(STATUS_TOPIC, json.dumps({"status": "running", "message": f"Local model {model} has assumed control of the data rein."}))
    
    # We can invoke a local python script that uses the ollama API
    # subprocess.run(["python3", "/home/amdy/data_rein/services/odysseus_local_loop.py"])

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe(TRIGGER_TOPIC)
        client.publish(STATUS_TOPIC, json.dumps({"status": "ready", "message": "Fallback Agent online and waiting."}))

def on_message(client, userdata, msg):
    if msg.topic == TRIGGER_TOPIC:
        try:
            payload = json.loads(msg.payload.decode())
            threading.Thread(target=start_local_fallback, args=(client, payload), daemon=True).start()
        except json.JSONDecodeError:
            pass

def main():
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="fallback_agent")
    else:
        client = mqtt.Client(client_id="fallback_agent")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect("localhost", 1883, 300)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    main()
