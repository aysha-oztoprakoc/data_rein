"""
Shared spine for the harness agent roles: data-agy, data-hermes, data-ody.

Before the convergence these three services each reached models a different way
(legacy UniversalModelRouter, raw ollama subprocess, hardcoded paths). This base
gives all of them one identity:

* ``self.router``  — the model-agnostic :class:`ModelRouter` (local-first plane).
* ``self.trail``   — the shared Task Trail.
* ``self.infer()`` — one routing call (category → best model, graceful failover).
* ``self.recall()``— consult the single monolith wiki (knowledge DB).

It is passive and PON-compliant: no polling, no background threads of its own.
"""

from __future__ import annotations
from reins.services.logger import log_degradation

import sqlite3
from typing import TypedDict

from reins.harness.model_types import RouteResult
from reins.harness.models import ModelRouter
from reins.services.task_trail import TaskTrail

# Single source of truth for the fixed fleet of long-running harness agents
# (tmux windows in the `data` session). Consumed by the Sofia dashboard for
# process lookup (kill/renice/cgroup) and by anything else that needs to know
# "what agents exist" without hardcoding the list a second time.
#
#   name       - tmux window / process identity
#   role       - human-readable role shown in the dashboard
#   signature  - substring matched against a process's cmdline to find its PID(s)
class AgentSpec(TypedDict):
    name: str
    role: str
    signature: str


KNOWN_AGENTS: list[AgentSpec] = [
    {"name": "data-agy", "role": "CLOUD/CORE", "signature": "agy "},
    {"name": "data-hermes", "role": "HUB", "signature": "hermes-agent"},
    {"name": "data-ody", "role": "LOCAL FAILSAFE", "signature": "reins.cli ody"},
    {"name": "data-sofia", "role": "AUTO-HEALER", "signature": "sofia_protocol"},
]


class RecallResult(TypedDict):
    pages: list[sqlite3.Row]
    memories: list[sqlite3.Row]


class HarnessAgent:
    """Base identity shared by every agent operating under data_rein."""

    role: str = "agent"

    def __init__(self, router: ModelRouter | None = None) -> None:
        self.router: ModelRouter = router or ModelRouter()
        self.trail: TaskTrail | None
        # Task trail is optional at construction so lightweight bridges can skip it.
        try:
            self.trail = TaskTrail()
        except Exception:  # noqa: BLE001  # noqa: BROAD_EXCEPT_OK
            log_degradation(__name__)
            self.trail = None

    def infer(self, category: str, prompt: str, node: str = "amdy", rag: bool = False) -> RouteResult:
        """Route one prompt to the best model for a category (never raises)."""
        from reins.harness import workflow

        return workflow.run(category, prompt, node=node, rag=rag, router=self.router)

    def recall(self, query: str, limit: int = 5) -> RecallResult:
        """Consult the shared knowledge DB. Degrades to empty results, never raises."""
        try:
            from reins.harness.wiki import WikiDB

            with WikiDB() as db:
                results = db.search(query, limit)
                return {"pages": results["pages"], "memories": results["memories"]}
        except Exception:  # noqa: BLE001  # noqa: BROAD_EXCEPT_OK
            log_degradation(__name__)
            return {"pages": [], "memories": []}

    def remember(self, text: str, *, category: str = "general", source: str | None = None) -> None:
        """Persist a learned fact into the shared wiki (best effort)."""
        try:
            from reins.harness.wiki import WikiDB

            with WikiDB() as db:
                _ = db.add_memory(text, category=category, source=source or self.role, owner=self.role)
        except Exception:  # noqa: BLE001  # noqa: BROAD_EXCEPT_OK
            log_degradation(__name__)
