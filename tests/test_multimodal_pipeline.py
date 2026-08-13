from __future__ import annotations

from pathlib import Path
from typing import ClassVar

import pytest
from pydantic import BaseModel, ConfigDict

from reins.extraction import registry
from reins.extraction.extractors.base import ExtractionResult
from reins.extraction.extractors import media_extractors
from reins.harness import dataset, digest
from reins.harness.wiki import WikiDB
from reins.services.data_nexus import nexus_daemon
from reins.training.records import TrainingMetadata, TrainingRecord


class _WikiPage(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    metadata_json: str


def _successful_content(result: ExtractionResult) -> str:
    output_path = result.get("output_path")
    assert isinstance(output_path, str)
    return Path(output_path).read_text(encoding="utf-8")


def _ocr_knowledge(_path: Path) -> str:
    return "OCR knowledge"


def _visual_knowledge(_path: Path) -> str:
    return "Visual relationship knowledge"


def _spoken_knowledge(_path: Path) -> str:
    return "Spoken lecture knowledge"


def _frame_knowledge(_path: Path) -> str:
    return "Frame knowledge"


def _frame_labels(_path: Path) -> str:
    return "Frame labels"


def _seminar_transcript(_path: Path) -> str:
    return "Seminar transcript"


def test_image_extraction_combines_ocr_and_visual_knowledge(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given an image and independent local OCR and vision analysis channels.
    source = tmp_path / "diagram.png"
    _ = source.write_bytes(b"image-fixture")
    monkeypatch.setattr(media_extractors, "_ocr_image", _ocr_knowledge, raising=False)
    monkeypatch.setattr(
        media_extractors,
        "_describe_image",
        _visual_knowledge,
        raising=False,
    )

    # When the registered image extractor processes the source.
    extractor = registry.get_extractor(source.suffix)
    assert extractor is not None
    result = extractor.extract(str(source), str(tmp_path / "out"))

    # Then both channels form one image knowledge artifact.
    assert result["status"] == "success"
    assert result["metadata"].get("modality") == "image"
    assert result["metadata"].get("channels") == ["ocr", "visual_description"]
    content = _successful_content(result)
    assert "OCR knowledge" in content
    assert "Visual relationship knowledge" in content


def test_audio_extraction_produces_a_transcript_channel(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given an audio source and an available local transcription backend.
    source = tmp_path / "lecture.wav"
    _ = source.write_bytes(b"audio-fixture")
    monkeypatch.setattr(
        media_extractors,
        "_transcribe_audio",
        _spoken_knowledge,
        raising=False,
    )

    # When the registered audio extractor processes the source.
    extractor = registry.get_extractor(source.suffix)
    assert extractor is not None
    result = extractor.extract(str(source), str(tmp_path / "out"))

    # Then the transcript is labeled as audio knowledge.
    assert result["status"] == "success"
    assert result["metadata"].get("modality") == "audio"
    assert result["metadata"].get("channels") == ["transcript"]
    assert "Spoken lecture knowledge" in _successful_content(result)


def test_video_extraction_combines_sampled_frames_and_audio(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given a video whose visual frames and audio track contain distinct knowledge.
    source = tmp_path / "seminar.mp4"
    _ = source.write_bytes(b"video-fixture")
    frame = tmp_path / "frame-0001.jpg"
    _ = frame.write_bytes(b"frame-fixture")
    audio = tmp_path / "track.wav"
    _ = audio.write_bytes(b"audio-fixture")

    def sampled_frames(_path: Path, _output_dir: Path) -> tuple[Path, ...]:
        return (frame,)

    def extracted_audio(_path: Path, _output_dir: Path) -> Path:
        return audio

    monkeypatch.setattr(
        media_extractors,
        "_sample_video_frames",
        sampled_frames,
        raising=False,
    )
    monkeypatch.setattr(
        media_extractors,
        "_extract_video_audio",
        extracted_audio,
        raising=False,
    )
    monkeypatch.setattr(
        media_extractors,
        "_describe_image",
        _frame_knowledge,
        raising=False,
    )
    monkeypatch.setattr(
        media_extractors,
        "_ocr_image",
        _frame_labels,
        raising=False,
    )
    monkeypatch.setattr(
        media_extractors,
        "_transcribe_audio",
        _seminar_transcript,
        raising=False,
    )

    # When the registered video extractor processes the source.
    extractor = registry.get_extractor(source.suffix)
    assert extractor is not None
    result = extractor.extract(str(source), str(tmp_path / "out"))

    # Then one video artifact preserves both modalities and frame provenance.
    assert result["status"] == "success"
    assert extractor.MODALITY == "video"
    assert result["metadata"].get("modality") == "video"
    assert result["metadata"].get("channels") == ["frame_ocr", "visual_description", "transcript"]
    assert result["metadata"].get("frame_count") == 1
    content = _successful_content(result)
    assert "Frame labels" in content
    assert "Frame knowledge" in content
    assert "Seminar transcript" in content


def test_digest_persists_structured_provenance_in_the_wiki(
    wiki: WikiDB,
    tmp_path: Path,
) -> None:
    # Given a text source entering the canonical digest path.
    source = tmp_path / "source.txt"
    _ = source.write_text("A durable extraction fact for model training.", encoding="utf-8")

    # When the source is digested into the isolated Wiki DB.
    results = digest.digest_path(str(source), enrich=False, log_trail=False)

    # Then its Wiki page retains machine-readable extraction provenance.
    assert results[0].ok is True
    assert results[0].slug is not None
    page = wiki.get_page(results[0].slug)
    assert page is not None
    stored = _WikiPage.model_validate(dict(page))
    metadata = TrainingMetadata.model_validate_json(stored.metadata_json)
    assert metadata.modality == "text"
    assert metadata.source_sha256
    assert metadata.extractor == "PlainTextExtractor"
    assert metadata.channels == ("text",)


def test_recursive_digest_ignores_unsupported_runtime_artifacts(
    tmp_path: Path,
) -> None:
    # Given a watched directory containing knowledge beside runtime database files.
    source = tmp_path / "source.txt"
    _ = source.write_text("supported knowledge", encoding="utf-8")
    _ = (tmp_path / "wiki.db").write_bytes(b"sqlite-runtime")

    # When the directory is digested recursively.
    results = digest.digest_path(
        str(tmp_path),
        recursive=True,
        enrich=False,
        log_trail=False,
    )

    # Then only registered source formats enter the result stream.
    assert [item.path for item in results] == [str(source)]
    assert results[0].ok is True


def test_training_export_segments_long_multimodal_pages_without_losing_provenance(
    wiki: WikiDB,
    tmp_path: Path,
) -> None:
    # Given one long video page carrying structured extraction provenance.
    metadata = TrainingMetadata(
        modality="video",
        source_sha256="a" * 64,
        extractor="VideoKnowledgeExtractor",
        channels=("visual_description", "transcript"),
    ).model_dump_json(exclude_none=True)
    _ = wiki.upsert_page(
        "seminar",
        "knowledge-segment " * 80,
        slug="seminar",
        category="digested/video",
        metadata_json=metadata,
    )
    output = tmp_path / "training.jsonl"

    # When the Wiki page is exported for a 128-character local training window.
    stats = dataset.export_jsonl(str(output), modality="video", min_chars=1, max_chars=128)

    # Then every segment remains traceable to the same source and modality.
    records = [
        TrainingRecord.model_validate_json(line)
        for line in output.read_text(encoding="utf-8").splitlines()
    ]
    assert stats.written == len(records)
    assert len(records) > 1
    assert {record.meta.modality for record in records} == {"video"}
    assert {record.meta.source_sha256 for record in records} == {"a" * 64}
    assert [record.meta.segment_index for record in records] == list(range(len(records)))
    assert {record.meta.segment_count for record in records} == {len(records)}


def test_nexus_extraction_event_delegates_to_the_canonical_digest_pipeline(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given a valid extraction event and a canonical digest service fake.
    source = tmp_path / "event.txt"
    _ = source.write_text("event knowledge", encoding="utf-8")
    calls: list[str] = []

    def digest_source(path: str, **_kwargs: bool) -> list[digest.DigestItem]:
        calls.append(path)
        return [digest.DigestItem(path=path, ok=True, slug="event", modality="text")]

    monkeypatch.setattr(digest, "digest_path", digest_source)
    daemon = nexus_daemon.NexusDaemon.__new__(nexus_daemon.NexusDaemon)

    # When Nexus receives the extraction work item.
    daemon.process_extraction({"filepath": str(source), "enrich": False})

    # Then it invokes the one Wiki-writing pipeline rather than a side metadata store.
    assert calls == [str(source)]
