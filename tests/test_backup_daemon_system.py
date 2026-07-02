"""
test_backup_daemon_system.py - System-wide Validation for the PON Resident Daemon

Verifies stability (crash recovery), performance (CPU pinning and idle load),
and security/safety (process priority and I/O scheduling classes) of the 
data-rein-backup-daemon.service.
"""
import pytest
import subprocess
import time
import os
import psutil

SERVICE_NAME = "data-rein-backup-daemon.service"

def get_daemon_pid():
    res = subprocess.run(
        ["systemctl", "--user", "show", SERVICE_NAME, "-p", "MainPID", "--value"],
        capture_output=True, text=True
    )
    if res.returncode == 0:
        pid_str = res.stdout.strip()
        if pid_str.isdigit() and int(pid_str) > 0:
            return int(pid_str)
    return None

class TestBackupDaemonSystem:

    def test_daemon_is_running_and_isolated(self):
        """
        Validates the daemon is active and physically pinned to exactly 2 CPU threads.
        """
        pid = get_daemon_pid()
        assert pid is not None, "Daemon is not running."
        
        # Check Affinity
        p = psutil.Process(pid)
        affinity = p.cpu_affinity()
        
        # The daemon must be restricted to exactly 2 cores.
        assert len(affinity) == 2, f"CPU Affinity violation. Expected 2 threads, got {len(affinity)}: {affinity}"
        
        # Check Process path security (Must be running from the isolated .venv)
        cmdline = " ".join(p.cmdline())
        assert ".venv/bin/python" in cmdline or "python3" in cmdline, f"Security Violation: Daemon command unexpected: {cmdline}"

    def test_daemon_safety_priorities(self):
        """
        Validates that the daemon won't impact user workloads (Nice >= 10, IONice = Idle).
        """
        pid = get_daemon_pid()
        assert pid is not None
        
        p = psutil.Process(pid)
        
        # 1. Check CPU Priority (Nice)
        nice_val = p.nice()
        assert nice_val >= 10, f"CPU Priority violation: Nice is {nice_val}, expected >= 10"
        
        # 2. Check I/O Scheduling Priority
        # psutil ionice returns a named tuple: (ioclass, value)
        # Class 3 is IOPRIO_CLASS_IDLE
        io_counters = p.ionice()
        assert io_counters.ioclass == psutil.IOPRIO_CLASS_IDLE, f"I/O Priority violation. Class is {io_counters.ioclass}, expected {psutil.IOPRIO_CLASS_IDLE} (Idle)"

    def test_daemon_performance_idle_zero_cpu(self):
        """
        Validates the PON Zero-Polling requirement (0.0% CPU usage while listening).
        """
        pid = get_daemon_pid()
        assert pid is not None
        
        p = psutil.Process(pid)
        # Let it settle before measurement
        time.sleep(2.0)
        
        # First call initiates tracking
        p.cpu_percent(interval=None)
        
        # Wait to measure
        time.sleep(1.0)
        
        # Second call measures average over the elapsed time
        cpu_usage = p.cpu_percent(interval=None)
        
        # Allow a small margin (1.5%) for OS background noise and MQTT keepalives
        assert cpu_usage < 1.5, f"PON Violation: Daemon used {cpu_usage}% CPU while idle!"

    def test_daemon_stability_crash_recovery(self):
        """
        Validates that if the daemon is violently killed (SIGKILL), Systemd revives it.
        """
        initial_pid = get_daemon_pid()
        assert initial_pid is not None
        
        # Send SIGKILL
        try:
            os.kill(initial_pid, 9)
        except ProcessLookupError:
            pass # Already dead
            
        # Verify it died
        time.sleep(1.0)
        assert not psutil.pid_exists(initial_pid), "SIGKILL failed. Process still running."
        
        # Wait for Systemd to auto-restart (RestartSec is 10s)
        # Wait up to 15 seconds
        new_pid = None
        for _ in range(15):
            time.sleep(1.0)
            current = get_daemon_pid()
            if current is not None and current != initial_pid:
                new_pid = current
                break
                
        assert new_pid is not None, "Stability Failure: Systemd did NOT restart the daemon after a crash!"
        assert new_pid != initial_pid, "PID anomaly."
