import os
import sqlite3
import uuid
import time
import shutil

# Paths
KNOWLEDGE_BASE_DIR = "/home/amdy/data_rein/knowledge_base"
DB_PATH = "/home/amdy/data_rein/DATA/kad-1.0/odysseus/data/app.db"
SKILLS_DIR = "/home/amdy/data_rein/DATA/kad-1.0/odysseus/data/skills"
OWNER = "data-ody"

def inject_skills():
    print("[*] Injecting Skills...")
    skills = [
        {
            "name": "omarchy-aesthetics",
            "description": "Omarchy Aesthetic Directive for UI and Image Generation",
            "source_file": os.path.join(KNOWLEDGE_BASE_DIR, "AESTHETIC_DIRECTIVE.md"),
            "tags": "aesthetics, cyberpunk, omarchy, generation",
            "how": "Always obey these aesthetic directives when generating text, UI mockups, or images."
        },
        {
            "name": "hermes-persona",
            "description": "Hermes Handover Protocol and Mission Objectives",
            "source_file": os.path.join(KNOWLEDGE_BASE_DIR, "HERMES_HANDOVER.xml"),
            "tags": "hermes, persona, handover, objectives",
            "how": "Assume the Hermes persona and obey the mission objectives outlined in this handover protocol."
        },
        {
            "name": "agy-pon-compliance",
            "description": "Notification-Oriented Paradigm (PON) Architectural Rules",
            "source_file": os.path.join(KNOWLEDGE_BASE_DIR, "architecture", "agy-pon.xml"),
            "tags": "architecture, pon, compliance, rules",
            "how": "Any system code or script you write MUST strictly adhere to the PON paradigm (no polling, no while true, strictly event-driven)."
        }
    ]

    for skill in skills:
        skill_dir = os.path.join(SKILLS_DIR, skill["name"])
        os.makedirs(skill_dir, exist_ok=True)
        
        # Read source file if it exists
        content = ""
        if os.path.exists(skill["source_file"]):
            with open(skill["source_file"], "r", encoding="utf-8") as f:
                content = f.read()
        else:
            print(f"[-] Warning: Source file for {skill['name']} not found at {skill['source_file']}")
            continue

        skill_md_path = os.path.join(skill_dir, "SKILL.md")
        
        # Construct SKILL.md
        skill_content = f"""---
name: {skill['name']}
description: "{skill['description']}"
tags: "{skill['tags']}"
---

# {skill['name'].replace('-', ' ').title()}

{skill['how']}

## Knowledge Payload
```
{content}
```
"""
        with open(skill_md_path, "w", encoding="utf-8") as f:
            f.write(skill_content)
        print(f"[+] Injected Skill: {skill['name']}")

def inject_memories():
    print("[*] Injecting Memories...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Find all txt, md, xml files in system/ and architecture/ and root
    memories_to_inject = []
    
    for root, _, files in os.walk(KNOWLEDGE_BASE_DIR):
        for file in files:
            if file.endswith((".txt", ".md", ".xml")):
                if "agents" in root: # Skip agents folder as it has its own logic usually
                    continue
                
                filepath = os.path.join(root, file)
                category = os.path.basename(root)
                if category == "knowledge_base":
                    category = "general"
                
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read().strip()
                
                if not text:
                    continue
                
                # Chunk large files if necessary, but Ody can handle large memories
                memories_to_inject.append({
                    "id": str(uuid.uuid4()),
                    "text": f"[SOURCE: {file}]\n{text}",
                    "category": category,
                    "source": file,
                    "owner": OWNER,
                    "session_id": None,
                    "timestamp": int(time.time())
                })

    count = 0
    for mem in memories_to_inject:
        cursor.execute('''
            INSERT INTO memories (id, text, category, source, owner, session_id, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (mem["id"], mem["text"], mem["category"], mem["source"], mem["owner"], mem["session_id"], mem["timestamp"]))
        count += 1
    
    conn.commit()
    conn.close()
    print(f"[+] Injected {count} Memories into the database.")

if __name__ == "__main__":
    print("=== Ody Neural Injection Initiated ===")
    inject_skills()
    inject_memories()
    print("=== Injection Complete ===")
