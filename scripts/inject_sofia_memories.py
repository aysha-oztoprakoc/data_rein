import os
import sqlite3
import uuid
import time
import xml.etree.ElementTree as ET

DB_PATH = "/home/amdy/data_rein/DATA/kad-1.0/odysseus/data/app.db"
EXTRACTED_DIR = "/home/amdy/data_rein/knowledge_base/sofia_protocol_extracted"
OWNER = "data-ody"

def inject_memories():
    print("[*] Injecting Sofia Protocol Memories into Ody...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    count = 0
    for file in os.listdir(EXTRACTED_DIR):
        if file.endswith(".xml"):
            filepath = os.path.join(EXTRACTED_DIR, file)
            try:
                tree = ET.parse(filepath)
                root = tree.getroot()
                
                metadata = root.find("metadata")
                content_elem = root.find("content")
                
                title = metadata.find("title").text if metadata is not None and metadata.find("title") is not None else file
                text = content_elem.text if content_elem is not None else ""
                
                if not text.strip():
                    continue
                
                # Split large texts into chunks if they exceed SQLite limits, though usually TEXT is very large
                # For safety, let's inject as a single memory node for now.
                mem_id = str(uuid.uuid4())
                category = "sofia_protocol"
                
                cursor.execute('''
                    INSERT INTO memories (id, text, category, source, owner, session_id, timestamp)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (mem_id, f"[SOURCE: {title}]\n{text}", category, file, OWNER, None, int(time.time())))
                
                count += 1
            except Exception as e:
                print(f"[-] Failed to inject {file}: {e}")
                
    conn.commit()
    conn.close()
    print(f"[+] Successfully injected {count} memories from Sofia Protocol.")

if __name__ == "__main__":
    inject_memories()
