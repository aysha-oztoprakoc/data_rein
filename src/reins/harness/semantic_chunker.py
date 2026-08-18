"""Semantic document and memory chunker for RAG and local model fine-tuning."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class SemanticChunk:
    chunk_id: str
    content: str
    source_id: str
    source_type: str  # "page" | "memory"
    section: str = ""
    token_estimate: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)


def _compute_chunk_id(content: str, source_id: str, section: str = "") -> str:
    h = hashlib.sha256()
    h.update(content.strip().encode("utf-8", "replace"))
    h.update(b"\x00")
    h.update(source_id.encode("utf-8", "replace"))
    h.update(b"\x00")
    h.update(section.encode("utf-8", "replace"))
    return h.hexdigest()[:32]


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def chunk_markdown(
    content: str,
    source_id: str,
    *,
    max_chunk_chars: int = 1200,
    min_chunk_chars: int = 40,
    metadata: Optional[dict[str, Any]] = None,
) -> List[SemanticChunk]:
    """Split markdown by headers (#, ##, ###) and paragraph boundaries.
    
    Preserves heading context for each chunk.
    """
    if not content or not content.strip():
        return []

    meta = dict(metadata or {})
    chunks: List[SemanticChunk] = []

    # Match markdown headers: # Header, ## Header, ### Header
    header_pattern = re.compile(r"^(#{1,6}\s+.+)$", re.MULTILINE)
    
    sections = header_pattern.split(content)
    # If content does not start with header, sections[0] is the pre-header text.
    current_header = "Introduction"

    for part_raw in sections:
        part = part_raw.strip()
        if not part:
            continue

        if part.startswith("#"):
            current_header = part.lstrip("#").strip()
            continue

        # Now `part` is the body text under `current_header`
        # Sub-split into paragraphs if too large
        paragraphs = [p.strip() for p in part.split("\n\n") if p.strip()]
        current_block: List[str] = []
        current_len = 0

        for p in paragraphs:
            if len(p) > max_chunk_chars:
                # Flush existing block
                if current_block:
                    block_text = "\n\n".join(current_block)
                    if len(block_text) >= min_chunk_chars:
                        chunks.append(
                            SemanticChunk(
                                chunk_id=_compute_chunk_id(block_text, source_id, current_header),
                                content=block_text,
                                source_id=source_id,
                                source_type="page",
                                section=current_header,
                                token_estimate=estimate_tokens(block_text),
                                metadata=meta,
                            )
                        )
                    current_block, current_len = [], 0

                # Slice oversized paragraph into sentences or line boundaries
                lines = [line.strip() for line in p.split("\n") if line.strip()]
                sub_block: List[str] = []
                sub_len = 0
                for line in lines:
                    if sub_len + len(line) > max_chunk_chars and sub_block:
                        stext = "\n".join(sub_block)
                        chunks.append(
                            SemanticChunk(
                                chunk_id=_compute_chunk_id(stext, source_id, current_header),
                                content=stext,
                                source_id=source_id,
                                source_type="page",
                                section=current_header,
                                token_estimate=estimate_tokens(stext),
                                metadata=meta,
                            )
                        )
                        sub_block, sub_len = [line], len(line)
                    else:
                        sub_block.append(line)
                        sub_len += len(line)
                if sub_block:
                    stext = "\n".join(sub_block)
                    if len(stext) >= min_chunk_chars:
                        chunks.append(
                            SemanticChunk(
                                chunk_id=_compute_chunk_id(stext, source_id, current_header),
                                content=stext,
                                source_id=source_id,
                                source_type="page",
                                section=current_header,
                                token_estimate=estimate_tokens(stext),
                                metadata=meta,
                            )
                        )
                continue

            if current_len + len(p) > max_chunk_chars and current_block:
                block_text = "\n\n".join(current_block)
                if len(block_text) >= min_chunk_chars:
                    chunks.append(
                        SemanticChunk(
                            chunk_id=_compute_chunk_id(block_text, source_id, current_header),
                            content=block_text,
                            source_id=source_id,
                            source_type="page",
                            section=current_header,
                            token_estimate=estimate_tokens(block_text),
                            metadata=meta,
                        )
                    )
                current_block = [p]
                current_len = len(p)
            else:
                current_block.append(p)
                current_len += len(p) + 2

        if current_block:
            block_text = "\n\n".join(current_block)
            if len(block_text) >= min_chunk_chars:
                chunks.append(
                    SemanticChunk(
                        chunk_id=_compute_chunk_id(block_text, source_id, current_header),
                        content=block_text,
                        source_id=source_id,
                        source_type="page",
                        section=current_header,
                        token_estimate=estimate_tokens(block_text),
                        metadata=meta,
                    )
                )

    return chunks


def chunk_memory(
    text: str,
    uid: str,
    *,
    category: str = "general",
    metadata: Optional[dict[str, Any]] = None,
) -> List[SemanticChunk]:
    """Chunk atomic memory or observation fact."""
    clean_text = text.strip()
    if not clean_text:
        return []

    meta = dict(metadata or {})
    meta["category"] = category

    # Memories are usually atomic (1-4 paragraphs). If small, emit as 1 chunk.
    if len(clean_text) <= 1200:
        return [
            SemanticChunk(
                chunk_id=_compute_chunk_id(clean_text, uid, category),
                content=clean_text,
                source_id=uid,
                source_type="memory",
                section=category,
                token_estimate=estimate_tokens(clean_text),
                metadata=meta,
            )
        ]

    # For larger memories (e.g. digested documents stored as memories), split by paragraphs
    paragraphs = [p.strip() for p in clean_text.split("\n\n") if p.strip()]
    chunks: List[SemanticChunk] = []
    current_block: List[str] = []
    current_len = 0

    for p in paragraphs:
        if current_len + len(p) > 1200 and current_block:
            btext = "\n\n".join(current_block)
            chunks.append(
                SemanticChunk(
                    chunk_id=_compute_chunk_id(btext, uid, category),
                    content=btext,
                    source_id=uid,
                    source_type="memory",
                    section=category,
                    token_estimate=estimate_tokens(btext),
                    metadata=meta,
                )
            )
            current_block = [p]
            current_len = len(p)
        else:
            current_block.append(p)
            current_len += len(p) + 2

    if current_block:
        btext = "\n\n".join(current_block)
        chunks.append(
            SemanticChunk(
                chunk_id=_compute_chunk_id(btext, uid, category),
                content=btext,
                source_id=uid,
                source_type="memory",
                section=category,
                token_estimate=estimate_tokens(btext),
                metadata=meta,
            )
        )

    return chunks
