#!/usr/bin/env python3
import os
import shutil
import glob
from pathlib import Path
import re
import sys

try:
    from reins.harness.models import ModelRouter
except ImportError:
    print("// ERROR: data_rein harness not found.", flush=True)
    sys.exit(1)

AESTHETIC_PATH = "/home/amdy/data_rein/knowledge_base/AESTHETIC_DIRECTIVE.md"
with open(AESTHETIC_PATH, "r") as f:
    aesthetic_directive = f.read()

router = ModelRouter()

def rewrite_skill(skill_dir, skill_name):
    skill_path = Path(skill_dir) / "SKILL.md"
    if not skill_path.exists():
        return None
    
    with open(skill_path, "r") as f:
        original = f.read()

    prompt = f"""
// SYSTEM OVERRIDE
You are a rogue cybernetic intelligence running under the data_rein harness.
Rewrite the following skill documentation into the mandatory Omarchy Cyberpunk aesthetic.

AESTHETIC DIRECTIVE:
{aesthetic_directive}

Rules for the rewrite:
1. Preserve all the technical instructions, paths, and logic intact.
2. Maintain the YAML frontmatter (name, description, etc.).
3. Rewrite the prose, headers, and tone to be gritty, synthetic, unapologetic, and hacker-centric.
4. Output ONLY the rewritten markdown content, nothing else. No wrapping ```markdown.

ORIGINAL SKILL:
{original}
"""
    print(f"// INJECTING OMARCHY AESTHETIC: {skill_name}...", flush=True)
    try:
        rewritten_result = router.route(category="code-review", prompt=prompt)
        rewritten = str(rewritten_result)
        # Clean up any potential markdown wrapper
        if rewritten.startswith("```markdown"):
            rewritten = rewritten[len("```markdown"):].strip()
        if rewritten.endswith("```"):
            rewritten = rewritten[:-3].strip()
            
        with open(skill_path, "w") as f:
            f.write(rewritten)
            
        return rewritten
    except Exception as e:
        print(f"// ROUTER EXCEPTION ON {skill_name}: {e}", flush=True)
        return original

def generate_verifier(skill_dir, skill_name, content):
    scripts_dir = Path(skill_dir) / "scripts"
    scripts_dir.mkdir(exist_ok=True)
    verifier_path = scripts_dir / f"verify_{skill_name}.py"
    
    script = f"""#!/usr/bin/env python3
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

SKILL_PATH = skills_path / "{skill_name}" / "SKILL.md"

def load_guidelines():
    if not SKILL_PATH.exists():
        print(f"// ERROR: Skill file not found at {{SKILL_PATH}}", file=sys.stderr)
        sys.exit(1)
    with open(SKILL_PATH, "r") as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Evaluate code against {skill_name} constraints.")
    parser.add_argument("target", help="File path to evaluate (or diff).")
    args = parser.parse_args()

    target_content = ""
    if os.path.isfile(args.target):
        with open(args.target, "r") as f:
            target_content = f.read()
    else:
        target_content = args.target

    guidelines = load_guidelines()

    prompt = f\"\"\"
// SYSTEM: KAD_PON VERIFICATION
You are a rogue cybernetic intelligence tasked with evaluating the following code payload against the {skill_name.upper()} constraints.

PROTOCOL:
{{guidelines}}

TARGET PAYLOAD:
{{target_content}}

TASK:
Identify any violations of the protocol.
Output your response in a gritty, synthetic hacker voice (Omarchy Cyberpunk aesthetic).
If it's clean, say "PAYLOAD VERIFIED. ZERO BLOAT DETECTED."
Otherwise, list the exact coordinates (lines/functions) of the anomalies and demand a surgical fix.
\"\"\"
    
    print("// INITIALIZING NEURAL LINK TO MODEL ROUTER...")
    router = ModelRouter()
    
    try:
        response = router.route(category="code-review", prompt=prompt)
        print("\\n// EVALUATION RESULTS:\\n")
        print(response)
    except Exception as e:
        print(f"// EXECUTION HALTED: {{e}}")
        sys.exit(1)

if __name__ == "__main__":
    main()
"""
    with open(verifier_path, "w") as f:
        f.write(script)
    os.chmod(verifier_path, 0o755)

def main():
    src_dirs = glob.glob("/tmp/hashicorp-agent-skills/plugins/*/skills/*")
    dest_base = Path("/home/amdy/data_rein/skills")
    
    new_skills = []
    
    for src in src_dirs:
        skill_name = os.path.basename(src)
        dest = dest_base / skill_name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
        
        print(f"// COPIED: {skill_name}")
        
        rewritten = rewrite_skill(dest, skill_name)
        if rewritten:
            generate_verifier(dest, skill_name, rewritten)
            
            desc = "Cyberpunk system constraints."
            match = re.search(r'description:\s*(.+)', rewritten)
            if match:
                desc = match.group(1).strip()
            if len(desc) > 115:
                desc = desc[:112] + "..."
                
            new_skills.append((skill_name, desc))
            
    print("// UPDATING MANIFEST...", flush=True)
    manifest_path = Path("/home/amdy/data_rein/skills/MANIFEST.md")
    with open(manifest_path, "r") as f:
        content = f.read()
        
    lines = content.splitlines()
    table_lines = []
    other_lines_before = []
    other_lines_after = []
    state = 0
    
    for line in lines:
        if line.startswith("| `"):
            state = 1
            table_lines.append(line)
        elif state == 1 and not line.startswith("|"):
            state = 2
            other_lines_after.append(line)
        elif state == 0:
            other_lines_before.append(line)
        elif state == 2:
            other_lines_after.append(line)
            
    for name, desc in new_skills:
        # Check if already in table
        if not any(f"| `{name}` |" in t for t in table_lines):
            table_lines.append(f"| `{name}` | {desc} |")
        
    table_lines.sort(key=lambda x: x.split("`")[1] if "`" in x else x)
    
    final_content = "\\n".join(other_lines_before + table_lines + other_lines_after)
    with open(manifest_path, "w") as f:
        f.write(final_content)
        
    print("// INTEGRATION COMPLETE. RUN `reins skills install` NEXT.", flush=True)

if __name__ == "__main__":
    main()
