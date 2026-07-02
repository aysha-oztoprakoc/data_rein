import threading
from datetime import datetime
from typing import Any
try:
    from paho.mqtt.client import CallbackAPIVersion  # type: ignore[attr-defined]
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt
from reins.services.logger import get_logger
from reins.services.data_nexus.knowledge_manager import KnowledgeManager
from reins.services.data_nexus.reasoning_engine import ReasoningEngine

logger = get_logger("data_nexus")
TRIGGER_TOPIC = "data_rein/nexus/trigger"

class NexusDaemon:
    def __init__(self) -> None:
        self.km = KnowledgeManager()
        self.re = ReasoningEngine()
        self.is_processing = False
        
        if PAHO_V2:
            self.client = mqtt.Client(
                CallbackAPIVersion.VERSION1, client_id="data_nexus")
        else:
            self.client = mqtt.Client(client_id="data_nexus")

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client: Any, userdata: Any, flags: Any, rc: Any, *args: Any) -> None:
        if rc == 0:
            logger.info("Data Nexus connected to broker. Subscribing to triggers.")
            client.subscribe(TRIGGER_TOPIC)
        else:
            logger.error(f"Data Nexus failed to connect. RC: {rc}")

    def on_message(self, client: Any, userdata: Any, msg: Any) -> None:
        if msg.topic == TRIGGER_TOPIC:
            if not self.is_processing:
                # Spawn a daemon thread to do the heavy LLM lifting (PON zero-blocking rule)
                threading.Thread(target=self.process_trigger, daemon=True).start()
            else:
                logger.warning("Nexus is already processing an insight. Skipping this trigger.")

    def process_trigger(self) -> None:
        self.is_processing = True
        try:
            logger.info("Data Nexus triggered. Initiating observation cycle...")
            insight = self.re.generate_optimization()
            
            if insight:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"nexus_insight_{timestamp}.md"
                self.km.save_insight(filename, insight)
                logger.info(f"Insight generated and saved as {filename}.")
            else:
                logger.info("No insight generated in this cycle.")
        except Exception as e:
            logger.error(f"Error in Nexus processing cycle: {e}")
        finally:
            self.is_processing = False

    def start(self) -> None:
        logger.info("Starting Data Nexus PON Daemon (Zero-Polling).")
        self.client.connect("localhost", 1883, 60)
        self.client.loop_forever()

if __name__ == "__main__":
    daemon = NexusDaemon()
    daemon.start()
