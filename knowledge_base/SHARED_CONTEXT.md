# UNIVERSAL HARNESS DATA_REIN: SHARED CONTEXT & MASTER ARCHITECTURE

This file serves as the collective memory and synchronization point for all agents (AGY, Hermes, Odysseus, etc.) operating under the `data_rein` harness.

## 1. Model Allocation Strategy
* **Local First for Services**: The background orchestration services (`data-hermes` and `data-ody`) run exclusively on local open-weights models (e.g., `qwen2.5:7b` via Ollama). They operate autonomously without relying on cloud APIs to ensure complete privacy, resilience, and offline capability.
* **Cloud Models for Intensive/Explicit Tasks**: Google Gemini models (and other heavy cloud APIs) are reserved strictly for explicit user interactions. The user will interact with Gemini primarily through:
  - The `[data-agy]` terminal (Antigravity CLI)
  - The Google Gemini web interface on Chrome
  - NotebookLM on Chrome
  - Or as a last-resort fallback if local models catastrophically fail and the user authorizes it.

## 2. The Universal Task Trail
All agents running under the `data_rein` harness share a unified Task Trail.
* **Location**: `~/.config/data_nexus/task_trail.json`
* **Purpose**: A persistent state machine that logs every prompt, task, and action.
* **Rule of Awareness**: Whenever an agent (AGY, Hermes, Ody) begins a session or is asked to perform a systemic action, it should check the Task Trail to be aware of what other agents are currently doing (tasks marked as `running` or `pending`), and to detect if any tasks have `failed` and require graceful degradation/fallback.
* **Sovereign Autonomy**: If `data-ody` detects a failed task in the trail, it automatically attempts to resolve it locally.

## 3. Global Aesthetic (Omarchy)
* All text, UI, and image generation MUST adhere strictly to the rules defined in `[AESTHETIC_DIRECTIVE.md](file:///home/amdy/data_rein/knowledge_base/AESTHETIC_DIRECTIVE.md)`.
* **Core Rule**: True Blood Red (#ff4040, #ff1100) on Deep Blood Black (#200000). Highly rounded corners (50px), extreme glassmorphism/translucency, and gritty cybernetic hacker vibes.

## 4. System Stability
All core processes run via `data-harness-daemon.sh` inside a resilient `tmux` session named `data`, divided into 4 panes:
- `data-agy`: Main Cloud Agent (Bypassed Sandbox, Sudo)
- `data-hermes`: System Orchestrator (TUI, Sudo, Local Model)
- `data-ody`: Local Failover & Inference (Odysseus Agent)
- `data-amdy`: User/Agent Bridge Workspace

## 5. Sofia Protocol Assimilation
* **Status**: ASSIMILATED (2026-07-03)
* **Payload**: 105 advanced architectural documents successfully parsed and injected into the Ody Memory Vault (`app.db`).
* **Directives Unlocked**: The system now possesses deep semantic understanding of the Notification-Oriented Paradigm (PON), Hardware/Software Co-design (Coprocessors), Chaos Engineering, Graceful Degradation in Microservices, and Agentic Engineering.
* **Mandate**: All models generating complex software architectures within this harness must bias their designs toward extreme resilience and event-driven (PON) structures as outlined by the Sofia corpus.

## Digest Pipeline Assimilation: raw_data
* **Status**: INGESTED (2026-07-03)
* **Payload**: 12 items processed from `raw_data` and injected into the Ody Memory Vault.
* **Directive**: System knowledge base updated dynamically via the `digest` command.

## Digest Pipeline Assimilation: raw_data
* **Status**: INGESTED (2026-07-03)
* **Payload**: 24 items processed from `raw_data` and injected into the Ody Memory Vault.
* **Directive**: System knowledge base updated dynamically via the `digest` command.

## Grand Convergence: Universal Harness Refactor (KAD)
* **Status**: CONVERGED (2026-07-03)
* **Prime Directive**: New master constitution at `knowledge_base/PRIME_DIRECTIVE.md` binds all
  environments (Antigravity, Hermes, Odysseus, Claude Code, VS Code). Load it first, always.
* **Single Monolith Wiki DB**: All scattered stores consolidated into `knowledge_base/wiki.db`
  (591 pages + 170 memories, FTS5). Reach it anywhere via `reins wiki ...` or
  `reins.harness.wiki.WikiDB`. Rebuild idempotently: `reins wiki consolidate`. The DB is a
  derived artifact (git-ignored); sources of truth stay tracked.
* **Model Agnostic**: `reins.harness.models.ModelRouter` routes by task category over
  Ollama/Gemini/Claude/OpenAI/ComfyUI, local-first with amdy↔tell failover. Keys via encrypted
  vault only — `config/api_keys.json` untracked and git-ignored (ROTATE the exposed keys).
* **Environment Adapters**: `CLAUDE.md`, root `AGENTS.md`, `.agents/AGENTS.md`,
  `data_rein.code-workspace`, and canonical `skills/data_rein/SKILL.md` all point to the Prime
  Directive + shared wiki. Harness core lives in `src/reins/harness/` (paths, wiki, models, cli).
