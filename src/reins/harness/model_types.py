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
    "gemini": frozenset({ExecutionPlane.CLOUD_TEXT}),
    "openai": frozenset({ExecutionPlane.CLOUD_TEXT}),
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
            return "claude"
        if model.startswith(("gpt", "openai", "o1", "o3")) or ":cloud" in model:
            return "openai"
        return "ollama"


@dataclass(frozen=True, slots=True)
class RouteResult:
    text: str | None
    model: str
    provider: str
    node: str
    ok: bool
    error: str | None = None
