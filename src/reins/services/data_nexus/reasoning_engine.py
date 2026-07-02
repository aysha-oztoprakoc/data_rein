import os
import random
import subprocess
from typing import Optional, List
from reins.services.logger import get_logger

logger = get_logger("reasoning_engine")

class ReasoningEngine:
    def __init__(self) -> None:
        self.repo_dir = os.path.expanduser("~/data_rein")
        self.model = "deepseek-r1:14b" # Will use Ollama locally if available

    def gather_context(self) -> str:
        """
        Randomly samples 3 Python or C++ files from the repository to analyze.
        """
        all_files: List[str] = []
        for root, dirs, files in os.walk(self.repo_dir):
            if ".git" in root or ".venv" in root or "node_modules" in root:
                continue
            for f in files:
                if f.endswith((".py", ".cpp", ".hpp", ".h", ".md")):
                    all_files.append(os.path.join(root, f))
        
        if not all_files:
            return "No files found to analyze."

        sampled_files = random.sample(all_files, min(3, len(all_files)))
        
        context = ""
        for fpath in sampled_files:
            try:
                with open(fpath, "r", encoding="utf-8") as file_obj:
                    content = file_obj.read()
                    # Truncate content if too large (naive chunking)
                    if len(content) > 10000:
                        content = content[:10000] + "\n...[TRUNCATED]"
                    context += f"--- FILE: {os.path.basename(fpath)} ---\n{content}\n\n"
            except Exception as e:
                context += f"Failed to read {fpath}: {e}\n"
        
        return context

    def generate_optimization(self) -> Optional[str]:
        """
        Uses Ollama to generate an optimization or test for the given context.
        """
        context = self.gather_context()
        prompt = (
            "You are Data-Nexus, an autonomous 24/7 observer daemon.\n"
            "Analyze the following codebase snippets and generate a specific, actionable optimization "
            "or a new test case. Focus on safety, performance, and PON (Notification-Oriented Paradigm) compliance.\n\n"
            f"Context:\n{context}\n\n"
            "Provide your analysis, optimization, or test case in Markdown format."
        )

        try:
            # We use subprocess to call local ollama run.
            # This is pedantically restricted but we need inference.
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
