"""
`reins digest` — turn raw files (text / audio / video / images / archives) into
wiki knowledge, in one command.

Pipeline per file:
    pick extractor by extension (reins.extraction) -> extract on the right node
    (text/archive on amdy, OCR/Whisper/ffmpeg media on tell via SSH) -> write the
    result into the single monolith wiki DB as a `page` (full text) + optional
    `memories` (atomic facts enriched by a *local* model) -> log to the Task Trail
    -> emit a PON `data_rein/extract/result` notification (best effort).

Privacy: this is the local-first sensitive-data path. Extraction runs only on
amdy/tell and enrichment routes through local models — file contents are never
sent to a cloud provider. This is the single write path into the wiki; it replaces
the old script that wrote to the legacy Odysseus app.db.
"""

from __future__ import annotations

import json
import socket
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterator, List, Optional

from reins.harness import paths
from reins.harness.wiki import WikiDB, slugify

MQTT_RESULT_TOPIC = "data_rein/extract/result"


@dataclass
class DigestItem:
    path: str
    ok: bool
    slug: Optional[str] = None
    node: str = "amdy"
    facts: int = 0
    error: Optional[str] = None
    skipped: bool = False


def _cache_path() -> Path:
    return paths.ensure_state_dir() / "digest_mtime_cache.json"


def _load_cache() -> dict:
    try:
        return json.loads(_cache_path().read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_cache(cache: dict) -> None:
    try:
        _cache_path().write_text(json.dumps(cache), encoding="utf-8")
    except Exception:
        pass  # best-effort; a lost cache just means the next run re-digests


def _extracted_text(output_path: str) -> str:
    """Pull the <content> body out of a `.extracted.xml`, or read the file raw."""
    try:
        root = ET.parse(output_path).getroot()
        node = root.find("content")
        if node is not None and node.text:
            return node.text
    except Exception:
        pass
    try:
        return Path(output_path).read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def watch_dirs() -> list[str]:
    """Directories the pending-extraction view watches (config-driven, user-edited).
    Never raises: missing/corrupt config just yields an empty list."""
    try:
        data = json.loads(paths.digest_watch_dirs().read_text(encoding="utf-8"))
        return [str(d) for d in data] if isinstance(data, list) else []
    except Exception:
        return []


def pending_status(recursive: bool = True) -> list[dict]:
    """
    For every configured watch dir, report each file's consumed/pending state.
    A file counts as consumed if either signal matches: an mtime-cache entry
    (the `reins digest` path) or an existing wiki page with a matching
    `source_path` (the `reins wiki consolidate` path) - the two ingestion
    routes track state independently, so both are checked.
    """
    from reins.extraction import registry

    cache = _load_cache()
    with WikiDB() as db:
        known_paths = {
            row["source_path"] for row in db.conn.execute(
                "SELECT source_path FROM pages WHERE source_path IS NOT NULL"
            )
        }

    out = []
    for wd in watch_dirs():
        files = []
        for f in _iter_files(wd, recursive):
            if registry.get_extractor(f.suffix.lower()) is None:
                continue  # unsupported format - not "pending", just not consumable
            key = str(f.resolve())
            try:
                mtime = f.stat().st_mtime
            except OSError:
                mtime = None
            consumed_cache = mtime is not None and cache.get(key) == mtime
            consumed_page = key in known_paths
            files.append({
                "path": key,
                "mtime": mtime,
                "consumed": consumed_cache or consumed_page,
                "reason": "mtime_cache" if consumed_cache else ("wiki_page" if consumed_page else None),
            })
        out.append({"watch_dir": wd, "files": files})
    return out


def trigger_digest(path: str, *, recursive: bool = False, enrich: bool = True) -> List[DigestItem]:
    """Safe wrapper for network-reachable callers (e.g. the wiki site's
    'Digest now' button): only allows paths equal to or nested under one of
    the configured watch_dirs(), never an arbitrary filesystem path."""
    resolved = Path(path).expanduser().resolve()
    allowed = [Path(d).expanduser().resolve() for d in watch_dirs()]
    if not any(resolved == a or a in resolved.parents for a in allowed):
        raise ValueError(f"{path!r} is not under a configured watch directory")
    return digest_path(str(resolved), recursive=recursive, enrich=enrich)


def _iter_files(path: str, recursive: bool) -> Iterator[Path]:
    p = Path(path).expanduser()
    if p.is_file():
        yield p
        return
    if p.is_dir():
        it = p.rglob("*") if recursive else p.iterdir()
        for f in sorted(it):
            if f.is_file():
                yield f


def _enrich_facts(content: str, source: str, node: str, db: WikiDB) -> int:
    """Ask a *local* model for a few atomic facts; store them as memories."""
    from reins.harness import workflow

    excerpt = content[:6000]
    prompt = (
        "Extract 3-6 concise, standalone atomic facts from the following document. "
        "One fact per line, no numbering, no preamble.\n\n" + excerpt
    )
    res = workflow.run("rag extraction", prompt, node=node)  # local-first, never raises
    if not res.ok or not res.text:
        return 0
    facts = 0
    for line in res.text.splitlines():
        fact = line.strip().lstrip("-*0123456789. ").strip()
        if len(fact) > 12:
            db.add_memory(fact, category="digested", source=source, owner="digest")
            facts += 1
    return facts


def _notify(payload: dict) -> None:
    """Best-effort PON notification; never blocks/raises if no broker is present."""
    try:
        with socket.create_connection(("localhost", 1883), timeout=0.3):
            pass
    except Exception:
        return
    try:
        import json
        import paho.mqtt.publish as publish
        publish.single(MQTT_RESULT_TOPIC, payload=json.dumps(payload), hostname="localhost", port=1883)
    except Exception:
        pass


def _digest_one(f: Path, registry, db: WikiDB, staging: Path, enrich: bool, trail) -> DigestItem:
    ext = f.suffix.lower()
    extractor = registry.get_extractor(ext)
    if extractor is None:
        return DigestItem(str(f), False, error=f"no extractor for '{ext}'")

    node = getattr(extractor, "NODE", "amdy")
    task_id = None
    if trail is not None:
        task_id = trail.create_task("digest", str(f), node)
        trail.set_status(task_id, "running")
    try:
        res = extractor.extract(str(f), str(staging))
        if res.get("status") != "success":
            raise RuntimeError(res.get("error", "extraction failed"))
        content = _extracted_text(res.get("output_path", ""))
        if not content.strip():
            raise RuntimeError("empty extraction")

        slug = slugify(str(f))
        db.upsert_page(f.name, content, slug=slug, source_path=str(f),
                       category="digested", owner="digest")
        facts = _enrich_facts(content, str(f), node, db) if enrich else 0

        if trail is not None and task_id:
            trail.set_status(task_id, "success")
        _notify({"filepath": str(f), "status": "success", "slug": slug, "node": node})
        return DigestItem(str(f), True, slug=slug, node=node, facts=facts)
    except Exception as e:  # graceful degradation: one bad file never aborts the batch
        if trail is not None and task_id:
            trail.set_status(task_id, "failed")
        _notify({"filepath": str(f), "status": "error", "error": str(e)})
        return DigestItem(str(f), False, node=node, error=str(e))


def digest_path(
    path: str,
    *,
    recursive: bool = False,
    enrich: bool = True,
    on_result: Optional[Callable[[DigestItem], None]] = None,
    log_trail: bool = True,
    force: bool = False,
) -> List[DigestItem]:
    """
    Digest a file or directory into the wiki. Returns one DigestItem per file.

    A file already digested at its current mtime is skipped (unless
    ``force=True``), so re-running over a large batch only re-processes what
    actually changed - makes repeated large-batch ingestion cheap instead of
    re-extracting everything every time.
    """
    from reins.extraction import registry  # import triggers extractor auto-registration

    trail = None
    if log_trail:
        try:
            from reins.services.task_trail import TaskTrail
            trail = TaskTrail()
        except Exception:
            trail = None

    cache = {} if force else _load_cache()
    staging = Path(tempfile.mkdtemp(prefix="reins_digest_"))
    results: List[DigestItem] = []
    with WikiDB() as db:
        for f in _iter_files(path, recursive):
            key = str(f.resolve())
            try:
                mtime = f.stat().st_mtime
            except OSError:
                mtime = None
            if mtime is not None and cache.get(key) == mtime:
                item = DigestItem(str(f), True, skipped=True)
                results.append(item)
                if on_result:
                    on_result(item)
                continue

            item = _digest_one(f, registry, db, staging, enrich, trail)
            results.append(item)
            if item.ok and mtime is not None:
                cache[key] = mtime
                _save_cache(cache)  # per-file, so an interrupted batch resumes cleanly
            if on_result:
                on_result(item)
    return results
