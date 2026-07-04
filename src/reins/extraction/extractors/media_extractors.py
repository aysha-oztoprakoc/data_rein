from typing import Any, Dict
from ..registry import registry
import os
import subprocess
from .base import BaseExtractor


class RemoteMediaExtractor(BaseExtractor):
    """Base for extractors running on tell via SSH"""
    NODE = "tell"

    def execute_remote(self, filepath: str, output_dir: str, command_template: str, expected_out: str) -> Dict[str, Any]:
        filename = os.path.basename(filepath)
        remote_path = f"/tmp/{filename}"

        # 1. SCP file to tell
        scp_res = subprocess.run(["scp", "-o", "BatchMode=yes", filepath,
                                 f"tell@192.168.0.2:{remote_path}"], capture_output=True)
        if scp_res.returncode != 0:
            return {"status": "error", "error": f"SCP failed: {scp_res.stderr.decode()}"}

        # Format command
        remote_cmd = command_template.format(remote_path=remote_path)

        # 2. Run extraction on tell
        ssh_res = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "tell@192.168.0.2", remote_cmd], capture_output=True)

        # Cleanup remote
        subprocess.run(["ssh", "-o", "BatchMode=yes",
                       "tell@192.168.0.2", f"rm -f {remote_path}*"])

        if ssh_res.returncode == 0:
            out_path = os.path.join(output_dir, expected_out)
            with open(out_path, "wb") as f:
                f.write(ssh_res.stdout)
            return {"status": "success", "output_path": out_path, "metadata": {"format": "remote_media"}}
        else:
            return {"status": "error", "error": f"Remote extraction failed: {ssh_res.stderr.decode()}"}


class ImageOCRExtractor(RemoteMediaExtractor):
    SUPPORTED_FORMATS = [".png", ".jpg", ".jpeg", ".tiff", ".bmp"]

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        expected_out = f"{os.path.basename(filepath)}.ocr.txt"
        cmd = "tesseract {remote_path} {remote_path}_out && cat {remote_path}_out.txt"
        return self.execute_remote(filepath, output_dir, cmd, expected_out)


class ConvertImageOCRExtractor(RemoteMediaExtractor):
    SUPPORTED_FORMATS = [".gif", ".webp"]

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        expected_out = f"{os.path.basename(filepath)}.ocr.txt"
        cmd = "convert {remote_path} {remote_path}.png && tesseract {remote_path}.png {remote_path}_out && cat {remote_path}_out.txt"
        return self.execute_remote(filepath, output_dir, cmd, expected_out)


class SVGOCRExtractor(RemoteMediaExtractor):
    SUPPORTED_FORMATS = [".svg"]

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        expected_out = f"{os.path.basename(filepath)}.ocr.txt"
        cmd = "rsvg-convert -o {remote_path}.png {remote_path} && tesseract {remote_path}.png {remote_path}_out && cat {remote_path}_out.txt"
        return self.execute_remote(filepath, output_dir, cmd, expected_out)


class AudioWhisperExtractor(RemoteMediaExtractor):
    SUPPORTED_FORMATS = [".mp3", ".wav", ".flac",
                         ".ogg", ".aac", ".m4a", ".wma", ".opus"]

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        expected_out = f"{os.path.basename(filepath)}.transcript.txt"
        # Assuming whisper CLI is installed on tell
        cmd = "whisper {remote_path} --output_format txt --output_dir /tmp && cat {remote_path}.txt"
        return self.execute_remote(filepath, output_dir, cmd, expected_out)


class VideoWhisperExtractor(RemoteMediaExtractor):
    SUPPORTED_FORMATS = [
        ".mp4", ".avi", ".mkv", ".mov", ".wmv",
        ".flv", ".webm", ".m4v", ".mpg", ".mpeg"
    ]

    def extract(self, filepath: str, output_dir: str) -> Dict[str, Any]:
        expected_out = f"{os.path.basename(filepath)}.transcript.txt"
        # Extract audio then transcribe
        cmd = "ffmpeg -i {remote_path} -q:a 0 -map a {remote_path}.mp3 -y && whisper {remote_path}.mp3 --output_format txt --output_dir /tmp && cat {remote_path}.mp3.txt"
        return self.execute_remote(filepath, output_dir, cmd, expected_out)


# Auto-register
registry.register(ImageOCRExtractor)
registry.register(ConvertImageOCRExtractor)
registry.register(SVGOCRExtractor)
registry.register(AudioWhisperExtractor)
registry.register(VideoWhisperExtractor)
