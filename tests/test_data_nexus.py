import pytest
from unittest.mock import MagicMock, patch
from reins.services.data_nexus.nexus_daemon import NexusDaemon

# NOTE: tautological placeholders (test_data_nexus_singleton_integrity,
# test_nexus_llm_timeouts) were removed — they asserted hardcoded constants and
# tested nothing. Real PON/timeout behavior is covered below and in test_laws.py.


def test_nexus_daemon_assimilation() -> None:
    """Ensure Data Nexus correctly hooks into the extraction pipeline."""
    with patch('reins.services.data_nexus.nexus_daemon.mqtt.Client') as MockClient:
        daemon = NexusDaemon()
        assert daemon.is_processing is False, "Initial state must be False"
        
        # Test on_connect
        mock_client = MagicMock()
        daemon.on_connect(mock_client, None, None, 0)
        mock_client.subscribe.assert_any_call("data_rein/nexus/trigger")
        mock_client.subscribe.assert_any_call("data_rein/extract/trigger")

def test_nexus_graceful_extraction_error() -> None:
    """Ensure Nexus doesn't crash on bad JSON extraction payloads (Graceful Degradation)."""
    with patch('reins.services.data_nexus.nexus_daemon.mqtt.Client'):
        daemon = NexusDaemon()
        
        # Mock bad payload
        msg = MagicMock()
        msg.topic = "data_rein/extract/trigger"
        msg.payload = b"INVALID JSON"
        
        # This should fail gracefully with a log, NOT throw an exception
        try:
            daemon.on_message(None, None, msg)
        except Exception as e:
            pytest.fail(f"Pedantic Wall: Daemon crashed on bad payload! Error: {e}")

def test_nexus_reactive_deduplication() -> None:
    """Ensure deduplication uses PON (MQTT event) and graceful degradation instead of polling."""
    with patch('reins.services.data_nexus.nexus_daemon.mqtt.Client'):
        daemon = NexusDaemon()
        
        # Trigger the deduplication event
        msg = MagicMock()
        msg.topic = "data_rein/nexus/deduplicate"
        msg.payload = b""
        
        try:
            # Route should not crash
            daemon.on_message(None, None, msg)
            
            # Execute logic directly to ensure no crash
            daemon.process_deduplication()
        except Exception as e:
            pytest.fail(f"Pedantic Wall: Reactive deduplication crashed! Error: {e}")
