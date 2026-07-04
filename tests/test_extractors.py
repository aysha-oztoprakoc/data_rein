import os
import json
import pytest
import zipfile
from unittest.mock import patch, MagicMock

from reins.extraction.registry import registry

def test_registry_has_formats() -> None:
    supported = registry.list_supported()
    assert ".xml" in supported
    assert ".html" in supported
    assert ".zip" in supported
    assert ".rar" in supported
    assert ".md" in supported
    assert ".txt" in supported
    assert ".pdf" in supported
    assert ".json" in supported

def test_json_extractor(tmp_path) -> None:
    extractor = registry.get_extractor(".json")
    assert extractor is not None
    
    json_file = tmp_path / "test.json"
    json_file.write_text('{"key": "value"}')
    
    result = extractor.extract(str(json_file), str(tmp_path))
    assert result["status"] == "success"
    assert "output_path" in result
    assert os.path.exists(result["output_path"])

def test_txt_extractor(tmp_path) -> None:
    extractor = registry.get_extractor(".txt")
    assert extractor is not None
    
    txt_file = tmp_path / "test.txt"
    txt_file.write_text("Hello World")
    
    result = extractor.extract(str(txt_file), str(tmp_path))
    assert result["status"] == "success"
    assert "output_path" in result
    assert os.path.exists(result["output_path"])

def test_zip_extractor(tmp_path) -> None:
    extractor = registry.get_extractor(".zip")
    assert extractor is not None
    
    zip_path = tmp_path / "test.zip"
    with zipfile.ZipFile(zip_path, 'w') as zf:
        zf.writestr("test1.txt", b"zip content 1")
        
    result = extractor.extract(str(zip_path), str(tmp_path))
    assert result["status"] == "success"
    assert "output_path" in result
    assert os.path.exists(result["output_path"])

@patch('reins.extraction.extractors.archive_extractors.subprocess.run')
def test_rar_extractor(mock_run, tmp_path) -> None:
    mock_res = MagicMock()
    mock_res.returncode = 0
    mock_run.return_value = mock_res
    
    extractor = registry.get_extractor(".rar")
    assert extractor is not None
    
    rar_path = tmp_path / "test.rar"
    rar_path.write_text("fake rar")
    
    result = extractor.extract(str(rar_path), str(tmp_path))
    assert result["status"] == "success"
    assert "output_path" in result

@patch('reins.extraction.extractors.text_extractors.subprocess.run')
def test_pdf_extractor(mock_run, tmp_path) -> None:
    mock_res = MagicMock()
    mock_res.returncode = 0
    
    def mock_pdf_run(*args, **kwargs):
        out_file = args[0][2]
        with open(out_file, 'w') as f:
            f.write("mocked pdf text")
        return mock_res
    mock_run.side_effect = mock_pdf_run
    
    extractor = registry.get_extractor(".pdf")
    assert extractor is not None
    
    pdf_path = tmp_path / "test.pdf"
    pdf_path.write_text("fake pdf")
    
    result = extractor.extract(str(pdf_path), str(tmp_path))
    assert result["status"] == "success"
    assert "output_path" in result
