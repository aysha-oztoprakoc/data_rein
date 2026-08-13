# Security Audit — 2026-08-13

**Task Trail:** `7f2b8251-513e-4d93-a8a0-cc74d15a3ee1`  
**Scope:** harness code, active scripts and shell tools, MCP stdio/HTTP boundaries,
canonical skills, backup/archive, model install, and local routing. No cloud provider
was invoked during this audit.

## Result

The audited delivery closes all Medium and High Bandit findings. Its original final
broad scan reported **0 Medium, 0 High, and 43 Low** findings with **8 narrow,
justified inline skips**. Post-audit reconciliation has reduced the current scan to
**41 Low** without adding suppressions. This is a security posture statement, not a
claim that the remaining Low findings or inherited structural debt are absent.

## Threat-to-control mapping

| Threat | Control | Observed result and evidence |
|---|---|---|
| Arbitrary or duplicated skill content writes | `skills/MANIFEST.md` is the canonical registry; `skill_registry` rejects symlinked/non-manifest entries; the injector only validates/lists registry entries and directs installation to `reins skills install`. | The injector driver and CLI listed exactly seven skills; temporary and live installer scenarios succeeded. `.omo/evidence/briefing-docs-lane/README.md`, `.omo/evidence/mcp-auth-lane/skills-cli-followup/qa-skills-list.txt`, `.omo/evidence/skills-process-ssh-lane/claim-3/report.txt`. |
| Secret disclosure or insecure HTTP token creation | Vault-backed token provisioning encrypts before replacement, constrains key/vault modes, and leaves no plaintext or temporary token artifact. | Provisioning changed ciphertext with key `0400`, vault `0600`, and zero plaintext/temp artifacts. `.omo/evidence/mcp-auth-lane/vault-provision-followup/live-provision.txt`, `live-http-qa-final.txt`. |
| Unauthenticated or DNS-rebound MCP access | HTTP MCP requires its token and validates local host policy; stdio remains an explicit local surface. | Real unauthenticated HTTP received `401`; authenticated discovery returned server `reins` and 24 tools; non-loopback was rejected. `.omo/evidence/mcp-auth-lane/vault-provision-followup/live-http-qa-final.txt`, `qa-asgi-http.txt`. |
| Hung or unclean MCP termination | Signal handling shuts down the server without exposing a traceback. | Ctrl+C scenario returned `0`, emitted a clean-shutdown marker, and showed no traceback/KeyboardInterrupt text. `.omo/evidence/mcp-auth-lane/interrupt-followup/live-ctrl-c-qa.txt`. |
| Cloud escape from ordinary routing | Execution planes separate `local_text`, `cloud_text`, and image providers; only explicit gated cloud tools may cross the cloud boundary. | Real `route_local` used `llama3.1:8b`, provider `ollama`, node `amdy`, and completed locally; no cloud provider was invoked. `.omo/evidence/privilege_router_lane/verification_claim_3/critical_scenarios.txt`. |
| SQL injection, unsafe XML/downloads, insecure temporary paths, and unsafe artifacts | Remediations narrow each dangerous operation; Bandit suppressions are line-specific and proven rather than global exclusions. | Unfiltered final scan has no Medium/High result. `.omo/evidence/security_gate_lane/bandit-unfiltered-final.json`, `bandit-unfiltered-final-summary.json`. |
| Known vulnerable dependencies | Locked dependency audit and upgrade of the affected crypto package. | `cryptography` moved from 49.0.0 to 50.0.0 after `PYSEC-2026-3552`; final audit has no known vulnerability, apart from the unauditable local package. `.omo/evidence/security_gate_lane/pip-audit.log`, `pip-audit-final.log`. |
| Comfy/model-install partial state | Install failure is fail-closed and does not publish final model or temporary artifacts. | Failing installer exited `1`, final model absent, temporary files `0`. `.omo/evidence/ingestion-backup-supply-lane/comfy-fail-closed.log`. |
| Archive/backup exposure or corrupt output | Archive verifies observable content; backup constrains rescue/archive/directory modes. | Archive completed with content observed; modes were `0700`, `0600`, and `0700`. `.omo/evidence/ingestion-backup-supply-lane/archive-manual-qa.log`, `backup-manual-qa.log`. |
| SSH host/key misuse or unsafe process launch | SSH enrollment checks non-TTY and host-key mismatch paths; privileged calls use exact argument vectors. | SSH scenario evidence and process boundary report are captured in `.omo/evidence/skills-process-ssh-lane/claim-3/report.txt` and `.omo/evidence/security_gate_lane/manual-security-surface.log`. |

## Security scan progression

| Stage | Invocation / policy | Binary observable | Artifact |
|---|---|---|---|
| Historical baseline | Broad-skip Bandit baseline | Task Trail delivery record: 22 Medium, 18 Low, 0 High | Task Trail `7f2b8251-513e-4d93-a8a0-cc74d15a3ee1` |
| Historical pre-remediation | Unfiltered Bandit scan | Task Trail delivery record: 11 Medium, 0 High | Task Trail `7f2b8251-513e-4d93-a8a0-cc74d15a3ee1` |
| Final | `uv run bandit -r src scripts tools -c pyproject.toml -f json` plus JSON severity assertion | 0 Medium, 0 High, 43 Low; 8 narrow inline skips | `.omo/evidence/security_gate_lane/bandit-unfiltered-final.json`, `bandit-unfiltered-final-summary.json` |

The eight skips are deliberately local and documented at the call sites; they are
not a broad configuration exemption. The 43 Low findings remain visible for later
triage. Direct inspection of the retained JSON artifacts found a historical-record
mismatch: the retained `bandit-unfiltered-before.json` contains 1 Medium/43 Low,
while the current source scan confirms 8 inline skips. The earlier counts above are
preserved as Task Trail history, not re-asserted from those retained JSON files.

## Supply-chain and secret checks

| Scenario | Invocation | Binary observable | Artifact |
|---|---|---|---|
| Dependency CVE | `uv run pip-audit --progress-spinner off` | Initial `cryptography 49.0.0` finding `PYSEC-2026-3552`; after upgrade to 50.0.0, no known vulnerability. Only local `data-rein` cannot be audited on PyPI. | `.omo/evidence/security_gate_lane/pip-audit.log`, `pip-audit-final.log` |
| Credential scan | Tracked regular files <=2 MiB scanned with generated/vendor exclusions for `DATA`, `ComfyUI`, `.obsidian`, and `knowledge_base/ingested_corpus` | Three baseline matches audited false positives: two pinned model revisions and one localhost placeholder; no credential found. | `.omo/evidence/security_gate_lane/secrets-final-summary.txt`, `secrets-size-excluded-final.txt`, `secrets-new-test.json` |
| Shell surface | `uvx --from shellcheck-py shellcheck` over 12 active shell files | 12/12 clean, exit 0. | `.omo/evidence/security_gate_lane/shellcheck-final.log` |

## TDD and quality evidence

Focused red/green evidence is retained under `.omo/evidence/` rather than inferred
from final green output. Relevant red artifacts include
`.omo/evidence/security_gate_lane/red-focused.log`,
`.omo/evidence/mcp-auth-lane/red-focused.txt`, and
`.omo/evidence/ingestion-backup-supply-lane/red-tests.log`; their corresponding
green/final artifacts are colocated in those lane directories.

| Scenario | Invocation | Binary observable | Artifact |
|---|---|---|---|
| Full suite | `uv run pytest -o addopts='' -q` | 296 tests passed. | `.omo/evidence/briefing-docs-lane/README.md` |
| Executable laws | `uv run pytest -o addopts='' -q tests/test_laws.py` | 49 laws passed. | `.omo/evidence/briefing-docs-lane/README.md` |
| Lint | `uv run ruff check --force-exclude ...` | Ruff green. | `.omo/evidence/security_gate_lane/ruff-final.log` |
| Typed changed surfaces | Focused `uv run basedpyright --level error <owned paths>` | 0 errors. | `.omo/evidence/security_gate_lane/basedpyright-final.log`, `.omo/evidence/mcp-auth-lane/final3-basedpyright-focused.txt` |
| Bytecode | `uv run python -m compileall ...` | Green. | `.omo/evidence/mcp-auth-lane/final3-compileall.exit` |

The full-repository BasedPyright attempt was host-killed and produced no usable
completion status. It is therefore **not claimed green**; only the named focused
checks above are claimed.

## Environment verification

- `nix flake check` against the bare flake failed because the required feature was
  disabled. A path-flake retry stalled without output and was interrupted; neither
  was recorded as a Nix pass during the original audit. The post-audit NIX-1
  reconciliation below supersedes this residual.
- Bare system-Python consolidation failed because the required dependency was not
  installed. `uv run ... --dry-run` passed; operators should use the locked `uv`
  environment.
- Stdio MCP discovery reported `reins` with 24 tools, and the local route scenario
  selected `llama3.1:8b` / `ollama` / `amdy`. Evidence:
  `.omo/evidence/mcp-auth-lane/qa-stdio-tools.txt` and
  `.omo/evidence/privilege_router_lane/verification_claim_3/critical_scenarios.txt`.

## Residual risk and deferred work

- 41 Bandit Low findings and 8 narrowly proven inline skips remain visible after
  the shell-boundary reconciliation below.
- A fresh whole-tree no-excuse audit reports 284 structural findings across 142
  files after the resilience reconciliation below. The earlier count of 24 came
  from a narrower audit surface and is not the current repository baseline.
- System Python is not a supported execution environment for consolidation; use
  `uv`.
- No cloud provider was invoked.

## Post-audit NIX-1 reconciliation

The path-flake stall was diagnosed on 2026-08-13 as source-ingress amplification:
`path:.` copied runtime/model trees from the 85 GB working directory, including
49 GB `ComfyUI`, 19 GB `ai_models`, 11 GB `DATA`, and 5.5 GB `odysseus` roots.
The active Nix client had physically read about 35.4 GB and held a file under
`ComfyUI`; daemon/store lock contention and nixpkgs or cross-system evaluation
were independently refuted.

An integration test also exposed that `DATA_REIN_HOME = toString ./.` resolved to
the immutable Nix-store source snapshot. The dev shell now resolves the Git
top-level checkout at activation, with the launch directory as a non-Git fallback.
An isolated source check evaluated both declared systems successfully, and the
x86_64 shell activated from `tests/` with `DATA_REIN_HOME=/home/amdy/data_rein`,
the pinned Python/uv/Ruff toolchain, an offline-clean uv lock, and SQLite import.
The resulting repository gate passed 297 tests, Ruff, focused BasedPyright, and
diff integrity.

## Post-audit encrypted-vault rollback reconciliation

Successful vault mutation now atomically persists the exact previous ciphertext
beside the active vault as `.secrets.enc.bak` before replacing `.secrets.enc`.
Both artifacts are mode `0600`, file-synchronized, atomically replaced, and
followed by parent-directory synchronization while the existing exclusive key-file
lock remains held. No plaintext backup is created.

If active replacement reports failure after the backup succeeds, the writer
atomically restores the previous ciphertext. If that rollback also fails, the
typed failure states that update and rollback failed while the durable encrypted
backup remains available. The public secret API signatures and existing-token
no-rewrite behavior remain unchanged.

The formerly mixed MCP security test module was split at its existing ownership
boundary into `tests/test_vault_security.py` (10 vault scenarios) and
`tests/test_mcp_security.py` (11 MCP scenarios). Red evidence was 7 passing legacy
vault scenarios and 3 failures for the absent backup/rollback contract. Final
verification passed 300 repository tests, 49 executable laws, Ruff, focused
BasedPyright, no-excuse checks, Bandit with 0 Medium/High findings, dependency
audit, diff integrity, and a real isolated Fernet mutation/rollback scenario with
private modes and zero plaintext or temporary artifacts.

## Post-audit shell-boundary reconciliation

Task Trail `9a1f261c-5fbc-49b1-82be-0a4a888bd5ca` closes the active
`os.system("uv pip install cryptography")` fallback in `scripts/encrypt_secrets.py`.
Cryptography is already a locked project dependency, so runtime package installation
was both unnecessary and a shell/PATH injection surface. The script now imports the
declared dependency directly and retains its clean no-plaintext degradation path.

The existing argv-only process law moved from the 250-pure-line `test_laws.py` into
the process-focused `test_security_boundaries.py` and now rejects `os.system` across
all non-legacy active Python sources. The test first failed specifically on the
encryption fallback, then passed after its removal. Final verification passed 300
repository tests, Ruff, focused BasedPyright, no-excuse checks, bytecode compilation,
diff integrity, and dependency audit. A real CLI invocation returned
`No plaintext secrets found. Skipping encryption.` without mutation. Bandit now
reports 0 Medium, 0 High, 41 Low, and the same 8 justified skips.

## Post-audit typed resilience configuration reconciliation

Task Trail `07efa872-24d0-4114-a2d9-f108d01e3104` replaces six anonymous
`ValueError` policy failures with `ResilienceConfigurationError`, a structured
`ValueError` subtype carrying the rejected field and reason. Existing catch sites
remain compatible while callers can now distinguish invalid circuit/retry policy
from unrelated value failures. `CircuitConfig` and `RetryPolicy` are also frozen,
slotted value objects.

A six-case hostile-input test covers every circuit and retry validation branch.
It first failed because all six constructors returned plain `ValueError`, then
passed against the typed contract. The touched resilience type and test modules
now have zero no-excuse findings, down from 16. Final verification passed 306
repository tests, Ruff, focused BasedPyright, bytecode compilation, and diff
integrity. A direct library invocation exposed the structured field/reason and
confirmed backward `ValueError` compatibility. The exact whole-tree baseline is
now 284 findings across 142 files, replacing the stale 24-finding handoff claim.
