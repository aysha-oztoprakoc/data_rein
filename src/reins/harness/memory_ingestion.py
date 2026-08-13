from __future__ import annotations

import logging
from pathlib import Path

from defusedxml import ElementTree as ET
from defusedxml.common import DefusedXmlException

from .wiki import WikiDB

logger = logging.getLogger(__name__)


def ingest_sofia_memories(
    extracted_dir: Path | str,
    wiki_path: Path | str | None = None,
    *,
    owner: str = "data-ody",
) -> int:
    count = 0
    with WikiDB(wiki_path) as wiki:
        for filepath in sorted(Path(extracted_dir).glob("*.xml")):
            try:
                tree = ET.parse(filepath)
                root = tree.getroot()
                if root is None:
                    continue
                metadata = root.find("metadata")
                content = root.find("content")
                title = metadata.findtext("title", filepath.name) if metadata is not None else filepath.name
                text = "".join(content.itertext()).strip() if content is not None else ""
                if not text:
                    continue
                _ = wiki.add_memory(
                    f"[SOURCE: {title}]\n{text}",
                    category="sofia_protocol",
                    source=filepath.name,
                    owner=owner,
                )
                count += 1
            except (OSError, ET.ParseError, DefusedXmlException) as error:
                logger.warning("Sofia memory import failed for %s: %s", filepath, error)
    return count


def ingest_knowledge_memories(
    knowledge_base_dir: Path | str,
    wiki_path: Path | str | None = None,
    *,
    owner: str = "data-ody",
) -> int:
    root = Path(knowledge_base_dir)
    count = 0
    with WikiDB(wiki_path) as wiki:
        for filepath in sorted(root.rglob("*")):
            if not filepath.is_file() or filepath.suffix.lower() not in {".txt", ".md", ".xml"}:
                continue
            relative_path = filepath.relative_to(root)
            if "agents" in relative_path.parts:
                continue
            try:
                text = filepath.read_text(encoding="utf-8", errors="replace").strip()
            except OSError as error:
                logger.warning("Knowledge memory import failed for %s: %s", filepath, error)
                continue
            if not text:
                continue
            category = relative_path.parent.name if relative_path.parent != Path(".") else "general"
            _ = wiki.add_memory(
                f"[SOURCE: {relative_path}]\n{text}",
                category=category,
                source=str(relative_path),
                owner=owner,
            )
            count += 1
    return count
