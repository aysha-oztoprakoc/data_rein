import os
import re
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

from src.data_harness.services.logger import get_logger

logger = get_logger("knowledge_ingestor")

SYNC_CHANGED_TOPIC = "data_rein/sync/changed"
SYNC_COMPLETED_TOPIC = "data_rein/sync/completed"

RAG_CODE_DIR = os.path.expanduser("~/data_rein/knowledge_base/projects")
RAG_DOCS_DIR = os.path.expanduser("~/data_rein/knowledge_base/pon")
# Rough token limit per chunk
MAX_TOKENS_PER_CHUNK = 12000

# Bounded concurrency for local file I/O processing
executor = ThreadPoolExecutor(max_workers=8, thread_name_prefix="ingestor")

def estimate_tokens(text: str) -> int:
    return len(text) // 4

def condense_code(content: str) -> str:
    content = re.sub(r'\n\s*\n', '\n\n', content)
    return content

def process_file_change(client, payload):
    source = payload.get("source")
    dest = payload.get("destination")
    changed_file = payload.get("changed_file")
    
    if not dest or not changed_file:
        return
        
    filepath = os.path.join(dest, changed_file)
    if not os.path.exists(filepath):
        return
        
    ext = os.path.splitext(filepath)[1].lower()
    if ext not in [".py", ".md", ".txt", ".json", ".csv", ".cpp", ".hpp", ".sh", ".yaml", ".toml"]:
        return
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = condense_code(content)
        tokens = estimate_tokens(content)
        
        # Determine output location
        if ext in ['.md', '.txt', '.csv']:
            out_dir = RAG_DOCS_DIR
        else:
            out_dir = RAG_CODE_DIR
            
        os.makedirs(out_dir, exist_ok=True)
        
        # Handle chunking if needed
        chunks = []
        if tokens > MAX_TOKENS_PER_CHUNK:
            # Simple chunking by character count
            chunk_size = MAX_TOKENS_PER_CHUNK * 4
            for i in range(0, len(content), chunk_size):
                chunks.append(content[i:i+chunk_size])
        else:
            chunks = [content]
            
        for i, chunk in enumerate(chunks):
            filename = f"{os.path.basename(filepath)}.chunk{i}.md"
            out_path = os.path.join(out_dir, filename)
            
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(f"---\n")
                f.write(f"source: {filepath}\n")
                f.write(f"chunk: {i+1}/{len(chunks)}\n")
                f.write(f"tokens: {estimate_tokens(chunk)}\n")
                f.write(f"---\n\n")
                f.write(f"```{ext[1:] if ext else 'text'}\n")
                f.write(chunk)
                f.write(f"\n```\n")
                
        logger.info(f"Ingested {filepath} into {len(chunks)} chunks.")
        client.publish(SYNC_COMPLETED_TOPIC, json.dumps({
            "status": "success",
            "file": filepath,
            "chunks": len(chunks)
        }))
    except Exception as e:
        logger.exception(f"Error ingesting {filepath}")
        client.publish(SYNC_COMPLETED_TOPIC, json.dumps({
            "status": "error",
            "file": filepath,
            "error": str(e)
        }))

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe(SYNC_CHANGED_TOPIC)
        logger.info("Knowledge Ingestor connected.")

def on_message(client, userdata, msg):
    if msg.topic == SYNC_CHANGED_TOPIC:
        try:
            payload = json.loads(msg.payload.decode())
            # Submit to thread pool instead of unbound threads
            executor.submit(process_file_change, client, payload)
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON payload")

def main():
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="knowledge_ingestor")
    else:
        client = mqtt.Client(client_id="knowledge_ingestor")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect("localhost", 1883, 300)
        client.loop_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down ingestor...")
        executor.shutdown(wait=False)
        client.disconnect()

if __name__ == "__main__":
    main()
