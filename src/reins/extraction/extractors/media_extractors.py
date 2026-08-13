"""Local multimodal extractors that produce one artifact per source file."""

from __future__ import annotations

import os
import subprocess
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import ClassVar

from typing_extensions import override

from reins.extraction.extractors.base import BaseExtractor, ExtractionMetadata, ExtractionResult
from reins.extraction.registry import registry
from reins.extraction.serialization import save_as_xml
from reins.extraction.vision import describe_image
from reins.harness import external_io


def _command_error(program: str, stderr: str) -> RuntimeError:
    detail = stderr.strip()[-500:] or "no diagnostic output"
    return RuntimeError(f"{program} failed: {detail}")


def _ocr_image(path: Path) -> str:
    result = external_io.run(
        ["tesseract", str(path), "stdout"],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode != 0:
        raise _command_error("tesseract", result.stderr)
    return result.stdout.strip()


def _describe_image(path: Path) -> str:
    return describe_image(path)


def _transcribe_audio(path: Path) -> str:
    from faster_whisper import WhisperModel

    model_name = os.environ.get("DATA_REIN_WHISPER_MODEL", "tiny.en")
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(path), vad_filter=True)
    transcript = " ".join(segment.text.strip() for segment in segments if segment.text.strip())
    if not transcript:
        raise RuntimeError("local Whisper backend returned an empty transcript")
    return transcript


def _prepare_image(source: Path, output_dir: Path) -> Path:
    if source.suffix.lower() not in {".gif", ".webp", ".svg"}:
        return source
    converted = output_dir / f"{source.stem}.png"
    result = external_io.run(
        ["magick", f"{source}[0]", str(converted)],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode != 0:
        raise _command_error("magick", result.stderr)
    return converted


def _sample_video_frames(source: Path, output_dir: Path) -> tuple[Path, ...]:
    output_dir.mkdir(parents=True, exist_ok=True)
    pattern = output_dir / "frame-%04d.png"
    result = external_io.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(source),
            "-vf",
            "select='eq(n,0)+gte(t-prev_selected_t,30)'",
            "-fps_mode",
            "vfr",
            "-frames:v",
            "12",
            str(pattern),
        ],
        capture_output=True,
        text=True,
        timeout=300,
    )
    if result.returncode != 0:
        raise _command_error("ffmpeg frame extraction", result.stderr)
    return tuple(sorted(output_dir.glob("frame-*.png")))


def _extract_video_audio(source: Path, output_dir: Path) -> Path | None:
    audio = output_dir / "audio.wav"
    result = external_io.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(source),
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            str(audio),
        ],
        capture_output=True,
        text=True,
        timeout=300,
    )
    return audio if result.returncode == 0 and audio.exists() else None


def _capture_channel(label: str, operation: Callable[[], str], warnings: list[str]) -> str:
    try:
        value = operation()
        return value.strip()
    except (OSError, RuntimeError, subprocess.SubprocessError, ValueError) as error:
        warnings.append(f"{label}: {error}")
        return ""


def _success(
    source: Path,
    output_dir: str,
    content: str,
    metadata: ExtractionMetadata,
) -> ExtractionResult:
    if not content.strip():
        warnings = "; ".join(metadata.get("warnings", []))
        return {"status": "error", "error": warnings or "no knowledge channels succeeded"}
    output_path = save_as_xml(content, str(source), output_dir)
    return {"status": "success", "output_path": output_path, "metadata": metadata}


class ImageKnowledgeExtractor(BaseExtractor):
    """Combine deterministic OCR and routed visual reasoning for one image."""

    SUPPORTED_FORMATS: ClassVar[list[str]] = [".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif", ".webp", ".svg"]
    MODALITY: ClassVar[str] = "image"

    @override
    def extract(self, filepath: str, output_dir: str) -> ExtractionResult:
        source = Path(filepath)
        warnings: list[str] = []
        with tempfile.TemporaryDirectory(prefix="reins_image_") as temporary:
            prepared = _prepare_image(source, Path(temporary))
            ocr = _capture_channel("ocr", lambda: _ocr_image(prepared), warnings)
            visual = _capture_channel("visual_description", lambda: _describe_image(prepared), warnings)
        channels = [name for name, value in (("ocr", ocr), ("visual_description", visual)) if value]
        sections = [f"## OCR\n{ocr}" if ocr else "", f"## Visual description\n{visual}" if visual else ""]
        return _success(
            source,
            output_dir,
            "\n\n".join(section for section in sections if section),
            {
                "format": source.suffix.lower().lstrip("."),
                "modality": self.MODALITY,
                "extractor": type(self).__name__,
                "node": self.NODE,
                "channels": channels,
                "warnings": warnings,
            },
        )


class AudioKnowledgeExtractor(BaseExtractor):
    """Transcribe spoken knowledge through the optional local Whisper backend."""

    SUPPORTED_FORMATS: ClassVar[list[str]] = [".mp3", ".wav", ".flac", ".ogg", ".aac", ".m4a", ".wma", ".opus"]
    MODALITY: ClassVar[str] = "audio"

    @override
    def extract(self, filepath: str, output_dir: str) -> ExtractionResult:
        source = Path(filepath)
        warnings: list[str] = []
        transcript = _capture_channel("transcript", lambda: _transcribe_audio(source), warnings)
        return _success(
            source,
            output_dir,
            f"## Transcript\n{transcript}" if transcript else "",
            {
                "format": source.suffix.lower().lstrip("."),
                "modality": self.MODALITY,
                "extractor": type(self).__name__,
                "node": self.NODE,
                "channels": ["transcript"] if transcript else [],
                "warnings": warnings,
            },
        )


class VideoKnowledgeExtractor(BaseExtractor):
    """Join sampled frame OCR, visual reasoning, and audio transcription."""

    SUPPORTED_FORMATS: ClassVar[list[str]] = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".mpg", ".mpeg"]
    MODALITY: ClassVar[str] = "video"

    @override
    def extract(self, filepath: str, output_dir: str) -> ExtractionResult:
        source = Path(filepath)
        warnings: list[str] = []
        with tempfile.TemporaryDirectory(prefix="reins_video_") as temporary:
            working = Path(temporary)
            frames = _sample_video_frames(source, working / "frames")
            audio = _extract_video_audio(source, working)
            frame_ocr = [
                value
                for index, frame in enumerate(frames, start=1)
                if (value := _capture_channel(f"frame_{index}_ocr", lambda frame=frame: _ocr_image(frame), warnings))
            ]
            visual = [
                value
                for index, frame in enumerate(frames, start=1)
                if (value := _capture_channel(f"frame_{index}_vision", lambda frame=frame: _describe_image(frame), warnings))
            ]
            transcript = (
                _capture_channel("transcript", lambda: _transcribe_audio(audio), warnings)
                if audio is not None
                else ""
            )
        channels = [
            name
            for name, value in (
                ("frame_ocr", frame_ocr),
                ("visual_description", visual),
                ("transcript", transcript),
            )
            if value
        ]
        sections = (
            ("Frame OCR", "\n".join(frame_ocr)),
            ("Visual description", "\n".join(visual)),
            ("Transcript", transcript),
        )
        content = "\n\n".join(f"## {title}\n{text}" for title, text in sections if text)
        return _success(
            source,
            output_dir,
            content,
            {
                "format": source.suffix.lower().lstrip("."),
                "modality": self.MODALITY,
                "extractor": type(self).__name__,
                "node": self.NODE,
                "channels": channels,
                "frame_count": len(frames),
                "warnings": warnings,
            },
        )


registry.register(ImageKnowledgeExtractor)
registry.register(AudioKnowledgeExtractor)
registry.register(VideoKnowledgeExtractor)
