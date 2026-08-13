"""Serialize extractor output without coupling media code to text extractors."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

from defusedxml import ElementTree as SafeET
from defusedxml.common import DefusedXmlException

_ILLEGAL_XML = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f\ud800-\udfff\ufffe\uffff]")
_ANSI_ESCAPE = re.compile(r"\x1b(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def remove_illegal_xml_chars(value: str) -> str:
    """Remove terminal escapes and code points forbidden by XML 1.0."""
    return _ILLEGAL_XML.sub("", _ANSI_ESCAPE.sub("", value))


def save_as_xml(text_content: str, filepath: str, output_dir: str) -> str:
    """Write one canonical knowledge document and return its absolute path."""
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    out_path = destination / f"{Path(filepath).name}.extracted.xml"
    root = ET.Element("knowledge_document")
    metadata = ET.SubElement(root, "metadata")
    ET.SubElement(metadata, "title").text = remove_illegal_xml_chars(Path(filepath).name)
    ET.SubElement(metadata, "path").text = remove_illegal_xml_chars(filepath)
    ET.SubElement(root, "content").text = remove_illegal_xml_chars(text_content)
    ET.indent(root, space="  ")
    ET.ElementTree(root).write(out_path, encoding="unicode", xml_declaration=True)
    return str(out_path)


def read_extracted_text(output_path: str) -> str:
    """Read canonical XML output, falling back to plain UTF-8 extractor output."""
    path = Path(output_path)
    try:
        tree = SafeET.parse(path)
        root = tree.getroot()
        node = root.find("content") if root is not None else None
    except DefusedXmlException:
        return ""
    except SafeET.ParseError:
        return path.read_text(encoding="utf-8", errors="replace")
    return node.text if node is not None and node.text is not None else ""
