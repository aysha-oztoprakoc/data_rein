"""Path-traversal hardening for the Vault Manager's memory write path.

The Vault Manager persists MQTT-delivered memory titles to a Markdown file
inside a fixed wiki directory. A malicious/accidental title containing path
separators or ``..`` must never escape that directory (CWE-22).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from reins.services.vault_manager import sanitize_vault_title


def test_sanitize_plain_title():
    assert sanitize_vault_title("Hello World") == "Hello_World"


def test_sanitize_title_with_spaces_trailing():
    assert sanitize_vault_title("  My Memory  ") == "My_Memory"


def test_sanitize_strips_parent_dir_component():
    assert sanitize_vault_title("../../etc/passwd") == "passwd"


def test_sanitize_strips_absolute_path():
    assert sanitize_vault_title("/etc/shadow") == "shadow"


def test_sanitize_strips_windows_separators():
    assert sanitize_vault_title("..\\..\\win\\evil") == "win\\evil" or sanitize_vault_title("..\\..\\win\\evil") == "evil"


def test_sanitize_rejects_nul_byte():
    with pytest.raises(ValueError):
        sanitize_vault_title("bad\x00name")


def test_sanitize_empty_or_blank_results_in_safe_fallbacks():
    assert sanitize_vault_title("") == ""
    assert sanitize_vault_title("   ").strip() == ""


def test_written_file_stays_within_wiki_dir(tmp_path, mocker):
    """Integration: even a hostile title yields a file inside the wiki dir."""
    from reins.services.vault_manager import VaultManager

    wiki_dir = tmp_path / "Memories"
    wiki_dir.mkdir(parents=True, exist_ok=True)

    manager = VaultManager.__new__(VaultManager)  # skip __init__ (no real MQTT)
    manager.wiki_dir = str(wiki_dir)
    manager.mqtt = None  # type: ignore[assignment]

    mocker.patch(
        "reins.services.vault_manager.VaultManager._mirror_into_wiki",
        return_value=None,
    )

    payload = {"title": "../../pwned", "content": "should stay inside"}
    manager._save_memory(payload)

    files = list(wiki_dir.iterdir())
    assert len(files) == 1
    assert files[0].name == "pwned.md"
    # Nothing was written outside the wiki dir.
    assert not (tmp_path / "pwned.md").exists()
    assert not (Path.home() / "pwned.md").exists()