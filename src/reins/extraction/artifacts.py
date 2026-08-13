"""Normalize plugin results into validated knowledge artifacts for the Wiki."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field

from reins.extraction.extractors.base import BaseExtractor, ExtractionResult
from reins.extraction.serialization import read_extracted_text


class KnowledgeArtifact(BaseModel):
    """Canonical extraction boundary shared by ingestion, RAG, and training."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    content: str = Field(min_length=1)
    modality: str = Field(min_length=1)
    source_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    extractor: str = Field(min_length=1)
    node: str = Field(min_length=1)
    channels: tuple[str, ...] = Field(min_length=1)
    format: str = "unknown"
    frame_count: int = Field(default=0, ge=0)
    duration_seconds: float | None = Field(default=None, ge=0)
    warnings: tuple[str, ...] = ()

    def wiki_metadata_json(self) -> str:
        """Return the exact metadata persisted beside the Wiki page."""
        return self.model_dump_json(exclude={"content"}, exclude_none=True)


def _source_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize_result(
    source: Path,
    extractor: BaseExtractor,
    result: ExtractionResult,
) -> KnowledgeArtifact:
    """Validate a legacy-compatible extractor result at the ingestion boundary."""
    if result.get("status") != "success":
        raise RuntimeError(result.get("error", "extraction failed"))
    output_path = result.get("output_path")
    if not output_path:
        raise ValueError("successful extraction omitted output_path")
    content = read_extracted_text(output_path).strip()
    if not content:
        raise ValueError("extraction produced no knowledge")
    metadata = result.get("metadata", {})
    modality = metadata.get("modality", extractor.MODALITY)
    channels = tuple(metadata.get("channels", ["text" if modality == "text" else modality]))
    return KnowledgeArtifact(
        content=content,
        modality=modality,
        source_sha256=_source_sha256(source),
        extractor=metadata.get("extractor", type(extractor).__name__),
        node=metadata.get("node", extractor.NODE),
        channels=channels,
        format=metadata.get("format", source.suffix.lower().lstrip(".") or "unknown"),
        frame_count=metadata.get("frame_count", 0),
        duration_seconds=metadata.get("duration_seconds"),
        warnings=tuple(metadata.get("warnings", [])),
    )
