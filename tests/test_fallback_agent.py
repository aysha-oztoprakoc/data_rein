from __future__ import annotations

from pathlib import Path

import pytest

from reins.services.fallback_agent import OdysseusAgent
from reins.services.harness_bootstrapper import HarnessBootstrapper
from reins.services.task_trail import TaskTrail


def test_odysseus_processes_only_explicit_fallback_tasks(
    trail: TaskTrail,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given unrelated active work and one task explicitly assigned to data-ody.
    audit_id = trail.create_task("harness:audit", "audit the harness", "amdy")
    fallback_id = trail.create_task("model:fallback", "summarize locally", "data-ody")
    agent = OdysseusAgent()
    agent.trail = trail
    observed_statuses: list[str | None] = []

    def generate(_prompt: str) -> str:
        fallback_task = trail.get_task(fallback_id)
        assert fallback_task is not None
        observed_statuses.append(fallback_task.get("status"))
        return "local result"

    monkeypatch.setattr(agent, "query_tiered_fallback", generate)

    # When the reactive fallback drain handles a trail notification.
    acted = agent.process_pending()

    # Then ownership stays explicit and unrelated work is not mutated.
    assert [task["task_id"] for task in acted] == [fallback_id]
    assert observed_statuses == ["running_fallback"]
    fallback_task = trail.get_task(fallback_id)
    audit_task = trail.get_task(audit_id)
    assert fallback_task is not None
    assert audit_task is not None
    assert fallback_task.get("status") == "success_fallback"
    assert audit_task.get("status") == "pending"


def test_bootstrap_does_not_scan_the_knowledge_base(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given a bootstrapper whose notification phase is isolated.
    monkeypatch.setenv("DATA_REIN_STATE_DIR", str(tmp_path / "state"))
    bootstrapper = HarnessBootstrapper()
    resumed: list[bool] = []
    monkeypatch.setattr(bootstrapper, "resume_pending_tasks", lambda: resumed.append(True))

    def reject_scan(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("bootstrap must not scan the knowledge base")

    monkeypatch.setattr("os.walk", reject_scan)

    # When a client initializes the harness.
    bootstrapper.bootstrap()

    # Then initialization only resumes event-driven work.
    assert resumed == [True]
