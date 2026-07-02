import json
import threading
import os

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

from strategies.token_compressor import TokenCompressor
from strategies.context_injector import ContextInjector
from strategies.format_adapter import FormatAdapter
from reins.services.logger import get_logger

logger = get_logger("prompt_optimizer_agent")

TRIGGER_TOPIC = "data_rein/prompt/optimize"
RESULT_TOPIC = "data_rein/prompt/optimized"

PROMPTS_DIR = os.path.expanduser("~/data_rein/prompts/optimized")

class PromptOptimizerAgent:
    def __init__(self):
        self.compressor = TokenCompressor()
        self.injector = ContextInjector()
        self.adapter = FormatAdapter()
        
    def optimize(self, prompt: str, task_type: str = "general") -> str:
        # 1. Compress prompt
        compressed = self.compressor.compress(prompt)
        
        # 2. Inject context (max 8k tokens)
        injected = self.injector.inject(compressed)
        
        # 3. Adapt format (add system prompt)
        final_prompt = self.adapter.adapt(injected, task_type)
        
        return final_prompt

agent = PromptOptimizerAgent()

def process_optimization(client, payload):
    request_id = payload.get("request_id")
    prompt = payload.get("prompt", "")
    task_type = payload.get("task_type", "general")
    
    if not prompt:
        client.publish(RESULT_TOPIC, json.dumps({"request_id": request_id, "status": "error", "error": "Empty prompt"}))
        return
        
    try:
        optimized = agent.optimize(prompt, task_type)
        
        # Save to history
        os.makedirs(PROMPTS_DIR, exist_ok=True)
        with open(os.path.join(PROMPTS_DIR, f"{request_id}.md"), 'w', encoding='utf-8') as f:
            f.write(optimized)
            
        client.publish(RESULT_TOPIC, json.dumps({
            "request_id": request_id,
            "status": "success",
            "optimized_prompt": optimized
        }))
    except Exception as e:
        client.publish(RESULT_TOPIC, json.dumps({
            "request_id": request_id,
            "status": "error",
            "error": str(e)
        }))

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe(TRIGGER_TOPIC)
        logger.info("Prompt Optimizer Agent connected.")

def on_message(client, userdata, msg):
    if msg.topic == TRIGGER_TOPIC:
        try:
            payload = json.loads(msg.payload.decode())
            # Run in daemon thread (PON compliant)
            threading.Thread(target=process_optimization, args=(client, payload), daemon=True).start()
        except json.JSONDecodeError:
            pass

def main():
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="prompt_optimizer")
    else:
        client = mqtt.Client(client_id="prompt_optimizer")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect("localhost", 1883, 300)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    main()
