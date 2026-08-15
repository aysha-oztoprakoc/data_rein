from __future__ import annotations

import hashlib
import json
import logging
import time
from collections.abc import Mapping
from dataclasses import dataclass, replace
from pathlib import Path
from typing import ClassVar, assert_never

from pydantic import ValidationError

from reins.harness import paths
from reins.harness.model_inventory import ModelInventory
from reins.harness.model_providers import ProviderHandler, ProviderRuntime
from reins.harness.model_types import DEFAULT_PROVIDER_CAPABILITIES, ExecutionPlane, ModelEntry, ModelSpec, RouteResult, RouterConfig
from reins.harness.combo_registry import ComboRegistry
from reins.harness.resilience import BreakerRegistry, with_retry
from reins.harness.resilience_types import BreakerState

logger = logging.getLogger(__name__)


def _record_breaker_transition(name: str, old_state: BreakerState, new_state: BreakerState) -> None:
    log = logger.warning if new_state is BreakerState.OPEN else logger.info
    log("model circuit %s changed from %s to %s", name, old_state.value, new_state.value)
    try:
        from reins.services.task_trail import TaskTrail

        digest = hashlib.sha256(name.encode()).hexdigest()[:16]
        status = {
            BreakerState.OPEN: "failed",
            BreakerState.HALF_OPEN: "running",
            BreakerState.CLOSED: "success",
        }[new_state]
        _ = TaskTrail().upsert_task(
            f"breaker-{digest}",
            task_type="breaker:transition",
            prompt=json.dumps({"circuit": name, "from": old_state.value, "to": new_state.value}),
            target_node="resilience",
            status=status,
            breaker_state=new_state.value,
        )
    except Exception:
        logger.warning("model circuit transition was not persisted", exc_info=True)


_DEFAULT_BREAKERS = BreakerRegistry(on_transition=_record_breaker_transition)
@dataclass(frozen=True, slots=True)
class _RouteRequest:
    plane: ExecutionPlane
    prompt: str
    category: str = ""
    node: str = "amdy"
    allow_fallback: bool = False
    provider: str | None = None


def _get_secret(name: str) -> str | None:
    try:
        from scripts.get_secrets import get_secret  # type: ignore[import-not-found]

        value = get_secret(name)
        if value:
            return value
    except Exception:
        logger.warning("vault lookup failed for %s", name, exc_info=True)
    return None


class ModelRouter:
    FALLBACK_MODEL: ClassVar[str] = "llama3.1:8b"

    def __init__(
        self,
        router_path: Path | None = None,
        *,
        breaker_registry: BreakerRegistry | None = None,
        model_inventory: ModelInventory | None = None,
        provider_handlers: dict[str, ProviderHandler] | None = None,
        provider_capabilities: Mapping[str, frozenset[ExecutionPlane]] | None = None,
    ) -> None:
        self.router_path: Path = router_path or paths.model_router()
        self.breaker_registry: BreakerRegistry = breaker_registry or _DEFAULT_BREAKERS
        self.model_inventory: ModelInventory = model_inventory or ModelInventory()
        self.table: dict[str, dict[str, list[dict[str, str | int | float | bool | None]]]] = {}
        self.remote_fallback: list[ModelSpec] = []
        self._last_usage: dict[str, int] | None = None
        self._runtime: ProviderRuntime = ProviderRuntime(_get_secret)
        self._combo_registry: ComboRegistry = ComboRegistry()
        self._omni_mode: bool = bool(self._combo_registry.config.combos)
        self._rate_limited: dict[str, float] = {}
        self.provider_handlers: dict[str, ProviderHandler] = (
            provider_handlers or self._default_provider_handlers()
        )
        self.provider_capabilities: Mapping[str, frozenset[ExecutionPlane]] = (
            provider_capabilities or DEFAULT_PROVIDER_CAPABILITIES
        )
        self._load()

    def _default_provider_handlers(self) -> dict[str, ProviderHandler]:
        return {
            "ollama": lambda model, prompt, node: self._ollama(model, prompt, node),
            "comfyui": lambda model, prompt, node: self._comfyui(model, prompt, node),
            "gemini": lambda model, prompt, _node: self._gemini(model, prompt),
            "claude": lambda model, prompt, _node: self._claude(model, prompt),
            "anthropic": lambda model, prompt, _node: self._claude(model, prompt),
            "openai": lambda model, prompt, _node: self._openai(model, prompt),
            "deepseek": lambda model, prompt, _node: self._deepseek(model, prompt),
            "xai": lambda model, prompt, _node: self._xai(model, prompt),
            "moonshot": lambda model, prompt, _node: self._moonshot(model, prompt),
            "zhipu": lambda model, prompt, _node: self._zhipu(model, prompt),
            "openrouter": lambda model, prompt, _node: self._openrouter(model, prompt),
        }

    def _load(self) -> None:
        try:
            config = RouterConfig.model_validate_json(self.router_path.read_text(encoding="utf-8"))
            self.table = {
                category: {
                    node: [entry.model_dump() for entry in routes.for_node(node)]
                    for node in ("amdy", "tell")
                }
                for category, routes in config.categories.items()
            }
            self.remote_fallback = [ModelSpec.from_entry(entry) for entry in config.remote_fallback]
        except (OSError, ValidationError):
            logger.warning("model router configuration failed to load", exc_info=True)
            self.table = {}
            self.remote_fallback = []

    def candidates(self, category: str, node: str = "amdy") -> list[ModelSpec]:
        category_entry = self.table.get(category) or self.table.get(category.lower()) or {}
        raw_entries = category_entry.get(node, [])
        specs = [ModelSpec.from_entry(ModelEntry.model_validate(entry)) for entry in raw_entries]
        if not specs:
            specs = [ModelSpec(model=self.FALLBACK_MODEL)]
        if node == "amdy":
            specs.extend(self._extra_local_candidates(specs))
        admitted = [
            spec
            for spec in specs
            if spec.resolved_provider != "ollama" or self.model_inventory.admit(node, spec.model)
        ]
        return [
            replace(
                spec,
                capabilities=self.provider_capabilities.get(spec.resolved_provider, frozenset()),
            )
            for spec in admitted
        ]

    def _extra_local_candidates(self, known: list[ModelSpec]) -> list[ModelSpec]:
        try:
            from reins.harness import local

            known_names = {spec.model for spec in known}
            return [
                ModelSpec(model=name, score=1.0, power="unknown")
                for name in local.list_models()
                if name not in known_names
            ]
        except Exception:
            logger.warning("installed model discovery failed", exc_info=True)
            return []

    def optimal(self, category: str, node: str = "amdy") -> ModelSpec:
        candidates = self.candidates(category, node)
        return candidates[0] if candidates else ModelSpec(model="none")

    def route(
        self, category: str, prompt: str, node: str = "amdy", *, allow_fallback: bool = True
    ) -> RouteResult:
        return self._execute_request(
            _RouteRequest(ExecutionPlane.LOCAL_TEXT, prompt, category, node, allow_fallback)
        )

    def route_cloud(self, prompt: str, provider: str | None = None) -> RouteResult:
        return self._execute_request(
            _RouteRequest(ExecutionPlane.CLOUD_TEXT, prompt, node="cloud", provider=provider)
        )

    def generate_image(self, category: str, prompt: str, node: str = "amdy") -> RouteResult:
        return self._execute_request(_RouteRequest(ExecutionPlane.IMAGE, prompt, category, node))

    def _execute_request(self, request: _RouteRequest) -> RouteResult:
        tried: list[tuple[str, str, str]] = []
        specs = self._policy_candidates(request)
        for spec in specs:
            if request.plane not in spec.capabilities:
                if (
                    request.plane is ExecutionPlane.LOCAL_TEXT
                    and ExecutionPlane.CLOUD_TEXT in spec.capabilities
                ):
                    tried.append(
                        (request.node, spec.model, "cloud provider requires explicit route_cloud authorization")
                    )
                continue
            provider = spec.resolved_provider
            text, error = self._dispatch(provider, spec.model, request.prompt, request.node, spec)
            if text is not None:
                return RouteResult(text, spec.model, provider, request.node, ok=True, combo_id=str(spec.extra.get("combo_id", "")))
            tried.append((request.node, spec.model, error or "empty"))
        if request.plane is ExecutionPlane.LOCAL_TEXT and request.allow_fallback:
            other = "tell" if request.node == "amdy" else "amdy"
            fallback = self._execute_request(replace(request, node=other, allow_fallback=False))
            if fallback.ok:
                return fallback
            tried.append((other, fallback.model, fallback.error or "empty"))
            
            # Explicitly log a failed local task to trigger the Odysseus fallback daemon
            try:
                from reins.services.task_trail import TaskTrail
                
                digest = hashlib.sha256(request.prompt.encode()).hexdigest()[:16]
                TaskTrail().upsert_task(
                    f"local-fail-{digest}", 
                    task_type="local:failed", 
                    prompt=request.prompt, 
                    status="failed"
                )
            except Exception as e:
                logger.warning(f"Could not record local failure to TaskTrail: {e}")

        provider, default = self._failure_policy(request)
        return self._failure(request.node, tried, provider, default)

    def _policy_candidates(self, request: _RouteRequest) -> list[ModelSpec]:
        if self._omni_mode:
            return self._omni_candidates(request)
        match request.plane:
            case ExecutionPlane.LOCAL_TEXT | ExecutionPlane.IMAGE:
                return self.candidates(request.category, request.node)
            case ExecutionPlane.CLOUD_TEXT:
                specs = [
                    replace(
                        spec,
                        capabilities=self.provider_capabilities.get(spec.resolved_provider, frozenset()),
                    )
                    for spec in self.remote_fallback
                ]
                if request.provider:
                    return [spec for spec in specs if spec.resolved_provider == request.provider.lower()]
                return specs
            case unreachable:
                assert_never(unreachable)

    def _omni_candidates(self, request: _RouteRequest) -> list[ModelSpec]:
        match request.plane:
            case ExecutionPlane.LOCAL_TEXT | ExecutionPlane.IMAGE:
                combos = self._combo_registry.combos_for_category(request.category, request.node)
                specs = [self._combo_registry.combo_to_spec(c) for c in combos]
                if not specs:
                    specs = [ModelSpec(model=self.FALLBACK_MODEL)]
            case ExecutionPlane.CLOUD_TEXT:
                if request.provider:
                    combos = [c for c in self._combo_registry.cloud_fallback_combos() 
                              if c.provider == request.provider.lower()]
                else:
                    combos = self._combo_registry.cloud_fallback_combos()
                specs = [self._combo_registry.combo_to_spec(c) for c in combos]
            case unreachable:
                assert_never(unreachable)
        
        now = time.monotonic()
        specs = [s for s in specs if now > self._rate_limited.get(str(s.extra.get("combo_id", "")), 0)]
        return [
            replace(
                spec,
                capabilities=self.provider_capabilities.get(spec.resolved_provider, frozenset()),
            )
            for spec in specs
        ]

    @staticmethod
    def _failure_policy(request: _RouteRequest) -> tuple[str, str]:
        match request.plane:
            case ExecutionPlane.LOCAL_TEXT:
                return "none", ""
            case ExecutionPlane.CLOUD_TEXT:
                return request.provider or "none", "no remote_fallback configured"
            case ExecutionPlane.IMAGE:
                return "comfyui", f"no image candidates for {request.category!r}"
            case unreachable:
                assert_never(unreachable)

    @staticmethod
    def _failure(
        node: str, tried: list[tuple[str, str, str]], provider: str = "none", default: str = ""
    ) -> RouteResult:
        error = "; ".join(f"{item_node}/{model}: {reason}" for item_node, model, reason in tried)
        return RouteResult(None, tried[-1][1] if tried else "none", provider, node, False, error or default)

    def _dispatch(self, provider: str, model: str, prompt: str, node: str, spec: ModelSpec | None = None) -> tuple[str | None, str | None]:
        if spec and spec.extra.get("combo_id"):
            secret_key = str(spec.extra.get("secret_key", ""))
            base_url = str(spec.extra.get("base_url", ""))
            if provider in ("deepseek", "xai", "moonshot", "zhipu", "openrouter") and secret_key:
                default_urls = {
                    "deepseek": "https://api.deepseek.com",
                    "xai": "https://api.x.ai/v1",
                    "moonshot": "https://api.moonshot.cn/v1",
                    "zhipu": "https://open.bigmodel.cn/api/paas/v4",
                    "openrouter": "https://openrouter.ai/api/v1",
                }
                handler = lambda m, p, n, prov=provider, k=secret_key, bu=base_url: self._runtime.openai_compat(
                    m, p, n, base_url=bu or default_urls.get(prov, ""), secret_name=k
                )
            elif provider in ("openai",) and secret_key:
                handler = lambda m, p, n, k=secret_key, bu=base_url: self._runtime.openai_compat(
                    m, p, n, base_url=bu or "https://api.openai.com/v1", secret_name=k
                )
            else:
                handler = self.provider_handlers.get(provider)
        else:
            handler = self.provider_handlers.get(provider)

        if handler is None:
            return None, f"unknown provider {provider}"

        def invoke() -> str:
            self._last_usage = None
            self._runtime.last_usage = None
            text = handler(model, prompt, node)
            self._last_usage = self._last_usage or self._runtime.last_usage
            if text is None:
                raise RuntimeError("provider returned an empty response")
            if provider not in {"ollama", "comfyui"}:
                combo_id = str(spec.extra.get("combo_id", "")) if spec else ""
                self._record_usage(provider, model, self._last_usage, combo_id)
            return text

        try:
            breaker = self.breaker_registry.get(f"{provider}:{node}:{model}")
            return with_retry(invoke, breaker=breaker, idempotent=False), None
        except Exception as error:
            error_str = str(error).lower()
            if "429" in error_str or "rate limit" in error_str or "quota" in error_str:
                combo_id = str(spec.extra.get("combo_id", "")) if spec else ""
                if combo_id:
                    self._rate_limited[combo_id] = time.monotonic() + 300
            logger.warning("model provider dispatch degraded", exc_info=True)
            return None, str(error)

    def _record_usage(self, provider: str, model: str, usage: dict[str, int] | None, combo_id: str = "") -> None:
        if not usage:
            return
        try:
            from reins.services.token_ledger import TokenLedger

            TokenLedger().record(provider, model, usage.get("input_tokens", 0), usage.get("output_tokens", 0))
        except Exception:
            logger.warning("token usage not recorded for %s/%s", provider, model, exc_info=True)

    def _comfyui(self, model: str, prompt: str, node: str) -> str | None:
        return self._runtime.comfyui(model, prompt, node)

    def _ollama(self, model: str, prompt: str, node: str) -> str | None:
        return self._runtime.ollama(model, prompt, node)

    def _gemini(self, model: str, prompt: str) -> str | None:
        return self._runtime.gemini(model, prompt, "cloud")

    def _claude(self, model: str, prompt: str) -> str | None:
        return self._runtime.claude(model, prompt, "cloud")

    def _openai(self, model: str, prompt: str) -> str | None:
        return self._runtime.openai(model, prompt, "cloud")

    def _deepseek(self, model: str, prompt: str) -> str | None:
        return self._runtime.openai_compat(
            model, prompt, "cloud",
            base_url="https://api.deepseek.com",
            secret_name="DEEPSEEK_API_KEY",
        )

    def _xai(self, model: str, prompt: str) -> str | None:
        return self._runtime.openai_compat(
            model, prompt, "cloud",
            base_url="https://api.x.ai/v1",
            secret_name="XAI_API_KEY",
        )

    def _moonshot(self, model: str, prompt: str) -> str | None:
        return self._runtime.openai_compat(
            model, prompt, "cloud",
            base_url="https://api.moonshot.cn/v1",
            secret_name="MOONSHOT_API_KEY",
        )

    def _zhipu(self, model: str, prompt: str) -> str | None:
        return self._runtime.openai_compat(
            model, prompt, "cloud",
            base_url="https://open.bigmodel.cn/api/paas/v4",
            secret_name="ZHIPU_API_KEY",
        )

    def _openrouter(self, model: str, prompt: str) -> str | None:
        return self._runtime.openai_compat(
            model, prompt, "cloud",
            base_url="https://openrouter.ai/api/v1",
            secret_name="OPENROUTER_API_KEY",
        )
