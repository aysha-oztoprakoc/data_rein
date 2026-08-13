"""
Data-Nexus reasoning engine.

Post-convergence this is a thin ``HarnessAgent``: it no longer carries its own
model router. The legacy ``UniversalModelRouter`` (raw ``ollama``/``ssh`` subprocess
dispatch + Hermes XML blueprint matrix + hand-rolled amdy<->tell failover) has been
removed — all of that now lives once, in ``reins.harness.models.ModelRouter``, which
this engine reaches through ``self.infer``. What remains here is the Nexus-specific
part: watch the training corpus for changes and synthesize an insight from them.
"""

import os
import json
import time
from typing import Optional

from reins.services.logger import get_logger, log_degradation
from reins.harness import paths
from reins.harness.agents import HarnessAgent

logger = get_logger("reasoning_engine")


class ReasoningEngine(HarnessAgent):
    """Continuous-learning reasoner: routes through the single harness gateway."""

    role = "data-nexus"

    def __init__(self) -> None:
        super().__init__()
        self.repo_dir = str(paths.home())
        self.training_dir = os.path.join(self.repo_dir, "moe_training")
        self.state_file = str(paths.state_dir() / "nexus_state.json")
        os.makedirs(self.training_dir, exist_ok=True)
        paths.ensure_state_dir()

    # -- change-watermark state ----------------------------------------------
    def get_last_run_timestamp(self) -> float:
        try:
            with open(self.state_file, "r") as f:
                return json.load(f).get("last_run", 0.0)
        except Exception:
            log_degradation(__name__)
            return 0.0

    def update_last_run_timestamp(self, ts: float) -> None:
        try:
            with open(self.state_file, "w") as f:
                json.dump({"last_run": ts}, f)
        except Exception as e:
            logger.error(f"Failed to update nexus state: {e}")

    def gather_training_context(self) -> str:
        last_run = self.get_last_run_timestamp()
        now = time.time()
        modified = []
        for root, _, files in os.walk(self.training_dir):
            for f in files:
                fpath = os.path.join(root, f)
                try:
                    if os.path.getmtime(fpath) > last_run:
                        modified.append(fpath)
                except Exception:
                    log_degradation(__name__)
                    pass
        if not modified:
            return ""

        self.update_last_run_timestamp(now)
        context = ""
        for fpath in modified[:5]:
            try:
                with open(fpath, "r", encoding="utf-8") as fo:
                    content = fo.read()
                    if len(content) > 5000:
                        content = content[:5000] + "\n...[TRUNCATED]"
                    context += f"--- NEW/MODIFIED FILE: {os.path.basename(fpath)} ---\n{content}\n\n"
            except Exception as e:
                logger.error(f"Failed to read {fpath}: {e}")
        return context

    # -- reasoning ------------------------------------------------------------
    def generate_optimization(self) -> Optional[str]:
        context = self.gather_training_context()
        if not context:
            logger.info("No training data changes detected. Idling.")
            return None

        prompt = (
            "You are Data-Nexus, the Searcher of Knowledge.\n"
            "Analyze the following newly added/modified training data and generate a "
            "synthesized insight, optimization, or learning extraction. Focus on safety, "
            "performance, and scalability.\n\n"
            f"Context:\n{context}\n\n"
            "Provide your insight in Markdown format."
        )
        # Log to the shared Task Trail so this reasoning pass is visible to
        # `agent_status()`/`trail_list()`/the Sofia dashboard, mirroring
        # subagent_manager.py's _execute_subagent. Never blocks/raises - trail
        # may be unavailable (HarnessAgent sets it to None on init failure).
        task_id = None
        if self.trail is not None:
            try:
                task_id = self.trail.create_task(f"{self.role}:optimization", prompt, "amdy")
                self.trail.set_status(task_id, "running")
            except Exception:
                log_degradation(__name__)
                task_id = None

        # One gateway: routes to the best local model with amdy<->tell failover,
        # never raises (graceful degradation is built into workflow.run).
        res = self.infer("data processing", prompt, node="amdy")

        if task_id is not None:
            try:
                self.trail.set_status(task_id, "success" if res.ok else "failed")
            except Exception:
                log_degradation(__name__)
                pass

        if res.ok:
            logger.info(f"Nexus insight generated on {res.model} ({res.node}).")
            return res.text
        logger.error(f"Nexus reasoning degraded: {res.error}")
        return None
