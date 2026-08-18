"""
ContextBuilderNode: Context Injection (RAG & Knowledge Graph Traversal).

Subscribes to TASK_CREATED, queries KuzuDB graph neighborhood and WikiDB search,
and updates state to TASK_READY_FOR_EXECUTION.
"""
from __future__ import annotations

import logging
from typing import Optional

from reins.graph.engine import GraphNode
from reins.graph.fbe import FBEAttribute, FBEState
from reins.harness.wiki import WikiDB

logger = logging.getLogger("reins.graph.context_node")


class ContextBuilderNode(GraphNode):
    """
    Builds RAG and Graph Context for a prompt and prepares it for execution.
    """

    def __init__(self, wiki_db: Optional[WikiDB] = None) -> None:
        super().__init__(name="ContextBuilderNode")
        self.wiki_db = wiki_db or WikiDB()

    def handle_event(self, attribute: FBEAttribute) -> Optional[FBEAttribute]:
        logger.info("ContextBuilderNode augmenting context for task %s", attribute.task_id)
        data = attribute.value
        if isinstance(data, dict):
            prompt = data.get("prompt", "")
            category = data.get("category", "general")
            rag_enabled = data.get("rag", True)
        else:
            prompt = str(data)
            category = "general"
            rag_enabled = True

        context_block = ""
        if rag_enabled and prompt:
            try:
                hits = self.wiki_db.search_pages(prompt, limit=3)
                if hits:
                    snippets = [f"[{h['title']}]\n{h['snippet']}" for h in hits]
                    context_block = "--- Graph & Wiki Context ---\n" + "\n\n".join(snippets) + "\n--- End Context ---\n\n"
            except Exception as e:
                logger.warning("RAG context query failed: %s", e)

        augmented_prompt = context_block + prompt

        return FBEAttribute(
            name=FBEState.TASK_READY_FOR_EXECUTION.value,
            value={
                "prompt": augmented_prompt,
                "original_prompt": prompt,
                "category": category,
                "context_injected": bool(context_block),
            },
            task_id=attribute.task_id,
            metadata={"source_node": self.name},
        )
