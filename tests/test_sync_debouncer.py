"""
test_sync_debouncer.py — Pedantic PON Validation for Sync Debouncer

Tests the debounce logic to ensure rapid filesystem events are collapsed
into a single Rsync operation, minimizing IO spam.
"""
import pytest
import time
from unittest.mock import MagicMock

from sync.sync_daemon import Debouncer


class TestSyncDebouncer:
    
    def test_debouncer_collapses_rapid_events(self, mocker):
        """
        Validates that rapid file events are collapsed, creating exactly one 
        rsync call, and that the previous timers are naturally cancelled.
        We use actual threading.Timer logic with a tiny wait time to verify
        real-world concurrency behavior.
        """
        mock_rsync = mocker.patch("sync.sync_daemon.run_rsync")
        client = MagicMock()
        
        mapping = {"source": "/test/source", "destination": "/test/dest"}
        excludes = []
        
        # Extremely fast debounce (10ms)
        debouncer = Debouncer(client, mapping, excludes, wait_time=0.01)
        
        # Fire 5 events sequentially and rapidly
        for i in range(5):
            debouncer.add_event(f"file_{i}.txt")
            
        # Wait slightly longer than the debounce window
        time.sleep(0.05)
        
        # Verify rsync was triggered exactly once
        mock_rsync.assert_called_once()
        
        # Verify MQTT published exactly 5 times (once for each changed file)
        assert client.publish.call_count == 5
        
    def test_debouncer_handles_separate_event_windows(self, mocker):
        """
        Validates that events separated by more than the wait_time trigger
        multiple rsyncs, proving the timer resets properly.
        """
        mock_rsync = mocker.patch("sync.sync_daemon.run_rsync")
        client = MagicMock()
        
        mapping = {"source": "/test/source", "destination": "/test/dest"}
        
        # 10ms debounce
        debouncer = Debouncer(client, mapping, excludes=[], wait_time=0.01)
        
        # First batch
        debouncer.add_event("a.txt")
        time.sleep(0.03) # wait past debounce
        
        # Second batch
        debouncer.add_event("b.txt")
        debouncer.add_event("c.txt")
        time.sleep(0.03) # wait past debounce
        
        assert mock_rsync.call_count == 2
        assert client.publish.call_count == 3
