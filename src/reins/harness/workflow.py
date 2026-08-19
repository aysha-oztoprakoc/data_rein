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
from reins.services.logger import get_logger, log_degradation

from dataclasses import dataclass
from typing import Callable, Iterable, Optional

from reins.harness.models import ModelRouter, RouteResult
from reins.harness.resilience import BreakerRegistry, CircuitOpenError
from reins.harness.trust_anchor import KnowledgeValidator

logger = get_logger("workflow")
_breaker_registry = BreakerRegistry()
_validator = KnowledgeValidator()


# Category presets: which task-router category each shortcut maps to, and the
# preferred node (small/fast nodes for low-effort work).
LOW_EFFORT = {
    "ask": ("momus", "tell"),      # quick Q&A -> small quantized models
    "summarize": ("metis", "amdy"),
    "classify": ("metis", "tell"),
    "optimize": ("metis", "tell"),
}


def _rag_context(prompt: str, max_docs: int = 3) -> str:
    """Best-effort RAG: pull top matching wiki pages as context. Degrades to ''."""
    try:
        from reins.harness.kuzu_wiki import KuzuWikiDB

        with KuzuWikiDB() as db:
            hits = db.search_pages(prompt, limit=max_docs)
        if not hits:
            return ""
        blocks = [f"[{h['title']}]\n{h['snippet']}" for h in hits]
        return "--- Context from the harness wiki ---\n" + "\n\n".join(blocks) + "\n--- end context ---\n\n"
    except Exception:
        log_degradation(__name__)
        return ""


def run(
    category: str,
    prompt: str,
    node: str = "amdy",
    rag: bool = False,
    router: Optional[ModelRouter] = None,
) -> RouteResult:
    """Route one prompt autonomously to the best model for a category. Never raises."""
    router = router or ModelRouter()
    if rag:
        prompt = _rag_context(prompt) + prompt
        
    breaker_key = f"model_router:{category}:{node}"
    breaker = _breaker_registry.get(breaker_key)
    
    if breaker.state.name == "OPEN":
        return RouteResult(text=None, model="circuit_breaker", provider="system", node=node, ok=False, error="Circuit open due to repeated anomalous outputs")
        
    try:
        def _operation():
            res = router.route(category, prompt, node=node)
            if res.ok and res.text:
                score = _validator.validate_update(res.text, "model")
                if score < 0.5:
                    raise ValueError(f"Poisoned output detected (trust_score={score})")
            return res
            
        return breaker.call(_operation)
    except CircuitOpenError:
        return RouteResult(text=None, model="circuit_breaker", provider="system", node=node, ok=False, error="Circuit open due to repeated anomalous outputs")
    except Exception as e:
        logger.warning("workflow operation failed: %s", e, exc_info=True)
        return RouteResult(text=None, model="unknown", provider="system", node=node, ok=False, error=str(e))

def robust_aggregate(prompts: list[str], category: str, node: str = "amdy", rag: bool = False) -> RouteResult:
    """Run multiple prompts and use TrimmedMean logic to aggregate results by discarding anomalous outputs."""
    results = []
    for prompt in prompts:
        res = run(category, prompt, node=node, rag=rag)
        if res.ok and res.text:
            results.append(res)
    
    if not results:
        return RouteResult(text=None, model="aggregate", provider="system", node=node, ok=False, error="No successful results to aggregate")
        
    # Trimmed Mean / FLTrust heuristic:
    if len(results) > 2:
        results.sort(key=lambda r: len(r.text or ""))
        trim_count = max(1, len(results) // 10)
        valid_results = results[trim_count:-trim_count]
    else:
        valid_results = results
        
    combined = "\n\n".join(r.text for r in valid_results if r.text)
    return RouteResult(text=combined, model="aggregate", provider="system", node=node, ok=True, error=None)


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
            log_degradation(__name__)
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
                log_degradation(__name__)
                task_id = None

        res = run(category, prompt, node=node, rag=rag, router=router)
        item = BatchItem(i, prompt, res.ok, res.model, res.text, res.error)
        results.append(item)

        if trail is not None and task_id is not None:
            try:
                trail.update_task(task_id, "success" if res.ok else "failed")
            except Exception:
                log_degradation(__name__)
                pass
        if on_result is not None:
            on_result(item)

    return results
