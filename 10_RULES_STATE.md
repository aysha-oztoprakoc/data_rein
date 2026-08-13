# 10 RULES — STATE SNAPSHOT (2026-07-06)

**Canonical source:** `knowledge_base/TEN_LAWS.md` — the repository-local 10
Laws adapted from the KAD constitution. The original source was
`/home/amdy/data-workspace/docs/TEN_LAWS.md`; the harness no longer depends on
another repository to load its operative rules.

**Harness contract (data_rein):** *Sync first · one wiki · any model · zero
polling · degrade, never crash · stay on-brand.*

## The 10 Laws (condensed)

| # | Law | One-line rule | Verification |
|---|-----|---------------|--------------|
| 1 | **PON-1** Atomic Notification | No polling: every wait ends via blocking I/O, callback, or notified fact — never `while`/`sleep` spin. | `tests/test_laws.py::test_law_pon_no_polling` (AST scan, incl. imported `reins.harness.*`) |
| 2 | **PON-2** Decoupling by Facts | Collaborators communicate via injected seams / published facts; no `Cls.__new__(Cls)` reach-through into internals. | `tests/test_laws.py::test_law_pon_no_reach_through` |
| 3 | **PON-3** Polynomial Cost | Fact evaluation is incremental; no exhaustive scans that grow with total state instead of the change. | `tests/test_resilience.py::test_breaker_window_is_bounded` |
| 4 | **GD-1** Universal Breaker | Every external I/O call sits behind a circuit breaker (Closed → Open → Half-open); state changes are notified facts. | `tests/test_resilience.py::test_breaker_opens_after_threshold`, `::test_breaker_half_open_probe` |
| 5 | **GD-2** Disciplined Retry | Retries only while Closed, only for idempotent ops, exponential backoff + jitter; billable non-idempotent calls never auto-retry. | `tests/test_resilience.py::test_retry_backoff_sequence`, `::test_retry_never_fires_for_non_idempotent` |
| 6 | **GD-3** Honest Failure | Degradation always leaves a diagnostic trace; bare `except: pass` swallows are forbidden. | `tests/test_providers.py::test_record_usage_failure_is_logged_not_silent` |
| 7 | **TDD-1** Test Precedence | A failing (Red) test defines the contract before any implementation is written. | Process gate (git history: test commit precedes impl commit), backed by TDD-3 |
| 8 | **TDD-2** Mandatory Refactor | Green is not done: remove duplication/unclear structure afterward, under the passing-test safety net. | Full suite stays green across refactor commits |
| 9 | **TDD-3** Quality Gate | No merge with a failing test; suite runs in ms via injected fakes for slow externals. | `ruff check && pytest -q` both exit 0 |
| 10 | **NIX-1** Configuration Determinism | Environment pinned by lockfile + declarative devShell; lockfile drift from `pyproject.toml` fails a test. | `tests/test_determinism.py::test_lockfile_matches_pyproject` |

## First-principles context (data_rein harness, Hephaestus survey)

Source paths in `/home/amdy/data_rein/`:
- `knowledge_base/PRIME_DIRECTIVE.md` — master constitution (sync-first init,
  one harness / many clients, amdy=execution / tell=state separation).
- `knowledge_base/wiki.db` — the single monolith knowledge store (never
  create a second store; `reins wiki *`).
- `config/model_router.json` + `src/reins/harness/models.py` — model-agnostic
  local-first routing; cloud only for explicit/heavy tasks; secrets via vault only.
- `knowledge_base/AESTHETIC_DIRECTIVE.md` — Blood Red `#ff4040` on Black
  `#200000`, gritty synthetic voice, for all generated text/UI.
- Universal Task Trail (`reins trail *`) — cross-agent coordination facts.
- The "10 Leis" meta-prompts in `tulpas/data-archimedes - NotebookLM_files/`
  are the generator spec; TEN_LAWS.md is their applied output.

## Compliance status

- **data-workspace: compliant as of 2026-07-06.** Prometheus's sweep found
  zero violations of PON / GD / single-store / secrets rules; the repo is
  AST-gated by `tests/test_laws.py`. One hardening flag (a hard-coded PON
  pre-push bypass in `scripts/install_hooks.sh`) is queued in
  `/home/amdy/data-workspace/QWEN_REFACTOR_PLAN.md`.
