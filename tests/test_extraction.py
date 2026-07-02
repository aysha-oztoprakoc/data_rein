"""
test_extraction.py — PON-Compliant Extraction Pipeline Tests

Tests the PlainTextExtractor and the MQTT-driven orchestrator routing logic.
All mocks target the orchestrator's local namespace references to ensure
proper isolation from the real extraction registry.
"""
import json
import os
import pytest
from unittest.mock import MagicMock

from src.data_harness.extraction.extractors.text_extractors import PlainTextExtractor


class TestPlainTextExtractor:
    """Unit tests for the PlainTextExtractor (NODE=amdy)."""

    def test_extract_produces_success(self, tmp_path):
        """Verify extraction succeeds and returns correct status."""
        dummy_file = tmp_path / "test.txt"
        dummy_file.write_text("Hello PON")
        out_dir = tmp_path / "out"
        out_dir.mkdir()

        extractor = PlainTextExtractor()
        result = extractor.extract(str(dummy_file), str(out_dir))

        assert result["status"] == "success"

    def test_extract_output_path_format(self, tmp_path):
        """
        The real PlainTextExtractor names its output as:
            <basename>.extracted.txt
        Verify the full naming convention.
        """
        dummy_file = tmp_path / "notes.txt"
        dummy_file.write_text("Data Harness content")
        out_dir = tmp_path / "out"
        out_dir.mkdir()

        extractor = PlainTextExtractor()
        result = extractor.extract(str(dummy_file), str(out_dir))

        expected_name = "notes.txt.extracted.txt"
        assert os.path.basename(result["output_path"]) == expected_name

    def test_extract_preserves_content(self, tmp_path):
        """Verify the extracted file's content matches the original."""
        content = "PON: Zero polling, zero waste."
        dummy_file = tmp_path / "readme.md"
        dummy_file.write_text(content)
        out_dir = tmp_path / "out"
        out_dir.mkdir()

        extractor = PlainTextExtractor()
        result = extractor.extract(str(dummy_file), str(out_dir))

        with open(result["output_path"], "r") as f:
            extracted = f.read()
        assert extracted == content

    def test_extract_metadata_format(self, tmp_path):
        """Verify the metadata field in the result dict."""
        dummy_file = tmp_path / "sample.txt"
        dummy_file.write_text("test")
        out_dir = tmp_path / "out"
        out_dir.mkdir()

        extractor = PlainTextExtractor()
        result = extractor.extract(str(dummy_file), str(out_dir))

        assert result["metadata"] == {"format": "plaintext"}


class TestOrchestratorRouting:
    """
    Tests the process_extraction function's MQTT routing logic.
    Mocks target the orchestrator module's local references for isolation.
    """

    def test_routes_and_publishes_result(self, mocker, tmp_path):
        """Verify the orchestrator calls the extractor and publishes to MQTT."""
        mock_registry = mocker.patch("src.data_harness.extraction.orchestrator.registry")
        mock_extractor = MagicMock()
        mock_extractor.NODE = "amdy"
        mock_extractor.extract.return_value = {"status": "success", "metadata": {}}
        mock_registry.get_extractor.return_value = mock_extractor

        # Mock the logger to prevent real file I/O in services.logger
        mocker.patch("src.data_harness.extraction.orchestrator.logger")

        dummy_file = tmp_path / "test.pdf"
        dummy_file.write_text("dummy")

        payload = {"filepath": str(dummy_file)}
        client = MagicMock()

        from src.data_harness.extraction.orchestrator import process_extraction
        process_extraction(client, payload)

        mock_extractor.extract.assert_called_once()
        client.publish.assert_called_once()
        args = client.publish.call_args[0]
        assert args[0] == "data_rein/extract/result"
        published = json.loads(args[1])
        assert published["status"] == "success"

    def test_missing_file_publishes_error(self, mocker):
        """Verify the orchestrator publishes an error for nonexistent files."""
        mocker.patch("src.data_harness.extraction.orchestrator.logger")

        payload = {"filepath": "/nonexistent/phantom.txt"}
        client = MagicMock()

        from src.data_harness.extraction.orchestrator import process_extraction
        process_extraction(client, payload)

        client.publish.assert_called_once()
        args = client.publish.call_args[0]
        published = json.loads(args[1])
        assert published["status"] == "error"
        assert "File not found" in published["error"]

    def test_unsupported_format_publishes_error(self, mocker, tmp_path):
        """Verify the orchestrator rejects unsupported file formats."""
        mock_registry = mocker.patch("src.data_harness.extraction.orchestrator.registry")
        mock_registry.get_extractor.return_value = None
        mocker.patch("src.data_harness.extraction.orchestrator.logger")

        dummy_file = tmp_path / "video.xyz"
        dummy_file.write_text("unknown")
        payload = {"filepath": str(dummy_file)}
        client = MagicMock()

        from src.data_harness.extraction.orchestrator import process_extraction
        process_extraction(client, payload)

        client.publish.assert_called_once()
        args = client.publish.call_args[0]
        published = json.loads(args[1])
        assert published["status"] == "error"
        assert "Unsupported format" in published["error"]
