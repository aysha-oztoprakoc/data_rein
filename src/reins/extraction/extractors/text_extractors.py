from typing import Any, Dict
from ..registry import registry
import os
import shutil
import json
import csv
import subprocess
from .base import BaseExtractor
import xml.etree.ElementTree as ET
from xml.dom import minidom
import re

try:
    import docx  # type: ignore
except ImportError:
    docx = None  # type: ignore
try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError:
    BeautifulSoup = None  # type: ignore
try:
    import ebooklib  # type: ignore
    from ebooklib import epub  # type: ignore
except ImportError:
    ebooklib = None  # type: ignore
    epub = None  # type: ignore
try:
    from striprtf.striprtf import rtf_to_text  # type: ignore
except ImportError:
    rtf_to_text = None  # type: ignore

def remove_illegal_xml_chars(val: str) -> str:
    _illegal_xml_chars_RE = re.compile('[\x00-\x08\x0b\x0c\x0e-\x1F\uD800-\uDFFF\uFFFE\uFFFF]')
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    val = ansi_escape.sub('', val)
    return _illegal_xml_chars_RE.sub('', val)

def save_as_xml(text_content: str, filepath: str, output_dir: str) -> str:
    out_path = os.path.join(output_dir, f"{os.path.basename(filepath)}.extracted.xml")
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


class PlainTextExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".txt", ".md"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            out_path = save_as_xml(text, filepath, output_dir)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "plaintext"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class JSONExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".json"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            text = json.dumps(data, indent=2)
            out_path = save_as_xml(text, filepath, output_dir)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "json"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class CSVExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".csv"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                text = "\n".join([", ".join(row) for row in reader])
            out_path = save_as_xml(text, filepath, output_dir)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "csv"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class PDFExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".pdf"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        out_path = os.path.join(output_dir, f"{os.path.basename(filepath)}.extracted.txt")
        try:
            res = subprocess.run(["pdftotext", filepath, out_path], capture_output=True)
            if res.returncode == 0:
                with open(out_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                os.remove(out_path)
                final_path = save_as_xml(text, filepath, output_dir)
                return {"status": "success", "output_path": final_path, "metadata": {"format": "pdf"}}
            return {"status": "error", "error": f"pdftotext failed: {res.stderr.decode()}"}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class DocxExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".docx"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        if docx is None:
            return {"status": "error", "error": "python-docx not installed"}
        try:
            doc = docx.Document(filepath)
            text = "\n".join([para.text for para in doc.paragraphs])
            out_path = save_as_xml(text, filepath, output_dir)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "docx"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class HTMLExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".html", ".htm"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        if BeautifulSoup is None:
            return {"status": "error", "error": "beautifulsoup4 not installed"}
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                soup = BeautifulSoup(f.read(), "html.parser")
            text = soup.get_text(separator="\n", strip=True)
            out_path = save_as_xml(text, filepath, output_dir)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "html"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class XMLExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".xml"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            text = "".join(root.itertext())
            out_path = save_as_xml(text, filepath, output_dir)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "xml"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class EpubExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".epub"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        if epub is None or ebooklib is None or BeautifulSoup is None:
            return {"status": "error", "error": "ebooklib or bs4 not installed"}
        try:
            book = epub.read_epub(filepath)
            text = ""
            for item in book.get_items():
                if item.get_type() == ebooklib.ITEM_DOCUMENT:
                    soup = BeautifulSoup(item.get_body_content(), 'html.parser')
                    text += soup.get_text(separator="\n", strip=True) + "\n"
            out_path = save_as_xml(text, filepath, output_dir)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "epub"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class RTFExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".rtf"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        if rtf_to_text is None:
            return {"status": "error", "error": "striprtf not installed"}
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                rtf = f.read()
            text = rtf_to_text(rtf)  # type: ignore[no-untyped-call]
            out_path = save_as_xml(text, filepath, output_dir)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "rtf"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


# Auto-register
registry.register(PlainTextExtractor)
registry.register(JSONExtractor)
registry.register(CSVExtractor)
registry.register(PDFExtractor)
registry.register(DocxExtractor)
registry.register(HTMLExtractor)
registry.register(XMLExtractor)
registry.register(EpubExtractor)
registry.register(RTFExtractor)
