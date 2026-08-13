"""Event-driven bridge from MQTT extraction facts to canonical Wiki ingestion."""

from __future__ import annotations

import hashlib
import json
import threading
from collections.abc import Mapping
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import ClassVar

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
from paho.mqtt.properties import Properties
from paho.mqtt.reasoncodes import ReasonCode
from pydantic import BaseModel, ConfigDict, JsonValue, ValidationError

from reins.harness import digest, external_io
from reins.services.data_nexus.knowledge_manager import KnowledgeManager
from reins.services.data_nexus.reasoning_engine import ReasoningEngine
from reins.services.logger import get_logger

logger = get_logger("data_nexus")
TRIGGER_TOPIC = "data_rein/nexus/trigger"
EXTRACT_TOPIC = "data_rein/extract/trigger"
RESULT_TOPIC = "data_rein/extract/result"
DEDUPE_TOPIC = "data_rein/nexus/deduplicate"
TRAINING_DATA_DIR = Path.home() / "data_rein" / "data-oby" / "TrainingData"

local_executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix="ext_local")


class ExtractionEvent(BaseModel):
    """Validated notification that enters the canonical Wiki digest path."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    filepath: str
    enrich: bool = True


class NexusDaemon:
    """Subscribe to facts and dispatch bounded ingestion or reasoning work."""

    def __init__(self) -> None:
        self.km: KnowledgeManager = KnowledgeManager()
        self.re: ReasoningEngine = ReasoningEngine()
        self.is_processing: bool = False
        self.known_hashes: set[str] = set()
        self.client: mqtt.Client = mqtt.Client(
            CallbackAPIVersion.VERSION2,
            client_id="data_nexus_prime",
        )
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(
        self,
        client: mqtt.Client,
        _userdata: JsonValue = None,
        _flags: mqtt.ConnectFlags | None = None,
        reason_code: ReasonCode | int = 0,
        _properties: Properties | None = None,
    ) -> None:
        if reason_code == 0:
            logger.info("Data Nexus connected; subscribing to notification topics")
            _ = external_io.mqtt_subscribe(client, TRIGGER_TOPIC)
            _ = external_io.mqtt_subscribe(client, EXTRACT_TOPIC)
            _ = external_io.mqtt_subscribe(client, DEDUPE_TOPIC)
        else:
            logger.error("Data Nexus connection failed: %s", reason_code)

    def process_deduplication(self) -> None:
        """Remove duplicate derived artifacts after an explicit notification."""
        logger.info("Training artifact deduplication started")
        try:
            for path in (item for item in TRAINING_DATA_DIR.rglob("*") if item.is_file()):
                digest_value = hashlib.sha256(path.read_bytes()).hexdigest()
                if digest_value in self.known_hashes:
                    path.unlink()
                else:
                    self.known_hashes.add(digest_value)
            logger.info("Training artifact deduplication completed")
        except OSError:
            logger.error("Training artifact deduplication degraded", exc_info=True)

    def process_extraction(
        self,
        payload: ExtractionEvent | Mapping[str, JsonValue],
    ) -> None:
        try:
            event = (
                payload
                if isinstance(payload, ExtractionEvent)
                else ExtractionEvent.model_validate(payload)
            )
        except ValidationError:
            logger.error("Invalid extraction event", exc_info=True)
            _ = external_io.mqtt_publish(
                self.client,
                RESULT_TOPIC,
                json.dumps({"status": "error", "error": "Invalid extraction event"}),
            )
            return
        if not Path(event.filepath).exists():
            logger.error("File not found: %s", event.filepath)
            _ = external_io.mqtt_publish(
                self.client,
                RESULT_TOPIC,
                json.dumps(
                    {
                        "filepath": event.filepath,
                        "status": "error",
                        "error": "File not found",
                    }
                ),
            )
            return
        results = digest.digest_path(event.filepath, enrich=event.enrich)
        succeeded = sum(item.ok for item in results)
        if succeeded:
            logger.info(
                "Canonical digest stored %s/%s extraction result(s) in the Wiki",
                succeeded,
                len(results),
            )
        else:
            logger.error("Canonical digest failed for %s", event.filepath)

    def on_message(
        self,
        _client: mqtt.Client,
        _userdata: JsonValue,
        message: mqtt.MQTTMessage,
    ) -> None:
        try:
            if message.topic == EXTRACT_TOPIC:
                event = ExtractionEvent.model_validate_json(message.payload)
                _ = local_executor.submit(self.process_extraction, event)
            elif message.topic == TRIGGER_TOPIC:
                if not self.is_processing:
                    threading.Thread(target=self.process_trigger, daemon=True).start()
            elif message.topic == DEDUPE_TOPIC:
                _ = local_executor.submit(self.process_deduplication)
        except (UnicodeDecodeError, ValidationError):
            logger.error("Invalid Nexus notification payload", exc_info=True)

    def process_trigger(self) -> None:
        self.is_processing = True
        try:
            insight = self.re.generate_optimization()
            if insight:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                self.km.save_insight(f"nexus_insight_{timestamp}.xml", insight)
        except (OSError, RuntimeError, ValueError):
            logger.error("Data Nexus reasoning cycle degraded", exc_info=True)
        finally:
            self.is_processing = False

    def run(self) -> None:
        logger.info("Starting Data Nexus PRIME on localhost")
        _ = external_io.mqtt_connect(self.client, "localhost", 1883, 60)
        _ = self.client.loop_forever()


if __name__ == "__main__":
    NexusDaemon().run()
