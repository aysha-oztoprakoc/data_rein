"""Local Piper Text-to-Speech synthesis with graceful degradation."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

from reins.harness import external_io
from reins.services.logger import log_degradation

logger = logging.getLogger("reins.tts")


class PiperTTS:
    """Offline CPU-based Text-to-Speech synthesis via piper."""

    def __init__(self, voice: str = "en_US-lessac-medium") -> None:
        self.voice = voice
        self._available: Optional[bool] = None

    def is_available(self) -> bool:
        """Check if piper is importable/executable."""
        if self._available is not None:
            return self._available
        try:
            import piper  # noqa: F401
            self._available = True
        except ImportError:
            try:
                import shutil
                self._available = bool(shutil.which("piper"))
            except Exception as exc:
                logger.warning("Piper binary probe degraded: %s", exc)
                self._available = False
        except Exception as exc:
            logger.warning("Piper import probe degraded: %s", exc)
            self._available = False
        return self._available

    def synthesize(self, text: str, output_path: str | Path) -> bool:
        """Synthesize text to WAV file at output_path."""
        if not text or not text.strip():
            return False

        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        try:
            import piper
            voice_path = Path.home() / ".local" / "share" / "piper-voices" / f"{self.voice}.onnx"
            if not voice_path.exists():
                import shutil
                piper_bin = shutil.which("piper")
                if piper_bin:
                    import subprocess
                    proc = external_io.call(
                        "piper:synthesize",
                        lambda: subprocess.run(
                            [piper_bin, "--output_file", str(out)],
                            input=text.encode("utf-8"),
                            capture_output=True,
                            timeout=30,
                        ),
                    )
                    return proc.returncode == 0 and out.exists()
                logger.info("Piper voice model not downloaded at %s; TTS ready for voice files.", voice_path)
                return False
            voice = piper.PiperVoice.load(str(voice_path))
            with open(out, "wb") as f:
                voice.synthesize(text, f)
            return out.exists()
        except Exception as exc:
            log_degradation("reins.tts")
            logger.warning("Piper TTS synthesis failed: %s", exc)
            return False


def synthesize_speech(text: str, output_path: str | Path, voice: str = "en_US-lessac-medium") -> bool:
    """Convenience wrapper for PiperTTS.synthesize."""
    return PiperTTS(voice=voice).synthesize(text, output_path)
