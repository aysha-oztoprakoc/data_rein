import json
import subprocess
import threading
import os
import urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from vault_manager import vault

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

REQUEST_TOPIC = "data_harness/request"
RESPONSE_TOPIC = "data_harness/response"
REGISTRY_PATH = os.path.expanduser("~/DATA/data_harness/model_registry.json")
API_KEYS_PATH = os.path.expanduser("~/DATA/data_harness/api_keys.json")

# ─── Routing Logic ───
def load_registry():
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "r") as f:
            return json.load(f)
    return {"amdy": {"tiers": {}}, "tell": {"tiers": {}}}

def load_keys():
    # Attempt to unlock vault on first access if needed
    if not vault.session_key:
        vault.unlock()
    return vault.get_api_keys()

def call_openai(model, prompt, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {"model": model, "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request(url, json.dumps(data).encode("utf-8"), headers)
    with urllib.request.urlopen(req, timeout=120) as res:
        out = json.loads(res.read().decode())
        return out["choices"][0]["message"]["content"]

def call_anthropic(model, prompt, api_key):
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01"
    }
    data = {"model": model, "max_tokens": 4096, "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request(url, json.dumps(data).encode("utf-8"), headers)
    with urllib.request.urlopen(req, timeout=120) as res:
        out = json.loads(res.read().decode())
        return out["content"][0]["text"]

def call_gemini(model, prompt, api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    req = urllib.request.Request(url, json.dumps(data).encode("utf-8"), headers)
    with urllib.request.urlopen(req, timeout=120) as res:
        out = json.loads(res.read().decode())
        return out["candidates"][0]["content"]["parts"][0]["text"]

def route_query_logic(model, prompt):
    keys = load_keys()
    
    try:
        # Route to Cloud Providers
        if model.startswith("gpt-"):
            if not keys.get("OPENAI_API_KEY") or keys["OPENAI_API_KEY"].startswith("sk-..."):
                return "Error: OPENAI_API_KEY not configured in api_keys.json"
            return call_openai(model, prompt, keys["OPENAI_API_KEY"])
            
        elif model.startswith("claude-"):
            if not keys.get("ANTHROPIC_API_KEY") or keys["ANTHROPIC_API_KEY"].startswith("sk-..."):
                return "Error: ANTHROPIC_API_KEY not configured in api_keys.json"
            return call_anthropic(model, prompt, keys["ANTHROPIC_API_KEY"])
            
        elif model.startswith("gemini-"):
            if not keys.get("GEMINI_API_KEY") or keys["GEMINI_API_KEY"].startswith("AIza"):
                return "Error: GEMINI_API_KEY not configured in api_keys.json"
            return call_gemini(model, prompt, keys["GEMINI_API_KEY"])
            
        # Route to Local Nodes
        registry = load_registry()
        node = "amdy"
        
        # Check tell's tiers
        tell_tiers = registry.get("tell", {}).get("tiers", {})
        for tier_list in tell_tiers.values():
            for item in tier_list:
                if item["model"] == model:
                    node = "tell"
                    break
                    
        cmd = ["ollama", "run", model, prompt]
        if node == "tell":
            cmd = ["ssh", "-o", "BatchMode=yes", "tell@192.168.0.2", "ollama", "run", model, prompt]
        
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if res.returncode == 0:
            return res.stdout.strip()
        else:
            return f"Error: {res.stderr.strip()}"
            
    except Exception as e:
        return f"Exception: {str(e)}"

# ─── MQTT Handlers ───
def route_mqtt_query(client, payload):
    model = payload.get("model", "deepseek-r1:14b")
    prompt = payload.get("prompt", "")
    request_id = payload.get("request_id", "unknown")
    
    result = route_query_logic(model, prompt)
    final_payload = {
        "request_id": request_id,
        "result": result
    }
    client.publish(RESPONSE_TOPIC, json.dumps(final_payload))

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe(REQUEST_TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
    except json.JSONDecodeError:
        return
        
    if msg.topic == REQUEST_TOPIC:
        threading.Thread(target=route_mqtt_query, args=(client, payload), daemon=True).start()

# ─── HTTP Server for VS Code ───
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

class APIHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/v1/chat/completions":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                payload = json.loads(post_data.decode('utf-8'))
                
                # OpenAI compatible extraction
                model = payload.get("model", "deepseek-r1:14b")
                messages = payload.get("messages", [])
                
                prompt = ""
                for msg in messages:
                    prompt += f"{msg.get('role', 'user')}: {msg.get('content', '')}\n"
                
                result = route_query_logic(model, prompt)
                
                response = {
                    "id": "chatcmpl-123",
                    "object": "chat.completion",
                    "created": 1677652288,
                    "model": model,
                    "choices": [{
                        "index": 0,
                        "message": {
                            "role": "assistant",
                            "content": result,
                        },
                        "finish_reason": "stop"
                    }]
                }
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run_http_server():
    server_address = ('0.0.0.0', 8080)
    httpd = ThreadedHTTPServer(server_address, APIHandler)
    httpd.serve_forever()

def main():
    # Start HTTP server for VS Code
    threading.Thread(target=run_http_server, daemon=True).start()

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
