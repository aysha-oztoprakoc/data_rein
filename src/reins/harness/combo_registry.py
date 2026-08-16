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


    def save(self) -> None:
        text = self._config.model_dump_json(indent=4)
        self._path.write_text(text, encoding="utf-8")

    def add_combo(self, combo: Combo) -> None:
        # replace if exists
        c_list = [c for c in self._config.combos if c.id != combo.id]
        c_list.append(combo)
        # We need to recreate _config since it's frozen
        # Pydantic v2 model_copy with update
        self._config = self._config.model_copy(update={"combos": tuple(c_list)})
        self._combos = {c.id: c for c in self._config.combos}
        self.save()

    def remove_combo(self, combo_id: str) -> bool:
        if combo_id not in self._combos:
            return False
        c_list = [c for c in self._config.combos if c.id != combo_id]
        self._config = self._config.model_copy(update={"combos": tuple(c_list)})
        self._combos = {c.id: c for c in self._config.combos}
        self.save()
        return True

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

    def set_category_model(self, category: str, combo_id: str, node: str = "amdy") -> bool:
        matching = [c.id for c in self.all_combos() if c.id == combo_id or c.model == combo_id]
        if matching:
            combo_id = matching[0]

        cat = self._config.categories.get(category)
        from reins.harness.model_types import OmniCategory
        if cat is None:
            cat = OmniCategory(description=f"Archetype category {category}", amdy=(combo_id,), tell=(), cloud=(combo_id,))
            new_cats = dict(self._config.categories)
            new_cats[category] = cat
        else:
            if node == "cloud":
                new_ids = [combo_id] + [cid for cid in cat.cloud if cid != combo_id]
                new_cat = cat.model_copy(update={"cloud": tuple(new_ids)})
            elif node == "tell":
                new_ids = [combo_id] + [cid for cid in cat.tell if cid != combo_id]
                new_cat = cat.model_copy(update={"tell": tuple(new_ids)})
            else:
                new_ids = [combo_id] + [cid for cid in cat.amdy if cid != combo_id]
                new_cat = cat.model_copy(update={"amdy": tuple(new_ids)})
            new_cats = dict(self._config.categories)
            new_cats[category] = new_cat

        self._config = self._config.model_copy(update={"categories": new_cats})
        self.save()
        return True

    @property
    def config(self) -> OmniRouterConfig:
        return self._config
