"""
Agent-as-a-Judge framework, per `blueprint.yaml`'s `agent_as_a_judge` section:
the Lead Agent evaluates a hierarchical dependency graph proposed by a lesser
model before any of its leaf actions proceed to action_gate dispatch. Each
check maps to a KAD persona (tulpas/KAD/):

* ARCHIMEDES         - decomposition validity (each leaf action must already
                        clear the action_gate, i.e. it targets a real,
                        allowlisted, schema-valid tool call).
* SOCRATES_PROTOCOL   - interrogative validation (every edge must carry a
                        non-empty rationale, or it is cut as unjustified).
* SOFIA_PROTOCOL      - knowledge grounding (a leaf action must not contradict
                        a recorded `known_failure` fact in the shared wiki).

The verdict (accept/reject per node, and overall) is always trail-logged
before any accepted node proceeds (GD-3: honest failure, not silent).
"""

from __future__ import annotations

import json
from typing import ClassVar, TypeAlias, TypedDict

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, ValidationError

from reins.harness.action_gate import ActionArgs, GateResult, gate_call, gate_validate
from reins.harness.dispatch import TOOL_DISPATCHERS
from reins.harness.wiki import WikiDB
from reins.services.task_trail import TaskTrail


class ActionProposal(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    context: str
    tool_name: str
    args: ActionArgs


class GraphNode(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    id: str
    action: ActionProposal


class GraphEdge(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(
        frozen=True,
        populate_by_name=True,
        extra="forbid",
    )

    from_node: str = Field(alias="from")
    to_node: str = Field(alias="to")
    rationale: str


class GraphProposal(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    nodes: list[GraphNode]
    edges: list[GraphEdge]


class NodeVerdict(TypedDict):
    accepted: bool


class JudgeVerdict(TypedDict):
    accepted: bool
    reason: str | None
    nodes: dict[str, NodeVerdict]
    task_id: str


class ExecutionOutcome(TypedDict):
    judge: JudgeVerdict
    dispatch: dict[str, GateResult]


class VerdictPayload(TypedDict, total=False):
    reason: str
    node: str
    nodes: dict[str, NodeVerdict]


RawAction: TypeAlias = dict[str, ActionArgs | str]
RawNode: TypeAlias = dict[str, RawAction | str]
RawEdge: TypeAlias = dict[str, str]

_NODE_ADAPTER = TypeAdapter(list[GraphNode])
_EDGE_ADAPTER = TypeAdapter(list[GraphEdge])


def _parse_graph(nodes: list[RawNode], edges: list[RawEdge]) -> GraphProposal:
    return GraphProposal.model_validate({"nodes": nodes, "edges": edges})


def _has_cycle(node_ids: set[str], edges: list[GraphEdge]) -> bool:
    graph: dict[str, list[str]] = {n: [] for n in node_ids}
    for edge in edges:
        graph.setdefault(edge.from_node, []).append(edge.to_node)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}

    def _visit(n: str) -> bool:
        color[n] = GRAY
        for neighbor in graph.get(n, []):
            if color.get(neighbor, WHITE) == GRAY:
                return True
            if color.get(neighbor, WHITE) == WHITE and _visit(neighbor):
                return True
        color[n] = BLACK
        return False

    return any(color[n] == WHITE and _visit(n) for n in graph)


def _socrates_check(edges: list[GraphEdge]) -> bool:
    """Every edge must carry a non-empty rationale, or it is unjustified."""
    return all(edge.rationale.strip() for edge in edges)


def _archimedes_check(action: ActionProposal) -> bool:
    """A leaf action must already clear the action_gate (validate-only, no dispatch)."""
    result = gate_validate(action.context, action.tool_name, action.args)
    return result["accepted"]


def _sofia_check(tool_name: str) -> bool:
    """A leaf action must not contradict a recorded `known_failure` fact."""
    with WikiDB() as db:
        memories = db.search_memories(tool_name, limit=10)
    return not any(m["category"] == "known_failure" for m in memories)


def _log_verdict(graph_id: str, accepted: bool, payload: VerdictPayload) -> str:
    trail = TaskTrail()
    task_id = trail.create_task("judge:verdict", json.dumps({"graph_id": graph_id, **payload}), graph_id)
    trail.update_task(task_id, "success" if accepted else "failed")
    return task_id


def _invalid_verdict(graph_id: str) -> JudgeVerdict:
    task_id = _log_verdict(graph_id, False, {"reason": "invalid_graph"})
    return {"accepted": False, "reason": "invalid_graph", "nodes": {}, "task_id": task_id}


def _judge_proposal(graph_id: str, proposal: GraphProposal) -> JudgeVerdict:
    node_ids = {node.id for node in proposal.nodes}

    if _has_cycle(node_ids, proposal.edges):
        task_id = _log_verdict(graph_id, False, {"reason": "cycle_detected"})
        return {"accepted": False, "reason": "cycle_detected", "nodes": {}, "task_id": task_id}

    if not _socrates_check(proposal.edges):
        task_id = _log_verdict(graph_id, False, {"reason": "unjustified_edge"})
        return {"accepted": False, "reason": "unjustified_edge", "nodes": {}, "task_id": task_id}

    node_verdicts: dict[str, NodeVerdict] = {}
    for node in proposal.nodes:
        action = node.action
        if not _archimedes_check(action):
            task_id = _log_verdict(graph_id, False, {"reason": "leaf_not_gate_approved", "node": node.id})
            return {"accepted": False, "reason": "leaf_not_gate_approved", "nodes": {}, "task_id": task_id}
        if not _sofia_check(action.tool_name):
            task_id = _log_verdict(graph_id, False, {"reason": "contradicts_wiki_fact", "node": node.id})
            return {"accepted": False, "reason": "contradicts_wiki_fact", "nodes": {}, "task_id": task_id}
        node_verdicts[node.id] = {"accepted": True}

    task_id = _log_verdict(graph_id, True, {"nodes": node_verdicts})
    return {"accepted": True, "reason": None, "nodes": node_verdicts, "task_id": task_id}


def judge_graph(graph_id: str, nodes: list[RawNode], edges: list[RawEdge]) -> JudgeVerdict:
    try:
        proposal = _parse_graph(nodes, edges)
    except ValidationError:
        return _invalid_verdict(graph_id)
    return _judge_proposal(graph_id, proposal)


def _execute_proposal(graph_id: str, proposal: GraphProposal) -> ExecutionOutcome:
    verdict = _judge_proposal(graph_id, proposal)
    if not verdict["accepted"]:
        return {"judge": verdict, "dispatch": {}}

    dispatch_results: dict[str, GateResult] = {}
    for node in proposal.nodes:
        action = node.action
        dispatch_fn = TOOL_DISPATCHERS[action.tool_name]
        dispatch_results[node.id] = gate_call(
            action.context, action.tool_name, action.args, dispatch_fn, authorized=True
        )
    return {"judge": verdict, "dispatch": dispatch_results}


def execute_graph(graph_id: str, nodes: list[RawNode], edges: list[RawEdge]) -> ExecutionOutcome:
    try:
        proposal = _parse_graph(nodes, edges)
    except ValidationError:
        return {"judge": _invalid_verdict(graph_id), "dispatch": {}}
    return _execute_proposal(graph_id, proposal)


def execute_graph_json(graph_id: str, nodes: str, edges: str) -> ExecutionOutcome:
    try:
        proposal = GraphProposal(
            nodes=_NODE_ADAPTER.validate_json(nodes),
            edges=_EDGE_ADAPTER.validate_json(edges),
        )
    except ValidationError:
        return {"judge": _invalid_verdict(graph_id), "dispatch": {}}
    return _execute_proposal(graph_id, proposal)
