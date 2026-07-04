"""
Workflow integration for local models under the data_rein harness.

Turns the routing infrastructure into everyday leverage:

* low-effort offload  — quick chat / summarize / classify / optimize on small fast
  local models, so trivial work never touches a paid cloud call.
* heavy automation    — run a model over many inputs unattended, with per-item
  graceful degradation and Task-Trail logging.

Everything routes through :class:`reins.harness.models.ModelRouter`, so it is
model-agnostic and inherits local-first + amdy<->tell failover for free.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Optional

from reins.harness.models import ModelRouter, RouteResult


# Category presets: which task-router category each shortcut maps to, and the
# preferred node (small/fast nodes for low-effort work).
LOW_EFFORT = {
    "ask": ("general chatting", "tell"),      # quick Q&A -> small quantized models
    "summarize": ("data processing", "amdy"),
    "classify": ("data organizing", "tell"),
    "optimize": ("prompt optimization", "tell"),
}


def _rag_context(prompt: str, max_docs: int = 3) -> str:
    """Best-effort RAG: pull top matching wiki pages as context. Degrades to ''."""
    try:
        from reins.harness.wiki import WikiDB

        with WikiDB() as db:
            hits = db.search_pages(prompt, limit=max_docs)
        if not hits:
            return ""
        blocks = [f"[{h['title']}]\n{h['snippet']}" for h in hits]
        return "--- Context from the harness wiki ---\n" + "\n\n".join(blocks) + "\n--- end context ---\n\n"
    except Exception:
        return ""


def run(
    category: str,
    prompt: str,
    node: str = "amdy",
    rag: bool = False,
    router: Optional[ModelRouter] = None,
) -> RouteResult:
    """Route one prompt to the best local model for a category. Never raises."""
    router = router or ModelRouter()
    if rag:
        prompt = _rag_context(prompt) + prompt
    return router.route(category, prompt, node)


def low_effort(kind: str, prompt: str, rag: bool = False) -> RouteResult:
    """Run a named low-effort shortcut (ask/summarize/classify/optimize)."""
    if kind not in LOW_EFFORT:
        raise ValueError(f"unknown low-effort task '{kind}'; choose from {sorted(LOW_EFFORT)}")
    category, node = LOW_EFFORT[kind]
    return run(category, prompt, node=node, rag=rag)


@dataclass
class BatchItem:
    index: int
    prompt: str
    ok: bool
    model: str
    text: Optional[str]
    error: Optional[str]


def batch(
    category: str,
    prompts: Iterable[str],
    node: str = "amdy",
    rag: bool = False,
    on_result: Optional[Callable[[BatchItem], None]] = None,
    log_trail: bool = True,
) -> list[BatchItem]:
    """
    Heavy automation: run a model over many prompts unattended.

    Each item is isolated — one failure degrades that item (ok=False) and the run
    continues. Optionally logs the batch to the shared Task Trail so other agents
    see the work. Returns one BatchItem per prompt.
    """
    router = ModelRouter()
    results: list[BatchItem] = []

    trail = None
    if log_trail:
        try:
            from reins.services.task_trail import TaskTrail

            trail = TaskTrail()
        except Exception:
            trail = None

    for i, prompt in enumerate(prompts):
        prompt = prompt.strip()
        if not prompt:
            continue
        task_id = None
        if trail is not None:
            try:
                task_id = trail.create_task(f"batch:{category}", prompt, node)
                trail.update_task(task_id, "running")
            except Exception:
                task_id = None

        res = run(category, prompt, node=node, rag=rag, router=router)
        item = BatchItem(i, prompt, res.ok, res.model, res.text, res.error)
        results.append(item)

        if trail is not None and task_id is not None:
            try:
                trail.update_task(task_id, "success" if res.ok else "failed")
            except Exception:
                pass
        if on_result is not None:
            on_result(item)

    return results
