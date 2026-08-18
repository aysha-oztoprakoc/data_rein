"""Wiki Graph & Vector Deduplication Pipeline.

PON-compliant: passive library / method node with zero polling.
Transforms flat SQLite pages and memories into a deduplicated, relational
knowledge graph indexed via ChromaDB (vectors) and Kùzu (graph), with graceful
fallbacks when optional native binaries are not installed.
"""

from __future__ import annotations

import hashlib
import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from reins.harness import paths
from reins.harness.embeddings import EmbeddingClient, cosine_similarity
from reins.harness.semantic_chunker import SemanticChunk, chunk_markdown, chunk_memory
from reins.harness.wiki import WikiDB

logger = logging.getLogger("reins.wiki_graph_pipeline")


@dataclass
class SyncStats:
    pages_processed: int = 0
    memories_processed: int = 0
    chunks_created: int = 0
    chunks_deduplicated: int = 0
    graph_nodes_added: int = 0
    graph_edges_added: int = 0


class WikiGraphPipeline:
    """Orchestrator for semantic chunking, vector deduplication, and graph syncing."""

    def __init__(
        self,
        wiki_db: Optional[WikiDB] = None,
        kuzu_dir: Optional[Path] = None,
        chroma_dir: Optional[Path] = None,
        embedding_client: Optional[EmbeddingClient] = None,
        similarity_threshold: float = 0.95,
    ) -> None:
        self.wiki_db = wiki_db or WikiDB()
        self.kuzu_dir = kuzu_dir or paths.kuzu_db_dir()
        self.chroma_dir = chroma_dir or paths.chroma_db_dir()
        self.embedder = embedding_client or EmbeddingClient()
        self.similarity_threshold = similarity_threshold
        
        self._kuzu_conn: Any = None
        self._chroma_coll: Any = None
        self._init_stores()

    def _init_stores(self) -> None:
        # 1. Initialize Kùzu Graph DB (if installed)
        try:
            import kuzu  # type: ignore
            self.kuzu_dir.mkdir(parents=True, exist_ok=True)
            db = kuzu.Database(str(self.kuzu_dir))
            conn = kuzu.Connection(db)
            self._init_kuzu_schema(conn)
            self._kuzu_conn = conn
            logger.debug("Kùzu embedded graph store initialized at %s", self.kuzu_dir)
        except ImportError:
            logger.debug("Kùzu not installed; degrading to lightweight internal graph sync.")
            self._kuzu_conn = None
        except Exception as e:
            logger.warning("Failed to initialize Kùzu database (%s); degrading gracefully.", e)
            self._kuzu_conn = None

        # 2. Initialize ChromaDB Vector Store (if installed)
        try:
            import chromadb  # type: ignore
            self.chroma_dir.mkdir(parents=True, exist_ok=True)
            chroma_client = chromadb.PersistentClient(path=str(self.chroma_dir))
            self._chroma_coll = chroma_client.get_or_create_collection(
                name="wiki_chunks",
                metadata={"hnsw:space": "cosine"},
            )
            logger.debug("ChromaDB vector store initialized at %s", self.chroma_dir)
        except ImportError:
            logger.debug("ChromaDB not installed; degrading to in-memory vector deduplication.")
            self._chroma_coll = None
        except Exception as e:
            logger.warning("Failed to initialize ChromaDB (%s); degrading gracefully.", e)
            self._chroma_coll = None

    def _init_kuzu_schema(self, conn: Any) -> None:
        """Create Kùzu Node and Rel tables if not existing."""
        ddls = [
            "CREATE NODE TABLE IF NOT EXISTS Document(slug STRING, title STRING, category STRING, PRIMARY KEY (slug));",
            "CREATE NODE TABLE IF NOT EXISTS MemoryNode(uid STRING, category STRING, PRIMARY KEY (uid));",
            "CREATE NODE TABLE IF NOT EXISTS Chunk(id STRING, content STRING, token_count INT64, PRIMARY KEY (id));",
            "CREATE REL TABLE IF NOT EXISTS Contains(FROM Document TO Chunk);",
            "CREATE REL TABLE IF NOT EXISTS DerivesFrom(FROM MemoryNode TO Chunk);",
            "CREATE REL TABLE IF NOT EXISTS SimilarTo(FROM Chunk TO Chunk, score DOUBLE);",
        ]
        for ddl in ddls:
            try:
                conn.execute(ddl)
            except Exception as e:
                logger.warning("Schema DDL notice: %s", e)

    def sync_pending(self, batch_size: int = 200) -> SyncStats:
        """Process all unchunked pages and memories from SQLite and sync to graph/vector stores."""
        stats = SyncStats()

        # In-memory vector and content-hash cache for deduplication when ChromaDB is absent
        local_vector_index: List[Tuple[str, List[float]]] = []
        exact_hash_index: Dict[str, str] = {}

        # 1. Fetch unchunked pages
        pages = self.wiki_db.get_unchunked_pages(limit=batch_size)
        processed_slugs: List[str] = []

        for row in pages:
            slug = row["slug"]
            title = row["title"]
            content = row["content"]
            category = row["category"]
            metadata_json = row["metadata_json"]
            try:
                meta = json.loads(metadata_json) if metadata_json else {}
            except Exception as e:
                logger.warning("Page metadata parse fallback: %s", e)
                meta = {}

            chunks = chunk_markdown(content, source_id=slug, metadata=meta)
            self._index_chunks(
                chunks=chunks,
                source_id=slug,
                source_title=title,
                source_category=category,
                source_type="page",
                stats=stats,
                local_vectors=local_vector_index,
                exact_hashes=exact_hash_index,
            )
            processed_slugs.append(slug)
            stats.pages_processed += 1

        if processed_slugs:
            self.wiki_db.mark_pages_chunked(processed_slugs)

        # 2. Fetch unchunked memories
        memories = self.wiki_db.get_unchunked_memories(limit=batch_size)
        processed_uids: List[str] = []

        for row in memories:
            uid = row["uid"]
            text = row["text"]
            category = row["category"]

            chunks = chunk_memory(text, uid=uid, category=category)
            self._index_chunks(
                chunks=chunks,
                source_id=uid,
                source_title=uid,
                source_category=category,
                source_type="memory",
                stats=stats,
                local_vectors=local_vector_index,
                exact_hashes=exact_hash_index,
            )
            processed_uids.append(uid)
            stats.memories_processed += 1

        if processed_uids:
            self.wiki_db.mark_memories_chunked(processed_uids)

        return stats

    def _index_chunks(
        self,
        chunks: List[SemanticChunk],
        source_id: str,
        source_title: str,
        source_category: str,
        source_type: str,
        stats: SyncStats,
        local_vectors: List[Tuple[str, List[float]]],
        exact_hashes: Dict[str, str],
    ) -> None:
        """Embed, deduplicate, and record nodes and edges in Kùzu and ChromaDB."""
        if not chunks:
            return

        # Insert source node in Kùzu
        if self._kuzu_conn is not None:
            try:
                if source_type == "page":
                    escaped_title = source_title.replace("'", "''")
                    self._kuzu_conn.execute(
                        f"MERGE (d:Document {{slug: '{source_id}', title: '{escaped_title}', category: '{source_category}'}});"
                    )
                else:
                    self._kuzu_conn.execute(
                        f"MERGE (m:MemoryNode {{uid: '{source_id}', category: '{source_category}'}});"
                    )
            except Exception as e:
                logger.warning("Kùzu source node error: %s", e)

        for chunk in chunks:
            stats.chunks_created += 1
            content_norm = chunk.content.strip().lower()
            chash = hashlib.sha256(content_norm.encode("utf-8", "replace")).hexdigest()

            # Fast O(1) exact content deduplication check first
            if chash in exact_hashes:
                stats.chunks_deduplicated += 1
                target_chunk_id = exact_hashes[chash]
            else:
                embedding = self.embedder.embed_text(chunk.content)
                duplicate_chunk_id, sim_score = self._find_duplicate(chunk.content, embedding, local_vectors)

                if duplicate_chunk_id:
                    stats.chunks_deduplicated += 1
                    target_chunk_id = duplicate_chunk_id
                    exact_hashes[chash] = duplicate_chunk_id
                else:
                    target_chunk_id = chunk.chunk_id
                    exact_hashes[chash] = chunk.chunk_id

                    # Add new vector to ChromaDB
                    if self._chroma_coll is not None:
                        try:
                            self._chroma_coll.add(
                                ids=[chunk.chunk_id],
                                embeddings=[embedding],
                                documents=[chunk.content],
                                metadatas=[{"source_id": source_id, "source_type": source_type, "section": chunk.section}],
                            )
                        except Exception as e:
                            logger.warning("Chroma add error: %s", e)
                    
                    if len(local_vectors) < 500:
                        local_vectors.append((chunk.chunk_id, embedding))

                    # Add new Chunk node in Kùzu
                    if self._kuzu_conn is not None:
                        try:
                            escaped_content = chunk.content.replace("'", "''").replace("\\", "\\\\")[:2000]
                            self._kuzu_conn.execute(
                                f"MERGE (c:Chunk {{id: '{chunk.chunk_id}', content: '{escaped_content}', token_count: {chunk.token_estimate}}});"
                            )
                            stats.graph_nodes_added += 1
                        except Exception as e:
                            logger.warning("Kùzu chunk node error: %s", e)

            # Link source to Chunk node in Kùzu
            if self._kuzu_conn is not None:
                try:
                    if source_type == "page":
                        self._kuzu_conn.execute(
                            f"MATCH (d:Document), (c:Chunk) WHERE d.slug = '{source_id}' AND c.id = '{target_chunk_id}' "
                            f"CREATE (d)-[:Contains]->(c);"
                        )
                    else:
                        self._kuzu_conn.execute(
                            f"MATCH (m:MemoryNode), (c:Chunk) WHERE m.uid = '{source_id}' AND c.id = '{target_chunk_id}' "
                            f"CREATE (m)-[:DerivesFrom]->(c);"
                        )
                    stats.graph_edges_added += 1
                except Exception as e:
                    logger.warning("Kùzu rel error: %s", e)

    def _find_duplicate(
        self,
        content: str,
        embedding: List[float],
        local_vectors: List[Tuple[str, List[float]]],
    ) -> Tuple[Optional[str], float]:
        """Check if identical or highly similar chunk already exists."""
        # 1. Check ChromaDB collection
        if self._chroma_coll is not None:
            try:
                results = self._chroma_coll.query(
                    query_embeddings=[embedding],
                    n_results=1,
                )
                if results and results.get("distances") and results["distances"][0]:
                    dist = results["distances"][0][0]
                    # Cosine distance in Chroma: sim = 1.0 - dist
                    sim = 1.0 - dist
                    if sim >= self.similarity_threshold:
                        existing_id = results["ids"][0][0]
                        return existing_id, sim
            except Exception as e:
                logger.warning("Chroma query error: %s", e)

        # 2. Check local vectors fallback (bounded to recent items)
        for existing_id, vec in reversed(local_vectors[-100:]):
            sim = cosine_similarity(embedding, vec)
            if sim >= self.similarity_threshold:
                return existing_id, sim

        return None, 0.0

    def graph_stats(self) -> Dict[str, Any]:
        """Return counts and status of the graph and vector stores."""
        stats: Dict[str, Any] = {
            "kuzu_available": self._kuzu_conn is not None,
            "chroma_available": self._chroma_coll is not None,
            "document_nodes": 0,
            "memory_nodes": 0,
            "chunk_nodes": 0,
            "total_vectors": 0,
        }

        if self._kuzu_conn is not None:
            try:
                r1 = self._kuzu_conn.execute("MATCH (d:Document) RETURN COUNT(*) AS c;").get_next()[0]
                r2 = self._kuzu_conn.execute("MATCH (m:MemoryNode) RETURN COUNT(*) AS c;").get_next()[0]
                r3 = self._kuzu_conn.execute("MATCH (c:Chunk) RETURN COUNT(*) AS c;").get_next()[0]
                stats["document_nodes"] = r1
                stats["memory_nodes"] = r2
                stats["chunk_nodes"] = r3
            except Exception as e:
                logger.warning("Kuzu count query error: %s", e)

        if self._chroma_coll is not None:
            try:
                stats["total_vectors"] = self._chroma_coll.count()
            except Exception as e:
                logger.warning("Chroma count query error: %s", e)

        return stats
