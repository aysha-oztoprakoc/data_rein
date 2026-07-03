import os
import json
import threading
from typing import Any
from xml.etree import ElementTree as ET
from reins.services.logger import get_logger
from reins.services.task_trail import TaskTrail

logger = get_logger("knowledge_ingestor")

class KnowledgeIngestor:
    """
    Continuous Learning Loop.
    Subscribes to 'data_rein/trail/success' and automatically parses the
    prompt/result of successful tasks, injecting them into the Universal XML Knowledge Base.
    """
    def __init__(self, mqtt_client: Any) -> None:
        self.mqtt = mqtt_client
        self.wiki_path = os.path.expanduser("~/data_rein/knowledge_base/agents/hermes/data_hermes_wiki.xml")
        self.trail = TaskTrail()
        
        # Subscribe to PON topic
        if self.mqtt:
            self.mqtt.subscribe("data_rein/trail/success")
            self.mqtt.message_callback_add("data_rein/trail/success", self.on_success)
            logger.info("Knowledge Ingestor online. Listening for successful tasks.")

    def on_success(self, client: Any, userdata: Any, msg: Any) -> None:
        try:
            payload = json.loads(msg.payload.decode("utf-8"))
            task_id = payload.get("task_id")
            result_text = payload.get("result", "")
            
            if task_id:
                # Fire and forget PON decoupling
                threading.Thread(target=self.ingest_task, args=(task_id, result_text), daemon=True).start()
        except Exception as e:
            logger.error(f"Error parsing success payload: {e}")

    def ingest_task(self, task_id: str, result_text: str) -> bool:
        tasks = self.trail._load()
        task = next((t for t in tasks if t["task_id"] == task_id), None)
        
        if not task:
            logger.warning(f"Task {task_id} not found in trail. Skipping ingestion.")
            return False
            
        if task.get("status") not in ["success", "success_fallback"]:
            logger.warning(f"Task {task_id} is not marked as successful. Skipping.")
            return False

        prompt = task.get("prompt", "")
        
        # Inject into XML safely
        try:
            self._append_to_xml(task_id, prompt, result_text)
            logger.info(f"Successfully ingested task {task_id} into Knowledge Base.")
            return True
        except Exception as e:
            logger.error(f"Failed to append to XML: {e}")
            return False

    def _append_to_xml(self, task_id: str, prompt: str, result_text: str) -> None:
        if not os.path.exists(self.wiki_path):
            os.makedirs(os.path.dirname(self.wiki_path), exist_ok=True)
            with open(self.wiki_path, "w") as f:
                f.write('<?xml version="1.0" ?>\n<knowledge_document>\n  <content>\n  </content>\n</knowledge_document>')

        with open(self.wiki_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Generate the XML node (wrapping in CDATA to avoid parsing issues)
        new_node = f'''
    <learned_task id="{task_id}">
      <prompt><![CDATA[{prompt}]]></prompt>
      <result><![CDATA[{result_text}]]></result>
    </learned_task>
'''
        # Inject before closing </content> or </knowledge_document>
        if "</content>" in content:
            content = content.replace("</content>", new_node + "  </content>")
        elif "</knowledge_document>" in content:
            content = content.replace("</knowledge_document>", new_node + "</knowledge_document>")
        else:
            content += new_node

        with open(self.wiki_path, "w", encoding="utf-8") as f:
            f.write(content)
