# SHARED PERSONA CONTEXT
> Synchronized at: 2026-07-02 11:26:28
> Source: Antigravity Architect Brain

This document contains the latest architectural changes, historical context, and technical implementation plans across the Data Harness ecosystem. All agent personas MUST read and align with this context before making decisions.

## 1. Master Walkthrough (Historical Context)
# BAK-1.1 Global Consolidation & Systemd Hooks Walkthrough

*This walkthrough details the execution of the Data Harness restructuring, OS-level integration of the backup service, and the RAG-optimized Obsidian Vault creation.*

## 1. Systemd OS Hooks (BAK-1.1 Automation)
To guarantee that a backup occurs whenever the system restarts or shuts down (preventing data loss or state desync), I created native systemd hooks that block the OS shutdown sequence securely using PON principles:
- **Created** `~/data_rein/services/systemd/pon_shutdown_trigger.py`: A Python PON script that safely blocks utilizing `threading.Event` (zero CPU cycles) while waiting for the MQTT `backup_service` to confirm a successful synchronization across all 4 locations.
- **Created** `~/data_rein/services/systemd/bak-on-shutdown.service`: A `oneshot` systemd unit file configured with `Before=poweroff.target reboot.target`.
- **Validation**: Wrote `~/data_rein/tests/test_shutdown_pon.py`. The PON test battery verified exactly 0 errors across the mocking of the OS shutdown block constraints.

## 2. RAG-Optimized Data Consolidation
The `~/data_rein` root directory was cluttered, hindering AI model vector ingestion (RAG) and architectural clarity.
- **Created** `~/data_rein/scripts/legacy/` to store old, loose scripts (e.g., `teste_reatividade_pon.py`, `gen_config.py`).
- **Archived BAK 1.0**: The original `BAK 1.0` implementation directory was officially migrated and deleted. Its theoretical foundation (`SISTEMA BAK 1.0.md`) was safely preserved inside the new Vault.

## 3. Obsidian Vault (`data-oby`)
To vastly improve the AI's ability to search your history and context via RAG, a massive monolithic markdown file was converted into an organized Obsidian Vault:
- **Initialized** `~/data_rein/data-oby/.obsidian`
- **Atomic Splitting**: I engineered a Python parser that split the monolithic `data_hermes_wiki.md` into **31 distinct, atomic Markdown files** inside `~/data_rein/data-oby/Wiki/`. 
- **Why this matters**: When you use AI (like NotebookLM or RAG pipelines) against the `data-oby` vault, the vectors are now bound to specific, small documents (e.g., `Architecture/BAK-1.0_Archive.md` or `Tipos de Microservices.md`). This increases precision and drastically reduces context token waste.

## Summary of State
- `BAK 1.0` is officially deprecated in favor of **BAK-1.1** (automated via Systemd and MQTT).
- The `data_rein` root is strictly pedantic and organized.
- The `data-oby` Vault is online and populated with 31 atomic historical documents ready for ingestion.


---

## 2. Master Implementation Plan (Current Goals)
# Implementation Plan: Handoff, RAG Ingestion, and `data_rein` Migration

This plan outlines the architecture for the RAG ingestion pipeline, the local LLM failsafe handoff script, and the pedantic global renaming of the `data_rein` workspace to `data_rein`.

## User Review Required

> [!CAUTION]
> **Workspace Renaming Risk**
> Renaming the root folder from `~/data_rein` to `~/data_rein` will break your current terminal sessions. Any active `tmux` panes or `uv run` commands currently inside `~/data_rein` will become orphaned. After I execute this rename, you will need to manually run `cd ~/data_rein` in your terminal to continue working.
> 
> Furthermore, I will use a global sed-replacement script to rewrite every single mention of `data_rein` to `data_rein` inside Python files, Systemd services, JSON configs, and Markdown files. Do you approve this invasive rename?

> [!WARNING]
> **Local LLM Handoff Strategy**
> To prevent goal failure due to Gemini token limits, the **very first thing** I will do upon your approval is write `~/data_rein/local_llm_handoff.py`. This script will contain the precise instructions, paths, and current execution state. If my loop drops, you can simply run `python local_llm_handoff.py`, which will format a prompt and send it to your local Odysseus/Ollama instance to finish the remaining tasks.

## Proposed Changes

### 1. Fail-Safe: Local LLM Handoff
#### [NEW] `~/data_rein/scripts/local_llm_handoff.py`
- Create a Python script that reads the current task list and context.
- Formats a strict PON-compliant prompt.
- Sends the prompt to the local `Odysseus` agent via the local Ollama API so it can seamlessly resume the refactoring process if the cloud API fails.

### 2. RAG Extraction Pipeline (Updating Central Intelligence)
#### [NEW] `~/data_rein/scripts/ingest_training_data.py`
- Create a script that iterates over all PDFs and Markdown files currently resting in `~/data_rein/training_data/text/`.
- Passes them through the existing `extraction_pipeline` (utilizing `PDFExtractor` for the PDFs).
- Synthesizes the extracted text and injects the distilled RAG vectors/summaries directly into the `data-oby` Obsidian Vault and the `SHARED_CONTEXT.md` (the "Central Intelligence").

### 3. Global Project Rename (`data_rein` -> `data_rein`)
#### [MODIFY] `~/data_rein/*` (All Files)
- Run a Python AST/Regex replacement script across the entire repository to pedantically replace every occurrence of the string `data_rein` with `data_rein`. This includes MQTT topics (e.g., `data_rein/extract/trigger` becomes `data_rein/extract/trigger`), Python imports, config files, and systemd units.
#### [RENAME] `~/data_rein` -> `~/data_rein`
- Move the entire physical directory.
- Re-run `uv sync` to fix the virtual environment paths.

## Verification Plan
1. Ensure `local_llm_handoff.py` correctly queries the local Ollama daemon.
2. Verify that the RAG pipeline correctly parses the PDFs and populates the `data-oby` vault.
3. After the global rename, run `uv run pytest tests/ -W error` from inside `~/data_rein` to mathematically prove that no internal paths or MQTT topics were broken during the transition.



## RAG Ingestion Update
- 71 academic PDFs extracted and appended to the Vault for RAG intelligence.
