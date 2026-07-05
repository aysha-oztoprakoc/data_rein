#!/usr/bin/env python3
"""
Consolidate every knowledge source in the harness into the single monolith Wiki DB.

This is the migration that fulfils the "one shared monolith wiki database" mandate.
It ingests, idempotently, from all of the previously scattered stores:

  1. knowledge_base/**            -> pages   (markdown / xml / txt)
  2. data-oby/** (Obsidian vault) -> pages   (markdown notes)
  3. every Odysseus app.db found  -> memories (the 'memories' table, merged/deduped)

It is PON-compliant: it runs on demand, does its work, and exits. Re-running is
safe - pages are keyed by slug and memories by content hash, so nothing is
duplicated. XML "knowledge_document" wrappers are unwrapped to their <content>.

Usage:
    python scripts/consolidate_wiki.py [--dry-run] [--quiet]
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

# Allow running straight from the repo without installation.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from reins.harness import paths  # noqa: E402
from reins.harness.wiki import WikiDB, slugify  # noqa: E402
from reins.services.task_trail import TaskTrail  # noqa: E402

PAGE_EXTS = {".md", ".xml", ".txt"}
SKIP_DIRS = {".git", ".obsidian", "node_modules", "__pycache__", ".venv"}


def _category_from(root: Path, path: Path) -> str:
    try:
        rel = path.relative_to(root)
    except ValueError:
        return "general"
    parts = rel.parts
    return parts[0] if len(parts) > 1 else "general"


def _read_content(path: Path) -> tuple[str, str]:
    """Return (title, content). XML knowledge_documents are unwrapped."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix == ".xml":
        try:
            root = ET.fromstring(raw)
            content_el = root.find(".//content")
            title_el = root.find(".//title")
            title = (title_el.text or "").strip() if title_el is not None else path.stem
            if content_el is not None and content_el.text:
                return (title or path.stem, content_el.text.strip())
        except ET.ParseError:
            pass
    return (path.stem, raw)


def ingest_tree(db: WikiDB, root: Path, owner: str, dry: bool) -> int:
    if not root.exists():
        return 0
    n = 0
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in PAGE_EXTS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        title, content = _read_content(path)
        if not content.strip():
            continue
        rel = str(path.relative_to(paths.home())) if str(path).startswith(str(paths.home())) else str(path)
        if not dry:
            db.upsert_page(
                title=title,
                content=content,
                slug=slugify(rel),
                source_path=rel,
                category=_category_from(root, path),
                fmt=path.suffix.lstrip("."),
                owner=owner,
            )
        n += 1
    return n


def ingest_memories(db: WikiDB, app_db: Path, dry: bool) -> int:
    if not app_db.exists():
        return 0
    try:
        src = sqlite3.connect(f"file:{app_db}?mode=ro", uri=True)
        src.row_factory = sqlite3.Row
    except sqlite3.OperationalError:
        return 0
    n = 0
    try:
        tables = {r[0] for r in src.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if "memories" not in tables:
            return 0
        cols = {r[1] for r in src.execute("PRAGMA table_info(memories)")}
        for row in src.execute("SELECT * FROM memories"):
            text = row["text"] if "text" in cols else None
            if not text or not str(text).strip():
                continue
            if not dry:
                db.add_memory(
                    str(text),
                    category=(row["category"] if "category" in cols else "general") or "general",
                    source=(row["source"] if "source" in cols else str(app_db)),
                    owner=(row["owner"] if "owner" in cols else "odysseus") or "odysseus",
                    session_id=(row["session_id"] if "session_id" in cols else None),
                )
            n += 1
    finally:
        src.close()
    return n


def find_app_dbs(home: Path) -> list[Path]:
    return sorted({p.resolve() for p in home.rglob("app.db") if ".git" not in p.parts})


def ingest_trail(db: WikiDB, dry: bool) -> int:
    """
    Materialize completed Task Trail activity into per-agent, per-day wiki
    pages (category="changelog") - documentation of what every agent actually
    did, not just what pages/notes it authored. Idempotent: one page per
    (owner, date), re-generated in full each run, keyed by slug so re-running
    replaces rather than duplicates.
    """
    trail = TaskTrail()
    tasks = [t for t in trail.all_tasks() if t.get("status") not in (None, "pending")]
    by_bucket: dict[tuple[str, str], list[dict]] = {}
    for t in tasks:
        task_type = str(t.get("task_type", "generic"))
        owner = task_type.split(":", 1)[0]
        ts = t.get("timestamp")
        try:
            date = datetime.fromtimestamp(float(ts), tz=timezone.utc).strftime("%Y-%m-%d")
        except (TypeError, ValueError):
            date = "unknown-date"
        by_bucket.setdefault((owner, date), []).append(t)

    n = 0
    for (owner, date), bucket in sorted(by_bucket.items()):
        lines = [f"# Changelog — {owner} — {date}", ""]
        for t in sorted(bucket, key=lambda t: t.get("timestamp", 0)):
            prompt_snip = str(t.get("prompt", ""))[:120].replace("\n", " ")
            lines.append(
                f"- `{t.get('status')}` **{t.get('task_type')}** "
                f"(node={t.get('target_node')}, attempts={t.get('attempts', 0)}): {prompt_snip}"
            )
        content = "\n".join(lines)
        if not dry:
            db.upsert_page(
                title=f"Changelog: {owner} ({date})",
                content=content,
                slug=slugify(f"changelog-{owner}-{date}"),
                source_path=f"task_trail:{owner}:{date}",
                category="changelog",
                fmt="md",
                owner=owner,
            )
        n += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description="Consolidate all knowledge into the monolith Wiki DB")
    ap.add_argument("--dry-run", action="store_true", help="report counts without writing")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    home = paths.home()

    def log(msg: str) -> None:
        if not args.quiet:
            print(msg)

    log(f"// data_rein wiki consolidation  [home={home}]")
    log(f"// target monolith DB -> {paths.wiki_db()}")
    if args.dry_run:
        log("// DRY RUN - no writes")

    db = WikiDB()
    try:
        kb = ingest_tree(db, paths.knowledge_base(), owner="knowledge_base", dry=args.dry_run)
        log(f"  [pages] knowledge_base    : {kb}")

        oby = ingest_tree(db, paths.obsidian_vault(), owner="oby-vault", dry=args.dry_run)
        log(f"  [pages] data-oby vault    : {oby}")

        skills = ingest_tree(db, paths.home() / "skills", owner="skills", dry=args.dry_run)
        log(f"  [pages] harness skills    : {skills}")

        mem_total = 0
        for app_db in find_app_dbs(home):
            c = ingest_memories(db, app_db, dry=args.dry_run)
            if c:
                log(f"  [mem]   {app_db.relative_to(home) if str(app_db).startswith(str(home)) else app_db} : {c}")
            mem_total += c

        changelog = ingest_trail(db, dry=args.dry_run)
        log(f"  [pages] task trail changelog : {changelog}")

        stats = db.stats()
        log("// ------------------------------------------------------------")
        log(f"// ingested this run: pages(kb+oby)={kb + oby}  memories={mem_total}")
        log(f"// monolith now holds: pages={stats['pages']}  memories={stats['memories']}")
        log(f"// categories: {db.categories()}")
        log("// [OK] harness knowledge unified.")
    finally:
        db.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
