import os
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom
import subprocess
import sqlite3
import uuid
import time
import argparse

DB_PATH = "/home/amdy/data_rein/DATA/kad-1.0/odysseus/data/app.db"
SHARED_CONTEXT = "/home/amdy/data_rein/knowledge_base/SHARED_CONTEXT.md"
OWNER = "data-ody"

def remove_illegal_xml_chars(val: str) -> str:
    import re
    _illegal_xml_chars_RE = re.compile('[\x00-\x08\x0b\x0c\x0e-\x1F\uD800-\uDFFF\uFFFE\uFFFF]')
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    val = ansi_escape.sub('', val)
    return _illegal_xml_chars_RE.sub('', val)

def save_as_xml(text_content: str, filepath: str, out_dir: str) -> str:
    out_path = os.path.join(out_dir, f"{os.path.basename(filepath)}.extracted.xml")
    content = remove_illegal_xml_chars(text_content)
    root = ET.Element("knowledge_document")
    meta = ET.SubElement(root, "metadata")
    title = ET.SubElement(meta, "title")
    title.text = remove_illegal_xml_chars(os.path.basename(filepath))
    path = ET.SubElement(meta, "path")
    path.text = remove_illegal_xml_chars(filepath)
    body = ET.SubElement(root, "content")
    body.text = content
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(xml_str)
    return out_path

def process_file(filepath, out_dir):
    ext = os.path.splitext(filepath)[1].lower()
    text = ""
    
    if ext == ".pdf":
        out_txt = filepath + ".tmp.txt"
        res = subprocess.run(["pdftotext", filepath, out_txt], capture_output=True)
        if res.returncode == 0 and os.path.exists(out_txt):
            with open(out_txt, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            os.remove(out_txt)
    elif ext in [".md", ".txt", ".json", ".csv", ".xml"]:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    elif ext in [".html", ".htm"]:
        try:
            from bs4 import BeautifulSoup
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
            text = soup.get_text(separator="\n", strip=True)
        except ImportError:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()

    if text.strip():
        xml_path = save_as_xml(text, filepath, out_dir)
        return xml_path
    return None

def inject_to_db(xml_paths):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    count = 0
    
    for filepath in xml_paths:
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            metadata = root.find("metadata")
            content_elem = root.find("content")
            
            title = metadata.find("title").text if metadata is not None and metadata.find("title") is not None else os.path.basename(filepath)
            text = content_elem.text if content_elem is not None else ""
            
            if not text.strip():
                continue
            
            mem_id = str(uuid.uuid4())
            category = "digested_raw_data"
            
            cursor.execute('''
                INSERT INTO memories (id, text, category, source, owner, session_id, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (mem_id, f"[SOURCE: {title}]\n{text}", category, os.path.basename(filepath), OWNER, None, int(time.time())))
            count += 1
        except Exception as e:
            print(f"[-] Failed to inject {filepath}: {e}")
            
    conn.commit()
    conn.close()
    return count

def update_trail(folder_name, count):
    if not os.path.exists(SHARED_CONTEXT):
        return
    with open(SHARED_CONTEXT, "a") as f:
        f.write(f"\n## Digest Pipeline Assimilation: {folder_name}\n")
        f.write(f"* **Status**: INGESTED ({time.strftime('%Y-%m-%d')})\n")
        f.write(f"* **Payload**: {count} items processed from `{folder_name}` and injected into the Ody Memory Vault.\n")
        f.write(f"* **Directive**: System knowledge base updated dynamically via the `digest` command.\n")

def main():
    parser = argparse.ArgumentParser(description="Digest pipeline for data_rein")
    parser.add_argument("folder", nargs="?", default="/home/amdy/Downloads/raw_data/", help="Folder to digest")
    args = parser.parse_args()
    
    raw_dir = os.path.abspath(args.folder)
    if not os.path.isdir(raw_dir):
        print(f"[-] Folder not found: {raw_dir}")
        sys.exit(1)
        
    out_dir = os.path.join("/home/amdy/data_rein/knowledge_base", "digested_" + os.path.basename(raw_dir.rstrip('/')))
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"[*] Digesting folder: {raw_dir}")
    xml_paths = []
    
    # Process files
    for root, _, files in os.walk(raw_dir):
        for file in files:
            filepath = os.path.join(root, file)
            print(f"[*] Extracting: {file}")
            xml_path = process_file(filepath, out_dir)
            if xml_path:
                xml_paths.append(xml_path)
                
    if not xml_paths:
        print("[!] No text content could be extracted.")
        sys.exit(0)
        
    # Inject
    print("[*] Injecting into Ody Memory Vault...")
    injected_count = inject_to_db(xml_paths)
    print(f"[+] Successfully injected {injected_count} memories.")
    
    # Update trail
    update_trail(os.path.basename(raw_dir.rstrip('/')), injected_count)
    
    # Restart Odysseus
    print("[*] Restarting Odysseus to flush cache...")
    subprocess.run(["docker", "compose", "-f", "/home/amdy/data_rein/DATA/kad-1.0/odysseus/docker-compose.yml", "restart", "odysseus"], cwd="/home/amdy/data_rein/DATA/kad-1.0/odysseus/")
    
    print("[+] Digest pipeline complete!")

if __name__ == "__main__":
    main()
