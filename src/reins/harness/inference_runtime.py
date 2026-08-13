from __future__ import annotations

import hashlib
import json
import logging
from typing import Protocol, final

from pydantic import TypeAdapter, ValidationError

from reins.harness.action_gate import ActionArgs, ActionResult
from reins.harness.inference_protocol import InferenceProtocol
from reins.harness.inference_types import (
    CompiledPromptPackage,
    InferenceExecutionResult,
    PromptOptimizationRequest,
)
from reins.harness.model_types import ModelSpec, RouteResult
from reins.harness.models import ModelRouter
from reins.harness.provider_protocols import parse_json
from reins.services.task_trail import TaskTrail

logger = logging.getLogger(__name__)


class RuntimeRouter(Protocol):
    def optimal(self, category: str, node: str = "amdy") -> ModelSpec: ...

    def route_cloud(self, prompt: str, provider: str | None = None) -> RouteResult: ...

    def route(
        self,
        category: str,
        prompt: str,
        node: str = "amdy",
        *,
        allow_fallback: bool = True,
    ) -> RouteResult: ...


@final
class InferenceRuntime:
    def __init__(
        self,
        *,
        router: RuntimeRouter | None = None,
        trail: TaskTrail | None = None,
    ) -> None:
        self._router: RuntimeRouter = router or ModelRouter()
        self._trail: TaskTrail = trail or TaskTrail()
        self._protocol = InferenceProtocol(
            select_target=self._router.optimal,
            generate_remote=self._router.route_cloud,
            generate_local=self._generate_local,
        )

    def compile_action(self, args: ActionArgs) -> ActionResult:
        source_digest = hashlib.sha256(json.dumps(args, sort_keys=True).encode()).hexdigest()
        task_id = self._trail.create_task(
            "inference:prompt-compile",
            json.dumps({"source_sha256": source_digest}),
            "cloud",
        )
        self._trail.update_task(task_id, "running")
        try:
            request = self._request(args)
            provider = self._required_string(args, "provider")
            if not provider.strip():
                raise ValueError("provider must name an explicit remote provider")
            result = self._protocol.compile(request, provider=provider, authorized=True)
            status = (
                "success_fallback"
                if result.package and result.package.degradation_reason
                else "success"
            )
            if not result.ok:
                status = "failed"
            result = result.model_copy(update={"task_id": task_id})
            package = result.package
            _ = self._trail.upsert_task(
                task_id,
                status=status,
                prompt=json.dumps(
                    {
                        "source_sha256": source_digest,
                        "category": request.category,
                        "node": request.node,
                        "provider": provider,
                        "target_model": package.target_model if package else None,
                        "remote_used": package.remote_used if package else False,
                    },
                    sort_keys=True,
                ),
            )
            return self._action_result(result.model_dump(mode="json"))
        except (ValidationError, ValueError) as exc:
            self._trail.update_task(task_id, "failed")
            return {"ok": False, "package": None, "error": str(exc), "task_id": task_id}
        except Exception as exc:
            logger.exception("remote prompt compilation degraded")
            self._trail.update_task(task_id, "failed")
            return {"ok": False, "package": None, "error": str(exc), "task_id": task_id}

    def execute_action(self, args: ActionArgs) -> ActionResult:
        raw_package = args.get("package_json")
        submitted_digest = hashlib.sha256(str(raw_package).encode()).hexdigest()
        task_id = self._trail.create_task(
            "inference:local-execute",
            json.dumps({"submitted_sha256": submitted_digest}),
            "amdy",
        )
        self._trail.update_task(task_id, "running")
        try:
            package = CompiledPromptPackage.model_validate_json(
                self._required_string(args, "package_json")
            )
            package_digest = hashlib.sha256(package.model_dump_json().encode()).hexdigest()
            result = self._protocol.execute(package).model_copy(update={"task_id": task_id})
            _ = self._trail.upsert_task(
                task_id,
                status="success" if result.ok else "failed",
                target_node=result.node,
                prompt=json.dumps(
                    {
                        "package_sha256": package_digest,
                        "source_sha256": package.source_sha256,
                        "category": package.category,
                        "target_model": package.target_model,
                        "executed_model": result.model,
                    },
                    sort_keys=True,
                ),
            )
            return self._action_result(result.model_dump(mode="json"))
        except (ValidationError, ValueError) as exc:
            self._trail.update_task(task_id, "failed")
            return self._execution_failure(str(exc), task_id, submitted_digest)
        except Exception as exc:
            logger.exception("compiled local inference degraded")
            self._trail.update_task(task_id, "failed")
            return self._execution_failure(str(exc), task_id, submitted_digest)

    def _generate_local(self, category: str, prompt: str, node: str) -> RouteResult:
        return self._router.route(category, prompt, node, allow_fallback=True)

    @staticmethod
    def _request(args: ActionArgs) -> PromptOptimizationRequest:
        constraints = TypeAdapter(tuple[str, ...]).validate_json(
            InferenceRuntime._required_string(args, "constraints_json")
        )
        return PromptOptimizationRequest.model_validate(
            {
                "task": InferenceRuntime._required_string(args, "task"),
                "category": InferenceRuntime._required_string(args, "category"),
                "node": InferenceRuntime._required_string(args, "node"),
                "context": InferenceRuntime._required_string(args, "context"),
                "constraints": constraints,
                "output_format": InferenceRuntime._required_string(args, "output_format"),
                "max_prompt_tokens": InferenceRuntime._required_int(args, "max_prompt_tokens"),
                "mode": InferenceRuntime._required_string(args, "mode"),
            }
        )

    @staticmethod
    def _required_string(args: ActionArgs, key: str) -> str:
        value = args.get(key)
        if isinstance(value, str):
            return value
        raise ValueError(f"{key} must be a string")

    @staticmethod
    def _required_int(args: ActionArgs, key: str) -> int:
        value = args.get(key)
        if isinstance(value, int) and not isinstance(value, bool):
            return value
        raise ValueError(f"{key} must be an integer")

    @staticmethod
    def _action_result(value: object) -> ActionResult:
        parsed = parse_json(value)
        if isinstance(parsed, dict):
            return parsed
        raise TypeError("inference result must be a JSON object")

    @staticmethod
    def _execution_failure(error: str, task_id: str, package_sha256: str) -> ActionResult:
        result = InferenceExecutionResult(
            ok=False,
            text=None,
            model="none",
            provider="none",
            node="amdy",
            error=error,
            package_sha256=package_sha256,
            task_id=task_id,
        )
        return InferenceRuntime._action_result(result.model_dump(mode="json"))
