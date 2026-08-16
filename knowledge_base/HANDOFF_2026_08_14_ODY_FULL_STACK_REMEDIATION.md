# Odysseus full-stack remediation handoff

**Task Trail:** `a2772747-94e6-4f64-ba03-c5fcc9e33a09`  
**Audited commits:** `b091950` (`feat(wiki): unified full-stack wiki editor integrated with odysseus`) and `2674a53` (`fix: pedantic frontend and backend safety sweep and bug squash`)  
**Signed:** Codex — sanity/safety/performance audit

## Initial sanity verdict

The audited state was not release-ready. Its full Odysseus suite reported `4431 passed, 3 skipped, 4 failed`. The exact failures were:

1. `tests/test_gpu_compose_standalone.py::test_nvidia_standalone_equals_base_plus_overlay`
2. `tests/test_gpu_compose_standalone.py::test_amd_standalone_equals_base_plus_overlay`
3. `tests/test_gpu_compose_standalone.py::test_amd_odysseus_adds_only_overlay`
4. `tests/test_model_routes.py::TestDockerLoopbackRewrite::test_rewrites_loopback_when_in_docker`

## Critical findings remediated

1. `/api/reins/system/secret` could reveal any decrypted vault value after checking only that a password field was non-empty. The API and browser UI were removed permanently. No browser route now returns decrypted secrets.
2. The Files Explorer exposed mounted host files to unrestricted read, write, delete, traversal, archive extraction, resource exhaustion, and filename-based DOM injection. It is now unregistered by default and available only through an authenticated, freshly reauthenticated, five-minute server-side capability with configured roots, secret-path denial, canonical no-symlink containment, bounded operations, exact recursive-delete confirmation, safe archive staging, and DOM `textContent` rendering.
3. Wiki page edits posted to a `PUT` route, memory edits silently created duplicates, and slugs entered inline JavaScript. Wiki CRUD now crosses an authenticated bounded MCP contract; pages update with `PUT`; specific memories have a single-item read; memories remain content-addressed and immutable, so revision creates a replacement while deletion of the old record remains a separate confirmed action; inline handlers were removed.

## Ordered remediation status

1. **Complete — immediate containment and baseline repair.** The secret-revelation route/UI is gone. `ODYSSEUS_FILES_ADMIN_ENABLED` defaults to `false`, controls are omitted from served HTML, and the router is not mounted unless explicitly enabled. AMD/NVIDIA overlays match the base contract and Docker loopback rewrite is deterministic under test.
2. **Complete — high-risk Files Admin boundary.** Operations are limited to configured roots (default `/home/amdy/data_rein` and `/home/amdy/data-workspace`), deny secret-bearing paths, reject symlinks and traversal, and enforce: 100-entry browse pages, 2 MiB text reads/writes, 25 MiB uploads, 5,000 archive entries, and 250 MiB expanded archives. Archive links/devices/traversal/bombs are rejected before staged publication. Actions emit content-free audit events.
3. **Complete — Wiki harness boundary and UI semantics.** Odysseus no longer imports `reins.harness`, SQLite, or blocking subprocess work in these routes. Bounded page/memory list, get, create, update/revise, and delete operations are MCP tools backed by the monolithic `knowledge_base/wiki.db`. List responses omit full content; stale searches are cancelled; CLI actions queue Task Trail work and return an operation ID.
4. **Tooling complete; publication intentionally blocked — deterministic Obsidian export.** `scripts/export_to_obsidian.py` now requires an explicit source revision, builds in staging, assigns deterministic names/content, writes `.export-manifest.json` with counts, mappings, hashes, and source revision, validates manifest ownership/stale files, scans every staged file for secrets, then atomically swaps with rollback. The full current export was rejected by the secret scanner. The previous 905-file, 82 MiB vault remained byte-for-byte in place, with no partial manifest or staging tree. This is the required fail-closed outcome; remediate the flagged source content before trying to publish again. Never bypass the scan.
5. **Complete — performance and evidence gates.** A 10,000-memory fixture verifies bounded list/search p95 below 250 ms and payload below 500 KiB. Hostile path, symlink, archive, upload, XSS, capability expiry, CRUD semantics, deterministic export, and failed-scan preservation tests are present. Live browser QA covered 375, 768, and 1280 px disabled views plus the enabled Files Admin workflow; it observed no Files/secret controls when disabled, safe literal rendering of a hostile filename, successful specific-file editing, no injected image/dialog, and no page errors. Two independent read-only visual reviews passed; one noted only that the modal Close label is visually tight but operable.

## Validation evidence

Run from `/home/amdy/data_rein` unless a command changes directory:

```bash
.venv/bin/python -m pytest -q
# 333 passed in 12.33s

cd odysseus
/home/amdy/data_rein/.venv/bin/python -m pytest -q
# 4451 passed, 3 skipped, 8 warnings in 106.75s

/home/amdy/data_rein/.venv/bin/python -m pytest -q \
  tests/test_files_admin_security.py \
  tests/test_serve_html_with_nonce.py \
  tests/test_reins_routes.py \
  tests/test_gpu_compose_standalone.py \
  tests/test_model_routes.py::TestDockerLoopbackRewrite::test_rewrites_loopback_when_in_docker \
  tests/test_run_order_report.py::test_subprocess_failure_exit_code_and_footer
# 39 passed

npx eslint static/js/filesExplorer.js static/js/harness.js static/app.js
# exit 0

cd ..
semgrep scan --config p/security-audit --no-git-ignore \
  odysseus/routes/files_routes.py odysseus/routes/files_security.py \
  odysseus/routes/files_archive.py odysseus/routes/reins_routes.py \
  odysseus/routes/reins_wiki_routes.py src/reins/harness/wiki_contract.py \
  src/reins/harness/mcp_server.py scripts/export_to_obsidian.py
# 0 findings

.venv/bin/bandit -q \
  odysseus/routes/files_routes.py odysseus/routes/files_security.py \
  odysseus/routes/files_archive.py odysseus/routes/reins_routes.py \
  odysseus/routes/reins_wiki_routes.py src/reins/harness/wiki_contract.py \
  src/reins/harness/mcp_server.py scripts/export_to_obsidian.py
# exit 0
```

The scoped Ruff and BasedPyright error-level checks also exit cleanly. Compose overlay coverage is included in the full suite and passed all 12 overlay cases.

## Safe vault publication command

After reviewing and removing every scanner finding from the source Wiki, run with the exact reviewed revision rather than an implicit moving ref:

```bash
uv run --script scripts/export_to_obsidian.py \
  --database knowledge_base/wiki.db \
  --output wiki_vault \
  --source-revision '<reviewed-full-commit-sha>' \
  --bootstrap-existing
```

Use `--bootstrap-existing` only for the first reviewed adoption of the pre-manifest vault. Subsequent exports must rely on the tracked prior manifest so stale-file removal remains ownership-bounded.
