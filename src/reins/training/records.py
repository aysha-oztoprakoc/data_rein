"""Validated, provenance-preserving records derived from the canonical Wiki."""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator


class TrainingMetadata(BaseModel):
    """Source identity and segmentation coordinates retained during training."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="allow")

    slug: str | None = None
    category: str | None = None
    source: str | None = None
    source_path: str | None = None
    source_sha256: str | None = None
    modality: str | None = None
    extractor: str | None = None
    channels: tuple[str, ...] = ()
    segment_index: int = Field(default=0, ge=0)
    segment_count: int = Field(default=1, ge=1)


class Message(BaseModel):
    role: str
    content: str


class TrainingRecord(BaseModel):
    """One bounded text or conversation sample accepted by the local fine-tuning loop."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    text: str | None = None
    messages: list[Message] | None = None
    meta: TrainingMetadata = Field(default_factory=TrainingMetadata)

    @model_validator(mode="after")
    def _validate_content(self) -> TrainingRecord:
        if not self.text and not self.messages:
            raise ValueError("training record must contain non-empty text or messages")
        return self


def segment_text(text: str, max_chars: int) -> tuple[str, ...]:
    if max_chars < 1:
        raise ValueError("max_chars must be positive")
    remaining = text.strip()
    segments: list[str] = []
    while remaining:
        if len(remaining) <= max_chars:
            segments.append(remaining)
            break
        boundary = remaining.rfind(" ", 0, max_chars + 1)
        if boundary < max_chars // 2:
            boundary = max_chars
        segment = remaining[:boundary].strip()
        if segment:
            segments.append(segment)
        remaining = remaining[boundary:].strip()
    return tuple(segments)


def validate_jsonl(path: Path) -> int:
    """Reject malformed or empty datasets before local model state changes."""
    count = 0
    with path.open("r", encoding="utf-8") as source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            try:
                _ = TrainingRecord.model_validate_json(line)
            except ValidationError as error:
                raise ValueError(f"training record {line_number} is invalid: {error}") from error
            count += 1
    if count == 0:
        raise ValueError("training record dataset is empty")
    return count
