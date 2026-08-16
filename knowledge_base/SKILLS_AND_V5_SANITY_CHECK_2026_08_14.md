# Skills and v5 Paper Sanity Check

Date: 2026-08-14

## Executive verdict

The canonical skills are installed consistently, but the skill registry’s
metadata enforcement is weaker than its manifest promises. The Downloads
directory does not contain a separately identifiable v5 paper. The two
available Data Rein PDFs are 10-page, versionless drafts whose content matches
the previously audited document; they are not evidence of a verified v5
revision and are not submission-ready in their current form.

## Artifact identity

The two Gemini explanation files are byte-identical copies:

`/home/amdy/Downloads/gemini explanation.txt` and
`/home/amdy/Downloads/gemini_explanation.txt`

SHA-256: `c09ba1f59a101249956b0d6f40ad2c390411e1096714549d5c87b94af7dd6829`.
They contain project context, not a paper, revision history, benchmark output,
or generation manifest.

The only Data Rein PDFs created in Downloads on 2026-08-14 are:

| File | SHA-256 | PDF evidence |
|---|---|---|
| `DATA_REIN_DOCUMENTO_TECNICO_PTBR.pdf` | `12db631e114d6b6844c78f85678eb95c0370e198e7145019265202342ab29d82` | 10 pages; WeasyPrint 69.0 |
| `DATA_REIN_TECHNICAL_DOCUMENT.pdf` | `0be076d3fdc6e2f8a67759c901b6c6354c5b5aff01c7aac9984898a2c8e55f8c` | 10 pages; WeasyPrint 69.0 |

Neither extracted PDF contains `v5`, `version 5`, `revision 5`, or an equivalent
revision marker. The conclusion below therefore applies to the available draft,
not to an unlocated v5 artifact.

A fresh independent scan at 2026-08-14 11:34 found the same four root-level
artifacts and no filename containing `v5`, `version 5`, or `versão 5` anywhere
under Downloads.

## Skills audit

### Verified

- `src/reins/harness/skill_registry.py` and `reins skills list` expose exactly
  eight canonical skills: `agy-pon-compliance`, `data_rein`,
  `deep-research-paper`, `hermes-persona`, `kad_pon`, `omarchy-aesthetics`,
  `pon_testing_suite`, and `prompt-optimizer`.
- Each canonical entry is a real directory containing `SKILL.md`; the eight
  skills have `name`, `description`, and `tags` frontmatter.
- All eight skills resolve to the canonical source through each of the six
  configured roots: project `.agents`, global `.agents`, `.codex`, `.claude`,
  `odysseus/data/skills`, and `odysseus/integrations/codex/skills`.
- The stale undated skill list in `knowledge_base/PRIME_DIRECTIVE.md` was
  corrected to enumerate all eight. Historical seven-skill entries in
  `SHARED_CONTEXT.md` were left intact as historical records.

### Residual skill issues

1. The manifest promises YAML frontmatter fields, but the registry validates
   only directory names and `SKILL.md` existence. A future missing tag or
   malformed frontmatter would not be rejected by `skill_registry.py`.
2. The directory/manifest name `pon_testing_suite` differs from that skill’s
   frontmatter name `pon-testing-suite`. This is currently link-safe, but it is
   an avoidable discovery/API ambiguity.
3. `skills/pon_testing_suite/scripts/pon_tester.py` is a limited static scanner:
   its security and PON checks are regex-based, it parses Python syntax only,
   scans a restricted set of extensions, and excludes directories such as
   `odysseus`. Its “approved” output cannot substantiate a whole-system “100%
   PON compliant” claim.
4. `deep-research-paper` is intended for papers of roughly 20 or more pages;
   the available artifact is 10 pages. Its workflow is useful, but the draft
   does not demonstrate that the full chunked literature workflow was followed.

## Paper claim audit

The following claims are contradicted or left unproven by the current tree.

| Paper claim | Current evidence | Verdict |
|---|---|---|
| Training uses `ProcessPoolExecutor`, streams batches, and has “zero-memory-leak” ingestion. | The active `src/reins/training/qlora.py` validates JSONL, unloads models, calls one backend, and performs one bounded OOM retry. `ProcessPoolExecutor` is absent from the active tree. | Contradicted / unsupported. |
| `ModelCoordinator` reads `OLLAMA_MAX_VRAM` on every load. | `flake.nix` exports that variable for shells, but `coordinator.py` reads `config/coordinator.json`; the runtime budget is 7.2 GB with headroom and KV overhead. | Contradicted. |
| TELL maintains a JSON Task Trail. | `paths.py` points to `task_trail.sqlite3`; the JSON file is retained only as a migration input. | Contradicted. |
| `pytest tests/test_pon_compliance.py` and a custom AST scanner produced zero violations. | That test file is absent. Current AST law checks live in `tests/test_laws.py`; the bundled skill scanner is regex-based and has narrower scope. | Test identity and scope are unsupported. |
| Thirteen legacy polling loops were found and removed from named Odysseus services. | The current tree contains no reproducible inventory, baseline revision, scan output, or matching `research_handler`/13-loop record. | Historical claim requiring archival evidence, otherwise remove. |
| Ten concurrent agents produced a before/after VRAM stress result, 100% continuity, and no failure. | No benchmark dataset, run command, raw output, timing, token rate, OOM trace, or hardware telemetry is included with the PDFs or repository evidence. | Unsupported empirical result. |
| The MCP UX uses “Web Sockets (via SSE)” and browser SSE notifications. | The live server is configured for MCP `streamable-http`; tests verify that transport and authentication, not a dashboard stress result. WebSockets and SSE are distinct mechanisms. | Terminology and evidence need correction. |
| Strict PON inherently resolves hardware saturation and maximizes token efficiency. | Admission/LRU/fallback code exists, but those causal claims require measured baselines and bounded conditions. | Overclaim. |
| Nix guarantees bit-for-bit identical amdy/tell operation. | The repository has a Nix/uv path, but the paper supplies no lockfile identity, node build logs, or reproducibility hash for both machines. | Unverified; narrow the wording. |

The paper also calls itself “exhaustive,” “comprehensive,” “seamless,” and
“incontrovertible” in places where it presents no reproducible measurement. These
should be replaced with bounded, falsifiable statements.

## Academic and visual sanity check

- The PDFs render cleanly on the inspected first and final pages: no clipping or
  broken glyphs was observed.
- The English and Portuguese abstracts contain approximately 220 and 284 words,
  respectively, within the 150–500-word range in the UTFPR/ABNT project skill.
- Numbered sections 1–6 and a reference list are present.
- No table of contents, figure/table inventory, benchmark table, appendix, or
  reproducibility appendix appears in the 10-page artifact. The title page and
  abstract are combined on page 1, so the document should be checked against the
  target UTFPR submission template before submission.
- The reference list has eight entries. The PON entry is described as “Internal
  Literature and Architectural Guidelines,” which is not sufficient by itself
  as a verifiable scholarly source; its exact UTFPR repository or publication
  record should be supplied.

## Required disposition

Do not label either available PDF as v5. To complete a v5 audit, place the actual
v5 PDF or source package in Downloads and preserve its filename, SHA-256, source
commit, generation inputs, and benchmark artifacts. Before submission, replace
the contradicted implementation descriptions, attach reproducible test and
stress evidence, narrow absolute claims, and reconcile the references with
primary sources.

## Evidence commands

The audit used `find`/`sha256sum`, `pdfinfo`, `pdftotext`, rendered-page
inspection, `python src/reins/harness/skill_registry.py`, the six-root symlink
check, the focused skill installer tests, and the PON scanner. The focused
installer suite passed 7 tests, Ruff passed for the changed test, and the
harness-target PON scan passed. A wider run of the coordinator, training, MCP,
and law tests exposed three current failures: malformed training data reaches
`_train_once` (`tests/test_training.py`), two broad handlers lack diagnostics
(`mcp_server.py:202` and `digest.py:193`), and the untracked
`reins.harness.autonomous` module lacks a test reference. Repository changes and
test results are intentionally not represented as paper evidence unless the
paper records the exact revision and command.

Primary repository source anchors: [canonical manifest](../skills/MANIFEST.md),
[skill registry](../src/reins/harness/skill_registry.py), [installer](../scripts/install_skills.sh),
[PON scanner](../skills/pon_testing_suite/scripts/pon_tester.py),
[coordinator](../src/reins/harness/coordinator.py), [training entry point](../src/reins/training/qlora.py),
[Task Trail paths](../src/reins/harness/paths.py), [Task Trail implementation](../src/reins/services/task_trail.py),
[PON/law tests](../tests/test_laws.py), [MCP server](../src/reins/harness/mcp_server.py),
and [previous draft audit](ACADEMIC_PAPER_SANITY_CHECK_V3.md).
