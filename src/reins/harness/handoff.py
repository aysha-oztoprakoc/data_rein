"""
Trail-based work handoff: a bigger model (Claude) queues a chunked task on the
Task Trail; a local model (qwen2.5-coder:7b via ModelRouter) picks up one
chunk at a time and follows the "trail of logic" forward via a running
SUMMARY line, so the whole task fits inside the local model's context window
even though no single call sees the full history.

Single knowledge store law: chunks/summaries live on the Task Trail record
itself (already the shared coordination store) - nothing new is created.
Graceful degradation: every public function catches its own errors and
returns a safe default (None / False) instead of raising or crashing a caller
that's polling the trail on a timer/hook.
"""

from __future__ import annotations

import uuid
from typing import Any, Dict, List, Optional

from reins.harness import chunking
from reins.services.task_trail import TaskTrail

MAESTRO_MODEL = "qwen2.5-coder:7b"

CHUNK_PROMPT_TEMPLATE = """[Step {step} of {total} - task: {goal}]

Prior progress so far (may be empty for the first step):
{prev_summary}

Context for this step:
{context}

Continue the work for this step only. End your reply with a single line
starting with "SUMMARY:" that condenses what you did/learned so the next
step can continue without re-reading this context."""


def _route_maestro(prompt: str, node: str, category: str):
    """Prefer the maestro model (qwen2.5-coder:7b) via a direct local.generate
    fast-path - the maestro is fixed by design for the meta harness, so we
    skip ModelRouter's category-ranking overhead on the common case. Any
    failure (model not pulled, server down, non-local node, ...) falls back
    to full multi-tier ModelRouter routing so degradation still happens."""
    from reins.harness.models import ModelRouter, RouteResult

    if node == "amdy":
        try:
            from reins.harness import local

            text = local.generate(MAESTRO_MODEL, prompt, options=local.default_options())
            return RouteResult(text=text, model=MAESTRO_MODEL, provider="ollama", node=node, ok=True)
        except Exception:
            pass  # fall through to ModelRouter's own degradation chain

    return ModelRouter().route(category, prompt, node=node)


def queue_chunked_task(
    task_type: str,
    goal: str,
    context_blocks: Optional[List[str]] = None,
    *,
    node: str = "amdy",
    model: Optional[str] = None,
) -> Optional[str]:
    """Split `goal`+`context_blocks` into local-model-sized chunks and enqueue
    them on the trail. Returns the task_id, or None on failure (logged, not
    raised - the caller may be a non-interactive hook)."""
    try:
        chunks = chunking.plan_chunks(goal, context_blocks, model=model)
        task_id = str(uuid.uuid4())
        trail = TaskTrail()
        trail.upsert_task(
            task_id,
            task_type=task_type,
            prompt=goal,
            target_node=node,
            status="queued",
            chunks=[{"goal": c.goal, "context": c.context} for c in chunks],
            chunk_cursor=0,
            chunk_summaries=[],
        )
        return task_id
    except Exception as e:
        _log_warning(f"queue_chunked_task failed: {e}")
        return None


def pickup_next(category: str = "coding: menial", node: str = "amdy") -> Optional[Dict[str, Any]]:
    """Execute exactly one chunk of the oldest queued/in-progress chunked task
    targeted at `node`. Returns a status dict, or None if there's nothing to
    pick up or something went wrong (logged honestly, never raised)."""
    try:
        trail = TaskTrail()
        candidates = [
            t for t in trail.by_status("queued", "chunk_in_progress")
            if t.get("chunks") and t.get("target_node") == node
        ]
        if not candidates:
            return None
        task = candidates[0]
        task_id = task["task_id"]
        chunks = task["chunks"]
        cursor = task.get("chunk_cursor", 0)

        if cursor >= len(chunks):
            trail.set_status(task_id, "done")
            return {"task_id": task_id, "status": "done"}

        chunk = chunks[cursor]
        summaries = list(task.get("chunk_summaries") or [])
        prev_summary = summaries[-1] if summaries else "(none yet)"
        prompt = CHUNK_PROMPT_TEMPLATE.format(
            step=cursor + 1,
            total=len(chunks),
            goal=chunk.get("goal", ""),
            prev_summary=prev_summary,
            context=chunk.get("context") or "(no additional context)",
        )

        result = _route_maestro(prompt, node, category)
        if not result.ok:
            trail.upsert_task(task_id, status="failed", error=result.error or "route failed")
            return {"task_id": task_id, "status": "failed", "error": result.error}

        summary = _extract_summary(result.text or "")
        summaries.append(summary)
        new_cursor = cursor + 1
        new_status = "done" if new_cursor >= len(chunks) else "chunk_in_progress"
        trail.upsert_task(
            task_id, status=new_status, chunk_cursor=new_cursor,
            chunk_summaries=summaries, last_model=result.model, last_node=result.node,
        )
        return {
            "task_id": task_id, "status": new_status,
            "chunk": cursor, "of": len(chunks), "summary": summary,
        }
    except Exception as e:
        _log_warning(f"pickup_next failed: {e}")
        return None


def _extract_summary(text: str) -> str:
    for line in text.splitlines():
        if line.strip().upper().startswith("SUMMARY:"):
            return line.strip()
    tail = text.strip()
    return tail[-500:] if tail else "(no summary produced)"


def _log_warning(msg: str) -> None:
    try:
        from reins.services.logger import get_logger

        get_logger("handoff").warning(msg)
    except Exception:
        pass
