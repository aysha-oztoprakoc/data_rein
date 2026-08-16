# Security Audit — 2026-08-16

**Task Trail:** `4e93e0c0-53ea-4e39-ba47-83cd309e514e`
**Scope:** Full tree including native — harness Python (`src/reins`, `scripts`, `tools`),
the Odysseus FastAPI web app (`odysseus/routes`, `odysseus/src`, `odysseus/core`), native
Rust PON engine (`native/reins-pon-engine`), the legacy C++ engine (`DATA/kad-1.0/tell`),
shell surface, dependencies (Python/JS/Rust), and secrets. Local-first scan; **no cloud
provider was invoked** (cloud was authorized but local SAST proved sufficient).

## Result

Two confirmed vulnerabilities were found and fixed, each with a regression test:

| # | Finding | Severity | File | Fix |
|---|---------|----------|------|-----|
| 1 | Path traversal via MQTT-delivered memory `title` (CWE-22) | **HIGH** | `src/reins/services/vault_manager.py` | `sanitize_vault_title()` strips path components / NUL / traversal tokens and the writer double-checks the resolved basename stays in the wiki dir |
| 2 | Untrusted `.docx` XML entity expansion / XXE (CWE-611/CWE-400, "billion laughs") | **MEDIUM** | `odysseus/src/markitdown_runtime.py` | Prefer `defusedxml`; hardened stdlib fallback rejects any `<!DOCTYPE` before parse |

After fixes: full harness suite **346 passed** (was 338) in 13.71s; ruff clean on changed
files; bandit **0 issues** on both changed files; PON **APROVADO**; markitdown unit tests
9 passed / 1 skipped (skip is the optional `markitdown` dependency); vault tests 8 passed.

## Threat-to-control mapping (surfaces reviewed)

| Threat | Control / result | Evidence |
|---|---|---|
| MQTT → filesystem write (vault memory) | Title sanitized to a bare basename; writer rejects any resolved path not inside the wiki dir. | `tests/test_vault_traversal.py` (8 cases incl. `../../`, absolute, Windows separators, NUL) |
| Untrusted office-document XML parsing | `defusedxml` preferred; `<!DOCTYPE` rejected on the portable stdlib fallback (no external/internal entity expansion). | `odysseus/tests/test_markitdown_runtime.py` (XXE, billion-laughs, case-insensitive doctype) |
| SQL injection | All flagged `hardcoded_sql_expressions` (harness `wiki.py`, `task_trail.py`, email/DB routes) use **bound parameters** with only **fixed literal** interpolation; confirmed false positives. | Reviewed `wiki.py:300-445`, `task_trail.py:150-175`, `email_routes.py:170` + clause helpers |
| Shell execution / RCE | `run_local`/`run_script`/`ssh_command` (`builtin_actions.py` `shell=True`) are admin-gated (`task_routes._ADMIN_ONLY_ACTIONS`); generic tool layer has `NON_ADMIN_BLOCKED_TOOLS` (bash/python/file/etc.) in `tool_security.py`. | `task_routes.py:466`, `builtin_actions.py:2748-2750`, `tool_security.py` |
| Privileged command runner | `run_sudo_cmd` callers are fully bounded: PIDs decimal-validated (`_positive_pid`), cgroup names regex-validated (no `/`, alnum start), governor/GPU targets from fixed sysfs globs, values enum/int-checked. | `sofia_controls.py`, `resource_budgets.py:126-156` |
| SSRF / URL opening | `urlopen` callers operate on operator-configured endpoint URLs (`ep.base_url`), not attacker-supplied; `0.0.0.0` in `llm_core`/`model_context` are SSRF allowlists, not server binds. | `cookbook_routes.py:1323`, `llm_core.py:311-329`, `model_context.py:19` |
| Side-channel / crypto | Vault uses Fernet; password hashing bcrypt; session tokens via `secrets`; TOTP present — no weak-hash or constant-time defect found in scope. | `auth.py`, `vault_manager.py`, `auth_routes.py` |
| Native memory safety | Rust `lib.rs`: `unsafe` blocks null-checked, `#[repr(C)]` FFI, no unbounded raw ops → memory-safe. Legacy C++: only bounded `fgets(buffer.size())`, no strcpy/sprintf. | `native/reins-pon-engine/src/lib.rs`, C++ scan |
| Secrets in source | `detect-secrets` against `.secrets.baseline` → no new leaks. `.gitignore` excludes `api_keys.json`, `.secrets.enc`, `vault.json`. | `detect_secrets scan` output (clean) |
| Known-vulnerable dependencies | `pip-audit`: **no known vulnerabilities** (`data-rein` unauditable on PyPI, as expected). `npm audit`: **0 vulnerabilities**. | `pip-audit`, `npm audit` logs |

## Security scan progression

| Stage | Tooling | Binary observable |
|---|---|---|
| Python SAST | `bandit -r src scripts tools odysseus` (vendor-excluded) | 511 project findings: **0 High**; highest content are SQL-FP family + `shell=True`(gated); resolved as above |
| JS/composition SAST | `semgrep --config=p/security` (ERROR/WARNING) | No findings |
| Dependency audit | `pip-audit`, `npm audit` | No known vulnerabilities |
| Secrets | `detect-secrets` + `.secrets.baseline` | Clean |
| Shell surface | shellcheck (via `uvx`, historical gate) | Clean in prior gate |
| Native | manual Rust/C++ review | No fixable memory-safety findings |
| Behavioral gates | `pytest tests/`, ruff, bandit, pon_tester, markitdown/vault units | 346 passed; ruff clean; bandit 0 on changed; PON approved |

## fp-check summary (candidate → verdict)

- Vault `title` traversal — **TRUE POSITIVE**, fixed.
- `.docx` DOCTYPE/entity expansion — **TRUE POSITIVE**, fixed.
- SQL injection flags — **FALSE POSITIVE** (parameterized).
- `bind_all_interfaces` — **FALSE POSITIVE** (SSRF allowlists).
- `shell=True` builtin actions — **MITIGATED** (admin + tool policy gating) — residual depends on auth deployment.
- `urlopen` — **FALSE POSITIVE/operator-controlled**, not attacker-reachable.
- `sudo_exec` — **NO VULNERABILITY** (all inputs validated).
- `markitdown`/XXE full-defusedxml — fixed via preferred `defusedxml` import.

## Residual risk and deferred work

- **cargo-audit not installed** — the Rust `Cargo.lock` dependency set was not tool-audited
  in this pass; run `cargo install cargo-audit && cargo audit` in
  `native/reins-pon-engine` to complete supply-chain coverage.
- **Admin fail-open / deployment footguns** (documented, not changed): `AUTH_ENABLED=false`
  disables admin gating, and `task_routes._is_admin` returns True when auth is unconfigured
  (single-operator mode). This is consistent with a local single-operator product, but any
  **network-exposed** deployment should default `AUTH_ENABLED=true` and ensure an admin
  account exists. Recommend fail-closed defaults if this app is ever bound off-loopback.
- **`/api/reins` admin tool passthrough** (`dataset/export` `out_path`, `cli/digest` `path`)
  can write/read arbitrary paths; gated behind `require_admin`. Defense-in-depth would
  constrain `out_path` to the harness state dir, but this would change intended admin
  dashboard flexibility — left as a hardening recommendation.
- **chmod 0755 on server-generated runner scripts** (`cookbook_routes.py`) — Low, accepted;
  content is server-controlled in a log dir.
- **HuggingFace downloads without revision pinning** (OD fusion/training scripts) — supply-chain
  malleability; Low. Revisions should be pinned on model downloads.
- **41 pre-existing Bandit Low + whole-tree baseline (~284 structural findings across 142 files)**
  from the 2026-08-13 audit remain visible; this audit did not re-adjudicate every Low.
- Legacy `DATA/kad-1.0` C++ reviewed for severe patterns (clean) but not built with
  ASan in this pass.

## Verification

- Full harness suite: `346 passed in 13.71s`.
- Changed-file gates: ruff clean; `bandit` 0 issues (`vault_manager.py`, `markitdown_runtime.py`);
  PON `pon_tester.py` ✅ APROVADO on `vault_manager.py`.
- `detect-secrets` clean against baseline; `pip-audit`/`npm audit` no known vulns.
- No cloud provider invoked.