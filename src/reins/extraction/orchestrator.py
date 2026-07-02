from typing import Any
import os
import json
from concurrent.futures import ThreadPoolExecutor

try:
    from paho.mqtt.client import CallbackAPIVersion  # type: ignore[attr-defined]
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

# Ensure extractors are registered by importing them
from .registry import registry
from src.reins.services.logger import get_logger

logger = get_logger("extractor_orchestrator")

TRIGGER_TOPIC = "data_rein/extract/trigger"
RESULT_TOPIC = "data_rein/extract/result"
TRAINING_DATA_DIR = os.path.expanduser("~/data_rein/training_data")

# Thread pools for bounded concurrency (PON compliant)
# Local extraction on amdy uses up to 16 threads (8C/16T processor)
local_executor = ThreadPoolExecutor(
    max_workers=16, thread_name_prefix="ext_local")
# Remote extraction on tell uses up to 4 threads to prevent overwhelming SSH/IO
remote_executor = ThreadPoolExecutor(
    max_workers=4, thread_name_prefix="ext_remote")


def get_output_dir(extractor_node: str, ext: str) -> str:
    if extractor_node == "amdy":
        return os.path.join(TRAINING_DATA_DIR, "text")
    elif ext in [".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif", ".webp", ".svg"]:
        return os.path.join(TRAINING_DATA_DIR, "image_descriptions")
    else:
        return os.path.join(TRAINING_DATA_DIR, "audio_transcripts")


def process_extraction(client: Any, payload: Any) -> Any:
    filepath = payload.get("filepath")
    if not filepath or not os.path.exists(filepath):
        logger.error(f"File not found: {filepath}")
        client.publish(RESULT_TOPIC, json.dumps(
            {"filepath": filepath, "status": "error", "error": "File not found"}))
        return

    ext = os.path.splitext(filepath)[1].lower()
    extractor = registry.get_extractor(ext)

    if not extractor:
        logger.warning(f"Unsupported format: {ext} for {filepath}")
        client.publish(RESULT_TOPIC, json.dumps({
            "filepath": filepath,
            "status": "error",
            "error": f"Unsupported format: {ext}"
        }))
        return

    output_dir = get_output_dir(extractor.NODE, ext)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(TRAINING_DATA_DIR, "metadata"), exist_ok=True)

    try:
        logger.info(f"Extracting {filepath} on node {extractor.NODE}...")
        result = extractor.extract(filepath, output_dir)
        result["filepath"] = filepath

        # Save metadata JSON
        if result["status"] == "success":
            metadata_path = os.path.join(
                TRAINING_DATA_DIR, "metadata", f"{os.path.basename(filepath)}.meta.json")
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            logger.info(f"Successfully extracted {filepath}")
        else:
            logger.error(
                f"Failed to extract {filepath}: {result.get('error')}")

        client.publish(RESULT_TOPIC, json.dumps(result))
    except Exception as e:
        logger.exception(f"Exception during extraction of {filepath}")
        client.publish(RESULT_TOPIC, json.dumps({
            "filepath": filepath,
            "status": "error",
            "error": str(e)
        }))


def on_connect(client: Any, userdata: Any, flags: Any, rc: int, *args: Any) -> None:
    if rc == 0:
        client.subscribe(TRIGGER_TOPIC)
        logger.info(
            f"Extraction Orchestrator connected. Supported formats: {registry.list_supported()}")


def on_message(client: Any, userdata: Any, msg: Any) -> None:
    if msg.topic == TRIGGER_TOPIC:
        try:
            payload = json.loads(msg.payload.decode())
            filepath = payload.get("filepath")
            if filepath:
                ext = os.path.splitext(filepath)[1].lower()
                extractor = registry.get_extractor(ext)
                if extractor and extractor.NODE == "tell":
                    remote_executor.submit(process_extraction, client, payload)
                else:
                    local_executor.submit(process_extraction, client, payload)
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON payload")


def main() -> None:
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1)
    else:
        client = mqtt.Client(client_id="data_extractor_orchestrator")

    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("localhost", 1883, 300)
        client.loop_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down extractor orchestrator...")
        local_executor.shutdown(wait=False)
        remote_executor.shutdown(wait=False)
        client.disconnect()


if __name__ == "__main__":
    main()
