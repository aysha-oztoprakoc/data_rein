# The Ten Laws of data_rein

This is the repository-local executable law set for the universal harness. It was
adapted on 2026-08-11 from the KAD-derived constitution previously stored at
`/home/amdy/data-workspace/docs/TEN_LAWS.md`. The Prime Directive remains the master
constitution; these laws make its PON, graceful-degradation, test, and environment
requirements independently verifiable without depending on another repository.

## PON-1: Atomic Notification

No component waits by rechecking state. Every wait ends through blocking I/O, a
callback, or a notified fact. `while`/`sleep` status loops are forbidden, including
deadline polling disguised as a bounded wait.

Verification: AST scanning of production source and real event-driven readiness tests.

## PON-2: Decoupling by Facts

Collaborators communicate through injected interfaces, the Task Trail, or published
facts. They do not reach through private state or construct invalid objects such as
`Class.__new__(Class)` merely to borrow internal behavior.

Verification: AST scanning for reach-through patterns and tests at public boundaries.

## PON-3: Bounded Incremental Cost

Fact evaluation is incremental. A routine action must not rescan total history,
knowledge, or backend state when it can process the changed subset. Windows and queues
are bounded, and durable indexes provide the lookup boundary.

Verification: bounded-window tests and startup scenarios whose work is independent of
knowledge-base size.

## GD-1: Universal Circuit Breaker

External HTTP, SSH, subprocess, MQTT, and provider calls sit behind a circuit breaker:
Closed, Open after repeated failures, Half-open after cooldown, then Closed or Open
based on a bounded probe. State transitions produce diagnostics and Task Trail facts.

Verification: threshold, cooldown, half-open, recovery, and bounded-history tests.

## GD-2: Disciplined Retry

Automatic retry is allowed only for idempotent operations while their breaker admits
calls. It uses bounded exponential backoff and jitter. Billable or otherwise
non-idempotent model generation is never retried automatically.

Verification: deterministic injected-clock tests for backoff and explicit tests that
non-idempotent operations execute once.

## GD-3: Honest Failure

Degradation must leave a useful diagnostic trace. Broad handlers may translate a
failure at a public boundary, but they log the underlying error. Silent exception
swallows are forbidden.

Verification: static handler scanning and failure-path tests that assert diagnostics.

## TDD-1: Test Precedence

Every behavioral change begins with a focused failing test that proves the contract is
not already satisfied.

Verification: recorded red evidence in the audit/task trail and review of change order.

## TDD-2: Mandatory Refactor

Green is followed by removal of duplication, unclear ownership, and accidental
complexity without changing the protected behavior.

Verification: the focused and full suites remain green after refactoring.

## TDD-3: Quality Gate

No handoff, push, backup, or completion claim occurs with failing tests or static
checks. Slow externals are injected so the suite stays deterministic and fast.

Verification: `ruff check`, BasedPyright on changed typed surfaces, `pytest -q`, the
PON suite, and real CLI/MCP scenarios all exit successfully.

## NIX-1: Configuration Determinism

Python and system dependencies are declared and locked. `uv.lock` pins Python packages;
an optional Nix flake supplies a reproducible dev shell over that lock. Dependency drift
between manifests and lockfiles fails a test.

Verification: frozen `uv` synchronization, lockfile consistency tests, and `nix flake
check` when Nix is available.

## Mapping from the Prime Directive

| Prime requirement | Operative laws |
|---|---|
| Zero polling and FBE notification | PON-1, PON-2, PON-3 |
| Graceful degradation | GD-1, GD-2, GD-3 |
| Test-driven implementation | TDD-1, TDD-2, TDD-3 |
| Reproducible clients and nodes | NIX-1 |

