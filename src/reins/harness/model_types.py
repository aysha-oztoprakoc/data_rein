from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from enum import StrEnum
from typing import ClassVar, Final, Self

from pydantic import BaseModel, ConfigDict, Field


class ExecutionPlane(StrEnum):
    LOCAL_TEXT = "local_text"
    CLOUD_TEXT = "cloud_text"
    IMAGE = "image"


DEFAULT_PROVIDER_CAPABILITIES: Final[Mapping[str, frozenset[ExecutionPlane]]] = {
    "ollama": frozenset({ExecutionPlane.LOCAL_TEXT}),
    "claude": frozenset({ExecutionPlane.CLOUD_TEXT}),
    "anthropic": frozenset({ExecutionPlane.CLOUD_TEXT}),
    "gemini": frozenset({ExecutionPlane.CLOUD_TEXT}),
    "openai": frozenset({ExecutionPlane.CLOUD_TEXT}),
    "deepseek": frozenset({ExecutionPlane.CLOUD_TEXT}),
    "xai": frozenset({ExecutionPlane.CLOUD_TEXT}),
    "moonshot": frozenset({ExecutionPlane.CLOUD_TEXT}),
    "zhipu": frozenset({ExecutionPlane.CLOUD_TEXT}),
    "openrouter": frozenset({ExecutionPlane.CLOUD_TEXT}),
    "comfyui": frozenset({ExecutionPlane.IMAGE}),
}


class ModelEntry(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="allow")

    model: str = "unknown"
    score: float = 0.0
    power: str = "medium"
    provider: str = ""
    backend: str = ""


class CategoryRoutes(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="allow")

    amdy: tuple[ModelEntry, ...] = ()
    tell: tuple[ModelEntry, ...] = ()

    def for_node(self, node: str) -> tuple[ModelEntry, ...]:
        return self.amdy if node == "amdy" else self.tell if node == "tell" else ()


class RouterConfig(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    categories: dict[str, CategoryRoutes] = Field(default_factory=dict)
    remote_fallback: tuple[ModelEntry, ...] = ()


class FitEntry(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    model: str


class NodeInventory(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    reachable: bool = False
    models_installed: tuple[str, ...] = ()
    models_fit: tuple[FitEntry, ...] = ()


class InventoryConfig(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    amdy: NodeInventory = Field(default_factory=NodeInventory)
    tell: NodeInventory = Field(default_factory=NodeInventory)

    def for_node(self, node: str) -> NodeInventory | None:
        return self.amdy if node == "amdy" else self.tell if node == "tell" else None


@dataclass(frozen=True, slots=True)
class ModelSpec:
    model: str
    score: float = 0.0
    power: str = "medium"
    provider: str = ""
    backend: str = ""
    extra: dict[str, str | int | float | bool | None] = field(default_factory=dict)
    capabilities: frozenset[ExecutionPlane] = frozenset()

    @classmethod
    def from_entry(cls, entry: ModelEntry) -> Self:
        return cls(
            model=entry.model,
            score=entry.score,
            power=entry.power,
            provider=entry.provider,
            backend=entry.backend,
        )

    @property
    def resolved_provider(self) -> str:
        if self.provider:
            return self.provider.lower()
        model = self.model.lower()
        if self.backend == "comfyui" or model.startswith("comfyui"):
            return "comfyui"
        if model.startswith("gemini"):
            return "gemini"
        if model.startswith(("claude", "anthropic")):
            return "anthropic"
        if model.startswith(("gpt", "openai", "o1", "o3")) or ":cloud" in model:
            return "openai"
        if model.startswith("deepseek"):
            return "deepseek"
        if model.startswith("grok"):
            return "xai"
        if model.startswith("moonshot"):
            return "moonshot"
        if model.startswith(("glm", "zhipu")):
            return "zhipu"
        return "ollama"


class Combo(BaseModel):
    """A labeled provider+model+key triple — the atomic routing unit."""
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="allow")

    id: str
    provider: str
    model: str
    secret_key: str = ""
    base_url: str = ""
    tier: str = "free"  # free | paid | local
    score: float = 0.0
    power: str = "medium"


class OmniCategory(BaseModel):
    """A category maps to ordered combo-ID chains per execution context."""
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="allow")

    description: str = ""
    amdy: tuple[str, ...] = ()
    tell: tuple[str, ...] = ()
    cloud: tuple[str, ...] = ()


class OmniRouterConfig(BaseModel):
    """Top-level schema for config/omnirouter.json."""
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    combos: tuple[Combo, ...] = ()
    categories: dict[str, OmniCategory] = Field(default_factory=dict)
    cloud_fallback: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class RouteResult:
    text: str | None
    model: str
    provider: str
    node: str
    ok: bool
    error: str | None = None
