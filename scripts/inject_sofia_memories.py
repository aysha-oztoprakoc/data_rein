from pathlib import Path

from reins.harness import paths
from reins.harness.memory_ingestion import ingest_sofia_memories

EXTRACTED_DIR = paths.knowledge_base() / "sofia_protocol_extracted"


def inject_memories(
    extracted_dir: Path | str = EXTRACTED_DIR,
    wiki_path: Path | str | None = None,
) -> int:
    print("[*] Injecting Sofia Protocol memories into the shared Wiki...")
    count = ingest_sofia_memories(extracted_dir, wiki_path)
    print(f"[+] Imported {count} Sofia Protocol memories into wiki.db.")
    return count

if __name__ == "__main__":
    _ = inject_memories()
