from __future__ import annotations

import logging
from pathlib import Path

from pydantic import ValidationError

from reins.harness import paths
from reins.harness.model_types import (
    Combo,
    ExecutionPlane,
    ModelSpec,
    OmniRouterConfig,
    DEFAULT_PROVIDER_CAPABILITIES,
)

logger = logging.getLogger(__name__)


class ComboRegistry:
    """Manages the combo registry from config/omnirouter.json."""

    def __init__(self, config_path: Path | None = None) -> None:
        self._path = config_path or paths.omnirouter_config()
        self._combos: dict[str, Combo] = {}
        self._config: OmniRouterConfig = OmniRouterConfig()
        self._load()

    def _load(self) -> None:
        try:
            text = self._path.read_text(encoding="utf-8")
            self._config = OmniRouterConfig.model_validate_json(text)
            self._combos = {combo.id: combo for combo in self._config.combos}
        except (OSError, ValidationError):
            logger.warning("omnirouter config failed to load from %s", self._path, exc_info=True)
            self._config = OmniRouterConfig()
            self._combos = {}

    def reload(self) -> None:
        self._load()

    def get_combo(self, combo_id: str) -> Combo | None:
        return self._combos.get(combo_id)

    def all_combos(self) -> list[Combo]:
        return list(self._config.combos)

    def combos_for_category(self, category: str, node: str = "amdy") -> list[Combo]:
        cat = self._config.categories.get(category)
        if cat is None:
            return []
        if node == "cloud":
            ids = cat.cloud
        elif node == "tell":
            ids = cat.tell
        else:
            ids = cat.amdy
        return [self._combos[cid] for cid in ids if cid in self._combos]

    def cloud_fallback_combos(self) -> list[Combo]:
        return [self._combos[cid] for cid in self._config.cloud_fallback if cid in self._combos]

    def combo_to_spec(self, combo: Combo) -> ModelSpec:
        capabilities = DEFAULT_PROVIDER_CAPABILITIES.get(combo.provider, frozenset())
        return ModelSpec(
            model=combo.model,
            score=combo.score,
            power=combo.power,
            provider=combo.provider,
            capabilities=capabilities,
            extra={"combo_id": combo.id, "secret_key": combo.secret_key, "base_url": combo.base_url, "tier": combo.tier},
        )

    @property
    def config(self) -> OmniRouterConfig:
        return self._config
