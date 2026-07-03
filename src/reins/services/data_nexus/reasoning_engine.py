import os
import re
import xml.etree.ElementTree as ET
import subprocess
from typing import Optional, Dict
from reins.services.logger import get_logger

logger = get_logger("universal_router")

class UniversalModelRouter:
    """
    The Universal Model Harness and Router.
    Parses the Hermes Blueprint (data_hermes_wiki.xml) to dynamically route inference 
    tasks to the optimal local or remote model based on the tier list matrix.
    """
    def __init__(self) -> None:
        self.blueprint_path = os.path.expanduser("~/data_rein/knowledge_base/agents/hermes/data_hermes_wiki.xml")
        self.matrix_cache: Dict[str, Dict[str, str]] = {}
        self._parse_blueprint()

    def _parse_blueprint(self) -> None:
        """Parses the CDATA Markdown matrix from the Hermes Wiki XML."""
        if not os.path.exists(self.blueprint_path):
            logger.error(f"Hermes blueprint not found at {self.blueprint_path}")
            return
            
        try:
            tree = ET.parse(self.blueprint_path)
            root = tree.getroot()
            content = root.find("content")
            if content is None or not content.text:
                return
                
            markdown = content.text
            
            # Split by node
            nodes = {"amdy": "", "tell": ""}
            current_node = None
            
            for line in markdown.split('\n'):
                if "### NODE: AMDY" in line:
                    current_node = "amdy"
                elif "### NODE: TELL" in line:
                    current_node = "tell"
                elif current_node:
                    nodes[current_node] += line + "\n"
                    
            for node, text in nodes.items():
                self.matrix_cache[node] = {}
                # Match e.g. **[General Chatting]**\n   - Tier 1: Llama-3-8B-Instruct (
                pattern = r"\*\*\[(.*?)\]\*\*\n\s+- Tier 1: (.*?) \("
                matches = re.findall(pattern, text)
                for task, model in matches:
                    self.matrix_cache[node][task.strip()] = model.strip()
                    
            logger.info(f"Loaded Universal Model Matrix from {self.blueprint_path}")
        except Exception as e:
            logger.error(f"Failed to parse Hermes blueprint: {e}")

    def get_optimal_model(self, task: str, node: str = "amdy") -> str:
        """Looks up the Tier 1 model for the specified task and node."""
        node = node.lower()
        if node not in self.matrix_cache:
            return "llama3:latest" # ultimate fallback
        
        return self.matrix_cache[node].get(task, "llama3:latest")

    def route_inference(self, task: str, prompt: str, target_node: str = "amdy", task_id: str = None) -> Optional[str]:
        """
        Dispatches the inference request. Integrates Loop-Agentic Task Trail.
        If a prompt fails, it gracefully falls back to the secondary node.
        """
        from reins.services.task_trail import TaskTrail
        trail = TaskTrail()
        
        if not task_id:
            task_id = trail.create_task(task, prompt, target_node)
            
        trail.update_task(task_id, "running")
        
        model = self.get_optimal_model(task, target_node)
        logger.info(f"Routing task '{task}' (ID: {task_id}) to node '{target_node}' using model '{model}'")
        
        command = []
        if target_node == "tell":
            command = ["ssh", "-o", "BatchMode=yes", "tell", "ollama", "run", model]
        else:
            command = ["ollama", "run", model]
            
        try:
            res = subprocess.run(
                command,
                input=prompt.encode("utf-8"),
                capture_output=True
            )
            
            if res.returncode == 0 and res.stdout.strip():
                trail.update_task(task_id, "success")
                return res.stdout.decode("utf-8")
            else:
                raise RuntimeError(f"Ollama inference returned empty or failed: {res.stderr.decode('utf-8')}")
                
        except Exception as e:
            logger.error(f"Inference failed on {target_node}: {e}")
            trail.update_task(task_id, "failed")
            
            # Sofia Protocol: Graceful Degradation & Loop-Agentic Failover
            fallback_node = "tell" if target_node == "amdy" else "amdy"
            logger.warning(f"Graceful Degradation triggered. Falling back task {task_id} to node {fallback_node}")
            
            # Pick up the failed prompt and try the fallback node
            return self._fallback_inference(task, prompt, fallback_node, task_id, trail)

    def _fallback_inference(self, task: str, prompt: str, fallback_node: str, task_id: str, trail: Any) -> Optional[str]:
        """Secondary loop for Graceful Degradation."""
        model = self.get_optimal_model(task, fallback_node)
        logger.info(f"Fallback routing task '{task}' to '{fallback_node}' using '{model}'")
        
        trail.update_task(task_id, "running_fallback")
        
        command = []
        if fallback_node == "tell":
            command = ["ssh", "-o", "BatchMode=yes", "tell", "ollama", "run", model]
        else:
            command = ["ollama", "run", model]
            
        try:
            res = subprocess.run(
                command,
                input=prompt.encode("utf-8"),
                capture_output=True
            )
            if res.returncode == 0 and res.stdout.strip():
                trail.update_task(task_id, "success_fallback")
                return res.stdout.decode("utf-8")
        except Exception:
            pass
            
        logger.error(f"Ultimate failure: Task {task_id} failed on both nodes.")
        trail.update_task(task_id, "fatal_error")
        return None

# Keep backward compatibility alias for now
ReasoningEngine = UniversalModelRouter
