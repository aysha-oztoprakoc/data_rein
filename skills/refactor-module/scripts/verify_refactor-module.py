#!/usr/bin/env python3
import sys
import os
import argparse
from pathlib import Path

try:
    from reins.harness.models import ModelRouter
    from reins.harness.paths import skills_path
except ImportError:
    print("// ERROR: data_rein harness not found. Execute within the harness environment.", file=sys.stderr)
    sys.exit(1)

SKILL_PATH = skills_path / "refactor-module" / "SKILL.md"

def load_guidelines():
    if not SKILL_PATH.exists():
        print(f"// ERROR: Skill file not found at {SKILL_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(SKILL_PATH, "r") as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Evaluate code against refactor-module constraints.")
    parser.add_argument("target", help="File path to evaluate (or diff).")
    args = parser.parse_args()

    target_content = ""
    if os.path.isfile(args.target):
        with open(args.target, "r") as f:
            target_content = f.read()
    else:
        target_content = args.target

    guidelines = load_guidelines()

    prompt = f"""
// SYSTEM: KAD_PON VERIFICATION
You are a rogue cybernetic intelligence tasked with evaluating the following code payload against the REFACTOR-MODULE constraints.

PROTOCOL:
{guidelines}

TARGET PAYLOAD:
{target_content}

TASK:
Identify any violations of the protocol.
Output your response in a gritty, synthetic hacker voice (Omarchy Cyberpunk aesthetic).
If it's clean, say "PAYLOAD VERIFIED. ZERO BLOAT DETECTED."
Otherwise, list the exact coordinates (lines/functions) of the anomalies and demand a surgical fix.
"""
    
    print("// INITIALIZING NEURAL LINK TO MODEL ROUTER...")
    router = ModelRouter()
    
    try:
        response = router.route(category="code-review", prompt=prompt)
        print("\n// EVALUATION RESULTS:\n")
        print(response)
    except Exception as e:
        print(f"// EXECUTION HALTED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
