"""
Autonomous execution workflow combining remote and local models.

Adapts prompts dynamically for local execution based on hardware metrics (e.g. context limit).
Escalates large or highly complex tasks seamlessly to cloud/remote models to optimize reliability, 
while preserving privacy/cost when the task fits locally.
"""
from __future__ import annotations

import logging
from reins.harness.models import ModelRouter
from reins.harness.model_types import RouteResult

logger = logging.getLogger(__name__)


class AutonomousWorkflow:
    def __init__(self, router: ModelRouter | None = None) -> None:
        self.router = router or ModelRouter()

    def _is_complex(self, prompt: str) -> bool:
        """
        Determine if the prompt is too complex for the best available local model.
        Heuristics include extreme length or explicit request for heavy architectures.
        """
        # > 1500 words is typically heavy for 8GB VRAM contexts
        if len(prompt.split()) > 1500:
            return True

        heavy_keywords = ["refactor", "architect", "comprehensive", "deep design", "huge planning"]
        prompt_lower = prompt.lower()
        if sum(1 for kw in heavy_keywords if kw in prompt_lower) >= 2:
            return True

        return False

    def _adapt_prompt(self, prompt: str, power: str) -> str:
        """
        Shrink or constrain the instructions for weaker models so they don't hallucinate.
        """
        if power == "low":
            return (
                "You are an autonomous local assistant with limited context.\n"
                "Provide a direct, exact, and highly condensed response.\n"
                "Skip explanations.\n\n"
                f"TASK:\n{prompt}"
            )
        elif power == "medium":
            return (
                "You are a capable local assistant.\n"
                "Provide a concise and direct answer without filler text.\n\n"
                f"TASK:\n{prompt}"
            )
        return prompt

    def _is_stuck(self, result: RouteResult) -> bool:
        """Evaluate if the local model failed or returned a hallucination/stuck loop."""
        if not result.ok or not result.text:
            return True

        text_lower = result.text.lower().strip()
        if len(text_lower) < 10:
            return True

        failure_signals = [
            "i don't know",
            "i cannot",
            "i am an ai",
            "i'm not sure",
            "an error occurred",
            "as an ai",
        ]
        if any(signal in text_lower for signal in failure_signals):
            return True

        return False

    def execute(self, category: str, prompt: str, node: str = "amdy") -> RouteResult:
        """
        End-to-end execution combining local and remote.
        """
        if self._is_complex(prompt):
            logger.info("Task flagged as overly complex or huge. Routing directly to cloud.")
            return self.router.route_cloud(prompt)

        optimal_local = self.router.optimal(category, node)
        power = getattr(optimal_local, "power", "unknown")

        # Pull model if it fits but is not installed
        if optimal_local.model != "none" and optimal_local.provider in {"", "ollama"}:
            try:
                from reins.harness import local
                installed = local.list_models()
                if optimal_local.model not in installed:
                    logger.info("Optimal local model '%s' is missing. Pulling now...", optimal_local.model)
                    success = local.pull_model(optimal_local.model)
                    if not success:
                        logger.warning("Failed to pull model '%s'. Escalating to cloud.", optimal_local.model)
                        return self.router.route_cloud(prompt)
            except Exception:
                logger.warning("Failed to verify or pull local model %s", optimal_local.model, exc_info=True)

        adapted = self._adapt_prompt(prompt, power)

        logger.info("Attempting task with local model '%s' (power=%s).", optimal_local.model, power)
        local_result = self.router.route(category, adapted, node)

        if self._is_stuck(local_result):
            logger.warning("Local model '%s' failed or got stuck. Escalating to cloud.", optimal_local.model)
            return self.router.route_cloud(prompt)

        return local_result
