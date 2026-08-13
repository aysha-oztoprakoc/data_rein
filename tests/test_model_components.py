from __future__ import annotations

from reins.harness.model_providers import ProviderRuntime
from reins.harness.model_types import ExecutionPlane, ModelEntry, ModelSpec
from reins.harness import provider_protocols


def test_model_entry_preserves_explicit_provider_selection() -> None:
    # Given a validated external model entry with an explicit custom provider.
    entry = ModelEntry.model_validate(
        {"model": "vendor-model-v1", "provider": "vendor", "score": 99.0}
    )

    # When it becomes an internal immutable model specification.
    spec = ModelSpec.from_entry(entry)

    # Then provider selection remains configuration-driven.
    assert spec.resolved_provider == "vendor"
    assert spec.score == 99.0


def test_provider_runtime_extracts_nested_comfyui_image_path() -> None:
    # Given a typed ComfyUI history result with a nested output folder.
    history = {
        "outputs": {
            "9": {
                "images": [
                    {"filename": "render.png", "subfolder": "reins"},
                ]
            }
        }
    }

    # When the provider boundary extracts the generated artifact.
    image_path = ProviderRuntime._extract_image_path(history)

    # Then callers receive one portable relative path.
    assert image_path == "reins/render.png"


def test_injected_non_ollama_provider_declares_local_text_capability() -> None:
    # Given a model spec enriched by an injected provider capability policy.
    spec = ModelSpec(
        model="vendor-local-v1",
        provider="vendor",
        capabilities=frozenset({ExecutionPlane.LOCAL_TEXT}),
    )

    # When consumers inspect execution eligibility.
    eligible = ExecutionPlane.LOCAL_TEXT in spec.capabilities

    # Then local execution is allowed independently of the provider's name.
    assert eligible is True


def test_provider_protocol_loader_accepts_structural_sdk(monkeypatch) -> None:
    # Given a runtime module that implements the Gemini SDK surface structurally.
    class FakeGemini:
        def configure(self, *, api_key: str) -> None:
            assert api_key

        def GenerativeModel(self, model: str):
            assert model
            return object()

    module = FakeGemini()
    monkeypatch.setattr(provider_protocols, "import_module", lambda _name: module)

    # When the optional provider loader checks the runtime interface.
    loaded = provider_protocols.load_gemini()

    # Then the structurally compatible module is returned without a hard dependency.
    assert loaded is module
