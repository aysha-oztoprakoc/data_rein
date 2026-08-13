from pathlib import Path

from reins.harness.memory_ingestion import ingest_knowledge_memories, ingest_sofia_memories
from reins.harness.wiki import WikiDB


def test_sofia_injection_is_idempotent_in_shared_wiki(tmp_path: Path) -> None:
    # Given one valid Sofia extraction and the canonical Wiki target.
    extracted = tmp_path / "extracted"
    extracted.mkdir()
    _ = (extracted / "protocol.xml").write_text(
        "<document><metadata><title>PON</title></metadata><content>Reactive facts only.</content></document>",
        encoding="utf-8",
    )
    wiki_path = tmp_path / "wiki.db"

    # When the import is repeated.
    assert ingest_sofia_memories(extracted, wiki_path) == 1
    assert ingest_sofia_memories(extracted, wiki_path) == 1

    # Then content addressing retains one searchable memory.
    with WikiDB(wiki_path) as wiki:
        results = wiki.search_memories("Reactive facts")
    assert len(results) == 1
    assert results[0]["category"] == "sofia_protocol"


def test_ody_injection_excludes_agent_payloads_and_deduplicates(tmp_path: Path) -> None:
    # Given knowledge content plus an agent-specific payload.
    knowledge_base = tmp_path / "knowledge_base"
    knowledge_base.mkdir()
    _ = (knowledge_base / "directive.md").write_text(
        "One shared source of truth.", encoding="utf-8"
    )
    agents = knowledge_base / "agents"
    agents.mkdir()
    _ = (agents / "private.md").write_text("agent private payload", encoding="utf-8")
    wiki_path = tmp_path / "wiki.db"

    # When broad ingestion is repeated.
    assert ingest_knowledge_memories(knowledge_base, wiki_path) == 1
    assert ingest_knowledge_memories(knowledge_base, wiki_path) == 1

    # Then the shared directive exists once and the excluded payload does not exist.
    with WikiDB(wiki_path) as wiki:
        shared = wiki.search_memories("shared source truth")
        private = wiki.search_memories("agent private payload")
    assert len(shared) == 1
    assert private == []


def test_sofia_injection_rejects_entity_expansion_without_wiki_write(tmp_path: Path) -> None:
    extracted = tmp_path / "extracted"
    extracted.mkdir()
    _ = (extracted / "hostile.xml").write_text(
        '<!DOCTYPE x [<!ENTITY a "entity-bomb">]>'
        "<document><content>&a;&a;</content></document>",
        encoding="utf-8",
    )
    wiki_path = tmp_path / "wiki.db"

    assert ingest_sofia_memories(extracted, wiki_path) == 0
    with WikiDB(wiki_path) as wiki:
        assert wiki.search_memories("entity-bomb") == []
