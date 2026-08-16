"""Event-driven Wiki Watcher (PON Compliance: zero polling, inotify-backed).

Watches `knowledge_base/` and `skills/` for markdown edits and triggers debounced
monolith wiki consolidation.
"""

from __future__ import annotations

import logging
import sys
import threading
from typing import Optional

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from reins.harness import external_io, paths

logger = logging.getLogger("reins.wiki_watcher")


class WikiChangeHandler(FileSystemEventHandler):
    """Debounced inotify event handler for wiki and skills documentation."""

    def __init__(self, debounce_seconds: float = 2.0) -> None:
        super().__init__()
        self.debounce_seconds = debounce_seconds
        self._timer: Optional[threading.Timer] = None
        self._lock = threading.Lock()

    def on_any_event(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        src_path = str(event.src_path)
        # Only react to markdown or schema documentation changes
        if src_path.endswith((".md", ".json", ".yaml", ".yml")):
            # Ignore sqlite database files, logs, and temp staging
            if any(ignore in src_path for ignore in ("wiki.db", ".stage", ".git", "__pycache__", ".previous")):
                return
            self._schedule_consolidation(src_path)

    def _schedule_consolidation(self, triggered_path: str) -> None:
        with self._lock:
            if self._timer is not None:
                self._timer.cancel()
            self._timer = threading.Timer(self.debounce_seconds, self._run_consolidation, args=[triggered_path])
            self._timer.daemon = True
            self._timer.start()

    def _run_consolidation(self, triggered_path: str) -> None:
        logger.info("Wiki change detected in %s -> running consolidation", triggered_path)
        script = paths.home() / "scripts" / "consolidate_wiki.py"
        try:
            res = external_io.run([sys.executable, str(script)], check=False)
            if res.returncode == 0:
                logger.info("Wiki consolidation completed automatically.")
            else:
                logger.warning("Wiki auto-consolidation returned warning: %s", res.stderr.strip())
        except Exception as e:
            logger.error("Failed to run wiki auto-consolidation: %s", e)


_observer: Optional[Observer] = None


def start_wiki_watcher(debounce_seconds: float = 2.0) -> Observer:
    """Start the inotify background observer watching skills/ and knowledge_base/."""
    global _observer
    if _observer is not None and _observer.is_alive():
        return _observer

    handler = WikiChangeHandler(debounce_seconds=debounce_seconds)
    observer = Observer()

    kb_dir = paths.knowledge_base()
    skills_dir = paths.skills()

    if kb_dir.exists():
        observer.schedule(handler, str(kb_dir), recursive=True)
    if skills_dir.exists():
        observer.schedule(handler, str(skills_dir), recursive=True)

    observer.daemon = True
    observer.start()
    _observer = observer
    logger.info("Wiki inotify watcher started on %s and %s", kb_dir, skills_dir)
    return observer


def stop_wiki_watcher() -> None:
    """Stop the inotify observer."""
    global _observer
    if _observer is not None:
        _observer.stop()
        _observer.join(timeout=2.0)
        _observer = None
