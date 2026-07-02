import os
import shutil
import subprocess
from pathlib import Path

DATA_HARNESS = Path("/home/amdy/data_rein")

def git_mv(src, dst):
    if not src.exists():
        print(f"Warning: Source {src} does not exist, skipping.")
        return
    print(f"Moving {src} -> {dst}")
    res = subprocess.run(["git", "mv", str(src), str(dst)], cwd=DATA_HARNESS, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  git mv failed: {res.stderr.strip()}, falling back to shutil.move")
        shutil.move(str(src), str(dst))
        subprocess.run(["git", "add", str(dst)], cwd=DATA_HARNESS)
        if src.exists():
            subprocess.run(["git", "rm", "-f", str(src)], cwd=DATA_HARNESS)

def main():
    # 1. Create new directory structure
    dirs = [
        "knowledge_base/pon/papers",
        "knowledge_base/pon/analysis",
        "knowledge_base/system",
        "knowledge_base/projects",
        "knowledge_base/agents/antigravity/builtin_skills",
        "knowledge_base/agents/agents_md/skills",
        "knowledge_base/agents/hermes",
        "knowledge_base/architecture",
        "prompts/templates",
        "prompts/optimized",
        "prompts/history",
        "training_data/text",
        "training_data/image_descriptions",
        "training_data/audio_transcripts",
        "training_data/metadata",
        "extraction_pipeline/extractors",
        "prompt_optimizer/strategies",
        "prompt_optimizer/templates",
        "sync",
        "services",
        "config",
        "scripts"
    ]
    
    for d in dirs:
        (DATA_HARNESS / d).mkdir(parents=True, exist_ok=True)
        # Create .gitkeep to ensure empty dirs are tracked if needed
        with open(DATA_HARNESS / d / ".gitkeep", "w") as f:
            pass
        subprocess.run(["git", "add", f"{d}/.gitkeep"], cwd=DATA_HARNESS)
    
    print("Created new directory structure.")

    # 2. Delete redundant knowledge_base/docs since it's identical to pon/
    docs_dir = DATA_HARNESS / "knowledge_base/docs"
    if docs_dir.exists():
        print("Removing redundant knowledge_base/docs...")
        subprocess.run(["git", "rm", "-r", "knowledge_base/docs"], cwd=DATA_HARNESS)
        if docs_dir.exists():
            shutil.rmtree(docs_dir)

    # 3. Move pon/ contents to knowledge_base/pon/
    pon_dir = DATA_HARNESS / "pon"
    if pon_dir.exists():
        print("Migrating pon/ directory...")
        for file in pon_dir.iterdir():
            if file.is_file():
                if file.suffix.lower() == '.pdf':
                    git_mv(file, DATA_HARNESS / "knowledge_base/pon/papers" / file.name)
                elif file.suffix.lower() in ['.md', '.txt']:
                    git_mv(file, DATA_HARNESS / "knowledge_base/pon/analysis" / file.name)
        # Clean up empty pon dir
        subprocess.run(["git", "rm", "-r", "pon"], cwd=DATA_HARNESS)
        if pon_dir.exists():
            shutil.rmtree(pon_dir)

    # 4. Move Hardware/Software Info
    hw_dir = DATA_HARNESS / "DATA/Hardware and Software Info"
    if hw_dir.exists():
        print("Migrating system telemetry...")
        for file in hw_dir.iterdir():
            if file.is_file() and file.name.endswith(".txt") and ("hardware" in file.name or "software" in file.name):
                git_mv(file, DATA_HARNESS / "knowledge_base/system" / file.name)
            elif file.suffix.lower() in ['.txt', '.md']:
                git_mv(file, DATA_HARNESS / "knowledge_base/architecture" / file.name)

    # 5. Move architecture docs from DATA
    data_dir = DATA_HARNESS / "DATA"
    if data_dir.exists():
        for file in data_dir.iterdir():
            if file.is_file() and file.suffix.lower() == '.md':
                git_mv(file, DATA_HARNESS / "knowledge_base/architecture" / file.name)

    # 6. Move core scripts to services/
    scripts_to_services = [
        "data_rein.py",
        "backup_service.py", 
        "system_health_check.py",
        "vault_manager.py",
        "knowledge_ingestor.py",
        "data_extractor_daemon.py"
    ]
    for script in scripts_to_services:
        git_mv(DATA_HARNESS / script, DATA_HARNESS / "services" / script)

    # 7. Move config files to config/
    configs = [
        "model_registry.json",
        "api_keys.json",
        ".secrets.env"
    ]
    for cfg in configs:
        git_mv(DATA_HARNESS / cfg, DATA_HARNESS / "config" / cfg)

    # 8. Move shell scripts to scripts/
    shell_scripts = [
        "dashboard.sh",
        "install_comfy.sh",
        "pull_models_amdy.sh",
        "pull_models_tell.sh"
    ]
    for script in shell_scripts:
        git_mv(DATA_HARNESS / script, DATA_HARNESS / "scripts" / script)

    # 9. Create __init__.py files
    init_dirs = ["extraction_pipeline", "extraction_pipeline/extractors", "prompt_optimizer", "prompt_optimizer/strategies", "sync", "services"]
    for d in init_dirs:
        with open(DATA_HARNESS / d / "__init__.py", "w") as f:
            pass
        subprocess.run(["git", "add", f"{d}/__init__.py"], cwd=DATA_HARNESS)

    print("Migration completed successfully.")

if __name__ == "__main__":
    main()
