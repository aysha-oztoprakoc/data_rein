# /// script
# requires-python = ">=3.11"
# dependencies = ["detect-secrets>=1.5.0"]
# ///

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any

from detect_secrets.core.scan import scan_file
from detect_secrets.settings import default_settings

from reins.harness.wiki import WikiDB


MANIFEST_NAME = ".export-manifest.json"


class ExportError(RuntimeError):
    pass


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _filename(identifier: str) -> str:
    readable = "".join(character if character.isalnum() or character in "-_" else "-" for character in identifier)
    readable = readable.strip("-")[:120] or "item"
    return f"{readable}-{_digest(identifier.encode('utf-8'))[:12]}.md"


def _frontmatter(fields: dict[str, Any], body: str) -> bytes:
    lines = ["---"]
    lines.extend(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in fields.items())
    lines.extend(["---", "", body, ""])
    return "\n".join(lines).encode("utf-8")


def _write_record(
    stage: Path,
    directory: str,
    identifier: str,
    fields: dict[str, Any],
    body: str,
) -> dict[str, str]:
    relative = Path(directory) / _filename(identifier)
    payload = _frontmatter(fields, body)
    target = stage / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(payload)
    return {"id": identifier, "kind": directory.lower(), "path": relative.as_posix(), "sha256": _digest(payload)}


def _build_stage(database_path: Path, stage: Path, source_revision: str) -> dict[str, Any]:
    records: list[dict[str, str]] = []
    with WikiDB(database_path) as database:
        pages = database.list_pages(limit=100000) if hasattr(database, "list_pages") else [dict(r) for r in database.conn.execute("SELECT * FROM pages ORDER BY slug").fetchall()]
        memories = database.list_memories(limit=100000) if hasattr(database, "list_memories") else [dict(r) for r in database.conn.execute("SELECT * FROM memories ORDER BY uid").fetchall()]
        for row in pages:
            page = dict(row)
            records.append(
                _write_record(
                    stage,
                    "Pages",
                    str(page["slug"]),
                    {
                        "slug": page["slug"],
                        "title": page["title"],
                        "category": page["category"],
                        "owner": page["owner"],
                        "format": page["fmt"],
                    },
                    str(page["content"]),
                )
            )
        for row in memories:
            memory = dict(row)
            records.append(
                _write_record(
                    stage,
                    "Memories",
                    str(memory["uid"]),
                    {
                        "uid": memory["uid"],
                        "category": memory["category"],
                        "source": memory["source"],
                        "owner": memory["owner"],
                    },
                    str(memory["text"]),
                )
            )
    manifest = {
        "schema_version": 1,
        "source_revision": source_revision,
        "counts": {"pages": len(pages), "memories": len(memories), "files": len(records)},
        "files": sorted(records, key=lambda item: item["path"]),
    }
    manifest_path = stage / MANIFEST_NAME
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def _scan_stage(stage: Path, manifest: dict[str, Any]) -> None:
    findings: list[dict[str, str]] = []
    generated_ids = {item["id"] for item in manifest["files"] if item["kind"] == "memories"}
    try:
        with default_settings():
            for path in sorted(stage.rglob("*")):
                if not path.is_file() or path.name == MANIFEST_NAME:
                    continue
                for secret in scan_file(str(path)):
                    if secret.secret_value in generated_ids:
                        continue
                    findings.append({"path": path.relative_to(stage).as_posix(), "type": secret.type})
    except Exception as error:
        raise ExportError("Secret scanning failed; existing vault was not changed") from error
    if findings:
        summary = json.dumps(findings, sort_keys=True)
        raise ExportError(f"Secret scan blocked vault export: {summary}")


def _managed_files(output: Path, bootstrap_existing: bool) -> set[str]:
    manifest_path = output / MANIFEST_NAME
    if not output.exists():
        return set()
    if not manifest_path.is_file():
        if bootstrap_existing:
            return {path.relative_to(output).as_posix() for path in output.rglob("*") if path.is_file()}
        raise ExportError("Existing vault has no manifest; use --bootstrap-existing once after review")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        managed = {str(item["path"]) for item in manifest["files"]}
    except (OSError, ValueError, KeyError, TypeError) as error:
        raise ExportError("Existing vault manifest is invalid") from error
    actual = {
        path.relative_to(output).as_posix()
        for path in output.rglob("*")
        if path.is_file() and path.name != MANIFEST_NAME
    }
    unmanaged = actual - managed
    if unmanaged:
        raise ExportError("Existing vault contains files not owned by its manifest")
    return managed


def export_vault(
    database_path: Path,
    output: Path,
    source_revision: str,
    *,
    bootstrap_existing: bool = False,
) -> dict[str, Any]:
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    _managed_files(output, bootstrap_existing)
    stage = Path(tempfile.mkdtemp(prefix=f".{output.name}.stage-", dir=output.parent))
    backup = output.parent / f".{output.name}.previous"
    try:
        manifest = _build_stage(database_path.resolve(), stage, source_revision)
        _scan_stage(stage, manifest)
        if backup.exists():
            raise ExportError(f"Recovery directory already exists: {backup}")
        if output.exists():
            output.rename(backup)
        try:
            stage.rename(output)
        except Exception:
            if backup.exists() and not output.exists():
                backup.rename(output)
            raise
        if backup.exists():
            shutil.rmtree(backup)
        return manifest
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", type=Path, default=Path("knowledge_base/wiki.db"))
    parser.add_argument("--output", type=Path, default=Path("wiki_vault"))
    parser.add_argument("--source-revision", required=True)
    parser.add_argument("--bootstrap-existing", action="store_true")
    arguments = parser.parse_args()
    manifest = export_vault(
        arguments.database,
        arguments.output,
        arguments.source_revision,
        bootstrap_existing=arguments.bootstrap_existing,
    )
    print(json.dumps(manifest["counts"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
