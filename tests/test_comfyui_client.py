from __future__ import annotations

import asyncio
import json
from collections.abc import AsyncIterator

import pytest

from reins.harness.comfyui_client import ComfyUIClient


async def event_stream(*events: dict[str, object]) -> AsyncIterator[str]:
    for event in events:
        yield json.dumps(event)


def test_wait_for_result_reacts_to_matching_completion(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given websocket events for another job followed by this job's completion.
    client = ComfyUIClient()
    expected = {"outputs": {"9": {"images": [{"filename": "result.png"}]}}}
    history_calls: list[str] = []

    async def get_history(prompt_id: str) -> dict[str, object]:
        history_calls.append(prompt_id)
        return expected

    monkeypatch.setattr(client, "get_history", get_history)
    events = event_stream(
        {"type": "executing", "data": {"prompt_id": "other", "node": None}},
        {"type": "executing", "data": {"prompt_id": "job-1", "node": None}},
    )

    # When the client blocks on the event stream.
    result = asyncio.run(client.wait_for_result("job-1", events, timeout=1.0))
    asyncio.run(client.close())

    # Then it fetches history exactly once after the matching notification.
    assert result == expected
    assert history_calls == ["job-1"]


def test_wait_for_result_degrades_on_execution_error() -> None:
    # Given a matching ComfyUI error notification.
    client = ComfyUIClient()
    events = event_stream(
        {
            "type": "execution_error",
            "data": {"prompt_id": "job-2", "exception_message": "out of memory"},
        }
    )

    # When the client receives the error fact.
    result = asyncio.run(client.wait_for_result("job-2", events, timeout=1.0))
    asyncio.run(client.close())

    # Then it returns the public degradation value.
    assert result is None
