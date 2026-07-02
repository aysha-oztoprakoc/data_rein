import os
import re
from pathlib import Path

KB_DIR = Path(os.path.expanduser("~/data_rein/knowledge_base"))
OUTPUT_FILE = KB_DIR / "agents" / "hermes" / "data_hermes_wiki.md"

# Rough 12k token limit ~ 48k characters
MAX_CHARS = 48000

def condense_text(text: str) -> str:
    # Remove consecutive empty lines
    text = re.sub(r'\n\s*\n', '\n', text)
    # Remove excess whitespace
    text = re.sub(r' {2,}', ' ', text)
    return text.strip()

def build_wiki():
    print(f"Building condensed wiki from {KB_DIR}...")
    
    os.makedirs(OUTPUT_FILE.parent, exist_ok=True)
    
    wiki_content = "# Data-Hermes Master Wiki\n\n"
    chars_used = len(wiki_content)
    
    # Prioritize certain folders: pon, architecture, agents
    priorities = ["pon", "architecture", "agents", "system_configs", "projects"]
    
    for category in priorities:
        cat_dir = KB_DIR / category
        if not cat_dir.exists():
            continue
            
        wiki_content += f"## Section: {category.upper()}\n"
        chars_used += len(f"## Section: {category.upper()}\n")
        
        for root, _, files in os.walk(cat_dir):
            # Skip hidden files or caches
            if '.gemini' in root or '.git' in root or '__pycache__' in root:
                continue
                
            for file in files:
                if not file.endswith(('.md', '.txt', '.yaml', '.json')):
                    continue
                    
                filepath = Path(root) / file
                
                # Skip the output file itself
                if filepath == OUTPUT_FILE:
                    continue
                    
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    condensed = condense_text(content)
                    
                    # Take up to 2000 chars per file to ensure we get a broad cross-section
                    chunk = condensed[:2000]
                    
                    if chars_used + len(chunk) > MAX_CHARS:
                        print("Reached maximum wiki size limit.")
                        break
                        
                    entry = f"\n### File: {file}\n{chunk}\n"
                    wiki_content += entry
                    chars_used += len(entry)
                    
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    
        if chars_used > MAX_CHARS:
            break
            
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(wiki_content)
        
    print(f"Wiki generated at {OUTPUT_FILE} with {chars_used} characters (~{chars_used//4} tokens).")

if __name__ == "__main__":
    build_wiki()
