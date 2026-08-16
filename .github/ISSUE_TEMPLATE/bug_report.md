---
name: Bug report
about: Report a defect in the data_rein harness
title: "[bug] "
labels: bug
assignees: ""
---

## Summary
<!-- One clear sentence describing the bug. -->

## Repro steps
1. Command / scenario: `reins ...`
2. Expected behaviour:
3. Actual behaviour:

## Environment
- `reins --version` / git ref (`git rev-parse --short HEAD`):
- Python version (`python --version`):
- Node / Ollama / ComfyUI versions if relevant:
- OS / machine (amdy / tell):

## Crash / logs
<!-- Paste the relevant traceback or log lines. Trim secrets. -->
<details><summary>logs</summary>

```text

```
</details>

## Scope check
<!-- The harness is PON (zero-polling) and local-first. Confirm the relevant law: -->
- [ ] This is reproducible outside the interactive agent layer (i.e. from the `reins` CLI or a known caller).
- [ ] No secrets are included above.

## Definition of done
<!-- What will make this verifiably "fixed"? Leave blank if unsure; maintainers may fill in. -->
- [ ] A minimal failing test is added under `tests/` (prefer a regression test).
- [ ] `uv run ruff check src tests scripts`, `uv run pytest tests/ -q` and the CI gate (`uv run basedpyright --baselinefile .basedpyright-baseline.txt`) stay green.