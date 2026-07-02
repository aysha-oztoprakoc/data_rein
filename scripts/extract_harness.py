import os
import json
from pathlib import Path

HARNESS_DIR = Path(os.path.expanduser("~/data_rein"))
OUTPUT_FILE = HARNESS_DIR / "knowledge_base" / "agents" / "hermes" / "data_hermes_guide.md"

def build_guide():
    print(f"Extracting AI Guide from {HARNESS_DIR}...")
    
    os.makedirs(OUTPUT_FILE.parent, exist_ok=True)
    
    guide_content = """# Data-Hermes Step-by-Step AI Guide

This guide is dynamically extracted from the `data_rein` architecture to teach any AI (specifically Hermes) how to interact with this system.

## 1. Zero Polling Paradigm (PON)
- **Rule**: Never use `while True` active polling or `time.sleep()`.
- **Implementation**: Utilize blocking IO (`inotifywait`, `queue.get()`) or event-driven timers (`threading.Timer`).
- **Communication**: Use MQTT topics on `localhost:1883` for message passing.

## 2. Model Routing
- Read `config/model_router.json` to select the optimal model based on the node (`amdy` or `tell`) and the category of the task (e.g., `image generation`, `general chatting`).

## 3. Data Extraction Pipeline
- **Trigger**: Publish `{"filepath": "/path/to/file"}` to MQTT topic `data_rein/extract/trigger`.
- **Processing**: The orchestrator (`extraction_pipeline/orchestrator.py`) handles bounding via ThreadPoolExecutor.
- **Output**: Listen on `data_rein/extract/result` for success/failure.

## 4. Prompt Optimization
- **Trigger**: Publish `{"prompt": "my query"}` to `data_rein/prompt/optimize`.
- **Processing**: BM25 ranks the knowledge base and injects top context. Token compressor reduces fluff.
- **Output**: Listen on `data_rein/prompt/optimized`.

## 5. Background Sync
- Avoid modifying the `knowledge_base` continuously. Batch writes where possible. The `sync_daemon.py` will debounce file changes and perform `rsync` automatically to synchronize AMDY and TELL.

## 6. Execution Identity
- When acting as `data-hermes`, mimic the precise, fast, tool-oriented workflow of Antigravity (AGY) and the deep, analytical tone of Odysseus AI. Prioritize the `data_hermes_wiki.md` for fast context retrieval.

"""
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(guide_content)
        
    print(f"Data-Hermes AI Guide extracted to {OUTPUT_FILE}")

if __name__ == "__main__":
    build_guide()
