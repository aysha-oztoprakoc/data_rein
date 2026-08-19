"""
The single shared monolith Wiki database for the data_rein universal harness.

Every environment under the harness - Antigravity, Hermes, Odysseus, Claude Code,
and the VS Code workspace - reads and writes knowledge through this one SQLite
file (see :func:`reins.harness.paths.wiki_db`). It replaces the previously
scattered stores: the two Odysseus ``app.db`` ``memories`` tables, the loose
``knowledge_base/**`` markdown/XML files, and the ``data-oby`` Obsidian notes.

Design goals:
* **Model / environment agnostic** - plain ``sqlite3`` from the stdlib, no ORM,
  no server. Any language on either node can open the same file or shell out to
  ``reins wiki`` for access.
* **Full-text search** - FTS5 virtual tables kept in sync via triggers.
* **Idempotent ingestion** - pages are keyed by a stable ``slug`` and memories
  by a content hash ``uid`` so re-running consolidation never duplicates.
* **PON-compliant** - a passive library: it does no polling and holds no
  background threads; callers open it on-event and close it.

Two logical stores live in one file:

``pages``     - documents/wiki entries (the knowledge base + oby vault content).
``memories``  - atomic facts/insights (the "Ody Memory Vault").
"""

from __future__ import annotations

import hashlib
import re
import sqlite3
import time
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Optional

from reins.harness import paths

SCHEMA_VERSION = 3

_SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT
);

CREATE TABLE IF NOT EXISTS pages (
    id          INTEGER PRIMARY KEY,
    slug        TEXT UNIQUE NOT NULL,
    title       TEXT NOT NULL,
    source_path TEXT,
    category    TEXT DEFAULT 'general',
    fmt         TEXT DEFAULT 'md',
    content     TEXT NOT NULL,
    metadata_json TEXT NOT NULL DEFAULT '{}',
    owner       TEXT DEFAULT 'harness',
    trust_score REAL DEFAULT 1.0,
    is_chunked  INTEGER DEFAULT 0,
    updated_at  REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS memories (
    id         INTEGER PRIMARY KEY,
    uid        TEXT UNIQUE NOT NULL,
    text       TEXT NOT NULL,
    category   TEXT DEFAULT 'general',
    source     TEXT,
    owner      TEXT DEFAULT 'harness',
    session_id TEXT,
    trust_score REAL DEFAULT 1.0,
    is_chunked INTEGER DEFAULT 0,
    timestamp  REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS audit_log (
    id          INTEGER PRIMARY KEY,
    entity_type TEXT NOT NULL,
    entity_id   TEXT NOT NULL,
    action      TEXT NOT NULL,
    previous_hash TEXT,
    new_hash    TEXT,
    owner       TEXT,
    timestamp   REAL NOT NULL
);

CREATE VIRTUAL TABLE IF NOT EXISTS pages_fts USING fts5(
    title, content, category,
    content='pages', content_rowid='id'
);
CREATE VIRTUAL TABLE IF NOT EXISTS memories_fts USING fts5(
    text, category,
    content='memories', content_rowid='id'
);

CREATE TRIGGER IF NOT EXISTS pages_ai AFTER INSERT ON pages BEGIN
    INSERT INTO pages_fts(rowid, title, content, category)
    VALUES (new.id, new.title, new.content, new.category);
END;
CREATE TRIGGER IF NOT EXISTS pages_ad AFTER DELETE ON pages BEGIN
    INSERT INTO pages_fts(pages_fts, rowid, title, content, category)
    VALUES ('delete', old.id, old.title, old.content, old.category);
END;
CREATE TRIGGER IF NOT EXISTS pages_au AFTER UPDATE ON pages BEGIN
    INSERT INTO pages_fts(pages_fts, rowid, title, content, category)
    VALUES ('delete', old.id, old.title, old.content, old.category);
    INSERT INTO pages_fts(rowid, title, content, category)
    VALUES (new.id, new.title, new.content, new.category);
END;

CREATE TRIGGER IF NOT EXISTS memories_ai AFTER INSERT ON memories BEGIN
    INSERT INTO memories_fts(rowid, text, category)
    VALUES (new.id, new.text, new.category);
END;
CREATE TRIGGER IF NOT EXISTS memories_ad AFTER DELETE ON memories BEGIN
    INSERT INTO memories_fts(memories_fts, rowid, text, category)
    VALUES ('delete', old.id, old.text, old.category);
END;
CREATE TRIGGER IF NOT EXISTS memories_au AFTER UPDATE ON memories BEGIN
    INSERT INTO memories_fts(memories_fts, rowid, text, category)
    VALUES ('delete', old.id, old.text, old.category);
    INSERT INTO memories_fts(rowid, text, category)
    VALUES (new.id, new.text, new.category);
END;
"""


def slugify(value: str) -> str:
    """Stable slug from a title or path fragment."""
    keep = "".join(c.lower() if c.isalnum() else "-" for c in value)
    while "--" in keep:
        keep = keep.replace("--", "-")
    return keep.strip("-")[:200] or "untitled"


def _hash(*parts: str) -> str:
    h = hashlib.sha256()
    for p in parts:
        h.update((p or "").encode("utf-8", "replace"))
        h.update(b"\x00")
    return h.hexdigest()


def _literal_fts_query(query: str) -> str | None:
    terms = re.findall(r"[^\W_]+", query, flags=re.UNICODE)
    return " AND ".join(f'"{term}"' for term in terms) or None


@dataclass
class Page:
    slug: str
    title: str
    content: str
    metadata_json: str = "{}"
    source_path: Optional[str] = None
    category: str = "general"
    fmt: str = "md"
    owner: str = "harness"
    trust_score: float = 1.0
    is_chunked: bool = False
    updated_at: float = 0.0


@dataclass
class Memory:
    uid: str
    text: str
    category: str = "general"
    source: Optional[str] = None
    owner: str = "harness"
    session_id: Optional[str] = None
    trust_score: float = 1.0
    is_chunked: bool = False
    timestamp: float = 0.0


from reins.harness.kuzu_wiki import KuzuWikiDB


class SQLiteWikiDB:
    """Legacy SQLite accessor for the monolith Wiki database."""

    def __init__(self, path: Optional[Path | str] = None) -> None:
        self.path = Path(path) if path else paths.wiki_db()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.path))
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL;")
        self.conn.execute("PRAGMA synchronous=NORMAL;")
        self._migrate()

    def _migrate(self) -> None:
        self.conn.executescript(_SCHEMA)
        columns = {row[1] for row in self.conn.execute("PRAGMA table_info(pages)")}
        if "metadata_json" not in columns:
            self.conn.execute(
                "ALTER TABLE pages ADD COLUMN metadata_json TEXT NOT NULL DEFAULT '{}'"
            )
        if "trust_score" not in columns:
            self.conn.execute("ALTER TABLE pages ADD COLUMN trust_score REAL DEFAULT 1.0")
        if "is_chunked" not in columns:
            self.conn.execute("ALTER TABLE pages ADD COLUMN is_chunked INTEGER DEFAULT 0")
            
        mem_columns = {row[1] for row in self.conn.execute("PRAGMA table_info(memories)")}
        if "trust_score" not in mem_columns:
            self.conn.execute("ALTER TABLE memories ADD COLUMN trust_score REAL DEFAULT 1.0")
        if "is_chunked" not in mem_columns:
            self.conn.execute("ALTER TABLE memories ADD COLUMN is_chunked INTEGER DEFAULT 0")
        if "is_deleted" not in columns:
            self.conn.execute("ALTER TABLE pages ADD COLUMN is_deleted INTEGER DEFAULT 0")
        if "is_deleted" not in mem_columns:
            self.conn.execute("ALTER TABLE memories ADD COLUMN is_deleted INTEGER DEFAULT 0")
            
        self.conn.execute("CREATE INDEX IF NOT EXISTS ix_pages_category ON pages(category);")
        self.conn.execute("CREATE INDEX IF NOT EXISTS ix_pages_is_chunked ON pages(is_chunked);")
        self.conn.execute("CREATE INDEX IF NOT EXISTS ix_pages_is_deleted ON pages(is_deleted);")
        self.conn.execute("CREATE INDEX IF NOT EXISTS ix_memories_category ON memories(category);")
        self.conn.execute("CREATE INDEX IF NOT EXISTS ix_memories_is_chunked ON memories(is_chunked);")
        self.conn.execute("CREATE INDEX IF NOT EXISTS ix_memories_is_deleted ON memories(is_deleted);")

        self.conn.execute(
            "INSERT INTO meta(key, value) VALUES('schema_version', ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (str(SCHEMA_VERSION),),
        )
        self.conn.commit()

    # -- context management -------------------------------------------------
    def __enter__(self) -> "WikiDB":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def close(self) -> None:
        try:
            self.conn.commit()
        finally:
            self.conn.close()

    @contextmanager
    def _tx(self) -> Iterator[sqlite3.Connection]:
        try:
            yield self.conn
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

    # -- pages --------------------------------------------------------------
    def upsert_page(
        self,
        title: str,
        content: str,
        *,
        slug: Optional[str] = None,
        source_path: Optional[str] = None,
        category: str = "general",
        fmt: str = "md",
        metadata_json: str = "{}",
        owner: str = "harness",
        trust_score: float = 1.0,
        is_chunked: bool = False,
    ) -> str:
        """Insert or update a page keyed by slug. Returns the slug used."""
        slug = slug or slugify(source_path or title)
        new_hash = _hash(title, content, category, fmt, metadata_json, owner)
        with self._tx() as conn:
            cur = conn.execute("SELECT content FROM pages WHERE slug = ?", (slug,))
            row = cur.fetchone()
            previous_hash = _hash(row["content"]) if row else None
            action = "update" if row else "insert"

            conn.execute(
                """
                INSERT INTO pages(
                    slug, title, source_path, category, fmt, content,
                    metadata_json, owner, trust_score, is_chunked, updated_at
                )
                VALUES(?,?,?,?,?,?,?,?,?,?,?)
                ON CONFLICT(slug) DO UPDATE SET
                    title=excluded.title,
                    source_path=excluded.source_path,
                    category=excluded.category,
                    fmt=excluded.fmt,
                    content=excluded.content,
                    metadata_json=excluded.metadata_json,
                    owner=excluded.owner,
                    trust_score=excluded.trust_score,
                    is_chunked=excluded.is_chunked,
                    updated_at=excluded.updated_at
                """,
                (
                    slug,
                    title,
                    source_path,
                    category,
                    fmt,
                    content,
                    metadata_json,
                    owner,
                    trust_score,
                    1 if is_chunked else 0,
                    time.time(),
                ),
            )
            
            conn.execute(
                """
                INSERT INTO audit_log(entity_type, entity_id, action, previous_hash, new_hash, owner, timestamp)
                VALUES(?,?,?,?,?,?,?)
                """,
                ("page", slug, action, previous_hash, new_hash, owner, time.time())
            )
        return slug

    def get_page(self, slug: str) -> Optional[sqlite3.Row]:
        cur = self.conn.execute("SELECT * FROM pages WHERE slug = ?", (slug,))
        return cur.fetchone()

    def list_pages(
        self,
        *,
        category: Optional[str] = None,
        owner: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
        order: str = "recent",
    ) -> list[sqlite3.Row]:
        """Browse pages (not full-text search) with optional category/owner
        filters, paginated. `order`: "recent" (updated_at DESC, default) or
        "title" (title ASC)."""
        where, params = [], []
        if category:
            where.append("category = ?")
            params.append(category)
        if owner:
            where.append("owner = ?")
            params.append(owner)
        clause = f"WHERE {' AND '.join(where)}" if where else ""
        order_sql = "title ASC" if order == "title" else "updated_at DESC"
        # Both SQL fragments are selected from fixed literals above; values remain parameters.
        cur = self.conn.execute(
            f"SELECT * FROM pages {clause} ORDER BY {order_sql} LIMIT ? OFFSET ?",  # nosec B608
            (*params, limit, offset),
        )
        return cur.fetchall()

    def get_unchunked_pages(self, limit: int = 100) -> list[sqlite3.Row]:
        """Return pages where is_chunked = 0."""
        cur = self.conn.execute(
            "SELECT * FROM pages WHERE is_chunked = 0 AND is_deleted = 0 ORDER BY updated_at ASC LIMIT ?",
            (limit,),
        )
        return cur.fetchall()

    def soft_delete_page(self, slug: str, owner: str = "harness") -> bool:
        """Soft delete a page by setting is_deleted=1."""
        with self._tx() as conn:
            row = conn.execute("SELECT * FROM pages WHERE slug = ?", (slug,)).fetchone()
            if not row or row["is_deleted"] == 1:
                return False
                
            previous_hash = _hash(row["content"])
            cur = conn.execute("UPDATE pages SET is_deleted = 1, updated_at = ? WHERE slug = ?", (time.time(), slug,))
            if cur.rowcount > 0:
                conn.execute(
                    """
                    INSERT INTO audit_log(entity_type, entity_id, action, previous_hash, new_hash, owner, timestamp)
                    VALUES(?,?,?,?,?,?,?)
                    """,
                    ("page", slug, "soft_delete", previous_hash, None, owner, time.time())
                )
                return True
            return False

    def mark_pages_chunked(self, slugs: list[str]) -> int:
        """Mark a list of pages as chunked."""
        if not slugs:
            return 0
        with self._tx() as conn:
            placeholders = ",".join("?" for _ in slugs)
            cur = conn.execute(
                f"UPDATE pages SET is_chunked = 1 WHERE slug IN ({placeholders})",  # nosec B608
                slugs,
            )
            return cur.rowcount

    def count_pages(self, *, category: Optional[str] = None, owner: Optional[str] = None) -> int:
        where, params = [], []
        if category:
            where.append("category = ?")
            params.append(category)
        if owner:
            where.append("owner = ?")
            params.append(owner)
        clause = f"WHERE {' AND '.join(where)}" if where else ""
        # The clause contains only the fixed column predicates assembled above.
        return int(self.conn.execute(f"SELECT COUNT(*) FROM pages {clause}", params).fetchone()[0])  # nosec B608

    def search_pages(self, query: str, limit: int = 10) -> list[sqlite3.Row]:
        fts_query = _literal_fts_query(query)
        if fts_query is None:
            return []
        cur = self.conn.execute(
            """
            SELECT p.slug, p.title, p.category, p.source_path, p.trust_score,
                   snippet(pages_fts, 1, '[', ']', ' ... ', 12) AS snippet,
                   bm25(pages_fts) AS rank
            FROM pages_fts
            JOIN pages p ON p.id = pages_fts.rowid
            WHERE pages_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (fts_query, limit),
        )
        return cur.fetchall()

    # -- memories -----------------------------------------------------------
    def add_memory(
        self,
        text: str,
        *,
        category: str = "general",
        source: Optional[str] = None,
        owner: str = "harness",
        session_id: Optional[str] = None,
        uid: Optional[str] = None,
        trust_score: float = 1.0,
        is_chunked: bool = False,
    ) -> str:
        """Insert a memory (deduped by content hash). Returns the uid used."""
        uid = uid or _hash(text, category, source or "")
        new_hash = _hash(text, category, str(source), owner)
        with self._tx() as conn:
            cur = conn.execute("SELECT text FROM memories WHERE uid = ?", (uid,))
            row = cur.fetchone()
            previous_hash = _hash(row["text"]) if row else None
            action = "update" if row else "insert"

            conn.execute(
                """
                INSERT INTO memories(uid, text, category, source, owner, session_id, trust_score, is_chunked, timestamp)
                VALUES(?,?,?,?,?,?,?,?,?)
                ON CONFLICT(uid) DO UPDATE SET
                    text=excluded.text,
                    category=excluded.category,
                    source=excluded.source,
                    trust_score=excluded.trust_score,
                    is_chunked=excluded.is_chunked
                """,
                (uid, text, category, source, owner, session_id, trust_score, 1 if is_chunked else 0, time.time()),
            )
            
            conn.execute(
                """
                INSERT INTO audit_log(entity_type, entity_id, action, previous_hash, new_hash, owner, timestamp)
                VALUES(?,?,?,?,?,?,?)
                """,
                ("memory", uid, action, previous_hash, new_hash, owner, time.time())
            )
        return uid

    def get_unchunked_memories(self, limit: int = 100) -> list[sqlite3.Row]:
        """Return memories where is_chunked = 0."""
        cur = self.conn.execute(
            "SELECT * FROM memories WHERE is_chunked = 0 AND is_deleted = 0 ORDER BY timestamp ASC LIMIT ?",
            (limit,),
        )
        return cur.fetchall()

    def delete_page(self, slug: str) -> bool:
        """Delete a page by slug."""
        with self._tx() as conn:
            cur = conn.execute("DELETE FROM pages WHERE slug = ?", (slug,))
            return cur.rowcount > 0

    def soft_delete_memory(self, uid: str, owner: str = "harness") -> bool:
        """Soft delete a memory by setting is_deleted=1."""
        with self._tx() as conn:
            row = conn.execute("SELECT * FROM memories WHERE uid = ?", (uid,)).fetchone()
            if not row or row["is_deleted"] == 1:
                return False
                
            previous_hash = _hash(row["text"])
            cur = conn.execute("UPDATE memories SET is_deleted = 1, timestamp = ? WHERE uid = ?", (time.time(), uid,))
            if cur.rowcount > 0:
                conn.execute(
                    """
                    INSERT INTO audit_log(entity_type, entity_id, action, previous_hash, new_hash, owner, timestamp)
                    VALUES(?,?,?,?,?,?,?)
                    """,
                    ("memory", uid, "soft_delete", previous_hash, None, owner, time.time())
                )
                return True
            return False

    def get_memory(self, uid: str) -> Optional[sqlite3.Row]:
        """Fetch a single memory by uid."""
        cur = self.conn.execute("SELECT * FROM memories WHERE uid = ?", (uid,))
        return cur.fetchone()

    def delete_memory(self, uid: str) -> bool:
        """Delete a memory by uid."""
        with self._tx() as conn:
            cur = conn.execute("DELETE FROM memories WHERE uid = ?", (uid,))
            return cur.rowcount > 0

    def list_memories(
        self,
        *,
        category: Optional[str] = None,
        owner: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> list[sqlite3.Row]:
        """List memories with preview."""
        where, params = [], []
        if category:
            where.append("category = ?")
            params.append(category)
        if owner:
            where.append("owner = ?")
            params.append(owner)
        clause = f"WHERE {' AND '.join(where)}" if where else ""
        cur = self.conn.execute(
            f"SELECT uid,category,source,owner,timestamp,substr(text,1,200) AS preview "
            f"FROM memories {clause} ORDER BY timestamp DESC LIMIT ? OFFSET ?",
            (*params, limit, offset),
        )
        return cur.fetchall()

    def count_memories(self, *, category: Optional[str] = None, owner: Optional[str] = None) -> int:
        """Count memories with optional filters."""
        where, params = [], []
        if category:
            where.append("category = ?")
            params.append(category)
        if owner:
            where.append("owner = ?")
            params.append(owner)
        clause = f"WHERE {' AND '.join(where)}" if where else ""
        return int(self.conn.execute(f"SELECT COUNT(*) FROM memories {clause}", params).fetchone()[0])

    def mark_memories_chunked(self, uids: list[str]) -> int:
        """Mark a list of memories as chunked."""
        if not uids:
            return 0
        with self._tx() as conn:
            placeholders = ",".join("?" for _ in uids)
            cur = conn.execute(
                f"UPDATE memories SET is_chunked = 1 WHERE uid IN ({placeholders})",  # nosec B608
                uids,
            )
            return cur.rowcount

    def search_memories(self, query: str, limit: int = 10) -> list[sqlite3.Row]:
        fts_query = _literal_fts_query(query)
        if fts_query is None:
            return []
        cur = self.conn.execute(
            """
            SELECT m.uid, m.category, m.source, m.trust_score,
                   snippet(memories_fts, 0, '[', ']', ' ... ', 16) AS snippet,
                   bm25(memories_fts) AS rank
            FROM memories_fts
            JOIN memories m ON m.id = memories_fts.rowid
            WHERE memories_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (fts_query, limit),
        )
        return cur.fetchall()

    # -- unified search -----------------------------------------------------
    def search(self, query: str, limit: int = 10) -> dict[str, list[sqlite3.Row]]:
        """Search both stores; used by the universal `reins wiki search`."""
        return {
            "pages": self.search_pages(query, limit),
            "memories": self.search_memories(query, limit),
        }

    # -- diagnostics --------------------------------------------------------
    def stats(self) -> dict[str, int]:
        def count(table: str) -> int:
            # The private caller supplies one of the two fixed table literals below.
            return int(self.conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])  # nosec B608

        return {"pages": count("pages"), "memories": count("memories")}

    def categories(self) -> dict[str, int]:
        out: dict[str, int] = {}
        for table in ("pages", "memories"):
            # The loop iterates only the fixed table tuple above.
            for row in self.conn.execute(
                f"SELECT category, COUNT(*) c FROM {table} GROUP BY category"  # nosec B608
            ):
                out[row["category"]] = out.get(row["category"], 0) + row["c"]
        return out


# Primary unified Wiki database backed by Kùzu graph and ChromaDB vectors
WikiDB = KuzuWikiDB
