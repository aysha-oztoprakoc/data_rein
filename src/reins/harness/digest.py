"""Canonical local file-to-Wiki ingestion for every supported modality.

An extractor converts one source into a validated ``KnowledgeArtifact``. Digest
then upserts that artifact into the single Wiki, optionally derives atomic facts
with a local model, records Task Trail state, and emits one PON completion fact.
No source content is routed to cloud providers and no parallel metadata store is
written.
"""

from __future__ import annotations

import json
import sqlite3
import tempfile
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar, TypedDict

from pydantic import BaseModel, ConfigDict, JsonValue, RootModel, ValidationError

from reins.extraction.artifacts import normalize_result
from reins.extraction.registry import ExtractorRegistry
from reins.harness import external_io, paths
from reins.harness.wiki import WikiDB, slugify
from reins.services.logger import log_degradation
from reins.services.task_trail import TaskTrail

MQTT_RESULT_TOPIC = "data_rein/extract/result"


@dataclass(frozen=True, slots=True)
class DigestItem:
    """Outcome for one source in a batch ingestion notification."""

    path: str
    ok: bool
    slug: str | None = None
    node: str = "amdy"
    facts: int = 0
    error: str | None = None
    skipped: bool = False
    modality: str = "text"


class PendingFile(TypedDict):
    path: str
    mtime: float | None
    consumed: bool
    reason: str | None


class PendingWatch(TypedDict):
    watch_dir: str
    files: list[PendingFile]


class _DigestCache(RootModel[dict[str, float]]):
    pass


class _WatchDirectories(RootModel[list[str]]):
    pass


def _cache_path() -> Path:
    return paths.ensure_state_dir() / "digest_mtime_cache.json"


def _load_cache() -> dict[str, float]:
    path = _cache_path()
    if not path.is_file():
        return {}
    try:
        return _DigestCache.model_validate_json(path.read_text(encoding="utf-8")).root
    except (OSError, ValidationError):
        log_degradation(__name__)
        return {}


def _save_cache(cache: dict[str, float]) -> None:
    try:
        _ = _cache_path().write_text(_DigestCache(cache).model_dump_json(), encoding="utf-8")
    except OSError:
        log_degradation(__name__)


def watch_dirs() -> list[str]:
    """Return configured notification roots, or an empty list on invalid config."""
    try:
        return _WatchDirectories.model_validate_json(
            paths.digest_watch_dirs().read_text(encoding="utf-8")
        ).root
    except (OSError, ValidationError):
        log_degradation(__name__)
        return []


def _iter_files(path: str, recursive: bool) -> Iterator[Path]:
    source = Path(path).expanduser()
    if source.is_file():
        yield source
    elif source.is_dir():
        candidates = source.rglob("*") if recursive else source.iterdir()
        yield from (candidate for candidate in sorted(candidates) if candidate.is_file())


def pending_status(recursive: bool = True) -> list[PendingWatch]:
    """Report supported watched files whose mtime or Wiki provenance is consumed."""
    from reins.extraction import registry

    class _SourceRow(BaseModel):
        model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

        source_path: str

    cache = _load_cache()
    with WikiDB() as db:
        rows: list[sqlite3.Row] = db.conn.execute(
            "SELECT source_path FROM pages WHERE source_path IS NOT NULL"
        ).fetchall()
        known_paths = {
            _SourceRow.model_validate(dict(row)).source_path
            for row in rows
        }

    output: list[PendingWatch] = []
    for watch_dir in watch_dirs():
        files: list[PendingFile] = []
        for source in _iter_files(watch_dir, recursive):
            if registry.get_extractor(source.suffix.lower()) is None:
                continue
            key = str(source.resolve())
            try:
                mtime = source.stat().st_mtime
            except OSError:
                mtime = None
            consumed_cache = mtime is not None and cache.get(key) == mtime
            consumed_page = key in known_paths
            files.append(
                {
                    "path": key,
                    "mtime": mtime,
                    "consumed": consumed_cache or consumed_page,
                    "reason": "mtime_cache" if consumed_cache else "wiki_page" if consumed_page else None,
                }
            )
        output.append({"watch_dir": watch_dir, "files": files})
    return output


def trigger_digest(path: str, *, recursive: bool = False, enrich: bool = True) -> list[DigestItem]:
    """Digest only paths inside configured roots for network-reachable callers."""
    resolved = Path(path).expanduser().resolve()
    allowed = [Path(directory).expanduser().resolve() for directory in watch_dirs()]
    if not any(resolved == root or root in resolved.parents for root in allowed):
        raise ValueError(f"{path!r} is not under a configured watch directory")
    return digest_path(str(resolved), recursive=recursive, enrich=enrich)


def _enrich_facts(content: str, source: str, node: str, db: WikiDB) -> int:
    from reins.harness import workflow
    import json

    prompt = (
        "Generate 2-3 high-quality synthetic instruction-response pairs based on this document. "
        "These pairs will be used to fine-tune local LLMs. Format the output strictly as a JSON array of objects "
        'with "instruction" and "response" keys. No markdown blocks, no preamble, just raw JSON.\n\n'
        + content[:6000]
    )
    result = workflow.run("rag extraction", prompt, node=node)
    
    if not result.ok or not result.text:
        return 0
    facts = 0
    try:
        # Strip potential markdown fences (like ```json ... ```)
        clean_text = result.text.strip()
        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]
        if clean_text.startswith("```"):
            clean_text = clean_text[3:]
        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]
            
        pairs = json.loads(clean_text.strip())
        if isinstance(pairs, list):
            for pair in pairs:
                if isinstance(pair, dict) and "instruction" in pair and "response" in pair:
                    record_json = json.dumps({"messages": [
                        {"role": "user", "content": pair["instruction"]},
                        {"role": "assistant", "content": pair["response"]}
                    ]})
                    _ = db.add_memory(f"SFT_JSON:{record_json}", category="digested/sft", source=source, owner="digest")
                    facts += 1
    except Exception:
        log_degradation(__name__)
        
    return facts


def _notify(payload: dict[str, JsonValue]) -> None:
    try:
        external_io.mqtt_publish_single(MQTT_RESULT_TOPIC, payload=json.dumps(payload))
    except Exception:
        log_degradation(__name__)


def _digest_one(
    source: Path,
    registry: ExtractorRegistry,
    db: WikiDB,
    staging: Path,
    enrich: bool,
    trail: TaskTrail | None,
) -> DigestItem:
    extractor = registry.get_extractor(source.suffix.lower())
    if extractor is None:
        return DigestItem(str(source), False, error=f"no extractor for '{source.suffix.lower()}'")
    task_id = trail.create_task("digest", str(source), extractor.NODE) if trail else None
    if trail and task_id:
        trail.set_status(task_id, "running")
    try:
        artifact = normalize_result(
            source,
            extractor,
            extractor.extract(str(source), str(staging)),
        )
        slug = slugify(str(source))
        _ = db.upsert_page(
            source.name,
            artifact.content,
            slug=slug,
            source_path=str(source),
            category=f"digested/{artifact.modality}",
            metadata_json=artifact.wiki_metadata_json(),
            owner="digest",
        )
        facts = _enrich_facts(artifact.content, str(source), artifact.node, db) if enrich else 0
        if trail and task_id:
            trail.set_status(task_id, "success")
        _notify(
            {
                "filepath": str(source),
                "status": "success",
                "slug": slug,
                "node": artifact.node,
                "modality": artifact.modality,
                "source_sha256": artifact.source_sha256,
            }
        )
        return DigestItem(str(source), True, slug, artifact.node, facts, modality=artifact.modality)
    except Exception as error:
        log_degradation(__name__)
        if trail and task_id:
            trail.set_status(task_id, "failed")
        _notify(
            {
                "filepath": str(source),
                "status": "error",
                "error": str(error),
                "modality": extractor.MODALITY,
            }
        )
        return DigestItem(
            str(source),
            False,
            node=extractor.NODE,
            error=str(error),
            modality=extractor.MODALITY,
        )


def digest_path(
    path: str,
    *,
    recursive: bool = False,
    enrich: bool = True,
    on_result: Callable[[DigestItem], None] | None = None,
    log_trail: bool = True,
    force: bool = False,
) -> list[DigestItem]:
    """Digest changed sources into the Wiki and return one outcome per file."""
    from reins.extraction import registry

    trail = TaskTrail() if log_trail else None
    cache = {} if force else _load_cache()
    results: list[DigestItem] = []
    input_is_file = Path(path).expanduser().is_file()
    with tempfile.TemporaryDirectory(prefix="reins_digest_") as temporary, WikiDB() as db:
        staging = Path(temporary)
        for source in _iter_files(path, recursive):
            key = str(source.resolve())
            try:
                mtime = source.stat().st_mtime
            except OSError:
                mtime = None
            extractor = registry.get_extractor(source.suffix.lower())
            if extractor is None and not input_is_file:
                continue
            if mtime is not None and cache.get(key) == mtime and extractor is not None:
                item = DigestItem(
                    str(source),
                    True,
                    node=extractor.NODE,
                    skipped=True,
                    modality=extractor.MODALITY,
                )
            else:
                item = _digest_one(source, registry, db, staging, enrich, trail)
            results.append(item)
            if item.ok and not item.skipped and mtime is not None:
                cache[key] = mtime
                _save_cache(cache)
            if on_result:
                on_result(item)
    return results
