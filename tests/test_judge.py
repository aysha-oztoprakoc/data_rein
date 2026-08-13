"""
Tests for the blueprint.yaml `agent_as_a_judge` framework: the Lead Agent
evaluates a hierarchical dependency graph proposed by a lesser model, mapping
each check to a KAD persona - ARCHIMEDES (decomposition), SOCRATES_PROTOCOL
(edge justification), SOFIA_PROTOCOL (wiki grounding) - before any leaf action
is allowed to proceed to action_gate dispatch.
"""

from __future__ import annotations

import pytest

from reins.harness.judge import RawEdge, RawNode
from reins.harness.model_types import RouteResult
from reins.harness.models import ModelRouter
from reins.harness.wiki import WikiDB
from reins.services.task_trail import TaskTrail


def _node(
    node_id: str,
    context: str = "route_local",
    tool_name: str = "local_generate",
    prompt: str = "do work",
) -> RawNode:
    return {
        "id": node_id,
        "action": {"context": context, "tool_name": tool_name, "args": {"prompt": prompt}},
    }


def test_judge_accepts_valid_dag_and_logs_verdict(trail: TaskTrail, wiki: WikiDB) -> None:
    from reins.harness.judge import judge_graph

    _ = trail, wiki
    nodes: list[RawNode] = [_node("a"), _node("b")]
    edges: list[RawEdge] = [
        {"from": "a", "to": "b", "rationale": "b summarizes a's output"},
    ]

    verdict = judge_graph("graph-1", nodes, edges)

    assert verdict["accepted"] is True
    assert verdict["nodes"]["a"]["accepted"] is True
    assert verdict["nodes"]["b"]["accepted"] is True

    from reins.services.task_trail import TaskTrail

    logged = TaskTrail().get_task(verdict["task_id"])
    assert logged is not None
    assert logged["task_type"] == "judge:verdict"
    assert logged["status"] == "success"


def test_judge_rejects_cyclic_graph(trail: TaskTrail, wiki: WikiDB) -> None:
    from reins.harness.judge import judge_graph

    _ = trail, wiki
    nodes: list[RawNode] = [_node("a"), _node("b")]
    edges: list[RawEdge] = [
        {"from": "a", "to": "b", "rationale": "a before b"},
        {"from": "b", "to": "a", "rationale": "b before a"},
    ]

    verdict = judge_graph("graph-cycle", nodes, edges)
    assert verdict["accepted"] is False
    assert verdict["reason"] == "cycle_detected"

    from reins.services.task_trail import TaskTrail

    logged = TaskTrail().get_task(verdict["task_id"])
    assert logged is not None
    assert logged["status"] == "failed"


def test_judge_rejects_unjustified_edge(trail: TaskTrail, wiki: WikiDB) -> None:
    from reins.harness.judge import judge_graph

    _ = trail, wiki
    nodes: list[RawNode] = [_node("a"), _node("b")]
    edges: list[RawEdge] = [{"from": "a", "to": "b", "rationale": ""}]

    verdict = judge_graph("graph-2", nodes, edges)
    assert verdict["accepted"] is False
    assert verdict["reason"] == "unjustified_edge"


def test_judge_rejects_leaf_not_gate_approved(trail: TaskTrail, wiki: WikiDB) -> None:
    from reins.harness.judge import judge_graph

    _ = trail, wiki
    nodes: list[RawNode] = [
        _node("a", context="route_local", tool_name="escalate_cloud")
    ]  # not allowlisted for route_local
    edges: list[RawEdge] = []

    verdict = judge_graph("graph-3", nodes, edges)
    assert verdict["accepted"] is False
    assert verdict["reason"] == "leaf_not_gate_approved"


def test_execute_graph_dispatches_accepted_leaves(
    trail: TaskTrail,
    wiki: WikiDB,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """An accepted graph's leaves are actually dispatched through the gate."""
    from reins.harness import judge

    _ = trail, wiki

    def _fake_route(
        self: ModelRouter,
        category: str,
        prompt: str,
        node: str = "amdy",
        *,
        allow_fallback: bool = True,
    ) -> RouteResult:
        _ = self, category, prompt, allow_fallback
        return RouteResult("ok", "qwen2.5-coder:7b", "ollama", node, ok=True)

    monkeypatch.setattr(ModelRouter, "route", _fake_route)

    nodes: list[RawNode] = [_node("a")]
    edges: list[RawEdge] = []
    outcome = judge.execute_graph("graph-exec-1", nodes, edges)

    assert outcome["judge"]["accepted"] is True
    assert outcome["dispatch"]["a"]["accepted"] is True
    result = outcome["dispatch"]["a"]["result"]
    assert result is not None
    assert result["ok"] is True


def test_execute_graph_skips_dispatch_when_judge_rejects(
    trail: TaskTrail,
    wiki: WikiDB,
) -> None:
    """A rejected graph must never reach dispatch for any node."""
    from reins.harness import judge

    _ = trail, wiki
    nodes: list[RawNode] = [_node("a"), _node("b")]
    edges: list[RawEdge] = [
        {"from": "a", "to": "b", "rationale": "a before b"},
        {"from": "b", "to": "a", "rationale": "b before a"},
    ]
    outcome = judge.execute_graph("graph-exec-cycle", nodes, edges)

    assert outcome["judge"]["accepted"] is False
    assert outcome["dispatch"] == {}


def test_judge_rejects_node_contradicting_wiki_fact(
    trail: TaskTrail,
    wiki: WikiDB,
) -> None:
    from reins.harness.judge import judge_graph

    _ = wiki.add_memory(
        "local_generate has repeatedly failed for category 'deep search' on amdy",
        category="known_failure",
        source="test",
        owner="test",
    )

    _ = trail
    nodes: list[RawNode] = [_node("a", tool_name="local_generate")]
    edges: list[RawEdge] = []

    verdict = judge_graph("graph-4", nodes, edges)
    assert verdict["accepted"] is False
    assert verdict["reason"] == "contradicts_wiki_fact"


def test_judge_rejects_malformed_model_graph_without_raising(
    trail: TaskTrail,
    wiki: WikiDB,
) -> None:
    from reins.harness.judge import execute_graph_json
    from reins.services.task_trail import TaskTrail

    _ = trail, wiki

    outcome = execute_graph_json(
        "graph-malformed",
        '[{"id":"a","action":{"context":"route_local"}}]',
        "[]",
    )
    verdict = outcome["judge"]

    assert verdict["accepted"] is False
    assert verdict["reason"] == "invalid_graph"
    logged = TaskTrail().get_task(verdict["task_id"])
    assert logged is not None
    assert logged["status"] == "failed"
