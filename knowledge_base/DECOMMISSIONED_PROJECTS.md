# // DECOMMISSIONED PROJECTS — data_rein

> Record of top-level directories removed from the working tree during the
> 2026-07-05 repo audit, so their existence and reason for removal isn't lost.
> This is a manually-maintained log, not auto-generated.

## `godot_project/`
Empty directory, zero files, never had any content committed. A future-project
stub that was never started. Removed 2026-07-05.

## `nixos_migration/` + `nix/`
An abandoned attempt at a NixOS-based deployment/migration path
(`configuration.nix`, `infect_tell.sh`, a `nix/README.md`). Superseded by the
current harness's actual deployment approach (plain venv + systemd units, see
`src/reins/services/backup.py` and `scripts/install_bin.sh`). Removed 2026-07-05.

## `ttrpg_dashboard/`
A never-built future-project stub, unrelated to the core harness. Removed
2026-07-05.

## `python_core/`
Pre-"Grand Convergence" (2026-07-03 "Universal Harness Convergence" commit)
scaffold, untouched by that refactor and never referenced by `src/reins/`.
Contained a `tests/scraper_benchmark.py` and similar orphaned scripts. Removed
2026-07-05.

## `cpp_core/`
Legacy C++ build directory (CMake cache/build artifacts only, no source of
lasting value). The actual PON architecture patterns this represented
(`SharedAttribute<T>`, `Rule{Premises→Actions}`, `Notifier`, `Instigation`)
are preserved conceptually in `skills/kad_pon/SKILL.md`, ported from the
original implementation at `DATA/kad-1.0/tell/src/pon/` (left in place, in
the separate `DATA/` repo, not part of this removal). Removed 2026-07-05.

## `DATA/kad-1.0/odysseus/`
An 11GB stale duplicate of the live, actively-developed `odysseus/` checkout
at the repo root, sitting inside the separate `DATA` nested git repository
(remote: `aysha-oztoprakoc/DATA`). Before removal, it was diffed against the
live `odysseus/` and found to carry 8 modified files with real, unique local
customizations never ported forward — all salvaged into the live `odysseus/`
first:
- An "omarchy" cyberpunk theme (`static/js/theme.js`, `static/style.css`,
  `static/img/cyberpunk_bg.png`) matching `knowledge_base/AESTHETIC_DIRECTIVE.md`
  (Blood Red `#ff4040` on Black `#200000`) — set as the new default theme.
- A `DEFAULT_SYSTEM_PROMPT` env var in `docker-compose.yml` that makes
  Odysseus's chat agent read the harness's init files on session start —
  adapted on port to match the real documented protocol (`PRIME_DIRECTIVE.md`
  then `SHARED_CONTEXT.md`, per `CLAUDE.md`), not just `SHARED_CONTEXT.md`
  as the stale copy had it.
- A GGUF-download fallback heuristic (`static/js/cookbookDownload.js`).
- An `AUTH_ENABLED` bypass flag in `routes/shell_routes.py` (disables
  admin-only gating on shell exec when set to `false` — security-relevant,
  ported at explicit user request).
- A host home-directory bind mount (`/home/amdy:/home/amdy:z`) for local LLM
  tool access from inside the container.
- The Dockerfile's Python-version pin needed no porting — the live
  `odysseus/` was already on Python 3.12 for both build stages (documented
  reason: Real-ESRGAN deps break on 3.13+).
- The remaining diff (a ~40k-line `services/hwfit/data/hf_models.json`
  change) was just a stale model-catalog cache, not logic — not ported.

Removed 2026-07-05 via `git rm -rf` + commit **within the `DATA` repo only**
(not pushed to its remote) — this is a separate repository's history from
`data_rein`'s, cross-referenced here for the record.
