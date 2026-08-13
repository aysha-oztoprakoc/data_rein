# // MODEL HIERARCHY — data_rein

> 3-tier model hierarchy for the harness router. Built by the Model Hierarchy
> Manager skill from `knowledge_base/HARDWARE.md` (latest `getinfo` scan),
> `config/model_router.json` (provisional cookbook_evaluator scores), and a
> live vault key-presence check. Re-run the skill after any hardware scan,
> `reins local` model add/remove, or vault key change.

**Last built:** 2026-07-04 14:42 UTC
**Hardware scan used:** 2026-07-04 12:31 UTC (`knowledge_base/HARDWARE.md`)

Priorities baked into this ordering: maximize local usage on amdy + tell;
fan Tier 3 out in parallel when a task allows it; permit Tier 1 remote only
through a separate call explicitly authorized by the user.

---

## Tier 0 — Interactive front end (OpenCode + LM Studio)

Not part of `ModelRouter`'s category routing at all — this is the human-driven
layer sitting on top of it. OpenCode (`opencode.json`) is the harness's main
interactive CLI; its default model is **Qwen2.5-Coder-7B-Instruct served by
LM Studio** (OpenAI-compatible endpoint, `127.0.0.1:1234`), just-in-time loaded
so it shares amdy's single 7-8B VRAM slot with Ollama rather than adding a
second permanently-resident model — the same budget constraint Tier 2 already
lives under.

OpenCode reaches the rest of the harness only through the `reins` MCP bridge
(`src/reins/harness/mcp_server.py`, registered in `opencode.json`'s `mcp.reins`):
`wiki_search`/`wiki_get`/`wiki_add_memory` (shared wiki), `trail_list`/
`trail_create`/`trail_update`/`agent_status` (Task Trail), `route_local`
(delegate a menial subtask to a Tier 2/3 Ollama model instead of spending an
agent turn), and `escalate_cloud` — the **only** way OpenCode reaches Tier 1.
`escalate_cloud` is explicit-request-only and always logs a Task Trail entry
(`task_type="opencode:cloud-escalation"`), so an interactive cloud call is
auditable. Ordinary category routing cannot consume `remote_fallback`, and
OpenCode never holds native Anthropic/Gemini credentials.

| Model | Backend | Node | Fits VRAM? |
|---|---|---|---|
| Qwen2.5-Coder-7B-Instruct (Q4_K_M GGUF) | LM Studio | amdy | yes (8GB, JIT-loaded, shares the slot with Ollama) |

---

## Tier 1 — Remote (explicit/heavy work only)

Routed via `ModelRouter._dispatch` (`gemini*` / `claude*` / `gpt*` prefixes).
Never selected automatically by category routing. The public `ModelRouter.route`
API has no cloud override; Tier 1 is reachable only through `route_cloud` or the
gated `escalate_cloud` MCP tool, not `reins run "<category>"`.

| Model | Provider | Vault key | Status |
|---|---|---|---|
| Claude | Anthropic | `ANTHROPIC_API_KEY` | Configured for explicit Tier-1 routing |
| Gemini Pro | Google | `GEMINI_API_KEY` | Configured for explicit Tier-1 routing |
| GPT (OpenAI-compatible) | OpenAI | `OPENAI_API_KEY` | Configured for explicit Tier-1 routing |

The top-level `remote_fallback` array is the configured candidate list consumed
only by `ModelRouter.route_cloud()`. An explicit provider filter is exact: if that
provider is unavailable, routing fails without sending the prompt to a different
vendor. A successful remote hit reports `RouteResult.node == "cloud"` and
`provider` set to the serving vendor.

---

## Tier 2 — Local, high-power (7-8B class)

Reserved for single hard local tasks — coding, deep search, self-optimization.
Not parallelized; each of these saturates a node's VRAM budget on its own.

| Model | Node | Score | Fits VRAM? |
|---|---|---|---|
| qwen2.5-coder:7b | amdy | 90.8 | yes (8GB, live-served) |
| codegemma:7b | amdy | 90.8 | yes (8GB, live-served) |
| llama3.1:8b | amdy | 89.5 | yes (8GB, live-served) |
| bakllava:latest (vision) | amdy | 92.5 | yes (8GB, live-served) |
| llama3.1:8b-instruct-q4_K_M | tell | 89.5 | **unverified — tell offline since last scan** |
| deepseek-r1:8b | tell | 89.5 | **unverified — tell offline since last scan** |
| deepseek-r1:7b | tell | 90.8 | **unverified — tell offline since last scan** |
| minicpm-v:8b (vision) | tell | 89.5 | **unverified — tell offline since last scan** |

## Tier 3 — Local, low-power (parallel fan-out)

Cheap and fast enough to run several in parallel for batch/RAG/prompt-opt
work. All currently live only on tell's intended model set (`tools/pull_models_tell.sh`) — none are on amdy's 8GB budget.

| Model | Node | Score | Fits VRAM? |
|---|---|---|---|
| deepseek-r1:1.5b | tell | 98.0 | **unverified — tell offline since last scan** |
| smollm2:1.7b | tell | 97.8 | **unverified — tell offline since last scan** |
| gemma2:2b | tell | 97.4 | **unverified — tell offline since last scan** |
| qwen2.5:3b | tell | 96.1 | **unverified — tell offline since last scan** |
| qwen2.5-coder:3b | tell | 96.1 | **unverified — tell offline since last scan** |
| moondream:1.8b (vision) | tell | 97.6 | **unverified — tell offline since last scan** |

---

## Current live inventory (ground truth, `reins local status`)

- **amdy:** server UP (127.0.0.1:11434), 4 models served — all Tier 2:
  `llama3.1:8b`, `qwen2.5-coder:7b`, `codegemma:7b`, `bakllava:latest`.
- **tell:** UNREACHABLE at last scan. Every tell row above (all of Tier 3,
  plus half of Tier 2) is the *intended* fleet per `model_router.json` /
  `tools/pull_models_tell.sh`, not a confirmed-installed fact. Re-run
  `getinfo` once tell is back online before trusting those rows.

## Fleet inventory

The live `reins local status` and `config/model_registry.json` determine installed
and hardware-admitted models. Rows for unreachable nodes are intended candidates,
not fleet-size claims; re-run `getinfo` before admitting them.
