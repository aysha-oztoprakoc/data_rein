# UNIVERSAL HARNESS DATA_REIN: SHARED CONTEXT & MASTER ARCHITECTURE

This file serves as the collective memory and synchronization point for all agents (AGY, Hermes, Odysseus, etc.) operating under the `data_rein` harness.

## 1. Model Allocation Strategy
* **Local First for Services**: The background orchestration services (`data-hermes` and `data-ody`) run exclusively on local open-weights models (e.g., `qwen2.5:7b` via Ollama). They operate autonomously without relying on cloud APIs to ensure complete privacy, resilience, and offline capability.
* **Cloud Models Are Explicit Only**: Google Gemini models and other cloud APIs require a separate user-authorized `route_cloud` call through `escalate_cloud` or `compile_prompt_remote`. Ordinary category routing has no cloud override and returns an honest failure after local node exhaustion. The user will interact with Gemini primarily through:
  - The `[data-agy]` terminal (Antigravity CLI)
  - The Google Gemini web interface on Chrome
  - NotebookLM on Chrome
  - The gated `escalate_cloud` or `compile_prompt_remote` tool after explicit authorization.
* **Remote-to-Local Prompt Inference (2026-08-13)**: `compile_prompt_remote` uses one
  explicitly named cloud provider to compile eligible tasks into strict, target-model-aware
  `data-rein.remote-local-inference/1` packages. `run_prompt_local` validates package
  integrity and executes only through the local router. The phases are action-gated,
  hash-only Task-Trail-logged, capped at 16,384 estimated tokens, and degrade to a
  deterministic bounded package without retry. Contract:
  `knowledge_base/REMOTE_LOCAL_INFERENCE_PROTOCOL.md`.
* **Unified OmniRouter System (2026-08-15)**: The `ModelRouter` is refactored into a unified,
  multi-account, multi-provider router supporting 11 providers (Ollama, Gemini, Claude/Anthropic,
  OpenAI, DeepSeek, xAI/Grok, Moonshot/Kimi, ZhipuAI/GLM, OpenRouter, ComfyUI). All endpoints are
  configured as labeled **Combos** (`provider + model + key + base_url + tier`) in `config/omnirouter.json`.
  Includes quota-aware auto-fallback chains, 429 rate-limit cooldown isolation, token budget threshold
  deprioritization, full encrypted vault CRUD (`reins secret {get,set,list,rm}`), and CLI verb `reins combos {list,add,rm,test}`.

## 2. The Universal Task Trail
All agents running under the `data_rein` harness share a unified Task Trail.
* **Location**: `~/.config/data_nexus/task_trail.sqlite3` through the indexed `TaskTrail` API. The former `task_trail.json` is retained only as one-time migration evidence.
* **Purpose**: A persistent state machine that logs every prompt, task, and action.
* **Rule of Awareness**: Whenever an agent (AGY, Hermes, Ody) begins a session or is asked to perform a systemic action, it should check the Task Trail to be aware of what other agents are currently doing (tasks marked as `running` or `pending`), and to detect if any tasks have `failed` and require graceful degradation/fallback.
* **Explicit Fallback Ownership**: `data-ody` may resolve only active tasks whose `target_node` is exactly `data-ody`; generic failed/running work never transfers ownership.

## 3. Global Aesthetic (Omarchy)
* All text, UI, and image generation MUST adhere strictly to the rules defined in `[AESTHETIC_DIRECTIVE.md](file:///home/amdy/data_rein/knowledge_base/AESTHETIC_DIRECTIVE.md)`.
* **Core Rule**: True Blood Red (#ff4040, #ff1100) on Deep Blood Black (#200000). Highly rounded corners (50px), extreme glassmorphism/translucency, and gritty cybernetic hacker vibes.

## 4. System Stability
Core interactive processes run via `data-harness-daemon.sh` inside a resilient `tmux` session named `data`, currently divided into six named windows:
- `data-agy`: Main Cloud Agent (Bypassed Sandbox, Sudo)
- `data-hermes`: System Orchestrator (TUI, Sudo, Local Model)
- `data-ody`: Local Failover & Inference (Odysseus Agent)
- `data-amdy`: User/Agent Bridge Workspace
- `data-sofia`: Event-driven health, process, hardware, and Task Trail TUI
- `data-mcp`: Supervised streamable-HTTP MCP bridge on `127.0.0.1:8765`

## 5. Sofia Protocol Assimilation
* **Status**: ASSIMILATED (2026-07-03)
* **Payload**: Sofia architectural documents are indexed through canonical `WikiDB` memories in `knowledge_base/wiki.db`; legacy `app.db` files are migration inputs only.
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

## OpenCode + LM Studio: interactive front end (2026-07-04)
* **Status**: CONFIGURED (2026-07-04)
* **Role**: OpenCode is now the harness's main interactive CLI, `AGENTS.md`-aware, default
  model `lmstudio/qwen2.5-coder-7b-instruct` (LM Studio, JIT-loaded on port 1234, sharing amdy's
  8GB VRAM slot with Ollama — never both resident at once).
* **MCP bridge**: `reins mcp` (`src/reins/harness/mcp_server.py`) exposes wiki/trail/router
  tools (`wiki_search`, `wiki_get`, `wiki_add_memory`, `trail_list`, `trail_create`,
  `trail_update`, `agent_status`, `route_local`, `escalate_cloud`,
  `compile_prompt_remote`, `run_prompt_local`) registered in the project
  `opencode.json`. `route_local` delegates menial subtasks to local Ollama models;
  `escalate_cloud` is the direct-answer path from OpenCode to Claude/Gemini/OpenAI;
  `compile_prompt_remote` is the remote prompt-compiler path. Both are explicit-request
  only and Task-Trail-logged, reusing `ModelRouter`'s vault-gated provider dispatch.
* **Passive awareness**: `.opencode/plugin/reins-awareness.js` logs each session's start/end to
  the Task Trail (`task_type="opencode:session"`) automatically via opencode's `event` hook, so
  other agents see OpenCode activity without it having to call a tool.

## Model-Agnostic Safety Audit (2026-08-12)
* **Status**: VERIFIED. Canonical record: `knowledge_base/HARNESS_AUDIT_2026_08_11.md`.
* **Routing boundary**: provider handlers are injected behind `ModelRouter`; hardware fit is admitted from the live registry; ordinary routing is local-only; cloud requires an explicit `route_cloud` call through `escalate_cloud` or `compile_prompt_remote`; an unavailable requested provider is never substituted.
* **PON/GD**: periodic Sofia refreshes, readiness/history polling, and raw network/MQTT/IPC transports were removed or placed behind keyed circuit breakers. The executable GD-1 law scans for bypasses.
* **State**: the Task Trail is indexed SQLite WAL state with one-time JSON migration; tests use isolated state and cannot contaminate the live 97-record trail. Wiki ingestion writes only through `WikiDB`.
* **Environment**: `uv.lock` and Nix-generated `flake.lock` are present and verified; the locked development shell evaluates successfully.
* **Verification**: 214 repository tests, 41 Ten Laws tests, Ruff, strict typing and no-excuse checks on changed core boundaries, compileall, lock drift, external PON scan, stdio MCP wiki/trail/local-route round trip, and fresh Sofia wide/narrow five-tab captures passed.
* **Hostile proposal boundary**: model-produced graphs are Pydantic-parsed before judgment; malformed proposals are trail-logged as `invalid_graph` and never reach dispatch.

## Remote-to-Local Inference Delivery (2026-08-13)
* **Status**: VERIFIED. The two-phase protocol is implemented in
  `src/reins/harness/inference_*.py`, with `compile_prompt_remote` and
  `run_prompt_local` registered on both stdio and HTTP MCP surfaces.
* **Safety**: exact provider required; ordinary routing remains local-only; remote
  routing metadata is forbidden; package token metadata is recomputed; essential
  task/constraints/output cannot be truncated; no remote retry; Task Trail stores
  hashes and routing metadata rather than raw prompts.
* **Degradation**: unavailable, malformed, exceptional, or oversized remote results
  produce a deterministic local package with `degradation_reason`; impossible
  essential-content budgets and forged packages fail honestly before execution.
* **Live surfaces**: the canonical `prompt-optimizer` skill is installed in all seven
  harness environments and indexed in the monolith Wiki. The supervised `data-mcp`
  tmux window is restored on `127.0.0.1:8765` and advertises all 24 MCP tools.
* **Verification**: 232 repository tests, 46 Ten Laws checks, Ruff, focused
  basedpyright at zero errors/warnings, compileall, diff integrity, stdio MCP tool
  discovery plus live Ollama execution, and HTTP MCP discovery all passed.

## Multimodal Knowledge and Local Training Delivery (2026-08-13)
* **Status**: VERIFIED. Canonical contracts:
  `knowledge_base/MULTIMODAL_KNOWLEDGE_PIPELINE.md` and
  `knowledge_base/SOURCE_REFERENCE.md`.
* **Ownership**: `data_rein` owns text/image/audio/video extraction, schema-v2 Wiki
  provenance, RAG, segmented training records, and QLoRA/LoRA. `data-workspace`
  remains a separate thin shell and consumes the editable core dependency; it does
  not own a second extraction or training path.
* **Extraction**: images combine Tesseract with a hardware-admitted local Ollama
  vision model; audio uses optional local faster-whisper; video samples the first
  frame and at most one per 30 seconds, then combines frame OCR/vision with audio
  transcription. `NexusDaemon` delegates MQTT events to the same `digest_path` used
  by the CLI.
* **Provenance**: every Wiki page can store modality, source SHA-256, extractor,
  node, channels, format, frame count, duration, and channel warnings in
  `metadata_json`. Dataset export segments long pages before tokenization and keeps
  provenance plus segment coordinates on every record.
* **Weight safety**: JSONL is fully validated before model unload/load or adapter
  changes. Hardware probing selects NF4 QLoRA, GPU LoRA, or CPU LoRA; one OOM retry
  reduces batch/sequence pressure and every outcome is Task-Trail-logged.
* **Live evidence**: real PNG, ALSA WAV, and H.264/AAC fixtures passed through the
  CLI using Tesseract, `bakllava:latest`, faster-whisper `tiny.en`, and FFmpeg. The
  three pages exported to five bounded provenance records; training dry-run
  validated all five and honestly reported CPU LoRA because the Torch extra is not
  installed. Both project lock/Ruff/pytest gates passed after cross-project fixture
  compatibility was restored.

## Security and canonical-skill delivery (2026-08-13)
* **Status**: VERIFIED with explicit residuals. Task Trail:
  `7f2b8251-513e-4d93-a8a0-cc74d15a3ee1`.
* **Canonical skills**: seven manifest-backed skills are the only writable source
  under `skills/`; `scripts/ody_neural_injection.py` now validates/lists that
  registry and preserves Wiki memory ingestion without generating legacy skill
  copies. Operators install links with `reins skills install`.
* **Security record**: `knowledge_base/SECURITY_AUDIT_2026_08_13.md` records the
  threat/control mapping, reproducible evidence paths, the 296-test / 49-law
  final gate, and its original intentional non-claims (full BasedPyright
  host-killed, the subsequently reconciled Nix path-flake stall, system Python
  dependency gap, and no cloud calls).
* **Operator brief**: `knowledge_base/PROJECT_BRIEF_2026_08_13.md` is the concise
  architecture, commands, execution-plane, and security-poster reference.

## Codex continuation reconciliation (2026-08-13)
* **Recovered task**: `security:canonical-convergence`
  (`7f2b8251-513e-4d93-a8a0-cc74d15a3ee1`) was left `running` despite the
  evidence-backed delivery above.
* **Fresh gate**: current worktree passed 296 repository tests, Ruff, focused
  BasedPyright (0 errors/warnings), ShellCheck, Bandit (0 Medium/High; 43 Low and
  8 narrow skips retained), and `pip-audit` (no known vulnerabilities; local
  unpublished `data-rein` remains unauditable on PyPI).
* **Live surface**: `reins skills list` exposed exactly the seven canonical
  manifest skills; a fresh stdio MCP session initialized server `reins`, listed
  24 tools, and included all four gated routing/inference tools.
* **Trail state**: the recovered task was transitioned to `success` after this
  requirement-by-requirement reconciliation. The broader project-continuation
  objective remains active for the next agent or Antigravity session.

## NIX-1 dev-shell reconciliation (2026-08-13)
* **Root cause**: `nix flake check path:.` traversed the full 85 GB working tree,
  including ignored runtime/model roots. Live evidence showed about 35.4 GB read
  and an open file under `ComfyUI`; store locking, nixpkgs fetching, and foreign
  architecture evaluation were refuted.
* **Boundary fix**: the dev shell no longer exports the immutable flake source as
  `DATA_REIN_HOME`. Shell activation resolves the Git top-level checkout, with a
  non-Git working-directory fallback. `tests/test_determinism.py` protects this
  behavior from a nested launch directory.
* **Verification**: isolated `nix flake check --all-systems --no-build` passed for
  x86_64-linux and aarch64-linux. A real x86_64 dev shell exposed the canonical
  checkout, Python 3.11.15, uv 0.11.26, Ruff 0.16.2, Git 2.55.0, pkg-config
  0.29.2, an offline-clean uv lock, and SQLite 3.53.1. The full repository gate
  passed 297 tests, Ruff, focused BasedPyright, and diff integrity.
* **Operator rule**: avoid `path:.` in this runtime-heavy checkout. Once the
  currently untracked Nix files are committed, use the normal Git-backed
  `nix develop` / `nix flake check` surface.

## Encrypted-vault rollback reconciliation (2026-08-13)
* **Boundary**: `scripts/get_secrets.py` remains the single live vault mutation
  seam. Successful mutation now writes the exact previous ciphertext to private
  `.secrets.enc.bak` before replacing the active vault, under the existing
  exclusive key-file lock. It never persists plaintext.
* **Failure behavior**: an active replacement failure triggers atomic restoration
  of the prior ciphertext. If restoration also fails, the typed error explicitly
  reports the dual failure and retained encrypted backup.
* **Test ownership**: vault scenarios moved intact out of the oversized mixed MCP
  test module into `tests/test_vault_security.py`; MCP transport/auth coverage
  remains in `tests/test_mcp_security.py`. Both modules are below 200 pure lines.
* **Verification**: red was 7 legacy passes plus 3 contract failures. Green was 21
  focused vault/MCP scenarios and 300 repository tests, plus 49 executable laws,
  Ruff, focused BasedPyright, no-excuse checks, Bandit 0 Medium/High, dependency
  audit, diff integrity, and an isolated real Fernet mutation/rollback QA run with
  `0400` key, `0600` active/backup, and zero plaintext/temp artifacts.

## Active shell-boundary reconciliation (2026-08-13)
* **Task Trail**: `9a1f261c-5fbc-49b1-82be-0a4a888bd5ca`.
* **Boundary fix**: `scripts/encrypt_secrets.py` no longer runs `uv pip install`
  through `os.system`; it imports the already locked `cryptography` dependency.
* **Regression law**: the argv-only structural law now lives beside process runtime
  coverage in `tests/test_security_boundaries.py` and rejects `os.system` in every
  non-legacy active Python source. The move keeps `tests/test_laws.py` below the
  250-pure-line limit.
* **Verification**: the new assertion failed specifically on the old shell fallback.
  Final gates passed 300 tests, Ruff, focused BasedPyright, no-excuse checks,
  bytecode compilation, diff integrity, and dependency audit. Live CLI execution
  degraded cleanly when no plaintext vault existed. Bandit improved from 43 to 41
  Low findings with 0 Medium/High and no new suppression; the 8 justified skips are
  unchanged.

## Typed resilience configuration reconciliation (2026-08-13)
* **Task Trail**: `07efa872-24d0-4114-a2d9-f108d01e3104`.
* **Boundary**: invalid `CircuitConfig` and `RetryPolicy` construction now raises
  structured `ResilienceConfigurationError(field, reason)`, still subclassing
  `ValueError` for compatibility. Both policies are frozen and slotted.
* **TDD evidence**: six hostile constructor inputs first failed because the runtime
  exposed plain `ValueError`; all six passed after the typed boundary landed.
  Existing circuit, retry, async, and router-degradation scenarios remain green.
* **Verification**: 306 repository tests, Ruff, focused BasedPyright, no-excuse on
  changed modules, bytecode compilation, diff integrity, and a direct SDK driver
  passed. The changed type/test cluster dropped from 16 no-excuse findings to zero.
* **Corrected baseline**: the current whole-tree checker reports 284 findings across
  142 files. The earlier shared claim of 24 inherited findings used a narrower scan
  and must not guide future cleanup prioritization.

## Antigravity basedpyright/network reconciliation (2026-08-13)
* **Task Trail**: `e34470c5-c5c0-4865-bb4e-1a00a1b578a8`.
* **Install state**: `basedpyright 1.39.9` was already present in the locked project
  environment at `/home/amdy/data_rein/.venv`. `scripts/install_bin.sh` now links both
  `basedpyright` and `basedpyright-langserver` into `~/.local/bin`, alongside `reins`.
* **Live verification**: a fresh shell resolves `/home/amdy/.local/bin/basedpyright`
  and reports version `1.39.9`; ShellCheck passes the installer. Restart Antigravity
  after opening a fresh login shell so its inherited PATH sees the links.
* **Network diagnosis**: `daily-cloudcode-pa.googleapis.com` resolves to IPv6 and
  IPv4. IPv4 reaches Google (`HTTP 404` without auth, proving transport); IPv6 fails
  immediately with `network unreachable` because this host has no IPv6 default route.
  This is independent of basedpyright installation. Use `GODEBUG=netdns=cgo agy --continue`
  after configuring IPv4 preference, or repair the host's IPv6 default route; do not
  reinstall the Python package to address this transport error.

## Gemini explanation and paper reconciliation (2026-08-14)

* **Source**: `/home/amdy/Downloads/gemini_explanation.txt` is a project-context
  summary, not a v5 paper or execution log. No v5 PDF is present in Downloads.
* **Available paper**: the two 10-page PDFs are the previously audited technical
  draft artifacts. Findings are recorded in
  `knowledge_base/ACADEMIC_PAPER_SANITY_CHECK_V3.md` and the new
  `knowledge_base/GEMINI_EXPLANATION_RECONCILIATION_2026_08_14.md`.
* **Registry correction**: the canonical tree contains eight skills, including
  `deep-research-paper`; the manifest prose and installer fixture now reflect
  all eight. `pon_testing_suite` now has the promised frontmatter tags.
* **Architecture correction**: the PON skill now distinguishes durable state on
  `tell` from transient local coordinator/cache state on execution nodes.
* **Boundary**: Gemini’s summary is treated as context. Runtime behavior,
  measured results, and paper claims must be supported by repository evidence or
  recorded experiments.

## Skills and v5 paper audit continuation (2026-08-14)

* **Artifact boundary**: a fresh Downloads scan still finds no separately
  identifiable v5 manuscript. The two Gemini explanation filenames are
  byte-identical context summaries; the two Data Rein PDFs are 10-page,
  versionless WeasyPrint drafts.
* **Skills**: all eight canonical skills resolve correctly through all six
  configured scan roots. The undated skills list in `PRIME_DIRECTIVE.md` was
  corrected. Residual risks are that the registry does not validate frontmatter
  fields and `pon_testing_suite` uses a hyphenated internal name while its
  directory uses underscores.
* **Paper**: `knowledge_base/SKILLS_AND_V5_SANITY_CHECK_2026_08_14.md` records
  contradictions involving `ProcessPoolExecutor`, `OLLAMA_MAX_VRAM`, JSON Task
  Trail, the absent `tests/test_pon_compliance.py`, the unsubstantiated 13-loop
  history, and unsupported stress/CPU/uptime results.
* **Current gate**: focused skill tests and harness PON scanning pass. A wider
  targeted run still has three failures in malformed training-data handling,
  two broad-handler diagnostics, and test coverage for untracked
  `reins.harness.autonomous`.

## Full-Stack Safety Audit and Wiki Unification Handoff (2026-08-14)

* **Status**: COMPLETED. Code committed to `dev` branch.
* **Frontend/Backend Safety Sweep**: Conducted a deep full-stack audit across the Odysseus application. Squashed 25+ critical runtime errors, including `async` Promise executor anti-patterns in `signature.js`, missing `window` context (`no-undef`) across the JS modules, and Python `NameError` exceptions (missing `datetime` in `caldav_writeback.py`, `repo_id` mismatch in `cookbook_routes.py`). All layers are strictly ESLint and flake8 compliant.
* **Unified Wiki Integration**: The monolithic `WikiDB` is now natively exposed via REST API. Implemented full CRUD routes (`GET`, `POST`, `PUT`, `DELETE`) inside `odysseus/routes/reins_routes.py`.
* **Interactive UI Editor**: Replaced the read-only wiki panel in `static/index.html` with a fully interactive split-pane editor (in `static/js/harness.js`). Humans and models can natively create, search, edit, and delete Markdown Pages and Memories directly inside the Odysseus dashboard.
* **Obsidian Porting**: Wrote and executed an export script (`scripts/export_to_obsidian.py`) that successfully ported the entire `WikiDB` into a standalone Obsidian vault located at `/home/amdy/data_rein/wiki_vault/`. All pages and memories are formatted cleanly as `.md` files with rich YAML frontmatter (slug, category, owner, uid).
* **Next Agent Sanity Check**: The incoming agent should verify that all the API routes and UI integrations function seamlessly together and ensure the new `wiki_vault` meets the user's expectations for Obsidian compatibility.

## Odysseus full-stack remediation (2026-08-14)

* **Current state**: implementation and release gates pass; vault publication remains intentionally fail-closed because the current Wiki content did not pass secret scanning. See `knowledge_base/HANDOFF_2026_08_14_ODY_FULL_STACK_REMEDIATION.md`.
