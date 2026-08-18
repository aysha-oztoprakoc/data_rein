---
name: deep-research-paper
description: Optimize the workflow for writing massive, extremely deep academic papers and monographs by chunking generation, organizing literature, enforcing Plan-Draft-Revise, and eliminating LLM writing smells.
tags: "academic, research, writing, chunks, handoff, model-agnostic, scaling, anti-smell"
---

# Deep Research Paper Generator (Optimized Workflow)

Use this skill when the user requests an extremely long, deep, or thoroughly researched academic document (e.g., TCC, monograph, 20+ pages paper) that exceeds the token output limits of a single model response.

This skill is inherently **model-agnostic** and relies on a structured handoff pipeline separating literature gathering from massive text generation, adhering to the highest standards of academic integrity.

## Category Mapping (for `route_local` and `reins batch`)

When routing tasks to local models, use these harness categories:

| Paper Task | Router Category | CLI Shortcut |
|------------|----------------|--------------|
| Literature summarization / RAG | `librarian` | `reins summarize <file>` |
| Deep technical section drafting | `oracle` | `reins run oracle "<prompt>" --rag` |
| Architecture / methodology sections | `hephaestus` | `reins run hephaestus "<prompt>" --rag` |
| Quality review / prompt critique | `metis` | `reins run metis "<prompt>"` |
| Quick Q&A / formatting | `momus` | `reins ask "<question>"` |
| Batch over many prompts | any of the above | `reins batch <category> <file> --rag` |

For ABNT-formatted papers (Brazilian academic context), also read
`skills/utfpr-tcc-abnt/SKILL.md` which defines the NBR 14724 structure,
NBR 10520 citation format, and NBR 6023 reference format.

## Phase 1: Planning & Literature Organization (Low-Cost)
1. **Search & Fetch**: Use web search (e.g. Google Scholar, ArXiv) to find the absolute latest papers (current year) on the requested topics.
2. **Organized Downloads**: Create categorized subfolders in `~/Downloads/DATA_REIN_REFERENCES/` (e.g., `/PON_Theory/`, `/NixOS/`). Download PDFs using `curl` or `wget`. For webpages, save both HTML and generate a PDF using `weasyprint`.
3. **Model Handoff (Summarization & Outlining)**: Do **not** exhaust the primary agent's context reading raw PDFs.
   - Use the `route_local` tool or `reins batch "<category>"` to cheaply summarize PDFs and extract citations using a localized model (e.g., a fast Qwen or Llama 8B). Use the `librarian` category for summarization, `oracle` for outline generation.
   - Generate a strict outline based *only* on the verified literature. Validate facts before proceeding.
4. **Ingest into Wiki**: Run `reins digest ~/Downloads/DATA_REIN_REFERENCES/<topic>/ --recursive` to make all downloaded literature searchable. Subsequent `--rag` calls will automatically inject relevant wiki context into model prompts.

## Phase 2: Chunked Academic Drafting (High-Capacity)
1. **Bypass Token Limits**: Divide the paper into discrete logical chunks based on the outline (e.g., `chunk1_intro.md`, `chunk2_methodology.md`).
2. **Drafting (NO LLM SMELLS)**: Generate each chunk sequentially using explicit constraints:
   - **Banned Adjectives:** *seamless, elegant, vivid, colossal, masterpiece, violently, undeniably, crucially, paradigm-shifting, groundbreaking, exhaustive, comprehensive, incontrovertible, inherently resolves.*
   - **Tone:** Use strict, dry, objective, and passive academic voice. Let the facts and citations speak for themselves; do not use marketing or flowery language.
3. **Structural Triad (Mandatory for Technology Sections)**: For each technology covered, the section MUST be structured as:
   - **Theory:** Meta-explanation of the pure theoretical mathematics/physics/science behind it.
   - **Application:** How this exact theory was specifically applied and engineered in this specific project.
   - **Room for Improvement / Next Steps:** Detailed academic description of current limitations and precise future steps to be taken.
4. **Storage**: Save all generated chunks to a temporary location (e.g., `scratch/` in the brain/workspace directory).

## Phase 3: Revising, Assembly & Recipe Generation
1. **Anti-Smell Validation**: Before reviewing content, run the companion script to catch banned words:
   ```bash
   bash skills/deep-research-paper/scripts/smell_check.sh scratch/chunks/chunk*.md
   ```
   Fix any matches before proceeding.
2. **Iterative Review**: Review the chunks for logical gaps or inconsistent flow. 
3. **Recipe for Improvement**: Generate a consolidated section detailing the "Recipe for Improvement" mapping all the Next Steps identified into a cohesive future-work architecture.
4. **Merge**: Once all chunks are written to disk and reviewed, use a deterministic script to concatenate them. You can use `scripts/merge_chunks.py` located in this skill's directory.
5. **Transparency**: Ensure a section is added (usually Methodology or Acknowledgments) disclosing the use of the `data_rein` AI harness for structural drafting.
6. **Deliver**: Provide the single, unified markdown file to the user.

## Important Constraints
- **Strictly Academic**: Do not include business plans or commercial projections unless explicitly requested. 
- **True Depth**: Do not summarize sections. Expand deeply on mathematical and computational physics. Use strict ABNT formatting (if Brazilian context applies).
- **Human-in-the-Loop**: Always encourage the user to verify claims against the downloaded primary sources.
