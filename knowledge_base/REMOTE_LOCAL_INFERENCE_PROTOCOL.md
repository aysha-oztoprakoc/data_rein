# Remote-to-Local Inference Protocol

## Purpose

`data-rein.remote-local-inference/1` uses a named remote model to compile selected
tasks into a bounded prompt package, then executes that package on the local model
plane. The remote model is a prompt compiler, never an execution authority.

The protocol complements the local-only `reins optimize` shortcut. It does not
change ordinary `ModelRouter.route` behavior and never introduces automatic cloud
fallback.

## Two Phases

1. `compile_prompt_remote` consumes explicit cloud authorization, selects the local
   target profile through `ModelRouter.optimal`, and sends one structured compiler
   envelope through `route_cloud` to the requested provider.
2. `run_prompt_local` validates the returned `CompiledPromptPackage` and sends only
   its prompt to `ModelRouter.route`. This phase has no remote-generation callable.

Keeping the phases separate lets the caller inspect, persist, reject, or edit the
task before local execution without granting the remote compiler another effect.

Target eligibility is capability-based: the selected provider must advertise the
`local_text` execution plane. Provider names do not grant eligibility. This allows
an injected non-Ollama local text backend while excluding cloud-text and image
providers from local package execution.

## Eligibility

The request mode controls remote compilation:

| Mode | Behavior |
|---|---|
| `auto` | Compile remotely when the category is complex, the task plus context is at least about 512 tokens, or two or more constraints are present. |
| `required` | Compile remotely for this request. Explicit authorization is still mandatory. |
| `bypass` | Build the deterministic local package without a remote call. |

Complex categories are `coding: complex`, `data processing`, `deep search`,
`prompt optimization`, and `self-optimization`.

## Compiler Contract

The remote compiler receives a JSON envelope with:

- protocol and operation identifiers;
- the original task, category, context, constraints, and desired output;
- the hardware-admitted target model, power tier, node, and token ceiling;
- the exact allowed output shape.

The response must contain only `system_prompt`, `task_prompt`, `context_prompt`,
and one or more `success_criteria`. Pydantic rejects extra fields, so remote output
cannot replace the category, node, model, provider, authorization, or protocol.

## Budget And Integrity

The caller chooses `max_prompt_tokens` from 128 through 16,384; the default is
4,096. The harness uses the deterministic ceiling estimate `ceil(characters / 4)`.
Every package carries this estimate, and the local phase recomputes it before
execution. A forged estimate or over-budget prompt is rejected.

The essential task, constraints, and output-format sections must fit the requested
budget before compilation begins. Only optional context may be truncated; the
protocol rejects an impossible budget instead of silently cutting task intent.

The estimate is a portable safety ceiling, not provider billing telemetry or an
exact tokenizer result.

## Degradation

One remote generation attempt is made. It is never retried automatically. A failed,
malformed, or over-budget remote result becomes a deterministic bounded package:

- the task and constraints are preserved;
- output format is preserved;
- excess tail context is truncated with an explicit marker;
- `remote_used=false` and `degradation_reason` explain the path.

Both phases are action-gated and Task-Trail-logged. Trail records contain prompt
hashes and routing metadata rather than raw prompt text.

## MCP Example

Call `compile_prompt_remote` with the task fields, a named provider such as
`claude`, `gemini`, or `openai`, and `constraints_json` as a JSON array. Inspect the
returned `package`, serialize that object as JSON, then pass it to
`run_prompt_local` as `package_json`.
