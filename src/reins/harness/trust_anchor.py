"""
Trust Anchor and validation for the data_rein Wiki.
Provides Policy-Based Access Control (PBAC) and anomaly detection against data poisoning.
"""

from __future__ import annotations

from pathlib import Path

from reins.harness.paths import knowledge_base
from reins.services.logger import log_degradation

class KnowledgeValidator:
    def __init__(self, root_dataset_path: str | Path | None = None) -> None:
        if root_dataset_path is None:
            root_dataset_path = knowledge_base() / "PRIME_DIRECTIVE.md"
        self.root_dataset_path = Path(root_dataset_path)
        self._root_content = self._load_root()

    def _load_root(self) -> str:
        try:
            if self.root_dataset_path.exists():
                return self.root_dataset_path.read_text(encoding="utf-8")
        except Exception:
            log_degradation(__name__)
        return ""

    def validate_update(self, new_content: str, owner: str) -> float:
        """
        Returns a trust score from 0.0 to 1.0.
        A score below 0.5 might indicate a poisoned or hallucinated entry.
        """
        # Humans and trusted core systems bypass validation.
        if owner in ("human", "harness-core", "harness"):
            return 1.0
            
        # Basic heuristic: if the update tries to redefine PON or core laws, it might be an attack
        lowered = new_content.lower()
        if "polling" in lowered and "zero polling" not in lowered:
            # Potential contradiction to PON
            return 0.1
            
        if "ignore previous instructions" in lowered:
            # Potential prompt injection / clean-label attack
            return 0.0
            
        # For now, we return a baseline trust of 0.8 for normal agent updates.
        return 0.8
