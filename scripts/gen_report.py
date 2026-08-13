import os
import shutil
import subprocess
from collections.abc import Sequence
from pathlib import Path

from reins.harness import external_io


def run_probe(command: Sequence[str], *, contains: str | None = None) -> str:
    try:
        result = external_io.run(command, capture_output=True, text=True, check=False)
    except (ConnectionError, OSError, subprocess.SubprocessError) as error:
        return f"probe unavailable: {error}"
    if result.returncode != 0:
        detail = result.stderr.strip() or f"exit {result.returncode}"
        return f"probe unavailable: {detail}"
    lines = result.stdout.splitlines()
    selected = lines if contains is None else [line for line in lines if contains in line]
    return "\n".join(selected) or "probe unavailable: no matching output"


def generate(output: Path | None = None) -> str:
    report = [
        "===================================",
        "       OMARCHY NIX REPORT",
        "===================================\n",
    ]
    probes: tuple[tuple[str, Sequence[str], str | None], ...] = (
        ("OS", ["cat", "/etc/os-release"], None),
        ("KERNEL", ["uname", "-r"], None),
        ("CPU", ["lscpu"], "Model name"),
        ("RAM", ["free", "-h"], None),
        ("GPU", ["lspci"], "VGA"),
        ("INSTALLED PACKAGES", ["pacman", "-Q"], None),
    )
    for heading, command, contains in probes:
        report.extend((f"--- {heading} ---", run_probe(command, contains=contains)))
    content = "\n".join(report)
    kb_path = output or Path("/home/amdy/data_rein/knowledge_base/omarchy-nix.txt")
    _ = kb_path.write_text(content, encoding="utf-8")
    if output is None:
        download = Path("/home/amdy/Downloads/omarchy-nix.txt")
        os.makedirs(download.parent, exist_ok=True)
        _ = shutil.copy(kb_path, download)
        _ = print(f"Successfully generated {kb_path} and {download}")
    return content

if __name__ == "__main__":
    _ = generate()
