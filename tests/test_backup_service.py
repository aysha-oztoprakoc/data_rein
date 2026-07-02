"""
test_backup_service.py — Unit Tests for the Backup Service (bak-1.2)
"""
import pytest
import json
import os
from unittest.mock import patch, MagicMock

# Import the service functions
from src.data_harness.services.backup_service import (
    safe_git_commit, 
    rsync_to_location_with_retry, 
    run_backup
)

class TestBackupService:

    @patch("src.data_harness.services.backup_service.subprocess.run")
    @patch("src.data_harness.services.backup_service.os.path.exists")
    def test_safe_git_commit_aborts_on_merge(self, mock_exists, mock_run):
        """
        Validates that safe_git_commit returns False if MERGE_HEAD exists.
        """
        # Mock exists to return True for MERGE_HEAD
        mock_exists.side_effect = lambda path: "MERGE_HEAD" in str(path)
        
        success, error = safe_git_commit("/mock/repo")
        assert success is False
        assert "Aborted due to active merge/conflict state" in error
        mock_run.assert_not_called()

    @patch("src.data_harness.services.backup_service.subprocess.run")
    @patch("src.data_harness.services.backup_service.os.path.exists")
    def test_safe_git_commit_skips_clean_repo(self, mock_exists, mock_run):
        """
        Validates that it skips commit (but attempts push) if repo has no changes.
        """
        mock_exists.return_value = False
        
        # Mock git status --porcelain returning empty
        mock_status = MagicMock()
        mock_status.stdout = ""
        
        # Mock git remote returning origin
        mock_remote = MagicMock()
        mock_remote.stdout = "origin\n"
        
        mock_run.side_effect = [mock_status, mock_remote, MagicMock()]
        
        success, error = safe_git_commit("/mock/repo")
        assert success is True
        assert error is None
        
        # Should have called status, remote, and push. But NOT commit.
        calls = mock_run.call_args_list
        cmds = [call[0][0] for call in calls]
        assert ["git", "status", "--porcelain"] in cmds
        assert ["git", "push", "origin", "HEAD"] in cmds
        assert ["git", "commit", "-m", "mock"] not in [cmd[:3] for cmd in cmds]

    @patch("src.data_harness.services.backup_service.subprocess.run")
    @patch("src.data_harness.services.backup_service.time.sleep")
    def test_rsync_retry_mechanism(self, mock_sleep, mock_run):
        """
        Validates that rsync retries up to 3 times on failure and respects exponential backoff.
        """
        client = MagicMock()
        dest_config = {"type": "local", "path": "~/mock/{repo_name}"}
        
        # Make subprocess fail twice, then succeed on the third try
        fail_res = MagicMock()
        fail_res.returncode = 1
        fail_res.stderr = b"Connection reset"
        
        success_res = MagicMock()
        success_res.returncode = 0
        
        # Mock run side effects
        mock_run.side_effect = [fail_res, fail_res, success_res]
        
        success, error = rsync_to_location_with_retry(client, "task_1", "/src", dest_config, "my_repo")
        
        assert success is True
        assert error is None
        assert mock_run.call_count == 3
        # Ensure sleep was called twice (after attempt 1 and 2)
        assert mock_sleep.call_count == 2
        # Backoff: base_delay(2) ** 1, base_delay(2) ** 2
        mock_sleep.assert_any_call(2)
        mock_sleep.assert_any_call(4)
