"""Kùzu and ChromaDB unified knowledge backend for the data_rein universal harness.

Implements the complete Wiki storage contract using Kùzu graph database as the primary
relational/node store and ChromaDB for semantic vector embeddings.
"""

from __future__ import annotations

import csv
import hashlib
import logging
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from reins.harness import paths
from reins.harness.embeddings import EmbeddingClient, cosine_similarity
from reins.services.logger import log_degradation

logger = logging.getLogger("reins.kuzu_wiki")

_KUZU_DATABASES: Dict[str, Any] = {}
_CHROMA_CLIENTS: Dict[str, Any] = {}


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


class KuzuWikiDB:
    """Graph & Vector native storage adapter fulfilling the Wiki database contract."""

    def __init__(
        self,
        kuzu_dir: Optional[Path | str] = None,
        chroma_dir: Optional[Path | str] = None,
        embedder: Optional[EmbeddingClient] = None,
    ) -> None:
        self.kuzu_dir = Path(kuzu_dir) if kuzu_dir else paths.kuzu_db_dir()
        self.chroma_dir = Path(chroma_dir) if chroma_dir else paths.chroma_db_dir()
        self.embedder = embedder or EmbeddingClient()

        self._kuzu_db: Any = None
        self._init_kuzu()
        self._init_chroma()

    def _init_kuzu(self) -> None:
        try:
            import kuzu  # type: ignore

            kpath = str(self.kuzu_dir)
            if kpath not in _KUZU_DATABASES:
                self.kuzu_dir.parent.mkdir(parents=True, exist_ok=True)
                if self.kuzu_dir.is_dir() and not any(self.kuzu_dir.iterdir()):
                    try:
                        self.kuzu_dir.rmdir()
                    except OSError:
                        pass
                _KUZU_DATABASES[kpath] = kuzu.Database(
                    kpath,
                    max_db_size=1024 * 1024 * 1024,
                    buffer_pool_size=128 * 1024 * 1024,
                )
            self._kuzu_db = _KUZU_DATABASES[kpath]
            self._init_schema()
        except Exception as e:
            logger.warning("Failed to initialize Kùzu database: %s", e)
            log_degradation(__name__)
            self._kuzu_db = None

    def _get_conn(self) -> Any:
        if self._kuzu_db is None:
            return None
        import kuzu  # type: ignore

        return kuzu.Connection(self._kuzu_db)

    def _init_schema(self) -> None:
        conn = self._get_conn()
        if conn is None:
            return
        ddls = [
            "CREATE NODE TABLE IF NOT EXISTS Document(slug STRING, title STRING, content STRING, category STRING, source_path STRING, fmt STRING, metadata_json STRING, owner STRING, trust_score DOUBLE, is_chunked INT64, is_deleted INT64, updated_at DOUBLE, PRIMARY KEY (slug));",
            "CREATE NODE TABLE IF NOT EXISTS MemoryNode(uid STRING, text STRING, category STRING, source STRING, owner STRING, session_id STRING, trust_score DOUBLE, is_chunked INT64, is_deleted INT64, timestamp DOUBLE, PRIMARY KEY (uid));",
            "CREATE NODE TABLE IF NOT EXISTS Chunk(id STRING, content STRING, token_count INT64, PRIMARY KEY (id));",
            "CREATE REL TABLE IF NOT EXISTS Contains(FROM Document TO Chunk);",
            "CREATE REL TABLE IF NOT EXISTS DerivesFrom(FROM MemoryNode TO Chunk);",
            "CREATE REL TABLE IF NOT EXISTS SimilarTo(FROM Chunk TO Chunk, score DOUBLE);",
        ]
        for ddl in ddls:
            try:
                conn.execute(ddl)
            except Exception as e:
                logger.info("Schema DDL notice: %s", e)

    def _init_chroma(self) -> None:
        try:
            import chromadb  # type: ignore

            cpath = str(self.chroma_dir)
            if cpath not in _CHROMA_CLIENTS:
                self.chroma_dir.mkdir(parents=True, exist_ok=True)
                _CHROMA_CLIENTS[cpath] = chromadb.PersistentClient(path=cpath)
            client = _CHROMA_CLIENTS[cpath]
            self._pages_coll = client.get_or_create_collection(
                name="wiki_pages_vectors",
                metadata={"hnsw:space": "cosine"},
            )
            self._memories_coll = client.get_or_create_collection(
                name="wiki_memories_vectors",
                metadata={"hnsw:space": "cosine"},
            )
        except Exception as e:
            logger.info("ChromaDB not initialized: %s", e)
            self._pages_coll = None
            self._memories_coll = None

    def __enter__(self) -> "KuzuWikiDB":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def close(self) -> None:
        pass

    # -- Pages CRUD ---------------------------------------------------------
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
        slug = slug or slugify(source_path or title)
        source_path = source_path or ""
        now = time.time()

        conn = self._get_conn()
        if conn is not None:
            conn.execute(
                """
                MERGE (d:Document {slug: $slug})
                ON CREATE SET d.title = $title, d.content = $content, d.category = $category,
                              d.source_path = $source_path, d.fmt = $fmt, d.metadata_json = $metadata_json,
                              d.owner = $owner, d.trust_score = $trust_score, d.is_chunked = $is_chunked,
                              d.is_deleted = 0, d.updated_at = $updated_at
                ON MATCH SET d.title = $title, d.content = $content, d.category = $category,
                             d.source_path = $source_path, d.fmt = $fmt, d.metadata_json = $metadata_json,
                             d.owner = $owner, d.trust_score = $trust_score, d.is_chunked = $is_chunked,
                             d.is_deleted = 0, d.updated_at = $updated_at;
                """,
                {
                    "slug": slug,
                    "title": title,
                    "content": content,
                    "category": category,
                    "source_path": source_path,
                    "fmt": fmt,
                    "metadata_json": metadata_json,
                    "owner": owner,
                    "trust_score": float(trust_score),
                    "is_chunked": 1 if is_chunked else 0,
                    "updated_at": float(now),
                },
            )

        if self._pages_coll is not None:
            try:
                emb = self.embedder.embed_text(f"{title}\n\n{content}"[:4000])
                self._pages_coll.upsert(
                    ids=[slug],
                    embeddings=[emb],
                    documents=[content[:4000]],
                    metadatas=[{"slug": slug, "title": title, "category": category}],
                )
            except Exception as e:
                logger.info("Chroma page upsert notice: %s", e)

        return slug

    def get_page(self, slug: str) -> Optional[Dict[str, Any]]:
        conn = self._get_conn()
        if conn is None:
            return None
        res = conn.execute(
            """
            MATCH (d:Document)
            WHERE d.slug = $slug AND d.is_deleted = 0
            RETURN d.slug, d.title, d.content, d.category, d.source_path, d.fmt,
                   d.metadata_json, d.owner, d.trust_score, d.is_chunked, d.updated_at;
            """,
            {"slug": slug},
        )
        if not res.has_next():
            return None
        row = res.get_next()
        return {
            "slug": row[0],
            "title": row[1],
            "content": row[2],
            "category": row[3],
            "source_path": row[4],
            "fmt": row[5],
            "metadata_json": row[6],
            "owner": row[7],
            "trust_score": row[8],
            "is_chunked": bool(row[9]),
            "updated_at": row[10],
        }

    def list_pages(
        self,
        *,
        category: Optional[str] = None,
        owner: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
        order: str = "recent",
    ) -> List[Dict[str, Any]]:
        conn = self._get_conn()
        if conn is None:
            return []
        where_clauses = ["d.is_deleted = 0"]
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if category:
            where_clauses.append("d.category = $category")
            params["category"] = category
        if owner:
            where_clauses.append("d.owner = $owner")
            params["owner"] = owner

        where_sql = " AND ".join(where_clauses)
        order_sql = "d.title ASC" if order == "title" else "d.updated_at DESC"
        query = f"""
            MATCH (d:Document)
            WHERE {where_sql}
            RETURN d.slug, d.title, d.content, d.category, d.source_path, d.fmt,
                   d.metadata_json, d.owner, d.trust_score, d.is_chunked, d.updated_at
            ORDER BY {order_sql}
            SKIP $offset LIMIT $limit;
        """
        res = conn.execute(query, params)
        items = []
        for row in res:
            items.append({
                "slug": row[0],
                "title": row[1],
                "content": row[2],
                "category": row[3],
                "source_path": row[4],
                "fmt": row[5],
                "metadata_json": row[6],
                "owner": row[7],
                "trust_score": row[8],
                "is_chunked": bool(row[9]),
                "updated_at": row[10],
            })
        return items

    def list_pages_summary(self, *, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        conn = self._get_conn()
        if conn is None:
            return []
        res = conn.execute(
            """
            MATCH (d:Document)
            WHERE d.is_deleted = 0
            RETURN d.slug, d.title, d.category, d.fmt, d.owner, d.updated_at
            ORDER BY d.updated_at DESC
            SKIP $offset LIMIT $limit;
            """,
            {"limit": limit, "offset": offset},
        )
        items = []
        for row in res:
            items.append({
                "slug": row[0],
                "title": row[1],
                "category": row[2],
                "fmt": row[3],
                "owner": row[4],
                "updated_at": row[5],
            })
        return items

    def count_pages(self, *, category: Optional[str] = None, owner: Optional[str] = None) -> int:
        conn = self._get_conn()
        if conn is None:
            return 0
        where_clauses = ["d.is_deleted = 0"]
        params: Dict[str, Any] = {}
        if category:
            where_clauses.append("d.category = $category")
            params["category"] = category
        if owner:
            where_clauses.append("d.owner = $owner")
            params["owner"] = owner
        where_sql = " AND ".join(where_clauses)
        res = conn.execute(f"MATCH (d:Document) WHERE {where_sql} RETURN COUNT(*);", params)
        if res.has_next():
            return int(res.get_next()[0])
        return 0

    def delete_page(self, slug: str) -> bool:
        conn = self._get_conn()
        if conn is None:
            return False
        if self.get_page(slug) is None:
            return False
        conn.execute("MATCH (d:Document) WHERE d.slug = $slug DETACH DELETE d;", {"slug": slug})
        if self._pages_coll is not None:
            try:
                self._pages_coll.delete(ids=[slug])
            except Exception as e:
                logger.info("Chroma page delete notice: %s", e)
        return True

    def soft_delete_page(self, slug: str, owner: str = "harness") -> bool:
        conn = self._get_conn()
        if conn is None:
            return False
        if self.get_page(slug) is None:
            return False
        conn.execute(
            "MATCH (d:Document) WHERE d.slug = $slug SET d.is_deleted = 1, d.updated_at = $now;",
            {"slug": slug, "now": float(time.time())},
        )
        return True

    def get_unchunked_pages(self, limit: int = 100) -> List[Dict[str, Any]]:
        conn = self._get_conn()
        if conn is None:
            return []
        res = conn.execute(
            """
            MATCH (d:Document)
            WHERE d.is_chunked = 0 AND d.is_deleted = 0
            RETURN d.slug, d.title, d.content, d.category, d.source_path, d.fmt,
                   d.metadata_json, d.owner, d.trust_score, d.is_chunked, d.updated_at
            ORDER BY d.updated_at ASC
            LIMIT $limit;
            """,
            {"limit": limit},
        )
        items = []
        for row in res:
            items.append({
                "slug": row[0],
                "title": row[1],
                "content": row[2],
                "category": row[3],
                "source_path": row[4],
                "fmt": row[5],
                "metadata_json": row[6],
                "owner": row[7],
                "trust_score": row[8],
                "is_chunked": bool(row[9]),
                "updated_at": row[10],
            })
        return items

    def mark_pages_chunked(self, slugs: List[str]) -> int:
        conn = self._get_conn()
        if not slugs or conn is None:
            return 0
        for s in slugs:
            conn.execute("MATCH (d:Document) WHERE d.slug = $slug SET d.is_chunked = 1;", {"slug": s})
        return len(slugs)

    # -- Memories CRUD ------------------------------------------------------
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
        uid = uid or _hash(text, category, source or "")
        source = source or ""
        session_id = session_id or ""
        now = time.time()

        conn = self._get_conn()
        if conn is not None:
            conn.execute(
                """
                MERGE (m:MemoryNode {uid: $uid})
                ON CREATE SET m.text = $text, m.category = $category, m.source = $source,
                              m.owner = $owner, m.session_id = $session_id, m.trust_score = $trust_score,
                              m.is_chunked = $is_chunked, m.is_deleted = 0, m.timestamp = $timestamp
                ON MATCH SET m.text = $text, m.category = $category, m.source = $source,
                             m.owner = $owner, m.session_id = $session_id, m.trust_score = $trust_score,
                             m.is_chunked = $is_chunked, m.is_deleted = 0, m.timestamp = $timestamp;
                """,
                {
                    "uid": uid,
                    "text": text,
                    "category": category,
                    "source": source,
                    "owner": owner,
                    "session_id": session_id,
                    "trust_score": float(trust_score),
                    "is_chunked": 1 if is_chunked else 0,
                    "timestamp": float(now),
                },
            )

        if self._memories_coll is not None:
            try:
                emb = self.embedder.embed_text(text[:4000])
                self._memories_coll.upsert(
                    ids=[uid],
                    embeddings=[emb],
                    documents=[text[:4000]],
                    metadatas=[{"uid": uid, "category": category, "source": source}],
                )
            except Exception as e:
                logger.info("Chroma memory upsert notice: %s", e)

        return uid

    def get_memory(self, uid: str) -> Optional[Dict[str, Any]]:
        conn = self._get_conn()
        if conn is None:
            return None
        res = conn.execute(
            """
            MATCH (m:MemoryNode)
            WHERE m.uid = $uid AND m.is_deleted = 0
            RETURN m.uid, m.text, m.category, m.source, m.owner, m.session_id,
                   m.trust_score, m.is_chunked, m.timestamp;
            """,
            {"uid": uid},
        )
        if not res.has_next():
            return None
        row = res.get_next()
        return {
            "uid": row[0],
            "text": row[1],
            "category": row[2],
            "source": row[3],
            "owner": row[4],
            "session_id": row[5],
            "trust_score": row[6],
            "is_chunked": bool(row[7]),
            "timestamp": row[8],
        }

    def list_memories(
        self,
        *,
        category: Optional[str] = None,
        owner: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> List[Dict[str, Any]]:
        conn = self._get_conn()
        if conn is None:
            return []
        where_clauses = ["m.is_deleted = 0"]
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if category:
            where_clauses.append("m.category = $category")
            params["category"] = category
        if owner:
            where_clauses.append("m.owner = $owner")
            params["owner"] = owner

        where_sql = " AND ".join(where_clauses)
        res = conn.execute(
            f"""
            MATCH (m:MemoryNode)
            WHERE {where_sql}
            RETURN m.uid, m.category, m.source, m.owner, m.timestamp, m.text, m.session_id, m.trust_score, m.is_chunked
            ORDER BY m.timestamp DESC
            SKIP $offset LIMIT $limit;
            """,
            params,
        )
        items = []
        for row in res:
            text_val = str(row[5]) if row[5] is not None else ""
            items.append({
                "uid": row[0],
                "category": row[1],
                "source": row[2],
                "owner": row[3],
                "timestamp": row[4],
                "text": text_val,
                "preview": text_val[:200],
                "session_id": row[6],
                "trust_score": row[7],
                "is_chunked": bool(row[8]),
            })
        return items

    def count_memories(self, *, category: Optional[str] = None, owner: Optional[str] = None) -> int:
        conn = self._get_conn()
        if conn is None:
            return 0
        where_clauses = ["m.is_deleted = 0"]
        params: Dict[str, Any] = {}
        if category:
            where_clauses.append("m.category = $category")
            params["category"] = category
        if owner:
            where_clauses.append("m.owner = $owner")
            params["owner"] = owner
        where_sql = " AND ".join(where_clauses)
        res = conn.execute(f"MATCH (m:MemoryNode) WHERE {where_sql} RETURN COUNT(*);", params)
        if res.has_next():
            return int(res.get_next()[0])
        return 0

    def delete_memory(self, uid: str) -> bool:
        conn = self._get_conn()
        if conn is None:
            return False
        if self.get_memory(uid) is None:
            return False
        conn.execute("MATCH (m:MemoryNode) WHERE m.uid = $uid DETACH DELETE m;", {"uid": uid})
        if self._memories_coll is not None:
            try:
                self._memories_coll.delete(ids=[uid])
            except Exception as e:
                logger.info("Chroma memory delete notice: %s", e)
        return True

    def soft_delete_memory(self, uid: str, owner: str = "harness") -> bool:
        conn = self._get_conn()
        if conn is None:
            return False
        if self.get_memory(uid) is None:
            return False
        conn.execute(
            "MATCH (m:MemoryNode) WHERE m.uid = $uid SET m.is_deleted = 1, m.timestamp = $now;",
            {"uid": uid, "now": float(time.time())},
        )
        return True

    def get_unchunked_memories(self, limit: int = 100) -> List[Dict[str, Any]]:
        conn = self._get_conn()
        if conn is None:
            return []
        res = conn.execute(
            """
            MATCH (m:MemoryNode)
            WHERE m.is_chunked = 0 AND m.is_deleted = 0
            RETURN m.uid, m.text, m.category, m.source, m.owner, m.session_id,
                   m.trust_score, m.is_chunked, m.timestamp
            ORDER BY m.timestamp ASC
            LIMIT $limit;
            """,
            {"limit": limit},
        )
        items = []
        for row in res:
            items.append({
                "uid": row[0],
                "text": row[1],
                "category": row[2],
                "source": row[3],
                "owner": row[4],
                "session_id": row[5],
                "trust_score": row[6],
                "is_chunked": bool(row[7]),
                "timestamp": row[8],
            })
        return items

    def mark_memories_chunked(self, uids: List[str]) -> int:
        conn = self._get_conn()
        if not uids or conn is None:
            return 0
        for u in uids:
            conn.execute("MATCH (m:MemoryNode) WHERE m.uid = $uid SET m.is_chunked = 1;", {"uid": u})
        return len(uids)

    def batch_insert_memories(self, items: List[Tuple[Any, ...]]) -> int:
        """Fast bulk insert of memories via CSV copy."""
        conn = self._get_conn()
        if not items or conn is None:
            return 0

        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            csv_path = f.name
            writer = csv.writer(f)
            for item in items:
                uid, text, category, source, owner, timestamp = item[:6]
                session_id = item[6] if len(item) > 6 else ""
                trust_score = item[7] if len(item) > 7 else 1.0
                is_chunked = item[8] if len(item) > 8 else 0
                is_deleted = 0
                writer.writerow([uid, text, category, source, owner, session_id, trust_score, is_chunked, is_deleted, timestamp])

        try:
            conn.execute(f"COPY MemoryNode FROM '{csv_path}';")
            return len(items)
        finally:
            Path(csv_path).unlink(missing_ok=True)

    # -- Semantic Search (ChromaDB + Kùzu fallback) -------------------------
    def search_pages(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        if not query or not query.strip():
            return []

        results: List[Dict[str, Any]] = []
        if self._pages_coll is not None and self._pages_coll.count() > 0:
            try:
                emb = self.embedder.embed_text(query)
                query_res = self._pages_coll.query(query_embeddings=[emb], n_results=min(limit, self._pages_coll.count()))
                if query_res and query_res.get("ids") and query_res["ids"][0]:
                    for idx, slug in enumerate(query_res["ids"][0]):
                        dist = query_res["distances"][0][idx] if query_res.get("distances") else 0.0
                        if dist > 0.40:
                            continue
                        page = self.get_page(slug)
                        if page:
                            doc_text = query_res["documents"][0][idx] if query_res.get("documents") else page["content"]
                            snippet = doc_text[:200] + "..." if len(doc_text) > 200 else doc_text
                            results.append({
                                "slug": page["slug"],
                                "title": page["title"],
                                "category": page["category"],
                                "source_path": page.get("source_path", ""),
                                "trust_score": page.get("trust_score", 1.0),
                                "snippet": snippet,
                                "rank": float(dist),
                            })
                    return results
            except Exception as e:
                logger.info("Chroma page search fallback: %s", e)

        # Fallback text scan via Kùzu
        all_pages = self.list_pages(limit=limit * 5)
        terms = [t.lower() for t in query.split() if t.strip()]
        for p in all_pages:
            content_lower = p["content"].lower()
            title_lower = p["title"].lower()
            if terms and all(t in title_lower or t in content_lower for t in terms):
                results.append({
                    "slug": p["slug"],
                    "title": p["title"],
                    "category": p["category"],
                    "source_path": p.get("source_path", ""),
                    "trust_score": p.get("trust_score", 1.0),
                    "snippet": p["content"][:200],
                    "rank": 1.0,
                })
            if len(results) >= limit:
                break
        return results

    def search_memories(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        if not query or not query.strip():
            return []

        results: List[Dict[str, Any]] = []
        if self._memories_coll is not None and self._memories_coll.count() > 0:
            try:
                emb = self.embedder.embed_text(query)
                query_res = self._memories_coll.query(query_embeddings=[emb], n_results=min(limit, self._memories_coll.count()))
                if query_res and query_res.get("ids") and query_res["ids"][0]:
                    for idx, uid in enumerate(query_res["ids"][0]):
                        dist = query_res["distances"][0][idx] if query_res.get("distances") else 0.0
                        if dist > 0.40:
                            continue
                        mem = self.get_memory(uid)
                        if mem:
                            doc_text = query_res["documents"][0][idx] if query_res.get("documents") else mem["text"]
                            snippet = doc_text[:200] + "..." if len(doc_text) > 200 else doc_text
                            results.append({
                                "uid": mem["uid"],
                                "category": mem["category"],
                                "source": mem.get("source", ""),
                                "trust_score": mem.get("trust_score", 1.0),
                                "snippet": snippet,
                                "rank": float(dist),
                            })
                    return results
            except Exception as e:
                logger.info("Chroma memory search fallback: %s", e)

        # Fallback text scan via Kùzu
        all_memories = self.list_memories(limit=limit * 5)
        terms = [t.lower() for t in query.split() if t.strip()]
        for m in all_memories:
            preview_lower = m["preview"].lower()
            if terms and all(t in preview_lower for t in terms):
                results.append({
                    "uid": m["uid"],
                    "category": m["category"],
                    "source": m.get("source", ""),
                    "trust_score": m.get("trust_score", 1.0),
                    "snippet": m["preview"],
                    "rank": 1.0,
                })
            if len(results) >= limit:
                break
        return results

    def search(self, query: str, limit: int = 10) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "pages": self.search_pages(query, limit=limit),
            "memories": self.search_memories(query, limit=limit),
        }

    # -- Diagnostics & Stats ------------------------------------------------
    def stats(self) -> Dict[str, int]:
        return {
            "pages": self.count_pages(),
            "memories": self.count_memories(),
        }

    def categories(self) -> Dict[str, int]:
        conn = self._get_conn()
        out: Dict[str, int] = {}
        if conn is None:
            return out
        try:
            r1 = conn.execute("MATCH (d:Document) WHERE d.is_deleted = 0 RETURN d.category, COUNT(*);")
            for row in r1:
                cat, cnt = str(row[0]), int(row[1])
                out[cat] = out.get(cat, 0) + cnt
            r2 = conn.execute("MATCH (m:MemoryNode) WHERE m.is_deleted = 0 RETURN m.category, COUNT(*);")
            for row in r2:
                cat, cnt = str(row[0]), int(row[1])
                out[cat] = out.get(cat, 0) + cnt
        except Exception as e:
            logger.info("Category aggregation notice: %s", e)
        return out
