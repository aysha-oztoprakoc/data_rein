"""
test_hermes_handover.py - Validation of the Hermes State Handover Protocol
"""
import os
import time

HANDOVER_FILE = "/home/amdy/data_rein/knowledge_base/HERMES_HANDOVER.md"

class TestHermesHandover:
    
    def test_handover_security_permissions(self):
        """
        Validates that the memory matrix is securely locked to owner read/write (0600).
        """
        assert os.path.exists(HANDOVER_FILE), "Handover file does not exist!"
        
        # Get octal permissions of the file
        stat_info = os.stat(HANDOVER_FILE)
        # Extract the lowest 9 bits
        permissions = oct(stat_info.st_mode & 0o777)
        
        # It must be 0600 (read/write by owner only)
        assert permissions == '0o600', f"Security Violation: File permissions are {permissions}, expected 0o600"
        
    def test_handover_performance_and_stability(self):
        """
        Validates that the handover file can be parsed rapidly and does not contain broken markdown.
        """
        start_time = time.time()
        
        with open(HANDOVER_FILE, "r") as f:
            content = f.read()
            
        end_time = time.time()
        elapsed_ms = (end_time - start_time) * 1000
        
        # Performance requirement: Must parse under 50ms
        assert elapsed_ms < 50.0, f"Performance Violation: Handover took {elapsed_ms:.2f}ms to load!"
        
        # Stability requirement: Must have content and valid headers
        assert len(content) > 100, "Stability Violation: Handover file is suspiciously short or empty."
        assert "# HERMES HANDOVER MATRIX" in content, "Stability Violation: Missing primary header."
        assert "## 1." in content, "Stability Violation: Missing structural breakdown."
