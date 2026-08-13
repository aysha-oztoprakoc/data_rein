from __future__ import annotations

import hashlib
import logging
from pathlib import Path

from pydantic import ValidationError

from reins.harness import paths
from reins.harness.model_types import InventoryConfig

logger = logging.getLogger(__name__)


class ModelInventory:
    def __init__(self, registry_path: Path | None = None) -> None:
        self.registry_path: Path = registry_path or paths.model_registry()
        self._config: InventoryConfig = self._load()

    def _load(self) -> InventoryConfig:
        try:
            return InventoryConfig.model_validate_json(self.registry_path.read_text(encoding="utf-8"))
        except (OSError, ValidationError):
            logger.warning("model inventory failed to load", exc_info=True)
            return InventoryConfig()

    def node_reachable(self, node: str) -> bool:
        if node == "cloud":
            return True
        inventory = self._config.for_node(node)
        return inventory is not None and inventory.reachable

    def model_fits(self, node: str, model: str) -> bool:
        inventory = self._config.for_node(node)
        return inventory is not None and any(item.model == model for item in inventory.models_fit)

    def record_rejection(self, node: str, model: str, reason: str) -> None:
        logger.warning("model rejected by hardware policy: %s/%s: %s", node, model, reason)
        try:
            from reins.services.task_trail import TaskTrail

            digest = hashlib.sha256(f"{node}:{model}:{reason}".encode()).hexdigest()[:16]
            _ = TaskTrail().upsert_task(
                f"hardware-rejection-{digest}",
                task_type="router:hardware-rejection",
                prompt=f"{node}/{model}: {reason}",
                target_node=node,
                status="failed",
                model=model,
                reason=reason,
            )
        except Exception:
            logger.warning("hardware rejection was not persisted", exc_info=True)

    def admit(self, node: str, model: str) -> bool:
        if not self.node_reachable(node):
            self.record_rejection(node, model, "node_unreachable")
            return False
        if not self.model_fits(node, model):
            self.record_rejection(node, model, "model_not_in_fit_registry")
            return False
        return True
