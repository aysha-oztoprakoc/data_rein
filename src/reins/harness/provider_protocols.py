from __future__ import annotations

from contextlib import AbstractAsyncContextManager
from importlib import import_module
from collections.abc import AsyncIterator
from typing import Protocol, cast, runtime_checkable

from reins.harness.model_types import RouteResult

JsonScalar = None | bool | int | float | str
JsonValue = JsonScalar | list["JsonValue"] | dict[str, "JsonValue"]
HistoryEntry = dict[str, JsonValue]


def parse_json(value: object) -> JsonValue:
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, list):
        return [parse_json(item) for item in cast(list[object], value)]
    if isinstance(value, dict):
        mapping = cast(dict[object, object], value)
        if not all(isinstance(key, str) for key in mapping):
            raise TypeError("JSON object contains a non-string key")
        return {cast(str, key): parse_json(item) for key, item in mapping.items()}
    raise TypeError(f"non-JSON value: {type(value).__name__}")


class GeminiUsage(Protocol):
    prompt_token_count: int
    candidates_token_count: int


class GeminiResponse(Protocol):
    usage_metadata: GeminiUsage | None
    text: str | None


class GeminiModel(Protocol):
    def generate_content(self, prompt: str) -> GeminiResponse: ...


@runtime_checkable
class GeminiModule(Protocol):
    def configure(self, *, api_key: str) -> None: ...
    def GenerativeModel(self, model: str) -> GeminiModel: ...


class ClaudeUsage(Protocol):
    input_tokens: int
    output_tokens: int


class ClaudeBlock(Protocol):
    type: str
    text: str


class ClaudeMessage(Protocol):
    usage: ClaudeUsage | None
    content: list[ClaudeBlock]


class ClaudeMessages(Protocol):
    def create(
        self, *, model: str, max_tokens: int, messages: list[dict[str, str]]
    ) -> ClaudeMessage: ...


class ClaudeClient(Protocol):
    messages: ClaudeMessages


@runtime_checkable
class ClaudeModule(Protocol):
    def Anthropic(self, *, api_key: str) -> ClaudeClient: ...


class OpenAIUsage(Protocol):
    prompt_tokens: int
    completion_tokens: int


class OpenAIMessage(Protocol):
    content: str | None


class OpenAIChoice(Protocol):
    message: OpenAIMessage


class OpenAIResponse(Protocol):
    usage: OpenAIUsage | None
    choices: list[OpenAIChoice]


class OpenAICompletions(Protocol):
    def create(self, *, model: str, messages: list[dict[str, str]]) -> OpenAIResponse: ...


class OpenAIChat(Protocol):
    completions: OpenAICompletions


class OpenAIClient(Protocol):
    chat: OpenAIChat


@runtime_checkable
class OpenAIModule(Protocol):
    def OpenAI(self, *, api_key: str) -> OpenAIClient: ...


@runtime_checkable
class LocalModule(Protocol):
    def ensure_server(self) -> bool: ...
    def generate(self, model: str, prompt: str) -> str: ...


@runtime_checkable
class Coordinator(Protocol):
    def generate(self, model: str, prompt: str) -> RouteResult | None: ...


@runtime_checkable
class CoordinatorModule(Protocol):
    def get_coordinator(self) -> Coordinator: ...


class ComfyUIClientContract(Protocol):
    async def close(self) -> None: ...
    async def check_health(self) -> bool: ...
    async def queue_prompt(
        self, prompt: dict[str, JsonValue], client_id: str | None = None
    ) -> str | None: ...
    def execution_events(
        self,
        client_id: str,
    ) -> AbstractAsyncContextManager[AsyncIterator[str]]: ...
    async def wait_for_result(
        self, prompt_id: str, events: AsyncIterator[str]
    ) -> HistoryEntry | None: ...


class ComfyUIClientFactory(Protocol):
    def __call__(self, base_url: str = "http://127.0.0.1:8188") -> ComfyUIClientContract: ...


@runtime_checkable
class ComfyUIModule(Protocol):
    ComfyUIClient: ComfyUIClientFactory

    def build_txt2img_workflow(self, prompt: str) -> dict[str, JsonValue]: ...


def load_gemini() -> GeminiModule:
    module = import_module("google.generativeai")
    if not isinstance(module, GeminiModule):
        raise TypeError("google.generativeai has an incompatible interface")
    return module


def load_claude() -> ClaudeModule:
    module = import_module("anthropic")
    if not isinstance(module, ClaudeModule):
        raise TypeError("anthropic has an incompatible interface")
    return module


def load_openai() -> OpenAIModule:
    module = import_module("openai")
    if not isinstance(module, OpenAIModule):
        raise TypeError("openai has an incompatible interface")
    return module


def load_local() -> LocalModule:
    module = import_module("reins.harness.local")
    if not isinstance(module, LocalModule):
        raise TypeError("local model module has an incompatible interface")
    return module


def load_coordinator() -> CoordinatorModule:
    module = import_module("reins.harness.coordinator")
    if not isinstance(module, CoordinatorModule):
        raise TypeError("coordinator module has an incompatible interface")
    return module


def load_comfyui() -> ComfyUIModule:
    module = import_module("reins.harness.comfyui_client")
    if not isinstance(module, ComfyUIModule):
        raise TypeError("ComfyUI module has an incompatible interface")
    return module
