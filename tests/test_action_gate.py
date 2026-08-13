"""
Tests for the blueprint.yaml `action_gates` pipeline: a lesser model's proposed
tool call is a proposal, never an instruction. `gate_call` runs it through
allowlist -> schema -> sanitize -> billing/idempotency-guard before dispatch,
and every rejection leaves an honest, trail-logged diagnostic (GD-3).
"""

from __future__ import annotations


import pytest

from reins.harness.action_gate import ActionArgs, ActionResult
from reins.services.task_trail import TaskTrail


def test_gate_accepts_allowlisted_valid_call_and_dispatches(trail: TaskTrail) -> None:
    from reins.harness.action_gate import gate_call

    _ = trail
    calls: list[ActionArgs] = []

    def _dispatch(args: ActionArgs) -> ActionResult:
        calls.append(args)
        return {"echo": args["prompt"]}

    result = gate_call(
        context="route_local",
        tool_name="local_generate",
        args={"prompt": "summarize this"},
        dispatch=_dispatch,
    )
    assert result["accepted"] is True
    assert result["result"] == {"echo": "summarize this"}
    assert calls == [{"prompt": "summarize this"}]


def test_gate_rejects_non_allowlisted_tool_and_logs_trail(trail: TaskTrail) -> None:
    from reins.harness.action_gate import gate_call
    from reins.services.task_trail import TaskTrail

    _ = trail
    result = gate_call(
        context="route_local",
        tool_name="escalate_cloud",
        args={"prompt": "do something"},
        dispatch=lambda args: pytest.fail("must not dispatch a rejected call"),
    )
    assert result["accepted"] is False
    assert result["reason"] == "not_allowlisted"

    logged = TaskTrail().get_failed_tasks()
    assert any(
        task["task_type"] == "gate:reject"
        and "not_allowlisted" in str(task["prompt"])
        for task in logged
    )


@pytest.mark.parametrize(
    "args",
    [
        {"prompt": 12345},
        {"prompt": "summarize", "shell": "rm -rf /"},
    ],
)
def test_gate_rejects_schema_invalid_args(trail: TaskTrail, args: ActionArgs) -> None:
    from reins.harness.action_gate import gate_call

    _ = trail
    result = gate_call(
        context="route_local",
        tool_name="local_generate",
        args=args,
        dispatch=lambda args: pytest.fail("must not dispatch a rejected call"),
    )
    assert result["accepted"] is False
    assert result["reason"] == "schema_invalid"


def test_gate_rejects_path_traversal(trail: TaskTrail) -> None:
    from reins.harness.action_gate import gate_call

    _ = trail
    result = gate_call(
        context="route_local",
        tool_name="read_file",
        args={"path": "../../etc/passwd"},
        dispatch=lambda args: pytest.fail("must not dispatch a rejected call"),
    )
    assert result["accepted"] is False
    assert result["reason"] == "sanitize_failed"


def test_gate_rejects_billable_call_without_authorization(trail: TaskTrail) -> None:
    from reins.harness.action_gate import gate_call

    _ = trail
    result = gate_call(
        context="escalate_cloud",
        tool_name="cloud_generate",
        args={"prompt": "use claude for this"},
        dispatch=lambda args: pytest.fail("must not dispatch a rejected call"),
        authorized=False,
    )
    assert result["accepted"] is False
    assert result["reason"] == "billing_or_idempotency_guard"


def test_gate_allows_billable_call_when_explicitly_authorized(trail: TaskTrail) -> None:
    from reins.harness.action_gate import gate_call

    _ = trail
    result = gate_call(
        context="escalate_cloud",
        tool_name="cloud_generate",
        args={"prompt": "use claude for this"},
        dispatch=lambda args: {"ok": True},
        authorized=True,
    )
    assert result["accepted"] is True


def test_gate_validate_matches_gate_call_without_dispatching(trail: TaskTrail) -> None:
    """gate_validate runs the same checks as gate_call but never calls dispatch."""
    from reins.harness.action_gate import gate_validate

    _ = trail
    accepted = gate_validate("route_local", "local_generate", {"prompt": "hello"})
    assert accepted == {"accepted": True, "reason": None}

    rejected = gate_validate("route_local", "escalate_cloud", {"prompt": "hello"})
    assert rejected == {"accepted": False, "reason": "not_allowlisted"}


def test_gate_rejection_never_raises_on_dispatch_error(trail: TaskTrail) -> None:
    """A rejected proposal must never reach dispatch, even if dispatch would raise."""
    from reins.harness.action_gate import gate_call

    def _boom(args: ActionArgs) -> ActionResult:
        pytest.fail(f"must not dispatch rejected args: {args}")

    _ = trail
    result = gate_call(
        context="route_local",
        tool_name="not_a_real_tool",
        args={},
        dispatch=_boom,
    )
    assert result["accepted"] is False
