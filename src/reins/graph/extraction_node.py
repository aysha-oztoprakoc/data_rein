"""
ExtractionNode: Event-driven file drop / raw data discovery.

Zero polling when idle: Uses watchdog/inotify to monitor extraction drop folders
or reacts to external discovery events and emits RAW_DATA_AVAILABLE FBE.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

from reins.graph.engine import GraphNode
from reins.graph.fbe import FBEAttribute, FBEState

logger = logging.getLogger("reins.graph.extraction_node")


class ExtractionNode(GraphNode):
    """
    Watches directories or reacts to raw data requests,
    emitting RAW_DATA_AVAILABLE FBE attributes.
    """

    def __init__(self, watch_dir: Optional[Path] = None) -> None:
        super().__init__(name="ExtractionNode")
        self.watch_dir = watch_dir

    def handle_event(self, attribute: FBEAttribute) -> Optional[FBEAttribute]:
        """
        Processes an extraction trigger or file event and produces RAW_DATA_AVAILABLE attribute.
        """
        logger.info("ExtractionNode received event: %s", attribute.name)
        payload = attribute.value
        
        # Extract file path or text content
        if isinstance(payload, dict):
            file_path = payload.get("file_path", "")
            content = payload.get("content", "")
            category = payload.get("category", "general")
        else:
            file_path = str(payload)
            content = ""
            category = "general"

        return FBEAttribute(
            name=FBEState.RAW_DATA_AVAILABLE.value,
            value={
                "file_path": file_path,
                "content": content,
                "category": category,
            },
            task_id=attribute.task_id,
            metadata={"source_node": self.name},
        )
