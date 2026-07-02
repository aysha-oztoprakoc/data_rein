import os
import json
import subprocess
from typing import Optional, List
from reins.services.logger import get_logger

logger = get_logger("reasoning_engine")

class ReasoningEngine:
    def __init__(self) -> None:
        self.repo_dir = os.path.expanduser("~/data_rein")
        self.training_dir = os.path.join(self.repo_dir, "moe_training")
        self.state_file = os.path.expanduser("~/.config/data_nexus/state.json")
        self.model = "deepseek-r1:14b"
        
        # Ensure training and state directories exist
        os.makedirs(self.training_dir, exist_ok=True)
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)

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
        """
        Scans the training data folder for files modified since the last run.
        """
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
            return "" # No changes

        self.update_last_run_timestamp(current_time)

        context = ""
        for fpath in modified_files[:5]: # Cap to 5 files to avoid context blowout
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
        """
        Uses Ollama to generate an optimization based on newly found training data.
        """
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

        try:
            res = subprocess.run(
                ["ollama", "run", self.model],
                input=prompt.encode("utf-8"),
                capture_output=True
            )
            
            if res.returncode == 0:
                return res.stdout.decode("utf-8")
            else:
                logger.error(f"Ollama inference failed: {res.stderr.decode('utf-8')}")
                return None
        except Exception as e:
            logger.error(f"Reasoning engine error: {e}")
            return None
