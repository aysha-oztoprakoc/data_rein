"""Local-only image understanding through the model-agnostic router inventory."""

from __future__ import annotations

import base64
import os
import urllib.request
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from reins.harness import external_io, local, paths
from reins.harness.models import ModelRouter


class _VisionResponse(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    response: str = ""


class _VisionRequest(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    model: str
    prompt: str
    images: tuple[str, ...]
    stream: bool = False
    options: dict[str, str | int | float | bool] = Field(default_factory=dict)


class _CoordinatorDefaults(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    defaults: dict[str, str | int | float | bool] = Field(
        default_factory=lambda: {"num_ctx": 2048, "num_thread": 8}
    )


def _default_options() -> dict[str, str | int | float | bool]:
    try:
        config = _CoordinatorDefaults.model_validate_json(
            paths.coordinator_config().read_text(encoding="utf-8")
        )
    except (OSError, ValidationError):
        config = _CoordinatorDefaults()
    return config.defaults


def _vision_model() -> str:
    for candidate in ModelRouter().candidates("image generation", "amdy"):
        if candidate.resolved_provider == "ollama":
            return candidate.model
    raise RuntimeError("no hardware-admitted local vision model is configured")


def describe_image(path: Path) -> str:
    """Describe visible entities, text, and relationships without cloud egress."""
    if not local.ensure_server():
        raise RuntimeError("local Ollama server is unavailable")
    prompt = (
        "Extract durable knowledge from this image. Describe visible text, entities, "
        "relationships, diagrams, and relevant spatial structure. Be precise and factual."
    )
    payload = _VisionRequest(
        model=_vision_model(),
        prompt=prompt,
        images=(base64.b64encode(path.read_bytes()).decode("ascii"),),
        options=_default_options(),
    )
    host = os.environ.get("OLLAMA_HOST", local.DEFAULT_HOST).replace("http://", "")
    request = urllib.request.Request(
        f"http://{host}/api/generate",
        data=payload.model_dump_json().encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with external_io.urlopen(request, timeout=300) as response:
        parsed = _VisionResponse.model_validate_json(response.read())
    if not parsed.response.strip():
        raise RuntimeError("local vision model returned an empty description")
    return parsed.response.strip()
