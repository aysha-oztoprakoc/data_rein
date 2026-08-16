#!/usr/bin/env python3
"""
Autonomous codebase analysis pipeline. Uses the local models via reins workflow batch
to read, summarize, and ingest codebase structure into the WikiDB.
"""

import sys
import argparse
from pathlib import Path

# Ensure src is in sys.path
repository_root = Path(__file__).resolve().parents[1]
if str(repository_root / "src") not in sys.path:
    sys.path.insert(0, str(repository_root / "src"))

from reins.harness.workflow import batch, BatchItem
from reins.harness.wiki import WikiDB
from reins.harness.trust_anchor import KnowledgeValidator

def main():
    parser = argparse.ArgumentParser(description="Deploy the local army to analyze the codebase.")
    parser.add_argument("--target", type=str, default="src/reins", help="Target directory or file relative to repo root.")
    args = parser.parse_args()

    target_path = (repository_root / args.target).resolve()
    if not target_path.exists():
        print(f"Target path {target_path} does not exist.")
        sys.exit(1)

    prompts = []
    file_mapping = {}
    
    def process_file(filepath: Path):
        if "__pycache__" in filepath.parts or filepath.name.startswith("."):
            return
            
        try:
            content = filepath.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return
            
        if not content.strip():
            return
            
        # Limit content size for local models (first 16KB)
        content = content[:16000]

        rel_path = filepath.relative_to(repository_root)
        prompt = (
            f"Analyze the following source code file from the data_rein project.\n"
            f"File: {rel_path}\n"
            f"Document its primary purpose, key classes/functions, and architectural role. "
            f"Provide your answer in concise Markdown.\n\n"
            f"```python\n{content}\n```"
        )
        prompts.append(prompt)
        file_mapping[len(prompts) - 1] = rel_path

    if target_path.is_file():
        if target_path.suffix == ".py":
            process_file(target_path)
    else:
        for filepath in target_path.rglob("*.py"):
            process_file(filepath)

    if not prompts:
        print("No Python files found to analyze.")
        sys.exit(0)

    validator = KnowledgeValidator()
    
    def on_result(item: BatchItem):
        filepath = file_mapping[item.index]
        if not item.ok or not item.text:
            print(f"[FAILED] Could not analyze {filepath}: {item.error}")
            return
            
        score = validator.validate_update(item.text, "army")
        
        slug = f"analysis_{str(filepath).replace('/', '_').replace('.', '_')}"
        try:
            with WikiDB() as db:
                db.upsert_page(
                    title=f"Codebase Analysis: {filepath}",
                    content=item.text,
                    slug=slug,
                    category="codebase_analysis",
                    fmt="md",
                    trust_score=score
                )
            print(f"[SUCCESS] Ingested analysis for {filepath} (score: {score})")
        except Exception as e:
            print(f"[ERROR] Failed to save analysis for {filepath} to WikiDB: {e}")

    print(f"Deploying army to analyze {len(prompts)} files in {args.target}...")
    batch(category="summarize", prompts=prompts, node="amdy", on_result=on_result)
    print("Done.")

if __name__ == "__main__":
    main()
