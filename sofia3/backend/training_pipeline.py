"""JSONL Training Data Pipeline for local models.

Exports the wiki pages and memories into a structured JSONL dataset
whenever the graph/wiki changes, with debouncing to avoid disk thrashing.
"""

import json
import logging
import threading
from pathlib import Path
from typing import Any

from reins.harness import paths
from reins.harness.wiki import WikiDB

logger = logging.getLogger("sofia3.training_pipeline")

_export_timer: threading.Timer | None = None
_export_lock = threading.Lock()
_DEBOUNCE_SEC = 5.0

def export_training_data() -> None:
    """Read active pages and memories and write to a .jsonl file."""
    try:
        # We output to data-workspace per the implementation plan
        out_dir = Path("/home/amdy/data-workspace")
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "training_ready.jsonl"
        
        records = []
        with WikiDB() as db:
            # 1. Active Pages
            # We don't want to export chunked pages if they are just chunks, but the pages themselves.
            # We fetch all pages that are not deleted.
            rows = db.conn.execute("SELECT title, content, category FROM pages WHERE is_deleted = 0").fetchall()
            for r in rows:
                title = r["title"]
                content = r["content"]
                cat = r["category"]
                records.append({
                    "instruction": f"Explain the knowledge base entry for '{title}' (Category: {cat}).",
                    "context": "",
                    "response": content
                })
            
            # 2. Active Memories
            mrows = db.conn.execute("SELECT text, category FROM memories WHERE is_deleted = 0").fetchall()
            for r in mrows:
                text = r["text"]
                cat = r["category"]
                records.append({
                    "instruction": f"Recall a memory regarding {cat}.",
                    "context": "",
                    "response": text
                })
        
        with open(out_file, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                
        logger.info("Exported %d records to %s", len(records), out_file)
    except Exception as exc:
        logger.warning("Training pipeline export failed: %s", exc)

def trigger_export() -> None:
    """Trigger a debounced export of the training data."""
    global _export_timer
    with _export_lock:
        if _export_timer is not None:
            _export_timer.cancel()
        _export_timer = threading.Timer(_DEBOUNCE_SEC, export_training_data)
        _export_timer.daemon = True
        _export_timer.start()
