import pytest
import time
import json
from unittest.mock import MagicMock, patch

from reins.services.data_nexus.nexus_daemon import NexusDaemon

def test_nexus_mqtt_flood_endurance() -> None:
    """Stress test: Flood the daemon with 5,000 extraction events in milliseconds."""
    with patch('reins.services.data_nexus.nexus_daemon.mqtt.Client'):
        daemon = NexusDaemon()
        
        # We mock process_extraction so the test doesn't actually trigger Ollama inferences.
        # We only want to test the ThreadPoolExecutor routing and Graceful Degradation under flood.
        with patch.object(daemon, 'process_extraction'):
            start_time = time.time()
            
            for i in range(5000):
                msg = MagicMock()
                msg.topic = "data_rein/extract/trigger"
                msg.payload = json.dumps({"filepath": f"/fake/path_{i}.txt"}).encode()
                
                try:
                    daemon.on_message(None, None, msg)
                except Exception as e:
                    pytest.fail(f"Pedantic Wall: Daemon crashed at msg {i} under stress. Error: {e}")
                    
            elapsed = time.time() - start_time
            # Thread pool submission should be nearly instantaneous. If it takes > 2s, we have a routing bottleneck.
            assert elapsed < 2.0, f"Pedantic Wall: MQTT Flood routing bottlenecked, took {elapsed}s."
            
            # Since the mock process_extraction was submitted 5000 times to the local_executor,
            # we don't block for completion, we just assert the daemon survived the flood.

def test_nexus_json_bomb_endurance() -> None:
    """Stress test: Inject deeply nested and corrupted JSON to force parsing crashes."""
    with patch('reins.services.data_nexus.nexus_daemon.mqtt.Client'):
        daemon = NexusDaemon()
        
        start_time = time.time()
        for i in range(1000):
            msg = MagicMock()
            msg.topic = "data_rein/extract/trigger"
            # Deeply nested, malformed JSON garbage to test parsing shield
            msg.payload = (b'{"filepath": "' + (b'[' * 50) + b'GARBAGE' + (b']' * 50) + b'"}')
            
            try:
                daemon.on_message(None, None, msg)
            except Exception as e:
                pytest.fail(f"Pedantic Wall: Daemon crashed on JSON Bomb at iter {i}. Error: {e}")
                
        elapsed = time.time() - start_time
        assert elapsed < 1.0, f"Pedantic Wall: JSON Bomb degradation took {elapsed}s, failing performance standards."
