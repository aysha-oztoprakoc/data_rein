import os
import glob
from pathlib import Path
try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None
from bs4 import BeautifulSoup
from markdownify import markdownify as md

downloads_dir = Path('/home/amdy/Downloads')
target_dir = Path('/home/amdy/data_rein/data-oby/TrainingData/Downloads_Ingested')
target_dir.mkdir(parents=True, exist_ok=True)

def extract_pdf(file_path):
    if not fitz: return "PyMuPDF not installed."
    doc = fitz.open(file_path)
    text = f"# {file_path.name}\n\n"
    for page in doc:
        text += page.get_text("text") + "\n\n"
    return text

def extract_html(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    return md(html, heading_style="ATX")

def extract_md(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

count = 0
for file_path in downloads_dir.rglob('*'):
    if not file_path.is_file(): continue
    
    ext = file_path.suffix.lower()
    content = ""
    try:
        if ext == '.pdf':
            content = extract_pdf(file_path)
        elif ext == '.html':
            content = extract_html(file_path)
        elif ext in ['.md', '.txt']:
            content = extract_md(file_path)
        else:
            continue
            
        if not content.strip(): continue
        
        # Avoid extremely long names or collisions
        target_name = file_path.stem[:100].replace(' ', '_').replace('/', '_') + '.md'
        target_file = target_dir / target_name
        
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Ingested: {file_path.name} -> {target_name}")
    except Exception as e:
        print(f"Error extracting {file_path.name}: {e}")

print(f"\nSuccessfully extracted and ingested {count} documents into {target_dir}.")
