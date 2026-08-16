# MISSION: Deterministic Execution Blueprint
**Role**: Principal Orchestration Agent (data-arquimedes)
**Constraint**: 5-hour local execution window. Context limits are strict. You must be token-economical.

## DIRECTIVES FOR THE AGENT
1. **Chunking**: Do not read entire directories at once. Use `ls`, `grep`, or `ast-bro` (if available) to map file structures first, then read only the highly relevant files.
2. **Context Management**: At the end of every phase, output a highly condensed summary of your findings to the terminal, and explicitly instruct the user: *"Phase X complete. Please run `/compact` before I proceed to Phase Y."*
3. **Self-Tracking**: Update this `ORCHESTRATION_GOAL.md` file by changing `[ ]` to `[x]` as you complete phases. 

## EXECUTION PHASES

### [x] Phase 1: Meta-Harness Assimilation
- **Target**: `/home/amdy/data_rein/`
- **Action**: Map the directory. Identify and read the files containing the "10 rules" and "first principles".
- **Output**: Append a bulleted summary of the core rules to the bottom of this document.
- **Checkpoint**: Halt and request `/compact`.

### [x] Phase 2: Project Digestion
- **Target**: `/home/amdy/data-workspace/`
- **Action**: Map the project structure. Focus on the CLI element, GUI element (opencode), and the `odysseus ai/omnigent/ohmyagents` integrations.
- **Output**: Append a brief architectural summary to this document.
- **Checkpoint**: Halt and request `/compact`.

### [x] Phase 3: Hardware & Local Model Boundaries
- **Action**: Draft the `local_model_rules` section of the blueprint.
- **Requirements**: Two-node cluster, per `knowledge_base/HARDWARE.md` (single source of
  truth — do not hand-edit, re-run `getinfo`/`SysProfiler` scan to refresh):
  - **amdy** (main workstation, online) — 8.0GB VRAM (AMD RX 9060 XT), 14.7GB RAM,
    Ryzen 7 7700 (8c/8t). Primary execution node; budget law lives in
    `config/coordinator.json` (`vram_budget_gb: 7.2`).
  - **tell** (server, currently being built — last scan: UNREACHABLE) — 6.0GB VRAM
    (last-known, NVIDIA Pascal-class), 16.0GB RAM, Intel Core i5 7th-gen (4c/4t).
    Treat as a lesser/failover node until it comes online and a fresh scan confirms specs.
  Define llama.cpp KV cache optimization and layer offloading strategies sized to
  amdy's 8GB budget as the primary target, with a degraded/smaller-model path for tell's
  6GB once it's reachable — based on your Phase 1/2 learnings.
- **Output**: Write the draft to `blueprint.yaml`.

### [x] Phase 4: Execution Rails & Action Gates
- **Action**: Draft the `action_gates` section for remote/lesser models. 
- **Requirements**: Lesser models must NOT execute tool calls directly. Design deterministic validation checks to capture and sanitize their probabilistic outputs.
- **Output**: Append to `blueprint.yaml`.

### [x] Phase 5: Agent-as-a-Judge Framework
- **Action**: Draft the `agent_as_a_judge` section.
- **Requirements**: Define the framework where Claude Opus (or the Lead Agent) evaluates the hierarchical dependencies proposed by lesser models, mapping them cleanly back to the concepts defined in the `tulpas` directory.
- **Output**: Finalize `blueprint.yaml` and print the final success message.

---

## Phase 1 Output — Core Rules Summary (2026-07-06)

Canonical law text: `/home/amdy/data-workspace/docs/TEN_LAWS.md` (supersedes
the old "3 Laws" in `knowledge_base/PRIME_DIRECTIVE.md`). Full state snapshot:
`/home/amdy/data_rein/10_RULES_STATE.md`.

- **PON-1** Zero polling — waits end via blocking I/O / callbacks / notified facts, never `while`/`sleep` spins (AST-enforced).
- **PON-2** Decoupling by facts — injected seams and published facts, no reach-through into collaborators' internals.
- **PON-3** Polynomial cost — incremental fact evaluation; no full-state rescans.
- **GD-1** Universal breaker — every external I/O call behind a circuit breaker; state changes are notified facts.
- **GD-2** Disciplined retry — backoff+jitter, idempotent ops only, never while the breaker is Open; billable calls never auto-retry.
- **GD-3** Honest failure — every degradation leaves a diagnostic trace; silent `except: pass` forbidden.
- **TDD-1** Test precedence — Red test defines the contract before implementation.
- **TDD-2** Mandatory refactor — Green is not done; dedup under the passing-test net.
- **TDD-3** Quality gate — `ruff check && pytest -q` must exit 0; hermetic, millisecond-fast suite.
- **NIX-1** Configuration determinism — lockfile-pinned env, declarative devShell, drift fails a test.

Harness contract: *Sync first · one wiki · any model · zero polling · degrade,
never crash · stay on-brand.*

## Phase 2 Output — data-workspace Architecture Summary (2026-07-07)

Source: `/home/amdy/data-workspace/docs/ARCHITECTURE.md` + `src/data_workspace/`.

- **CLI element**: entry point `data` (`pyproject.toml [project.scripts]` →
  `data_workspace.cli:main`). OpenCode terminal shell wired via
  `src/data_workspace/shells/opencode.py` + `opencode.json`, which points its
  MCP server at `reins.harness.mcp_server` and loads the
  `.opencode/plugin/data-awareness.js` plugin for session→trail bookkeeping.
- **GUI element (Odysseus)**: `src/data_workspace/shells/gui.py` — the web
  dashboard, extended with Omnigent mgmt panels (sessions, budgets, model
  matrix) and a Living Wiki view. Talks to the Core only via MCP-over-HTTP
  (`odysseus/integrations/reins/mcp_client.py`), zero direct filesystem access.
- **Supervisor (Omnigent)**: meta-harness process supervision — spawns/resumes
  both shells, session registry, exposed via `sys_session_*` / `sys_terminal_*`
  MCP tools; local footprint at `.omo/` and the `OhMyAgents_macos-arm64.dmg`
  bundle in this repo's root.
- **Orchestrator Selector / Hybrid Execution**: session-start model choice
  (ChatGPT/Claude/Gemini/Grok/Deepseek/local) backed by `ModelRouter`
  (`src/reins/harness/models.py`) + `config/model_router.json`
  `remote_fallback` tiers. Remote orchestrators call local models as
  agents/subagents via the `route_local` (never cloud) / `escalate_cloud`
  (explicit, trail-logged) MCP tools in `src/reins/harness/mcp_server.py`.
- **Core mold (`data_rein`)**: single `wiki.db` (pages + memories, FTS5) and
  Task Trail as global state; Skill Registry symlink installer
  (`skills/MANIFEST.md`, `scripts/install_skills.sh`); Memory Pipeline
  (extract → enrich → ingest into `wiki.db`); Cookbook
  (`src/reins/services/sys_profiler.py` — hardware scan → benchmark →
  recommend); Resilience core (`src/data_workspace/resilience.py`) wrapping
  every external I/O chokepoint in circuit breaker + disciplined retry.

**Checkpoint reached.** Directive 2 calls for a `/compact` halt here before
Phase 3.

### [x] Phase 6: Codebase Pruning & Tech Debt Eradication
- **Target**: `data_rein` & `odysseus` test suite
- **Action**: Removed 25MB of leaked root binary artifacts, purged `scripts/legacy`, and migrated legacy `unittest.TestCase` files to native `pytest`.
- **Output**: See `CLEANUP_PLAN.md` and updated `10_RULES_STATE.md`.

### [x] Phase 7: Training Pipeline & Friction Optimization
- **Target**: `src/reins/training/` and `src/reins/harness/`
- **Action**: Optimized data pipeline memory scaling by streaming cursor iteration, hardened QLoRA degradation to explicitly empty VRAM cache before retry, and enabled multithreaded dataset tokenization.
- **Output**: Improved OOM resilience and faster dataset extraction. See `training_pipeline_optimization.md`.
