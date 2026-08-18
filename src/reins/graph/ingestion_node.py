"""
IngestionNode: Reacts to RAW_DATA_AVAILABLE and writes into KuzuDB & WikiGraphPipeline.

Parses text/markdown/documents and indexes chunks into the Kuzu Graph store
and Chroma vector collection, with graceful fallback.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

from reins.graph.engine import GraphNode
from reins.graph.fbe import FBEAttribute, FBEState
from reins.harness.wiki import WikiDB
from reins.services.wiki_graph_pipeline import WikiGraphPipeline

logger = logging.getLogger("reins.graph.ingestion_node")


class IngestionNode(GraphNode):
    """
    Subscribes to RAW_DATA_AVAILABLE FBEs.
    Parses content, writes to WikiDB, and invokes WikiGraphPipeline to sync KuzuDB.
    """

    def __init__(
        self,
        wiki_db: Optional[WikiDB] = None,
        graph_pipeline: Optional[WikiGraphPipeline] = None,
    ) -> None:
        super().__init__(name="IngestionNode")
        self.wiki_db = wiki_db or WikiDB()
        self.pipeline = graph_pipeline or WikiGraphPipeline(wiki_db=self.wiki_db)

    def handle_event(self, attribute: FBEAttribute) -> Optional[FBEAttribute]:
        logger.info("IngestionNode processing raw data for task %s", attribute.task_id)
        data = attribute.value
        if not isinstance(data, dict):
            return None

        file_path_str = data.get("file_path", "")
        content = data.get("content", "")
        category = data.get("category", "general")

        if file_path_str and not content:
            path = Path(file_path_str)
            if path.exists() and path.is_file():
                try:
                    content = path.read_text(encoding="utf-8", errors="replace")
                except Exception as e:
                    logger.warning("Failed to read file %s: %s", path, e)
                    content = ""

        if not content:
            logger.info("No content to ingest for task %s", attribute.task_id)
            return None

        title = Path(file_path_str).stem if file_path_str else f"ingest-{attribute.task_id[:8]}"
        
        # 1. Upsert to WikiDB
        try:
            slug = self.wiki_db.upsert_page(
                title=title,
                content=content,
                category=category,
                is_chunked=False,
            )
            # 2. Sync to Kuzu Graph and Chroma
            stats = self.pipeline.sync_pending(batch_size=50)
            logger.info(
                "Ingestion completed for slug %s (chunks created: %d, deduplicated: %d)",
                slug, stats.chunks_created, stats.chunks_deduplicated,
            )
        except Exception as e:
            logger.error("Ingestion failed: %s", e)
            return None

        return FBEAttribute(
            name=FBEState.TASK_CREATED.value,
            value={
                "slug": slug,
                "title": title,
                "category": category,
                "chunks_created": stats.chunks_created,
            },
            task_id=attribute.task_id,
            metadata={"source_node": self.name},
        )
