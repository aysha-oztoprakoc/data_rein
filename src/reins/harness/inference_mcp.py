from __future__ import annotations

import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from reins.harness.action_gate import ActionArgs, gate_call
from reins.harness.inference_runtime import InferenceRuntime

_runtime_factory: Callable[[], InferenceRuntime] = InferenceRuntime


def compile_prompt_remote(
    task: str,
    category: str,
    provider: str,
    context: str = "",
    constraints_json: str = "[]",
    output_format: str = "",
    max_prompt_tokens: int = 4_096,
    mode: str = "auto",
    node: str = "amdy",
) -> str:
    """Explicitly compile an eligible prompt with one named remote provider for local use."""
    args: ActionArgs = {
        "task": task,
        "category": category,
        "provider": provider,
        "context": context,
        "constraints_json": constraints_json,
        "output_format": output_format,
        "max_prompt_tokens": max_prompt_tokens,
        "mode": mode,
        "node": node,
    }
    runtime = _runtime_factory()
    gated = gate_call(
        "compile_prompt_remote",
        "remote_prompt_compile",
        args,
        runtime.compile_action,
        authorized=True,
    )
    if not gated["accepted"]:
        return json.dumps(
            {"ok": False, "package": None, "error": gated["reason"], "task_id": None}
        )
    return json.dumps(gated["result"])


def run_prompt_local(package_json: str) -> str:
    """Validate and execute one compiled prompt package on the local model plane only."""
    args: ActionArgs = {"package_json": package_json}
    runtime = _runtime_factory()
    gated = gate_call(
        "run_prompt_local",
        "compiled_local_generate",
        args,
        runtime.execute_action,
    )
    if not gated["accepted"]:
        return json.dumps(
            {"ok": False, "text": None, "error": gated["reason"], "task_id": None}
        )
    return json.dumps(gated["result"])


def register_inference_tools(server: FastMCP) -> None:
    _ = server.tool()(compile_prompt_remote)
    _ = server.tool()(run_prompt_local)
