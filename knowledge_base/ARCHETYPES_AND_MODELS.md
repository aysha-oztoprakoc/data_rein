# OhMyOpenAgents (OMO) Archetypes & Model Matrix

This document establishes the canonical organization for all models across the data_rein project, grouped by OhMyOpenAgents archetypes.

## Philosophy & Core Rules
1. **Zero Permissions Default:** All models begin with zero permissions (`permissions: []`). Access to the filesystem, shell, or remote APIs must be explicitly granted on a strict need-to-know basis.
2. **Smooth Execution:** Despite having zero base permissions, the harness automatically bridges necessary context (via Notification-Oriented Paradigm/PON event buses) so models can operate without friction.
3. **Hardware Optimized Defaults:** The default local models are strictly partitioned by VRAM capability:
   - **amdy (RX 9060 XT 8GB)**: Operates high-power 7B-9B class models (Qwen2.5-Coder 7B, Llama3.3 8B, Qwen3.5 9B).
   - **tell (GTX 1060 6GB)**: Operates low-power, fast fan-out 1.5B-3B class models (Qwen2.5 3B, DeepSeek-R1 1.5B, Gemma2 2B).
4. **User Supremacy:** The user holds ultimate veto power over routing and model selection via the config files (`config/model_router.json` and `~/.omo/omo.jsonc`).

---

## 1. Sisyphus (The Coder)
* Relentlessly writes, refactors, and debugs code. Optimized for syntax and logic.
* **Capabilities:** `code_generation`, `code_review`, `debugging`, `syntax_analysis`
* **Default Permissions:** `[]` (Given read/write access to specific project directories *only* during task execution).
* **Hardware Optimal Choices:**
  * **Local (amdy):** `qwen2.5-coder:7b` (Score: 95.0)
  * **Local (tell):** `qwen2.5-coder:3b` (Score: 96.1)
  * **Remote (tier-1):** `claude-3-7-sonnet-20250219`

## 2. Hephaestus (The Architect/Planner)
* Breaks down goals, creates execution plans, and orchestrates lower-level agents.
* **Capabilities:** `planning`, `system_design`, `architecture`, `task_breakdown`
* **Default Permissions:** `[]`
* **Hardware Optimal Choices:**
  * **Local (amdy):** `qwen3:8b` (Score: 97.2) / `llama3.3:8b`
  * **Local (tell):** `deepseek-r1:1.5b` (Score: 98.0)
  * **Remote (tier-1):** `o3-mini`

## 3. Oracle (The High-Reasoning Strategist)
* Deep insight, complex problem solving, and strategic foresight.
* **Capabilities:** `complex_reasoning`, `strategy`, `decision_making`, `foresight`
* **Default Permissions:** `[]`
* **Hardware Optimal Choices:**
  * **Local (amdy):** `qwen3.5:9b` (Score: 96.5) / `phi4-mini` (Score: 95.0)
  * **Local (tell):** `deepseek-r1:8b` (Score: 89.5)
  * **Remote (tier-1):** `claude-3-7-sonnet-20250219`

## 4. Librarian (The Knowledge Keeper)
* RAG extraction, documentation search, and file context synthesis.
* **Capabilities:** `rag`, `summarization`, `knowledge_retrieval`, `document_analysis`
* **Default Permissions:** `[]` (Read-only access to `/knowledge_base`)
* **Hardware Optimal Choices:**
  * **Local (amdy):** `llama3.1:8b` (Score: 89.5)
  * **Local (tell):** `smollm2:1.7b` (Score: 97.8) / `gemma2:2b`
  * **Remote (tier-1):** `gemini-2.5-pro`

## 5. Explore (The Deep Researcher)
* Explores external context, fetches internet data, and broad surveys.
* **Capabilities:** `web_search`, `exploration`, `data_gathering`
* **Default Permissions:** `[]` (Web-search capability provided via MCP searxng bridge only on demand)
* **Hardware Optimal Choices:**
  * **Local (amdy):** `llama3.1:8b` (Score: 89.5)
  * **Local (tell):** `qwen2.5:3b` (Score: 96.1)
  * **Remote (tier-1):** `claude-3-5-haiku-20241022`

## 6. Multimodal-Looker (The Visionary)
* Image analysis, UI to code translation, and visual reasoning.
* **Capabilities:** `vision`, `image_analysis`, `ui_generation`
* **Default Permissions:** `[]`
* **Hardware Optimal Choices:**
  * **Local (amdy):** `bakllava:latest` (Score: 92.5)
  * **Local (tell):** `minicpm-v:8b` (Score: 89.5) / `moondream:1.8b` (Score: 97.6)
  * **Remote (tier-1):** `gpt-4o`

## 7. Prometheus (The Creator)
* Generates raw assets, images, audio, and large unstructured outputs.
* **Capabilities:** `asset_generation`, `image_generation`, `audio_generation`
* **Default Permissions:** `[]`
* **Hardware Optimal Choices:**
  * **Local (amdy):** `comfyui_sdxl_base` (Score: 95.0), `comfyui_audio_bark` (Score: 92.0)
  * **Local (tell):** `llama3.1:8b-instruct-q4_K_M` (Score: 89.5)
  * **Remote (tier-1):** `dall-e-3`

## 8. Metis (The Optimizer & Reviewer)
* Evaluates output, optimizes prompts, and performs critical quality control.
* **Capabilities:** `code_review`, `prompt_optimization`, `quality_control`, `evaluation`
* **Default Permissions:** `[]`
* **Hardware Optimal Choices:**
  * **Local (amdy):** `qwen3.5:9b` (Score: 96.5)
  * **Local (tell):** `deepseek-r1:1.5b` (Score: 98.0)
  * **Remote (tier-1):** `claude-3-7-sonnet-20250219`

## 9. Momus (The Generalist Orchestrator)
* Handles routine conversational tasks, user alignment, and dynamic routing.
* **Capabilities:** `general_chat`, `orchestration`, `routing`, `formatting`
* **Default Permissions:** `[]`
* **Hardware Optimal Choices:**
  * **Local (amdy):** `llama3.3:8b` (Score: 95.8)
  * **Local (tell):** `qwen2.5:3b` (Score: 96.1)
  * **Remote (tier-1):** `gpt-4o-mini`
