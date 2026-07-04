import os
import zipfile
import subprocess
import tempfile
from typing import Dict, Any
from .base import BaseExtractor
from ..registry import registry
from .text_extractors import save_as_xml

class ZIPExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".zip"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        try:
            text_content = ""
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                for info in zip_ref.infolist():
                    if not info.is_dir():
                        ext = os.path.splitext(info.filename)[1].lower()
                        if ext in ['.txt', '.md', '.json', '.xml', '.csv', '.html']:
                            try:
                                with zip_ref.open(info) as f:
                                    text_content += f"\n--- {info.filename} ---\n"
                                    text_content += f.read().decode('utf-8', errors='ignore')
                            except Exception:
                                pass
            out_path = save_as_xml(text_content, filepath, output_dir)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "zip"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}

class RARExtractor(BaseExtractor):
    SUPPORTED_FORMATS = [".rar"]
    NODE = "amdy"

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        try:
            text_content = ""
            with tempfile.TemporaryDirectory() as tmpdir:
                res = subprocess.run(["7z", "x", filepath, f"-o{tmpdir}", "-y"], capture_output=True)
                if res.returncode != 0:
                    return {"status": "error", "error": f"7z failed: {res.stderr.decode()}"}
                for root, _, files in os.walk(tmpdir):
                    for file in files:
                        ext = os.path.splitext(file)[1].lower()
                        if ext in ['.txt', '.md', '.json', '.xml', '.csv', '.html']:
                            try:
                                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                                    rel_path = os.path.relpath(os.path.join(root, file), tmpdir)
                                    text_content += f"\n--- {rel_path} ---\n"
                                    text_content += f.read()
                            except Exception:
                                pass
            out_path = save_as_xml(text_content, filepath, output_dir)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "rar"}}
        except Exception as e:
            return {"status": "error", "error": str(e)}

registry.register(ZIPExtractor)
registry.register(RARExtractor)
