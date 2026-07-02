from typing import Any, Dict
from ..registry import registry
import os
import shutil
import json
import csv
import subprocess
from .base import BaseExtractor
import xml.etree.ElementTree as ET

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


class PlainTextExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".txt", ".md"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        out_path = os.path.join(
            output_dir, f"{os.path.basename(filepath)}.extracted.txt")
        shutil.copy(filepath, out_path)
        return {"status": "success", "output_path": out_path, "metadata": {"format": "plaintext"}}


class JSONExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".json"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        out_path = os.path.join(
            output_dir, f"{os.path.basename(filepath)}.extracted.txt")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            # Flatten to text representation
            text = json.dumps(data, indent=2)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(text)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "json"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class CSVExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".csv"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        out_path = os.path.join(
            output_dir, f"{os.path.basename(filepath)}.extracted.txt")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                text = "\n".join([", ".join(row) for row in reader])
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(text)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "csv"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class PDFExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".pdf"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        out_path = os.path.join(
            output_dir, f"{os.path.basename(filepath)}.extracted.txt")
        try:
            res = subprocess.run(
                ["pdftotext", filepath, out_path], capture_output=True)
            if res.returncode == 0:
                return {"status": "success", "output_path": out_path, "metadata": {"format": "pdf"}}
            return {"status": "error", "error": f"pdftotext failed: {res.stderr.decode()}"}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class DocxExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".docx"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        out_path = os.path.join(
            output_dir, f"{os.path.basename(filepath)}.extracted.txt")
        if docx is None:
            return {"status": "error", "error": "python-docx not installed"}
        try:
            doc = docx.Document(filepath)
            text = "\n".join([para.text for para in doc.paragraphs])
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(text)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "docx"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class HTMLExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".html", ".htm"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        out_path = os.path.join(
            output_dir, f"{os.path.basename(filepath)}.extracted.txt")
        if BeautifulSoup is None:
            return {"status": "error", "error": "beautifulsoup4 not installed"}
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                soup = BeautifulSoup(f.read(), "html.parser")
            text = soup.get_text(separator="\n", strip=True)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(text)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "html"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class XMLExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".xml"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        out_path = os.path.join(
            output_dir, f"{os.path.basename(filepath)}.extracted.txt")
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            text = "".join(root.itertext())
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(text)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "xml"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class EpubExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".epub"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        out_path = os.path.join(
            output_dir, f"{os.path.basename(filepath)}.extracted.txt")
        if epub is None or ebooklib is None or BeautifulSoup is None:
            return {"status": "error", "error": "ebooklib or bs4 not installed"}
        try:
            book = epub.read_epub(filepath)
            text = ""
            for item in book.get_items():
                if item.get_type() == ebooklib.ITEM_DOCUMENT:
                    soup = BeautifulSoup(
                        item.get_body_content(), 'html.parser')
                    text += soup.get_text(separator="\n", strip=True) + "\n"
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(text)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "epub"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}


class RTFExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".rtf"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        out_path = os.path.join(
            output_dir, f"{os.path.basename(filepath)}.extracted.txt")
        if rtf_to_text is None:
            return {"status": "error", "error": "striprtf not installed"}
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                rtf = f.read()
            text = rtf_to_text(rtf)  # type: ignore[no-untyped-call]
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(text)
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
