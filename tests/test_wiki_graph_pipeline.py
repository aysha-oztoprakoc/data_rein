from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from reins.harness.embeddings import EmbeddingClient, cosine_similarity, fallback_embed
from reins.harness.semantic_chunker import chunk_markdown, chunk_memory
from reins.harness.wiki import WikiDB
from reins.services.wiki_graph_pipeline import WikiGraphPipeline


def test_semantic_chunker_markdown_splits_headers_and_paragraphs() -> None:
    content = """# Architecture Overview
This is the core architecture description.

## Data Pipelines
We extract data via PON triggers.
Each pipeline emits results on MQTT.

## Hardware Matrix
Node amdy has 16GB VRAM.
Node tell has 6GB VRAM.
"""
    chunks = chunk_markdown(content, source_id="architecture-doc")
    assert len(chunks) >= 3
    sections = {c.section for c in chunks}
    assert "Architecture Overview" in sections
    assert "Data Pipelines" in sections
    assert "Hardware Matrix" in sections
    assert all(c.token_estimate > 0 for c in chunks)
    assert all(c.source_id == "architecture-doc" for c in chunks)


def test_semantic_chunker_memory_atomic() -> None:
    text = "amdy GPU VRAM is 8.0GB (RX 9060 XT), RAM 14.7GB. See knowledge_base/HARDWARE.md."
    chunks = chunk_memory(text, uid="mem-123", category="system")
    assert len(chunks) == 1
    assert chunks[0].source_id == "mem-123"
    assert chunks[0].source_type == "memory"
    assert chunks[0].section == "system"


def test_embeddings_and_cosine_similarity() -> None:
    vec1 = fallback_embed("data rein universal harness")
    vec2 = fallback_embed("data rein universal harness")
    vec3 = fallback_embed("completely unrelated quantum physics concept")

    sim_identical = cosine_similarity(vec1, vec2)
    sim_different = cosine_similarity(vec1, vec3)

    assert sim_identical > 0.99
    assert sim_different < sim_identical


def test_wiki_schema_is_chunked_flag_and_queries(tmp_path: Path) -> None:
    db_path = tmp_path / "wiki.db"
    with WikiDB(db_path) as db:
        # Insert a page and memory
        page_slug = db.upsert_page(title="Test Page", content="Some test content", is_chunked=False)
        mem_uid = db.add_memory("Test memory text", is_chunked=False)

        # Query unchunked
        unchunked_pages = db.get_unchunked_pages()
        unchunked_memories = db.get_unchunked_memories()

        assert len(unchunked_pages) == 1
        assert unchunked_pages[0]["slug"] == page_slug
        assert len(unchunked_memories) == 1
        assert unchunked_memories[0]["uid"] == mem_uid

        # Mark as chunked
        db.mark_pages_chunked([page_slug])
        db.mark_memories_chunked([mem_uid])

        assert len(db.get_unchunked_pages()) == 0
        assert len(db.get_unchunked_memories()) == 0


def test_wiki_graph_pipeline_sync_and_deduplication(tmp_path: Path) -> None:
    db_path = tmp_path / "wiki.db"
    with WikiDB(db_path) as db:
        # Insert two documents with duplicate content
        shared_body = "This is a recurring knowledge segment describing the PON zero polling paradigm."
        db.upsert_page(title="Doc 1", content=f"# Section 1\n{shared_body}", slug="doc-1")
        db.upsert_page(title="Doc 2", content=f"# Section 2\n{shared_body}", slug="doc-2")
        db.add_memory(shared_body, uid="mem-dup")

        pipeline = WikiGraphPipeline(
            wiki_db=db,
            kuzu_dir=tmp_path / "kuzu",
            chroma_dir=tmp_path / "chroma",
            similarity_threshold=0.90,
        )

        stats = pipeline.sync_pending(batch_size=100)

        assert stats.pages_processed == 2
        assert stats.memories_processed == 1
        assert stats.chunks_created >= 3
        assert stats.chunks_deduplicated >= 1  # Successfully deduplicated!

        # Verify all marked chunked in SQLite
        assert len(db.get_unchunked_pages()) == 0
        assert len(db.get_unchunked_memories()) == 0


def test_wiki_graph_pipeline_graceful_degradation_without_libraries(tmp_path: Path) -> None:
    db_path = tmp_path / "wiki.db"
    with WikiDB(db_path) as db:
        db.upsert_page(title="Fallback Doc", content="Testing fallback functionality without native binaries.")
        
        pipeline = WikiGraphPipeline(
            wiki_db=db,
            kuzu_dir=tmp_path / "kuzu",
            chroma_dir=tmp_path / "chroma",
        )
        # Force connections to None simulating absent libraries
        pipeline._kuzu_conn = None
        pipeline._chroma_coll = None

        stats = pipeline.sync_pending(batch_size=50)

        assert stats.pages_processed == 1
        assert len(db.get_unchunked_pages()) == 0
        graph_stats = pipeline.graph_stats()
        assert graph_stats["kuzu_available"] is False
        assert graph_stats["chroma_available"] is False
