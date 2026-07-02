import os
import json
import time
import hashlib
import threading
from datetime import datetime
from typing import Any, Set
from concurrent.futures import ThreadPoolExecutor

try:
    from paho.mqtt.client import CallbackAPIVersion  # type: ignore[attr-defined]
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

from reins.services.logger import get_logger
from reins.services.data_nexus.knowledge_manager import KnowledgeManager
from reins.services.data_nexus.reasoning_engine import ReasoningEngine
from reins.extraction.registry import registry

logger = get_logger("data_nexus")
TRIGGER_TOPIC = "data_rein/nexus/trigger"
EXTRACT_TOPIC = "data_rein/extract/trigger"
RESULT_TOPIC = "data_rein/extract/result"
DEDUPE_TOPIC = "data_rein/nexus/deduplicate"

TRAINING_DATA_DIR = os.path.expanduser("~/data_rein/training_data")

# PON compliant execution pools for graceful degradation
local_executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix="ext_local")
remote_executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="ext_remote")

def get_output_dir(extractor_node: str, ext: str) -> str:
    if extractor_node == "amdy":
        return os.path.join(TRAINING_DATA_DIR, "text")
    elif ext in [".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif", ".webp", ".svg"]:
        return os.path.join(TRAINING_DATA_DIR, "image_descriptions")
    else:
        return os.path.join(TRAINING_DATA_DIR, "audio_transcripts")

class NexusDaemon:
    def __init__(self) -> None:
        self.km = KnowledgeManager()
        self.re = ReasoningEngine()
        self.is_processing = False
        
        # Deduplication state
        self.known_hashes: Set[str] = set()
        
        if PAHO_V2:
            self.client = mqtt.Client(
                CallbackAPIVersion.VERSION1, client_id="data_nexus_prime")
        else:
            self.client = mqtt.Client(client_id="data_nexus_prime")

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client: Any, userdata: Any, flags: Any, rc: Any, *args: Any) -> None:
        if rc == 0:
            logger.info("Data Nexus PRIME connected. Subscribing to triggers.")
            client.subscribe(TRIGGER_TOPIC)
            client.subscribe(EXTRACT_TOPIC)
            client.subscribe(DEDUPE_TOPIC)
        else:
            logger.error(f"Data Nexus PRIME failed to connect. RC: {rc}")

    def process_deduplication(self) -> None:
        """Reactive deduplication handler (PON compliant event)."""
        logger.info("RAG Deduplication started (Event Triggered).")
        try:
            # Scan training_data for duplicates
            for root, _, files in os.walk(TRAINING_DATA_DIR):
                for f in files:
                    fpath = os.path.join(root, f)
                    try:
                        with open(fpath, "rb") as file_obj:
                            file_hash = hashlib.sha256(file_obj.read()).hexdigest()
                            if file_hash in self.known_hashes:
                                logger.warning(f"Deduplication: Removing duplicate knowledge {fpath}")
                                os.remove(fpath)
                            else:
                                self.known_hashes.add(file_hash)
                    except Exception:
                        continue
            logger.info("RAG Deduplication completed.")
        except Exception as e:
            logger.error(f"Deduplication error (gracefully recovering): {e}")

    def process_extraction(self, payload: Any) -> None:
        filepath = payload.get("filepath")
        if not filepath or not os.path.exists(filepath):
            logger.error(f"File not found: {filepath}")
            self.client.publish(RESULT_TOPIC, json.dumps({"filepath": filepath, "status": "error", "error": "File not found"}))
            return

        ext = os.path.splitext(filepath)[1].lower()
        extractor = registry.get_extractor(ext)

        if not extractor:
            logger.warning(f"Unsupported format: {ext} for {filepath}")
            self.client.publish(RESULT_TOPIC, json.dumps({"filepath": filepath, "status": "error", "error": f"Unsupported format: {ext}"}))
            return

        output_dir = get_output_dir(extractor.NODE, ext)
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.join(TRAINING_DATA_DIR, "metadata"), exist_ok=True)

        try:
            logger.info(f"Extracting {filepath} on node {extractor.NODE}...")
            result = extractor.extract(filepath, output_dir)
            result["filepath"] = filepath

            if result["status"] == "success":
                metadata_path = os.path.join(TRAINING_DATA_DIR, "metadata", f"{os.path.basename(filepath)}.meta.json")
                with open(metadata_path, 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=2)
                logger.info(f"Successfully extracted {filepath}. Triggering INSTANT reasoning engine...")
                
                # Continuous Learning 100% of the time: immediately trigger reasoning!
                if not self.is_processing:
                    threading.Thread(target=self.process_trigger, daemon=True).start()
                    
            else:
                logger.error(f"Failed to extract {filepath}: {result.get('error')}")

            self.client.publish(RESULT_TOPIC, json.dumps(result))
        except Exception as e:
            logger.exception(f"Exception during extraction of {filepath}")
            # Graceful Degradation: Publish error instead of crashing
            self.client.publish(RESULT_TOPIC, json.dumps({"filepath": filepath, "status": "error", "error": str(e)}))

    def on_message(self, client: Any, userdata: Any, msg: Any) -> None:
        try:
            if msg.topic == EXTRACT_TOPIC:
                try:
                    payload = json.loads(msg.payload.decode())
                    filepath = payload.get("filepath")
                    if filepath:
                        ext = os.path.splitext(filepath)[1].lower()
                        extractor = registry.get_extractor(ext)
                        if extractor and extractor.NODE == "tell":
                            remote_executor.submit(self.process_extraction, payload)
                        else:
                            local_executor.submit(self.process_extraction, payload)
                except json.JSONDecodeError:
                    logger.error("Failed to decode JSON payload")

            elif msg.topic == TRIGGER_TOPIC:
                if not self.is_processing:
                    threading.Thread(target=self.process_trigger, daemon=True).start()
                else:
                    logger.warning("Nexus is already processing an insight. Skipping this trigger.")
                    
            elif msg.topic == DEDUPE_TOPIC:
                local_executor.submit(self.process_deduplication)
        except Exception as e:
            # Absolute Graceful Degradation: Do not let rogue payloads crash the MQTT loop
            logger.critical(f"Unhandled exception in on_message (gracefully recovering): {e}")

    def process_trigger(self) -> None:
        self.is_processing = True
        try:
            logger.info("Data Nexus reasoning cycle initiated...")
            insight = self.re.generate_optimization()
            
            if insight:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"nexus_insight_{timestamp}.md"
                self.km.save_insight(filename, insight)
                logger.info(f"Insight generated and saved as {filename}.")
        except Exception as e:
            # Graceful Degradation: Catch error, log it, and free the lock
            logger.error(f"Error in Nexus reasoning cycle: {e}")
        finally:
            self.is_processing = False

    def start(self) -> None:
        logger.info("Starting Data Nexus PRIME (Assimilation Mode).")
        self.client.connect("localhost", 1883, 60)
        self.client.loop_forever()

if __name__ == "__main__":
    daemon = NexusDaemon()
    daemon.start()
