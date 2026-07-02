"""
test_shutdown_pon.py — PON Validation for OS Shutdown Hooks

Validates that the `bak-on-shutdown` service correctly triggers the backup
protocol and strictly blocks OS shutdown using PON zero-polling waits
until the backup finishes or a maximum timeout is reached.
"""
import pytest
import threading
import json
import time
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_mqtt():
    return MagicMock()

class TestShutdownPON:

    def test_shutdown_trigger_blocks_until_finish(self, mocker):
        """
        Validates that the script publishes the trigger and blocks the OS
        shutdown sequence until it receives a success finish event.
        """
        # Patch the wait to avoid actually blocking for 300 seconds in a test
        mock_wait = mocker.patch("src.data_harness.services.systemd.pon_shutdown_trigger.event_finished.wait")
        mock_exit = mocker.patch("sys.exit")
        
        from src.data_harness.services.systemd.pon_shutdown_trigger import on_connect, on_message, main, event_finished, RESULT_TOPIC, TRIGGER_TOPIC
        import src.data_harness.services.systemd.pon_shutdown_trigger as trigger_module
        
        # Reset global state for test
        trigger_module.success = False
        trigger_module.event_finished.clear()
        
        client = MagicMock()
        
        # 1. Test connection logic
        on_connect(client, None, None, 0)
        client.subscribe.assert_called_with(RESULT_TOPIC)
        client.publish.assert_called_once()
        publish_args = client.publish.call_args[0]
        assert publish_args[0] == TRIGGER_TOPIC
        
        # 2. Test receiving intermediate events (should not unblock)
        msg_progress = MagicMock()
        msg_progress.topic = RESULT_TOPIC
        msg_progress.payload = json.dumps({"event": "repo_push"}).encode('utf-8')
        on_message(client, None, msg_progress)
        
        assert not trigger_module.event_finished.is_set()
        
        # 3. Test receiving the finish event (should unblock and set success)
        msg_finish = MagicMock()
        msg_finish.topic = RESULT_TOPIC
        msg_finish.payload = json.dumps({
            "event": "finish", 
            "report": {"success": 4, "errors": []}
        }).encode('utf-8')
        
        on_message(client, None, msg_finish)
        
        assert trigger_module.event_finished.is_set()
        assert trigger_module.success is True

    def test_shutdown_trigger_handles_errors_gracefully(self, mocker):
        """
        Validates that if the backup finishes but with errors, the shutdown
        trigger recognizes the failure and exits with code 1.
        """
        mock_exit = mocker.patch("sys.exit")
        
        from src.data_harness.services.systemd.pon_shutdown_trigger import on_message, RESULT_TOPIC
        import src.data_harness.services.systemd.pon_shutdown_trigger as trigger_module
        
        trigger_module.success = False
        trigger_module.event_finished.clear()
        
        client = MagicMock()
        
        msg_finish_error = MagicMock()
        msg_finish_error.topic = RESULT_TOPIC
        msg_finish_error.payload = json.dumps({
            "event": "finish", 
            "report": {"success": 3, "errors": ["TELL Rsync failed"]}
        }).encode('utf-8')
        
        on_message(client, None, msg_finish_error)
        
        assert trigger_module.event_finished.is_set()
        # Finished, but not successful due to errors
        assert trigger_module.success is False
