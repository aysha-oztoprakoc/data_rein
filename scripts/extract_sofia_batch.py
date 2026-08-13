import os
import sys
import xml.etree.ElementTree as ET
from defusedxml import minidom
from reins.harness import external_io

# Add src to path to allow importing extractors if needed, but we will use standalone logic for robustness
sys.path.append("/home/amdy/data_rein/src")

RAW_DATA_DIR = "/home/amdy/Downloads/raw_data/sofia_protocol"
OUT_DIR = "/home/amdy/data_rein/knowledge_base/sofia_protocol_extracted"

os.makedirs(OUT_DIR, exist_ok=True)

def remove_illegal_xml_chars(val: str) -> str:
    import re
    _illegal_xml_chars_RE = re.compile('[\x00-\x08\x0b\x0c\x0e-\x1F\uD800-\uDFFF\uFFFE\uFFFF]')
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    val = ansi_escape.sub('', val)
    return _illegal_xml_chars_RE.sub('', val)

def save_as_xml(text_content: str, filepath: str) -> str:
    out_path = os.path.join(OUT_DIR, f"{os.path.basename(filepath)}.extracted.xml")
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

def process_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    text = ""
    
    if ext == ".pdf":
        out_txt = filepath + ".tmp.txt"
        res = external_io.run(["pdftotext", filepath, out_txt], capture_output=True)
        if res.returncode == 0 and os.path.exists(out_txt):
            with open(out_txt, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            os.remove(out_txt)
        else:
            print(f"[-] Failed to extract PDF: {filepath}")
            return
    elif ext in [".md", ".txt"]:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    elif ext in [".html", ".htm"]:
        try:
            from bs4 import BeautifulSoup
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
            text = soup.get_text(separator="\n", strip=True)
        except ImportError:
            print("[-] BeautifulSoup not found, falling back to raw text")
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
    else:
        print(f"[-] Unsupported format {ext} for {filepath}")
        return

    if text.strip():
        save_as_xml(text, filepath)
        print(f"[+] Successfully extracted {os.path.basename(filepath)}")
    else:
        print(f"[-] Empty text extracted from {filepath}")

def main():
    print(f"[*] Starting extraction from {RAW_DATA_DIR}")
    for file in os.listdir(RAW_DATA_DIR):
        filepath = os.path.join(RAW_DATA_DIR, file)
        if os.path.isfile(filepath):
            process_file(filepath)

if __name__ == "__main__":
    main()
