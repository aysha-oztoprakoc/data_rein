"""Validated local fine-tuning configuration for model-agnostic adapters."""

from __future__ import annotations

from collections.abc import Mapping
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field, JsonValue, ValidationError

from reins.harness import paths
from reins.services.logger import log_degradation


class LoraSettings(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    r: int = Field(default=16, ge=1)
    alpha: int = Field(default=32, ge=1)
    dropout: float = Field(default=0.05, ge=0, lt=1)
    target_modules: tuple[str, ...] = ("q_proj", "v_proj")


class TrainingConfig(BaseModel):
    """Hardware-bounded settings consumed by one optional training backend."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    base_model: str = "Qwen/Qwen2.5-3B-Instruct"
    base_model_revision: str = Field(
        default="aa8e72537993ba99e69dfaafa59ed015b17504d1",
        pattern=r"^[0-9a-f]{40}$",
    )
    small_base_model: str = "Qwen/Qwen2.5-3B-Instruct"
    small_base_model_revision: str = Field(
        default="aa8e72537993ba99e69dfaafa59ed015b17504d1",
        pattern=r"^[0-9a-f]{40}$",
    )
    tiny_base_model: str = "Qwen/Qwen2.5-0.5B-Instruct"
    tiny_base_model_revision: str = Field(
        default="7ae557604adf67be50417f59c2c2f167def9a775",
        pattern=r"^[0-9a-f]{40}$",
    )
    dataset_path: str = ""
    output_dir: str | None = None
    max_seq_len: int = Field(default=2048, ge=256)
    per_device_batch_size: int = Field(default=1, ge=1)
    gradient_accumulation_steps: int = Field(default=16, ge=1)
    num_train_epochs: float = Field(default=3, gt=0)
    learning_rate: float = Field(default=0.0002, gt=0)
    lora: LoraSettings = Field(default_factory=LoraSettings)
    optim: str = "paged_adamw_8bit"
    gradient_checkpointing: bool = True

    def base_for(self, key: str) -> str:
        return {
            "base_model": self.base_model,
            "small_base_model": self.small_base_model,
            "tiny_base_model": self.tiny_base_model,
        }.get(key, self.base_model)

    def source_for(self, key: str) -> tuple[str, str]:
        return {
            "base_model": (self.base_model, self.base_model_revision),
            "small_base_model": (self.small_base_model, self.small_base_model_revision),
            "tiny_base_model": (self.tiny_base_model, self.tiny_base_model_revision),
        }.get(key, (self.base_model, self.base_model_revision))


def load_training_config(
    overrides: Mapping[str, JsonValue] | None = None,
) -> TrainingConfig:
    try:
        base = TrainingConfig.model_validate_json(
            paths.training_config().read_text(encoding="utf-8")
        )
    except (OSError, ValidationError):
        log_degradation(__name__)
        base = TrainingConfig()
    if not overrides:
        return base
    merged = base.model_dump()
    merged.update(overrides)
    return TrainingConfig.model_validate(merged)
