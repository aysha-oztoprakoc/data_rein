import os
import re
import json
import xml.etree.ElementTree as ET
import subprocess
from typing import Optional, Dict, Any
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
        self.repo_dir = os.path.expanduser("~/data_rein")
        self.training_dir = os.path.join(self.repo_dir, "moe_training")
        self.state_file = os.path.expanduser("~/.config/data_nexus/state.json")
        
        os.makedirs(self.training_dir, exist_ok=True)
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
        
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
        """
        Looks up the Tier 1 model for the specified task and node.

        Prefers the model-agnostic harness router (config/model_router.json) so
        routing is driven by the single canonical config; falls back to the
        legacy Hermes XML blueprint matrix, then to a hard default.
        """
        node = node.lower()

        # 1. Canonical, model-agnostic router (config/model_router.json).
        try:
            from reins.harness.models import ModelRouter
            spec = ModelRouter().optimal(task.lower(), node)
            if spec and spec.model and spec.model != ModelRouter.FALLBACK_MODEL:
                return spec.model
        except Exception:
            pass

        # 2. Legacy XML blueprint matrix.
        if node in self.matrix_cache:
            legacy = self.matrix_cache[node].get(task)
            if legacy:
                return legacy

        # 3. Ultimate fallback.
        return "llama3.1:8b"

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

    def get_last_run_timestamp(self) -> float:
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r") as f:
                    return json.load(f).get("last_run", 0.0)
            except Exception:
                return 0.0
        return 0.0

    def update_last_run_timestamp(self, ts: float) -> None:
        try:
            with open(self.state_file, "w") as f:
                json.dump({"last_run": ts}, f)
        except Exception as e:
            logger.error(f"Failed to update state: {e}")

    def gather_training_context(self) -> str:
        last_run = self.get_last_run_timestamp()
        current_time = __import__('time').time()
        
        modified_files = []
        for root, _, files in os.walk(self.training_dir):
            for f in files:
                fpath = os.path.join(root, f)
                try:
                    if os.path.getmtime(fpath) > last_run:
                        modified_files.append(fpath)
                except Exception:
                    pass
        
        if not modified_files:
            return ""

        self.update_last_run_timestamp(current_time)

        context = ""
        for fpath in modified_files[:5]:
            try:
                with open(fpath, "r", encoding="utf-8") as file_obj:
                    content = file_obj.read()
                    if len(content) > 5000:
                        content = content[:5000] + "\n...[TRUNCATED]"
                    context += f"--- NEW/MODIFIED FILE: {os.path.basename(fpath)} ---\n{content}\n\n"
            except Exception as e:
                logger.error(f"Failed to read {fpath}: {e}")
        
        return context

    def generate_optimization(self) -> Optional[str]:
        context = self.gather_training_context()
        if not context:
            logger.info("No training data changes detected. Idling.")
            return None
            
        prompt = (
            "You are Data-Nexus, the Searcher of Knowledge.\n"
            "Analyze the following newly added/modified training data and generate a synthesized insight, "
            "optimization, or learning extraction. Focus on safety, performance, and scalability.\n\n"
            f"Context:\n{context}\n\n"
            "Provide your insight in Markdown format."
        )

        return self.route_inference(task="Data Processing", prompt=prompt, target_node="amdy")

# Keep backward compatibility alias for now
ReasoningEngine = UniversalModelRouter
