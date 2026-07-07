"""
Context chunking for local-model handoff.

qwen2.5-coder:7b (and similarly-sized local models) has an 8192-token input
window. When a bigger model (Claude) hands work to the trail for a local model
to continue, the context has to be split into self-contained, budget-sized
blocks rather than dumped in whole - this module does that packing. It never
raises; callers get a best-effort chunking even on bad input.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

CHARS_PER_TOKEN = 4  # rough heuristic; good enough for budget packing, not billing

MODEL_CONTEXT_LIMITS = {
    "qwen2.5-coder:7b": 8192,
    "qwen2.5-coder:3b": 8192,
    "codegemma:7b": 8192,
    "llama3.1:8b": 8192,
}
DEFAULT_CONTEXT_LIMIT = 8192

OUTPUT_RESERVE_TOKENS = 1024   # room for the model's own reply
SCAFFOLD_RESERVE_TOKENS = 300  # room for the goal/prev-summary/instruction framing
MIN_BUDGET_TOKENS = 512


@dataclass
class Chunk:
    index: int
    goal: str
    context: str


def context_budget_tokens(model: Optional[str] = None, *, extra_reserve_tokens: int = 0) -> int:
    limit = MODEL_CONTEXT_LIMITS.get(model or "", DEFAULT_CONTEXT_LIMIT)
    budget = limit - OUTPUT_RESERVE_TOKENS - SCAFFOLD_RESERVE_TOKENS - extra_reserve_tokens
    return max(MIN_BUDGET_TOKENS, budget)


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // CHARS_PER_TOKEN)


def plan_chunks(
    goal: str,
    context_blocks: Optional[List[str]] = None,
    *,
    model: Optional[str] = None,
    extra_reserve_tokens: int = 0,
) -> List[Chunk]:
    """Pack `context_blocks` into as few chunks as fit the model's token budget.

    Each block is kept whole where possible (so a chunk never splits a fact
    mid-thought); a single block bigger than the whole budget is hard-sliced.
    """
    blocks = [b for b in (context_blocks or []) if b and b.strip()]
    budget_chars = context_budget_tokens(model, extra_reserve_tokens=extra_reserve_tokens) * CHARS_PER_TOKEN

    if not blocks:
        return [Chunk(index=0, goal=goal, context="")]

    packed: List[str] = []
    current: List[str] = []
    current_len = 0

    def _flush():
        if current:
            packed.append("\n\n".join(current))

    for block in blocks:
        if len(block) > budget_chars:
            _flush()
            current, current_len = [], 0
            for start in range(0, len(block), budget_chars):
                packed.append(block[start:start + budget_chars])
            continue

        added_len = len(block) + (2 if current else 0)
        if current and current_len + added_len > budget_chars:
            _flush()
            current, current_len = [block], len(block)
        else:
            current.append(block)
            current_len += added_len

    _flush()

    return [Chunk(index=i, goal=goal, context=ctx) for i, ctx in enumerate(packed)]
