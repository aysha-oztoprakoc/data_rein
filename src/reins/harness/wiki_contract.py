from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from typing import Any

from reins.harness.wiki import WikiDB, slugify
from reins.harness.trust_anchor import KnowledgeValidator

_validator = KnowledgeValidator()


class WikiContractError(ValueError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


@dataclass(frozen=True, slots=True)
class WikiCrud:
    db: WikiDB

    def list_pages(self, *, limit: int = 50, offset: int = 0) -> dict[str, Any]:
        limit, offset = self._page(limit, offset)
        if hasattr(self.db, "list_pages_summary"):
            items = self.db.list_pages_summary(limit=limit, offset=offset)
        elif hasattr(self.db, "conn"):
            rows = self.db.conn.execute(
                "SELECT slug,title,category,fmt,owner,updated_at FROM pages "
                "ORDER BY updated_at DESC LIMIT ? OFFSET ?",
                (limit, offset),
            ).fetchall()
            items = [dict(row) for row in rows]
        else:
            pages = self.db.list_pages(limit=limit, offset=offset, order="recent")
            items = [
                {
                    "slug": p.get("slug") if isinstance(p, dict) else p["slug"],
                    "title": p.get("title") if isinstance(p, dict) else p["title"],
                    "category": p.get("category", "general") if isinstance(p, dict) else p["category"],
                    "fmt": p.get("fmt", "md") if isinstance(p, dict) else p["fmt"],
                    "owner": p.get("owner", "harness") if isinstance(p, dict) else p["owner"],
                    "updated_at": p.get("updated_at", 0.0) if isinstance(p, dict) else p["updated_at"],
                }
                for p in pages
            ]
        total = self.db.count_pages() if hasattr(self.db, "count_pages") else int(self.db.conn.execute("SELECT COUNT(*) FROM pages").fetchone()[0])
        return {"items": items, "total": total, "limit": limit, "offset": offset}

    def get_page(self, slug: str) -> dict[str, Any]:
        row = self.db.get_page(self._text(slug, "slug", 200))
        if row is None:
            raise WikiContractError("not_found", "Page not found")
        return dict(row) if not isinstance(row, dict) else row

    def create_page(
        self,
        *,
        title: str,
        content: str,
        slug: str = "",
        category: str = "general",
        fmt: str = "md",
        metadata_json: str = "{}",
    ) -> dict[str, str]:
        title = self._text(title, "title", 500)
        page_slug = self._text(slug, "slug", 200) if slug else slugify(title)
        if self.db.get_page(page_slug) is not None:
            raise WikiContractError("conflict", "Page already exists")
        return {"slug": self._write_page(page_slug, title, content, category, fmt, metadata_json)}

    def update_page(
        self,
        slug: str,
        *,
        title: str,
        content: str,
        category: str = "general",
        fmt: str = "md",
        metadata_json: str = "{}",
    ) -> dict[str, str]:
        page_slug = self._text(slug, "slug", 200)
        if self.db.get_page(page_slug) is None:
            raise WikiContractError("not_found", "Page not found")
        return {"slug": self._write_page(page_slug, title, content, category, fmt, metadata_json)}

    def delete_page(self, slug: str) -> dict[str, bool]:
        page_slug = self._text(slug, "slug", 200)
        if hasattr(self.db, "delete_page"):
            ok = self.db.delete_page(page_slug)
        else:
            with self.db._tx() as connection:
                cursor = connection.execute("DELETE FROM pages WHERE slug = ?", (page_slug,))
                ok = cursor.rowcount > 0
        if not ok:
            raise WikiContractError("not_found", "Page not found")
        return {"ok": True}

    def list_memories(self, *, limit: int = 50, offset: int = 0) -> dict[str, Any]:
        limit, offset = self._page(limit, offset)
        if hasattr(self.db, "list_memories"):
            rows = self.db.list_memories(limit=limit, offset=offset)
            items = [
                {
                    "uid": row["uid"] if isinstance(row, dict) else row[0],
                    "category": row["category"] if isinstance(row, dict) else row[1],
                    "source": row["source"] if isinstance(row, dict) else row[2],
                    "owner": row["owner"] if isinstance(row, dict) else row[3],
                    "timestamp": row["timestamp"] if isinstance(row, dict) else row[4],
                    "preview": row.get("preview", (row.get("text") or "")[:200]) if isinstance(row, dict) else (row[5] if len(row) > 5 else "")[:200],
                }
                for row in rows
            ]
        else:
            rows = self.db.conn.execute(
                "SELECT uid,category,source,owner,timestamp,substr(text,1,200) AS preview "
                "FROM memories ORDER BY timestamp DESC LIMIT ? OFFSET ?",
                (limit, offset),
            ).fetchall()
            items = [dict(row) for row in rows]
        total = self.db.count_memories() if hasattr(self.db, "count_memories") else int(self.db.conn.execute("SELECT COUNT(*) FROM memories").fetchone()[0])
        return {"items": items, "total": total, "limit": limit, "offset": offset}

    def get_memory(self, uid: str) -> dict[str, Any]:
        memory_uid = self._text(uid, "uid", 128)
        if hasattr(self.db, "get_memory"):
            row = self.db.get_memory(memory_uid)
        else:
            row = self.db.conn.execute(
                "SELECT * FROM memories WHERE uid = ?",
                (memory_uid,),
            ).fetchone()
        if row is None:
            raise WikiContractError("not_found", "Memory not found")
        return dict(row) if not isinstance(row, dict) else row

    def create_memory(self, *, text: str, category: str = "general") -> dict[str, str]:
        memory_text = self._text(text, "text", 2 * 1024 * 1024)
        memory_category = self._text(category, "category", 200)
        trust_score = _validator.validate_update(memory_text, "harness")
        uid = self.db.add_memory(memory_text, category=memory_category, source="odysseus", owner="harness", trust_score=trust_score)
        return {"uid": uid}

    def revise_memory(self, uid: str, *, text: str, category: str = "general") -> dict[str, Any]:
        old = self.get_memory(uid)
        replacement = self.create_memory(text=text, category=category)
        return {"old_uid": old["uid"], "new_uid": replacement["uid"], "old_retained": True}

    def delete_memory(self, uid: str) -> dict[str, bool]:
        memory_uid = self._text(uid, "uid", 128)
        if hasattr(self.db, "delete_memory"):
            ok = self.db.delete_memory(memory_uid)
        else:
            with self.db._tx() as connection:
                cursor = connection.execute("DELETE FROM memories WHERE uid = ?", (memory_uid,))
                ok = cursor.rowcount > 0
        if not ok:
            raise WikiContractError("not_found", "Memory not found")
        return {"ok": True}

    def _write_page(
        self,
        slug: str,
        title: str,
        content: str,
        category: str,
        fmt: str,
        metadata_json: str,
    ) -> str:
        trust_score = _validator.validate_update(content, "harness")
        return self.db.upsert_page(
            title=self._text(title, "title", 500),
            content=self._text(content, "content", 2 * 1024 * 1024, allow_empty=True),
            slug=slug,
            category=self._text(category, "category", 200),
            fmt=self._text(fmt, "fmt", 32),
            metadata_json=self._text(metadata_json, "metadata_json", 64 * 1024),
            owner="harness",
            trust_score=trust_score,
        )

    @staticmethod
    def _page(limit: int, offset: int) -> tuple[int, int]:
        if not 1 <= limit <= 200 or not 0 <= offset <= 1_000_000:
            raise WikiContractError("invalid", "Pagination is out of bounds")
        return limit, offset

    @staticmethod
    def _text(value: str, field: str, maximum: int, *, allow_empty: bool = False) -> str:
        if not isinstance(value, str) or len(value) > maximum or (not allow_empty and not value.strip()):
            raise WikiContractError("invalid", f"Invalid {field}")
        return value


def contract_result(action) -> str:
    import json

    try:
        return json.dumps(action())
    except WikiContractError as error:
        return json.dumps({"error": str(error), "code": error.code})
    except sqlite3.Error:
        return json.dumps({"error": "Wiki database operation failed", "code": "database"})
