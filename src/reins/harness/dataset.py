"""Export disposable, provenance-preserving training JSONL from the Wiki."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar, Iterator, Literal

from pydantic import BaseModel, ConfigDict, ValidationError

from reins.harness import paths
from reins.harness.wiki import WikiDB
from reins.training.records import TrainingMetadata, TrainingRecord, segment_text


@dataclass(frozen=True, slots=True)
class ExportStats:
    written: int = 0
    skipped: int = 0
    out_path: str = ""


class _PageRow(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    slug: str
    content: str
    category: str
    source_path: str | None = None
    metadata_json: str = "{}"


class _MemoryRow(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    text: str
    category: str
    source: str | None = None


def _page_modality(category: str, metadata: TrainingMetadata) -> str | None:
    if metadata.modality:
        return metadata.modality
    prefix = "digested/"
    return category[len(prefix) :] if category.startswith(prefix) else None


def _page_metadata(row: _PageRow) -> TrainingMetadata:
    raw = row.metadata_json or "{}"
    metadata = TrainingMetadata.model_validate_json(raw)
    return metadata.model_copy(
        update={
            "slug": row.slug,
            "category": row.category,
            "source_path": row.source_path,
            "modality": _page_modality(row.category, metadata),
        }
    )


def _records(text: str, metadata: TrainingMetadata, max_chars: int) -> tuple[TrainingRecord, ...]:
    segments = segment_text(text, max_chars)
    count = len(segments)
    return tuple(
        TrainingRecord(
            text=segment,
            meta=metadata.model_copy(
                update={"segment_index": index, "segment_count": count}
            ),
        )
        for index, segment in enumerate(segments)
    )


def _confine_out_path(out_path: str) -> Path:
    """Resolve ``out_path`` inside the bounded export root (fail-closed).

    Relative paths (bare filenames) land under ``paths.export_dir()``; absolute
    paths must resolve within it. Any escape attempt raises ``ValueError`` so an
    untrusted caller cannot write JSONL outside the export root.
    """
    root = paths.export_dir()
    raw = Path(out_path).expanduser()
    if not raw.is_absolute():
        raw = root / raw
    resolved = raw.resolve()
    root_resolved = root.resolve()
    if root_resolved not in resolved.parents and resolved != root_resolved:
        raise ValueError(f"export path escapes the export root ({root}): {out_path}")
    return resolved


def export_jsonl(
    out_path: str,
    *,
    categories: list[str] | None = None,
    modality: str | None = None,
    kind: Literal["completion", "memories"] = "completion",
    min_chars: int = 64,
    max_chars: int = 8192,
    limit: int = 0,
) -> ExportStats:
    """Derive bounded records; the Wiki remains the sole knowledge store."""
    written = 0
    skipped = 0
    output = _confine_out_path(out_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    selected = list(categories) if categories else []
    if modality:
        selected.append(f"digested/{modality}")

    with WikiDB() as db, output.open("w", encoding="utf-8") as destination:
        rows = (
            _query_memories(db, selected, limit)
            if kind == "memories"
            else _query_pages(db, selected, limit)
        )
        for row in rows:
            try:
                if kind == "memories":
                    memory = _MemoryRow.model_validate(dict(row))
                    text = memory.text
                    metadata = TrainingMetadata(
                        category=memory.category,
                        source=memory.source,
                    )
                    if text.startswith("SFT_JSON:"):
                        import json
                        from reins.training.records import Message
                        payload = json.loads(text[9:])
                        messages = [Message(**m) for m in payload.get("messages", [])]
                        record = TrainingRecord(messages=messages, meta=metadata)
                        _ = destination.write(record.model_dump_json(exclude_none=True) + "\n")
                        written += 1
                        continue
                else:
                    page = _PageRow.model_validate(dict(row))
                    text = page.content
                    metadata = _page_metadata(page)
                if len(text) < min_chars:
                    skipped += 1
                    continue
                for record in _records(text, metadata, max_chars):
                    _ = destination.write(record.model_dump_json(exclude_none=True) + "\n")
                    written += 1
            except (TypeError, ValueError, ValidationError):
                skipped += 1

    return ExportStats(written=written, skipped=skipped, out_path=str(output))


def _query_pages(db: WikiDB, categories: list[str], limit: int) -> Iterator[sqlite3.Row]:
    sql = "SELECT slug, content, category, source_path, metadata_json FROM pages"
    params: list[str | int] = []
    if categories:
        sql += " WHERE " + " OR ".join(["category LIKE ?"] * len(categories))
        params.extend(f"{category}%" for category in categories)
    if limit:
        sql += " LIMIT ?"
        params.append(limit)
    return db.conn.execute(sql, params)


def _query_memories(db: WikiDB, categories: list[str], limit: int) -> Iterator[sqlite3.Row]:
    sql = "SELECT text, category, source FROM memories"
    params: list[str | int] = []
    if categories:
        sql += " WHERE " + " OR ".join(["category LIKE ?"] * len(categories))
        params.extend(f"{category}%" for category in categories)
    if limit:
        sql += " LIMIT ?"
        params.append(limit)
    return db.conn.execute(sql, params)
