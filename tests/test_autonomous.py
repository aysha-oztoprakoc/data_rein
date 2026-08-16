from __future__ import annotations

from unittest.mock import MagicMock

from reins.harness.autonomous import AutonomousWorkflow
from reins.harness.model_types import ModelSpec, RouteResult


def test_autonomous_workflow_is_complex_detection():
    wf = AutonomousWorkflow(router=MagicMock())
    assert wf._is_complex("word " * 1600) is True
    assert wf._is_complex("Please refactor and architect this whole system") is True
    assert wf._is_complex("Simple summary please") is False


def test_autonomous_workflow_adapt_prompt():
    wf = AutonomousWorkflow(router=MagicMock())
    low_prompt = wf._adapt_prompt("Do task", "low")
    assert "limited context" in low_prompt
    assert "Do task" in low_prompt

    med_prompt = wf._adapt_prompt("Do task", "medium")
    assert "concise and direct" in med_prompt
    assert "Do task" in med_prompt

    normal_prompt = wf._adapt_prompt("Do task", "high")
    assert normal_prompt == "Do task"


def test_autonomous_workflow_is_stuck_detection():
    wf = AutonomousWorkflow(router=MagicMock())
    assert wf._is_stuck(RouteResult(ok=False, text="", model="m", provider="p", node="n")) is True
    assert wf._is_stuck(RouteResult(ok=True, text="too short", model="m", provider="p", node="n")) is True
    assert wf._is_stuck(RouteResult(ok=True, text="I cannot do this task because I am an AI", model="m", provider="p", node="n")) is True
    assert wf._is_stuck(RouteResult(ok=True, text="Here is the complete solution implementing the requested feature cleanly.", model="m", provider="p", node="n")) is False


def test_autonomous_workflow_execute_routes_complex_to_cloud():
    mock_router = MagicMock()
    mock_router.route_cloud.return_value = RouteResult(ok=True, text="Cloud result", model="cloud", provider="gemini", node="cloud")
    wf = AutonomousWorkflow(router=mock_router)

    result = wf.execute("general", "Please refactor and architect this huge planning task")
    assert result.ok is True
    assert result.text == "Cloud result"
    mock_router.route_cloud.assert_called_once()


def test_autonomous_workflow_execute_local_success():
    mock_router = MagicMock()
    mock_router.optimal.return_value = ModelSpec(model="qwen2.5:7b", provider="ollama", power="high")
    mock_router.route.return_value = RouteResult(ok=True, text="Valid local answer that is long enough.", model="qwen2.5:7b", provider="ollama", node="amdy")
    wf = AutonomousWorkflow(router=mock_router)

    result = wf.execute("general", "Simple task", "amdy")
    assert result.ok is True
    assert "Valid local answer" in result.text
