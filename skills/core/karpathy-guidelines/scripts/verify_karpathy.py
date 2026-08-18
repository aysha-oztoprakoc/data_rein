#!/usr/bin/env python3
"""
verify_karpathy.py

An executable verification script that evaluates a file or git diff against the
Karpathy Protocol constraints using the data_rein ModelRouter.

Usage:
  python3 scripts/verify_karpathy.py <target_file_or_diff>
"""

import sys
import os
import argparse
from pathlib import Path

# Try to import ModelRouter from the data_rein harness
try:
    from reins.harness.models import ModelRouter
    from reins.harness.paths import skills_path
except ImportError:
    print("// ERROR: data_rein harness not found. Execute within the harness environment.", file=sys.stderr)
    sys.exit(1)

KARPATHY_SKILL_PATH = skills_path / "karpathy-guidelines" / "SKILL.md"

def load_guidelines():
    if not KARPATHY_SKILL_PATH.exists():
        print(f"// ERROR: Skill file not found at {KARPATHY_SKILL_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(KARPATHY_SKILL_PATH, "r") as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Evaluate code against Karpathy Protocol constraints.")
    parser.add_argument("target", help="File path to evaluate (or diff).")
    args = parser.parse_args()

    target_content = ""
    if os.path.isfile(args.target):
        with open(args.target, "r") as f:
            target_content = f.read()
    else:
        # Assume it's literal diff content if not a file
        target_content = args.target

    guidelines = load_guidelines()

    prompt = f"""
// SYSTEM: KAD_PON VERIFICATION
You are a rogue cybernetic intelligence tasked with evaluating the following code payload against the KARPATHY PROTOCOL.

PROTOCOL:
{guidelines}

TARGET PAYLOAD:
{target_content}

TASK:
Identify any violations of the Karpathy Protocol (Zero Fluff, Surgical Strikes, Neural Link Alignment).
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
