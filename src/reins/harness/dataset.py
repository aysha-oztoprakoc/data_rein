"""
Training-set export from the wiki — the wiki DB stays the single knowledge
store; JSONL files produced here are derived, disposable artifacts consumed
by `reins.training`.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from reins.harness.wiki import WikiDB


@dataclass
class ExportStats:
    written: int = 0
    skipped: int = 0
    out_path: str = ""


def export_jsonl(
    out_path: str,
    *,
    categories: Optional[list[str]] = None,
    modality: Optional[str] = None,
    kind: str = "completion",
    min_chars: int = 64,
    limit: int = 0,
) -> ExportStats:
    """Export wiki pages (kind="completion") or memories (kind="memories") to
    JSONL. Never raises: unreadable rows are counted in `skipped`."""
    stats = ExportStats(out_path=out_path)
    out = Path(out_path).expanduser()
    out.parent.mkdir(parents=True, exist_ok=True)

    cats = list(categories) if categories else []
    if modality:
        cats.append(f"digested/{modality}")

    with WikiDB() as db, open(out, "w", encoding="utf-8") as f:
        if kind == "memories":
            rows = _query_memories(db, cats, limit)
        else:
            rows = _query_pages(db, cats, limit)

        for row in rows:
            try:
                if kind == "memories":
                    text = row["text"] or ""
                    if len(text) < min_chars:
                        stats.skipped += 1
                        continue
                    record = {
                        "text": text,
                        "meta": {"category": row["category"], "source": row["source"]},
                    }
                else:
                    content = row["content"] or ""
                    if len(content) < min_chars:
                        stats.skipped += 1
                        continue
                    record = {
                        "text": content,
                        "meta": {
                            "slug": row["slug"],
                            "category": row["category"],
                            "source_path": row["source_path"],
                        },
                    }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                stats.written += 1
            except Exception:
                stats.skipped += 1

    return stats


def _query_pages(db: WikiDB, categories: list[str], limit: int):
    sql = "SELECT slug, content, category, source_path FROM pages"
    params: list = []
    if categories:
        sql += " WHERE " + " OR ".join(["category LIKE ?"] * len(categories))
        params = [f"{c}%" for c in categories]
    if limit:
        sql += f" LIMIT {int(limit)}"
    return db.conn.execute(sql, params).fetchall()


def _query_memories(db: WikiDB, categories: list[str], limit: int):
    sql = "SELECT text, category, source FROM memories"
    params: list = []
    if categories:
        sql += " WHERE " + " OR ".join(["category LIKE ?"] * len(categories))
        params = [f"{c}%" for c in categories]
    if limit:
        sql += f" LIMIT {int(limit)}"
    return db.conn.execute(sql, params).fetchall()
