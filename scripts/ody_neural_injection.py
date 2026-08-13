from pathlib import Path

from reins.harness import paths
from reins.harness.memory_ingestion import ingest_knowledge_memories
from reins.harness.skill_registry import canonical_skills

KNOWLEDGE_BASE_DIR = paths.knowledge_base()
OWNER = "data-ody"

def inject_skills() -> None:
    print("[*] Validating canonical harness skills...")
    for skill in canonical_skills():
        print(f"[+] Canonical skill: {skill.name} — {skill.description}")
    print("[*] Install canonical links on demand with: reins skills install")

def inject_memories(
    knowledge_base_dir: Path | str = KNOWLEDGE_BASE_DIR,
    wiki_path: Path | str | None = None,
) -> int:
    print("[*] Injecting memories into the shared Wiki...")
    count = ingest_knowledge_memories(knowledge_base_dir, wiki_path, owner=OWNER)
    print(f"[+] Imported {count} memories into wiki.db.")
    return count

if __name__ == "__main__":
    print("=== Ody Neural Injection Initiated ===")
    inject_skills()
    _ = inject_memories()
    print("=== Injection Complete ===")
