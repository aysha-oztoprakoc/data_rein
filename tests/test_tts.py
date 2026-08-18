import pytest
from pathlib import Path
from reins.services.tts import PiperTTS, synthesize_speech


def test_piper_tts_availability():
    tts = PiperTTS()
    avail = tts.is_available()
    assert isinstance(avail, bool)


def test_piper_tts_empty_text():
    tts = PiperTTS()
    assert tts.synthesize("", "/tmp/test.wav") is False
    assert tts.synthesize("   ", "/tmp/test.wav") is False


def test_piper_tts_synthesize_graceful_missing_model(tmp_path):
    out = tmp_path / "speech.wav"
    tts = PiperTTS(voice="nonexistent_voice_12345")
    # Should not raise exception; degrades gracefully
    res = tts.synthesize("Hello from data_rein PON testing", out)
    assert isinstance(res, bool)


def test_synthesize_speech_wrapper():
    res = synthesize_speech("", "/tmp/test.wav")
    assert res is False
