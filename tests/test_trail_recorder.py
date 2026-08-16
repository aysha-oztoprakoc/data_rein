from __future__ import annotations

from reins.services.task_trail import TaskTrail
from reins.services.trail_recorder import TrailRecorder


def test_record_plan_appends_steps_and_tracks_commits(trail: TaskTrail) -> None:
    recorder = TrailRecorder(trail)
    task_id = recorder.record_plan(
        task_id="plan:test",
        task_type="plan:production-readiness",
        prompt="recover + resume the Kimi plan",
        plan_md="# Plan\n## Phase 1\n",
        author="kimi-k3",
    )

    recorder.append_step(
        task_id,
        "fixed kimi context limits",
        commits=["abc123"],
        files=["opencode.json"],
    )
    recorder.append_step(task_id, "wired trail CLI verbs", status="running")

    record = trail.get_task(task_id)
    assert record is not None
    assert record["kind"] == "plan"
    assert record["status"] == "active"
    assert record["author"] == "kimi-k3"
    assert record["plan_md"].startswith("# Plan")
    assert record["steps_count"] == 2
    steps = record["steps"]
    assert steps[0]["summary"] == "fixed kimi context limits"
    assert steps[0]["commits"] == ["abc123"]
    assert steps[0]["files"] == ["opencode.json"]
    assert steps[1]["status"] == "running"


def test_recorder_is_idempotent_across_sessions(trail: TaskTrail) -> None:
    recorder = TrailRecorder(trail)
    task_id = recorder.record_plan(task_id="plan:stable", prompt="long-running work")

    # A later session appends a step to the SAME stable task id.
    recorder.append_step(task_id, "continued work, session 2")

    record = trail.get_task(task_id)
    assert record is not None
    assert len(record["steps"]) == 1


def test_finish_plan_marks_complete_and_keeps_history(trail: TaskTrail) -> None:
    recorder = TrailRecorder(trail)
    task_id = recorder.record_plan(task_id="plan:close", prompt="ship it")
    recorder.append_step(task_id, "executed phase")
    recorder.finish_plan(task_id)

    record = trail.get_task(task_id)
    assert record is not None
    assert record["status"] == "success"
    assert record["finished_at"] > 0
    assert len(record["steps"]) == 1  # history preserved


def test_failed_step_marks_plan_failed(trail: TaskTrail) -> None:
    recorder = TrailRecorder(trail)
    task_id = recorder.record_plan(task_id="plan:fail", prompt="risky step")
    recorder.append_step(task_id, "boom", status="failed")

    record = trail.get_task(task_id)
    assert record is not None
    assert record["status"] == "failed"