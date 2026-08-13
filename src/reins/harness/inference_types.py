from __future__ import annotations

from enum import Enum
from typing import Annotated, ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, field_validator, model_validator

MAX_PROMPT_TOKENS = 16_384

NodeName = Literal["amdy", "tell"]
NonEmptyText = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1, max_length=65_536),
]
ShortText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=4_096)]


class OptimizationMode(str, Enum):
    AUTO = "auto"
    REQUIRED = "required"
    BYPASS = "bypass"


class PromptOptimizationRequest(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    task: NonEmptyText
    category: NonEmptyText
    node: NodeName = "amdy"
    context: str = Field(default="", max_length=65_536)
    constraints: tuple[str, ...] = Field(default=(), max_length=64)
    output_format: str = Field(default="", max_length=8_192)
    max_prompt_tokens: int = Field(default=4_096, ge=128, le=MAX_PROMPT_TOKENS)
    mode: OptimizationMode = OptimizationMode.AUTO

    @field_validator("constraints")
    @classmethod
    def validate_constraints(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(value.strip() for value in values)
        if any(not value or len(value) > 4_096 for value in normalized):
            raise ValueError("constraints must contain non-empty strings of at most 4096 chars")
        return normalized

    @model_validator(mode="after")
    def validate_essential_budget(self) -> PromptOptimizationRequest:
        sections = [f"[TASK]\n{self.task}"]
        if self.constraints:
            sections.append(
                "[CONSTRAINTS]\n" + "\n".join(f"- {item}" for item in self.constraints)
            )
        if self.output_format:
            sections.append(f"[OUTPUT FORMAT]\n{self.output_format}")
        essential = "\n\n".join(sections)
        if max(1, (len(essential) + 3) // 4) > self.max_prompt_tokens:
            raise ValueError("task, constraints, and output format exceed max_prompt_tokens")
        return self


class RemotePromptPackage(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    system_prompt: NonEmptyText
    task_prompt: NonEmptyText
    context_prompt: str = Field(default="", max_length=65_536)
    success_criteria: tuple[ShortText, ...] = Field(min_length=1, max_length=32)

    @field_validator("success_criteria")
    @classmethod
    def validate_criteria(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        normalized = tuple(value.strip() for value in values)
        if any(not value or len(value) > 4_096 for value in normalized):
            raise ValueError("success criteria must be non-empty strings of at most 4096 chars")
        return normalized


class CompiledPromptPackage(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    protocol: Literal["data-rein.remote-local-inference/1"] = (
        "data-rein.remote-local-inference/1"
    )
    source_sha256: Annotated[str, StringConstraints(pattern=r"^[0-9a-f]{64}$")]
    category: NonEmptyText
    node: NodeName
    target_model: NonEmptyText
    target_power: NonEmptyText
    max_prompt_tokens: int = Field(ge=128, le=MAX_PROMPT_TOKENS)
    estimated_tokens: int = Field(ge=1, le=MAX_PROMPT_TOKENS)
    prompt: NonEmptyText
    success_criteria: tuple[ShortText, ...] = Field(min_length=1, max_length=32)
    optimizer_provider: str | None = None
    optimizer_model: str | None = None
    remote_attempted: bool
    remote_used: bool
    degradation_reason: str | None = None

    @model_validator(mode="after")
    def validate_budget_integrity(self) -> CompiledPromptPackage:
        actual_tokens = max(1, (len(self.prompt) + 3) // 4)
        if self.estimated_tokens != actual_tokens:
            raise ValueError("estimated_tokens does not match the canonical estimate")
        if actual_tokens > self.max_prompt_tokens:
            raise ValueError("compiled prompt exceeds max_prompt_tokens")
        return self


class CompilationResult(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    ok: bool
    package: CompiledPromptPackage | None = None
    error: str | None = None
    task_id: str | None = None


class InferenceExecutionResult(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    ok: bool
    text: str | None
    model: str
    provider: str
    node: str
    error: str | None = None
    package_sha256: str
    task_id: str | None = None


class CompilerTarget(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    model: NonEmptyText
    power: NonEmptyText
    node: NodeName
    max_prompt_tokens: int = Field(ge=128, le=MAX_PROMPT_TOKENS)


class RemoteCompilerEnvelope(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    protocol: Literal["data-rein.prompt-compiler/1"]
    operation: Literal["compress_context_and_adapt_format"]
    request: PromptOptimizationRequest
    target: CompilerTarget
    output_schema: dict[str, str]
    rules: tuple[str, ...]
