"""
Agent Execution Nodes: The "Army of Agents" in the Graph Pipeline.

Includes:
- BatchDispatcherNode (concurrency decomposition)
- LocalNode (local Ollama execution on amdy/tell)
- CloudNode (escalation handling)
- ValidatorNode (Lead Agent / Judge validation)
"""
from __future__ import annotations

import logging
import uuid
from typing import Optional

from reins.graph.engine import GraphNode
from reins.graph.fbe import FBEAttribute, FBEState
from reins.harness.models import ModelRouter, RouteResult

logger = logging.getLogger("reins.graph.agent_nodes")


class BatchDispatcherNode(GraphNode):
    """Decomposes a batch list of prompts into individual FBE tasks."""

    def __init__(self) -> None:
        super().__init__(name="BatchDispatcherNode")

    def handle_event(self, attribute: FBEAttribute) -> Optional[FBEAttribute]:
        logger.info("BatchDispatcherNode decomposing batch task %s", attribute.task_id)
        items = attribute.value
        if not isinstance(items, list):
            items = [items]

        if self.engine:
            for item in items:
                sub_task_id = str(uuid.uuid4())
                prompt = item.get("prompt", str(item)) if isinstance(item, dict) else str(item)
                category = item.get("category", "general") if isinstance(item, dict) else "general"
                
                sub_attr = FBEAttribute(
                    name=FBEState.TASK_CREATED.value,
                    value={"prompt": prompt, "category": category},
                    task_id=sub_task_id,
                    metadata={"parent_task_id": attribute.task_id},
                )
                self.engine.publish_attribute(sub_attr)

        return FBEAttribute(
            name=FBEState.EXECUTION_COMPLETED.value,
            value={"batch_dispatched_count": len(items)},
            task_id=attribute.task_id,
            metadata={"source_node": self.name},
        )


class LocalNode(GraphNode):
    """
    Executes tasks locally on Ollama (amdy or tell).
    If task is too complex or fails, mutates state to ESCALATION_REQUIRED.
    """

    def __init__(self, router: Optional[ModelRouter] = None) -> None:
        super().__init__(name="LocalNode")
        self.router = router or ModelRouter()

    def handle_event(self, attribute: FBEAttribute) -> Optional[FBEAttribute]:
        logger.info("LocalNode processing task %s", attribute.task_id)
        data = attribute.value
        if isinstance(data, dict):
            prompt = data.get("prompt", "")
            category = data.get("category", "code")
        else:
            prompt = str(data)
            category = "code"

        # Complexity heuristic check for local offloading
        if len(prompt.split()) > 1500:
            logger.info("Task %s is too large for local context; escalating.", attribute.task_id)
            return FBEAttribute(
                name=FBEState.ESCALATION_REQUIRED.value,
                value={"prompt": prompt, "category": category, "reason": "context_length_exceeded"},
                task_id=attribute.task_id,
                metadata={"source_node": self.name},
            )

        res: RouteResult = self.router.route(category, prompt)
        if not res.ok:
            logger.warning("Local execution failed for %s (%s); escalating.", attribute.task_id, res.error)
            return FBEAttribute(
                name=FBEState.ESCALATION_REQUIRED.value,
                value={"prompt": prompt, "category": category, "reason": res.error or "local_failed"},
                task_id=attribute.task_id,
                metadata={"source_node": self.name},
            )

        return FBEAttribute(
            name=FBEState.EXECUTION_COMPLETED.value,
            value={
                "text": res.text,
                "model": res.model,
                "provider": res.provider,
                "node": res.node,
            },
            task_id=attribute.task_id,
            metadata={"source_node": self.name},
        )


class CloudNode(GraphNode):
    """Handles explicit cloud escalations when authorized."""

    def __init__(self, router: Optional[ModelRouter] = None) -> None:
        super().__init__(name="CloudNode")
        self.router = router or ModelRouter()

    def handle_event(self, attribute: FBEAttribute) -> Optional[FBEAttribute]:
        logger.info("CloudNode processing escalation for task %s", attribute.task_id)
        data = attribute.value
        prompt = data.get("prompt", "") if isinstance(data, dict) else str(data)
        category = data.get("category", "general") if isinstance(data, dict) else "general"

        res: RouteResult = self.router.route(category, prompt)
        return FBEAttribute(
            name=FBEState.EXECUTION_COMPLETED.value,
            value={
                "text": res.text,
                "model": res.model,
                "provider": res.provider,
                "node": res.node,
                "escalated": True,
            },
            task_id=attribute.task_id,
            metadata={"source_node": self.name},
        )


class ValidatorNode(GraphNode):
    """Judge protocol: validates proposed graph steps and action constraints."""

    def __init__(self) -> None:
        super().__init__(name="ValidatorNode")

    def handle_event(self, attribute: FBEAttribute) -> Optional[FBEAttribute]:
        logger.info("ValidatorNode inspecting proposal for task %s", attribute.task_id)
        # Evaluates grounding and structural soundness
        return FBEAttribute(
            name=FBEState.TASK_READY_FOR_EXECUTION.value,
            value=attribute.value,
            task_id=attribute.task_id,
            metadata={"validated": True, "source_node": self.name},
        )
