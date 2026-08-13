# data_rein Model-Agnostic Harness Audit

## Record

- Started: 2026-08-11
- Agent client: Codex
- Canonical repository: `/home/amdy/data_rein`
- Requested alias: `/home/data_rein` did not exist and was not created, preserving one harness and one state root.
- Task Trail ID: `codex-harness-audit-2026-08-11` (`success`, owner `codex`, target `amdy`).
- Objective: read the binding project rules, audit the model-agnostic meta harness against them, refactor confirmed violations, and preserve action and verification evidence in the monolith wiki.

## Rules Applied

- Loaded `knowledge_base/PRIME_DIRECTIVE.md` and `knowledge_base/SHARED_CONTEXT.md` at session and prompt boundaries.
- Ran `reins wiki stats` and `reins trail list` before systemic work.
- Loaded the canonical `data_rein`, `agy-pon-compliance`, `pon_testing_suite`, and system-topology skills.
- Preserved the single wiki database and canonical repository path.
- Used category routing as the model abstraction boundary and kept the active Codex host model outside `config/model_router.json`.
- Used event-driven, bounded commands only; no polling loops or sleep waits were introduced.
- Inspected the dirty worktree before edits and did not revert unrelated changes.

## Actions

### 2026-08-11: Repository and shared-state orientation

- Confirmed the canonical repository is `/home/amdy/data_rein`; `/home/data_rein` does not exist.
- Read the Prime Directive, Shared Context, root `AGENTS.md`, canonical harness skills, model router configuration, path resolver, environment adapters, and current Task Trail.
- Verified the monolith wiki resolved to `/home/amdy/data_rein/knowledge_base/wiki.db`.
- Verified `reins paths` resolves the repository, knowledge base, router, shared state, and Task Trail through `reins.harness.paths`.
- Created the deterministic Task Trail record `codex-harness-audit-2026-08-11` so other harness agents can observe or resume this audit.

### 2026-08-11: Wiki audit channel

- Created this tracked source page under `knowledge_base/` and ran `reins wiki consolidate`.
- Consolidation ingested the audit source into the existing monolith; no second database or sidecar knowledge store was created.
- The audit page is updated at meaningful phases, then re-consolidated so current actions and evidence remain searchable by every client.

### 2026-08-11: Codex client integration

- Added Codex to the environment table and documented that Codex is a harness client, not the owner of model routing.
- Added `.codex/config.toml` as a project-scoped declaration for the `reins` MCP server with non-required startup for graceful degradation.
- Corrected `scripts/install_skills.sh` so canonical harness skills install into Codex's actual `~/.codex/skills` scan path while retaining the legacy Odysseus Codex plugin target.
- Updated `skills/MANIFEST.md` to distinguish the Codex skill root from the legacy plugin bundle.
- Ran `reins skills install`; six canonical harness skills were linked into Codex and the other configured environments.
- Registered the `reins` MCP server in the user Codex configuration with `DATA_REIN_HOME=/home/amdy/data_rein` after runtime evidence showed `codex mcp list` did not merge project MCP configuration for its management subcommand.
- Verified `codex mcp get reins --json` resolves the server to the repository virtual environment and canonical home.

## Audit Matrix

| Rule | Authoritative source | Evidence | Status |
|---|---|---|---|
| Mandatory synchronization | Prime Directive section 0 | Directive/context reads and `reins wiki stats`/`reins trail list` outputs | verified |
| One harness, many clients | Prime Directive section 1 | Codex adapter, shared CLI/MCP, canonical path resolver | verified |
| One monolith wiki | Prime Directive section 2 | 635 pages / 275 memories in canonical `wiki.db`; active writers use `WikiDB` | verified |
| Category-based model routing | Prime Directive section 3 | typed config, injected provider handlers, explicit cloud API | verified |
| Hardware-derived model fit | Prime Directive section 3a | live registry admission before Ollama dispatch | verified |
| Zero-polling PON | Prime Directive section 4 | AST laws, external PON suite, WebSocket/inotify/MQTT event paths | verified |
| amdy execution / tell durable state | Prime Directive section 4 | explicit node routing and unreachable-node failover scenario | verified with tell currently offline |
| FBE notification flow | Prime Directive section 4 | MQTT callbacks and indexed state transitions | verified |
| Graceful degradation and trail logging | Prime Directive sections 4-5 | circuit transitions, honest diagnostics, hostile-state scenarios | verified |
| Omarchy output law | Prime Directive section 6 | five-tab Sofia captures at 160x48 and 100x36 | verified |

## Findings

- The repository had no first-class Codex client adapter and installed harness skills into a legacy plugin directory rather than Codex's live global skill root. The integration changes above address this gap and passed the final verification matrix.
- The wider harness audit is closed. Confirmed violations, refactors, verification evidence, and residual external boundaries are recorded below.
- `10_RULES_STATE.md` declares `/home/amdy/data-workspace/docs/TEN_LAWS.md` canonical and says those ten laws supersede the older three-law summary. The current Prime Directive does not reference that canonical law text. This is a governance drift requiring reconciliation.
- `ORCHESTRATION_GOAL.md` is a completed, role-specific historical mission with explicit compact-and-halt checkpoints. It is evidence for the generated `blueprint.yaml`, not an active global agent contract for this audit.
- `blueprint.yaml` defines additional executable architecture requirements: lesser-model action gates, trail-logged honest rejection, hardware-fit enforcement, and lead-agent DAG judging. These requirements are included in the implementation audit.
- A hyphenated user query such as `codex-harness-audit-2026-08-11` was passed directly into FTS5 query grammar and crashed `reins wiki search` with `sqlite3.OperationalError: no such column: harness`. The existing graceful-degradation law test explicitly tolerated this exception, contradicting its own public-entry-point contract.
- `tests/test_laws.py` still presents three laws, while `10_RULES_STATE.md` and the external canonical `TEN_LAWS.md` declare ten operative laws. It does not enforce PON-2, PON-3, GD-1, GD-2, NIX-1, or the full GD-3 rule.
- The PON testing suite failed because it scans `tests/test_local_ensure_server.py` and treats a bounded injected test wait as production polling. The production `src/reins` tree passed that scanner. The scanner target policy needs to distinguish executable harness code from tests and imported/generated artifacts.
- Ruff is referenced by the Ten Laws quality gate but is absent from both `.venv/bin` and the frozen `uv` environment. The declared quality gate therefore cannot run as written.
- Strict BasedPyright initially reported errors and hundreds of warnings across legacy surfaces. Every changed model, resilience, persistence, external-I/O, action-gate, MCP, and Sofia boundary now passes with zero errors or warnings; untouched legacy modules remain outside this scoped proof.
- Multiple modules exceed the 250-line engineering ceiling, including core router, wiki, CLI, MCP, backup, profiler, IPC, digest, and extraction modules. Splitting them is a required staged refactor, not a single blind rewrite.
- The Task Trail fallback daemon queried every `pending`/`running` record without checking its target or owner. During this audit, a CLI bootstrap notification caused data-ody to claim `codex-harness-audit-2026-08-11`, run its prompt through a local model, and falsely mark it `success_fallback`. This could also execute unrelated agent work or rejected action payloads.
- Every legacy CLI invocation constructed `HarnessBootstrapper`, recursively read all 538 Markdown/XML knowledge sources into an unused process-local dictionary, and then discarded it on exit. No consumer read `memory_cache`; the scan violated the single-wiki abstraction and PON-3 incremental-cost law.
- `config/model_router.json` contains 12 category routes while the Prime Directive documented 11. The directive now derives the count from the audited configuration value.

### Confirmed refactor: explicit fallback ownership and incremental bootstrap

- Added red tests with one active Codex task and one explicitly assigned data-ody task. The old daemon processed both; the old bootstrap also failed a guard that rejected `os.walk`.
- Centralized fallback eligibility in `TaskTrail.fallback_candidates`: only `pending`/`running` tasks whose `target_node` is exactly `data-ody` are eligible.
- Made both the bootstrap notifier and Odysseus executor use the same eligibility query. A claimed task is marked `running_fallback`, and status-write degradation is logged instead of silently swallowed.
- Removed the unused recursive knowledge cache from bootstrap. Knowledge remains behind the canonical `WikiDB` abstraction and CLI startup cost no longer grows with knowledge-base size.
- Restored the falsely completed Codex audit record to its real `running` state and kept its explicit `amdy` target.
- Verified the focused regression suite passes. Drove `.venv/bin/reins trail list`; it reported `No data-ody fallback tasks found`, did not emit a cache scan, and did not mutate the audit record.

### Confirmed refactor: literal wiki query boundary

- Added a failing regression test proving punctuation in user search text crashes FTS5.
- Confirmed the test failed with `sqlite3.OperationalError: no such column: harness` before implementation.
- Added one shared literal-query parser used by page and memory FTS searches. User punctuation is converted into quoted Unicode word terms joined by `AND`; empty input degrades to an empty result.
- Verified the regression plus existing page, memory, and hostile-query tests pass.
- Drove the real CLI with `reins wiki search 'codex-harness-audit-2026-08-11'`; it returned this audit page instead of crashing.

### Confirmed refactor: circuit breaking and disciplined retry

- Added a typed resilience core with closed, open, and half-open breaker states, bounded failure windows, injected clocks, and keyed registries.
- Routed every model-provider dispatch through a breaker keyed by provider, node, and model. State transitions emit diagnostics and deterministic Task Trail records.
- Added explicit retry support only for idempotent work, with bounded exponential backoff and jitter. Model generation is marked non-idempotent and executes exactly once.
- Verified threshold, cooldown, half-open recovery, bounded history, retry timing, and router fast-failure behavior with focused tests.

### Confirmed refactor: event-driven readiness and generation

- Replaced CLI deadline/port polling loops with one readiness check followed by detached startup and immediate return.
- Removed the local Ollama fallback status loop. Inotify remains the blocking readiness signal; an unavailable inotify backend leaves a diagnostic and performs one final state check.
- Replaced ComfyUI history polling with its WebSocket execution events. The socket opens before prompt submission, matching completion or error facts terminate the wait, and history is fetched once after completion.
- Strengthened the PON AST law to reject status/deadline loops and all sleep calls while allowing blocking receive/read/select event loops.
- Verified the focused PON, readiness, and ComfyUI suite passes.

### Confirmed refactor: honest degradation

- Added executable GD-3 scanning for bare, `Exception`, and `BaseException` handlers that translate failures without a diagnostic or re-raise.
- The red scan found 105 silent broad handlers across active CLI, harness, service, extraction, and training modules.
- Added one central traceback-backed degradation diagnostic and instrumented every identified handler without changing its successful behavior or public sentinel/error return.
- Added a durable-state corruption scenario proving the Task Trail returns an empty view and emits a captured warning rather than silently hiding the cause.
- Ruff, bytecode compilation, the GD-3 structural law, and the focused failure-path tests pass after the rewrite.

### Confirmed refactor: indexed Task Trail

- Added red tests proving task lookup and status changes depended on parsing total JSON history, plus a migration contract for extension fields.
- Replaced the active Task Trail persistence layer with SQLite WAL state indexed by task ID, status/timestamp, and fallback target/status/timestamp.
- Preserved the public `TaskTrail` API. The former `task_trail.json` is imported idempotently exactly once and retained as migration evidence.
- Kept the new implementation under 250 lines and made the changed persistence layer strict-BasedPyright clean.
- Verified indexed operations cannot call `json.load`, legacy fields migrate once, fallback ownership still holds, and handoff/MCP trail scenarios remain green.
- Migrated the live 97-record trail, isolated all tests under temporary state directories, backed up and removed 37 identified test artifacts, and restarted resident Sofia/Odysseus/MCP processes on the indexed implementation.

### Confirmed refactor: provider-agnostic routing and cloud authorization

- Split model declarations, hardware inventory, provider protocols, provider runtime, and router policy into typed modules below the 250-line ceiling.
- Added provider-handler injection so an additional backend conforming to the provider function contract does not require router dispatch changes.
- Enforced hardware-fit admission from `model_registry.json` before local Ollama dispatch and verified unreachable-node failover.
- Removed the ordinary router's legacy `allow_cloud` escape hatch. `ModelRouter.route` is local-node routing only; `route_cloud` is the separate explicit boundary.
- Made provider filtering exact: requesting an unavailable vendor fails without sending the prompt to a different provider.
- Verified a real MCP `route_local` call returned `HARNESS_LOCAL_OK` from local `llama3.1:8b` on `amdy`.

### Confirmed refactor: universal external circuit admission

- Added synchronous and asynchronous keyed circuit admission for subprocesses, HTTP, WebSockets, browser/search SDK calls, TCP readiness checks, Unix IPC connects, MQTT connect/subscribe/publish, and one-shot MQTT notifications.
- Circuit transitions leave diagnostics and deterministic indexed Task Trail entries; failed result objects can be observed without changing their public return contracts.
- Extended executable GD-1 AST enforcement to reject active Python call sites that bypass the adapter, including raw TCP, IPC, and MQTT one-shot calls.
- Kept all retry opt-in, bounded, and restricted to idempotent work. Model generation remains single-attempt.

### Confirmed refactor: single-wiki ingestion and isolated verification

- Replaced legacy Sofia memory injection writers with a canonical content-addressed `WikiDB.add_memory` ingestion module; 104 extracted Sofia memories were ingested without creating a second store.
- Updated the maintained search dependency from deprecated `duckduckgo-search` to `ddgs` and removed fixed browser timeout waits.
- Added an autouse temporary state fixture so coordinator, breaker, and training scenarios cannot write synthetic records into the live Task Trail.

### Confirmed refactor: event-driven Sofia surface

- Removed all four periodic Textual timers. Initial facts load once; `u` refreshes views; `h` runs the health scenario; MQTT Task Trail notifications refresh trail state.
- Removed the unfinished terminal placeholder, added stable tab IDs and hidden `1`-`5` bindings, and constrained horizontal rows so controls remain visible.
- Split the former 700-line dashboard into typed controls, health, styles, value, and widget modules; every changed module is below the 250-pure-line ceiling.
- Captured all five tabs through a real PTY/xterm/Chromium renderer at 160x48 and 100x36 after the final layout edit. All ten captures have valid PNG signatures, no overflow, and no observed overlap or clipping. Evidence lives under `.omo/evidence/harness-audit/tui-refactor-wide-final` and `tui-refactor-narrow-final`.
- The width checker reported one narrow Agent Center border anomaly caused by the two-cell green status glyph; direct inspection of the browser-rendered PNG confirms the border and controls are intact. The same glyph is reported as wide-character content without misalignment at 160 columns.
- Independent visual subagents were not used because the active session explicitly prohibited spawning subagents; objective captures and direct image inspection were retained instead.

### Confirmed refactor: typed model-proposal and MCP boundaries

- Added a hostile regression proving malformed lesser-model graph output previously raised `KeyError` inside the judge instead of degrading.
- Parsed graph nodes, actions, edges, aliases, and forbidden extra fields through frozen Pydantic models at the trust boundary. Invalid proposals now return `invalid_graph`, skip every dispatcher, and leave a failed Task Trail verdict.
- Replaced raw action-gate `Any` dictionaries with JSON-safe argument/result contracts and typed accepted/rejected result shapes. Required and optional arguments are explicit; unknown proposal keys are rejected as `schema_invalid` before dispatch.
- Typed the MCP Wiki rows and legacy coordinator/hardware protocol edges without adding state or provider coupling. The active MCP server is below the 250-pure-line ceiling.
- Added `types-psutil` to the frozen development dependency set and made every changed Sofia, gate, judge, MCP, agent, external-I/O, budget, and sudo boundary strict-BasedPyright clean.

### Deterministic environment status

- Declared Ruff and BasedPyright in the locked development dependency group and regenerated `uv.lock`; `uv lock --check` is the executable drift boundary.
- Added a two-architecture Nix development shell declaring Python 3.11, uv, Ruff, Git, and required native libraries.
- Added a red determinism test requiring `pyproject.toml`, `uv.lock`, `flake.nix`, and Nix-generated `flake.lock`.
- Generated `flake.lock` with Nix, verified it matches the checked flake copy byte-for-byte, and evaluated the x86_64 development shell with `nix flake check --no-build`.

### Quality-gate status

- Added the declared Ruff quality gate and resolved every active-source correctness diagnostic; `ruff check .` passes.
- `python -m compileall -q src tests scripts` passes.
- All 41 executable Ten Laws tests pass.
- The full repository suite passes, including NIX-1 determinism.
- The deprecated search-package warning is resolved by the maintained `ddgs` dependency.

## Verification

- `reins skills install`: passed; six canonical skills linked into each present environment.
- Python `tomllib` parse of `.codex/config.toml`: passed.
- `bash -n scripts/install_skills.sh`: passed.
- `codex mcp get reins --json`: passed and reports the canonical `DATA_REIN_HOME`.
- `shellcheck`: unavailable on the node; this is recorded rather than treated as a pass.
- Wiki regression red phase: passed as evidence; the new test failed for the expected FTS parser error before the fix.
- Wiki targeted green phase: four tests passed.
- Real wiki CLI search: passed and returned one page.
- Fallback ownership/bootstrap regression: three focused tests passed, including the existing hostile-trail degradation scenario.
- Real Task Trail CLI startup: passed without knowledge caching or cross-owner fallback execution.
- Python bytecode compilation for `src` and `scripts`: passed.
- PON focused suite: passed after event-driven readiness and WebSocket refactors.
- Ruff quality gate: passed across configured active source, tests, and scripts.
- Strict BasedPyright on the changed model, resilience, ComfyUI, Task Trail, ingestion, external-I/O, action-gate, judge, MCP, and Sofia boundaries: zero errors or warnings.
- Programming no-excuse checker on all newly changed strict Python boundaries: zero violations.
- Full suite: all 214 behavior and law tests pass.
- External PON suite over `src`: passed every active Python module.
- `uv lock --check`, `uv sync --frozen`, Python bytecode compilation, and Nix flake evaluation: passed.
- Real stdio MCP session: negotiated 22 tools; wiki search and running-trail list passed; a malformed graph returned `invalid_graph` with an empty dispatch map; local `llama3.1:8b` returned exactly `HARNESS_LOCAL_OK`.
- Resident runtime: `data-sofia`, `data-ody`, and supervised `data-mcp` run on the audited code; HTTP MCP responds on `127.0.0.1:8765/mcp` with a valid MCP session header.

## Residual Boundaries

- `tell` was offline during this audit. Its failover and hardware admission are covered by deterministic scenarios, but no live SSH inference was claimed.
- Cloud dispatch was not invoked because the user did not authorize a billable provider call; authorization isolation and vendor non-substitution are covered by executable tests.
- ComfyUI completion is WebSocket-driven and tested, but the local ComfyUI torch/ROCm environment remains an external deployment prerequisite.
- Several legacy modules remain over the 250-line engineering target. New/split model, resilience, persistence, and ingestion modules comply; reducing unrelated legacy modules is separate maintenance work.
