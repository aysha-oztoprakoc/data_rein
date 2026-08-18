from __future__ import annotations

import time
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from reins.graph.agent_nodes import BatchDispatcherNode, CloudNode, LocalNode, ValidatorNode
from reins.graph.context_node import ContextBuilderNode
from reins.graph.engine import GraphNode, PONGraphEngine
from reins.graph.extraction_node import ExtractionNode
from reins.graph.fbe import FBEAttribute, FBEState, LoopBudget, LoopBudgetExceededError
from reins.graph.ingestion_node import IngestionNode
from reins.graph.training_node import QLoRANode, TrainingThresholdNode
from reins.harness.model_types import RouteResult
from reins.harness.wiki import WikiDB


def test_fbe_attribute_serialization() -> None:
    attr = FBEAttribute(
        name=FBEState.TASK_CREATED.value,
        value={"prompt": "test prompt"},
        task_id="task-001",
        metadata={"user": "amdy"},
    )
    json_str = attr.to_json()
    deserialized = FBEAttribute.from_json(json_str)

    assert deserialized.name == FBEState.TASK_CREATED.value
    assert deserialized.task_id == "task-001"
    assert deserialized.value == {"prompt": "test prompt"}
    assert deserialized.metadata["user"] == "amdy"


def test_loop_budget_prevents_infinite_cycling() -> None:
    budget = LoopBudget(max_iterations=3)
    task_id = "task-infinite"

    assert budget.record_step(task_id) == 1
    assert budget.record_step(task_id) == 2
    assert budget.record_step(task_id) == 3

    with pytest.raises(LoopBudgetExceededError):
        budget.record_step(task_id)


def test_extraction_and_ingestion_nodes(tmp_path: Path) -> None:
    db_path = tmp_path / "wiki.db"
    sample_file = tmp_path / "test_doc.md"
    sample_file.write_text("# Graph Architecture\nKnowledge extraction via PON.", encoding="utf-8")

    extraction_node = ExtractionNode()
    extract_event = FBEAttribute(
        name="trigger",
        value={"file_path": str(sample_file), "category": "architecture"},
        task_id="task-extract-1",
    )
    res_extract = extraction_node.handle_event(extract_event)
    assert res_extract is not None
    assert res_extract.name == FBEState.RAW_DATA_AVAILABLE.value

    with WikiDB(db_path) as db:
        ingestion_node = IngestionNode(wiki_db=db)
        res_ingest = ingestion_node.handle_event(res_extract)
        assert res_ingest is not None
        assert res_ingest.name == FBEState.TASK_CREATED.value
        assert "slug" in res_ingest.value


def test_context_builder_node(tmp_path: Path) -> None:
    db_path = tmp_path / "wiki.db"
    with WikiDB(db_path) as db:
        db.upsert_page(title="Graph Note", content="Kuzu and PON are central.", is_chunked=True)
        context_node = ContextBuilderNode(wiki_db=db)

        task_attr = FBEAttribute(
            name=FBEState.TASK_CREATED.value,
            value={"prompt": "Explain Graph Note architecture", "rag": True},
            task_id="task-ctx-1",
        )
        res = context_node.handle_event(task_attr)
        assert res is not None
        assert res.name == FBEState.TASK_READY_FOR_EXECUTION.value
        assert "prompt" in res.value


def test_local_and_cloud_nodes() -> None:
    mock_router = MagicMock()
    mock_router.route.return_value = RouteResult(
        text="Execution completed successfully",
        model="qwen2.5-coder:1.5b",
        provider="ollama",
        node="amdy",
        ok=True,
    )

    local_node = LocalNode(router=mock_router)
    attr = FBEAttribute(
        name=FBEState.TASK_READY_FOR_EXECUTION.value,
        value={"prompt": "Write a quick test", "category": "code"},
        task_id="task-exec-1",
    )
    res = local_node.handle_event(attr)
    assert res is not None
    assert res.name == FBEState.EXECUTION_COMPLETED.value
    assert res.value["text"] == "Execution completed successfully"


def test_training_threshold_node(tmp_path: Path) -> None:
    db_path = tmp_path / "wiki.db"
    with WikiDB(db_path) as db:
        db.add_memory("Memory 1")
        db.add_memory("Memory 2")

        threshold_node = TrainingThresholdNode(threshold=2, wiki_db=db)
        attr = FBEAttribute(name=FBEState.TASK_CREATED.value, value={}, task_id="task-train-1")
        res = threshold_node.handle_event(attr)
        assert res is not None
        assert res.name == FBEState.TRAINING_REQUIRED.value
