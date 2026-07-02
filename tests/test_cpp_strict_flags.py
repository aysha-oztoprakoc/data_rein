"""
test_cpp_strict_flags.py — Pedantic C++ Compilation Validation

Tests if the CMake build system correctly enforces PON's strict C++ rules:
-Wall -Wextra -Werror -Wpedantic.
Any anti-pattern (like unused variables) must cause a compilation failure,
preventing bad code from entering the engine.
"""
import pytest
import subprocess
import os
import shutil
from pathlib import Path

class TestCppStrictFlags:

    @pytest.fixture(autouse=True)
    def setup_teardown(self, tmp_path):
        """Creates a temporary mock CMake project mimicking our C++ Core."""
        self.test_dir = tmp_path / "cpp_mock"
        self.test_dir.mkdir()
        
        self.src_dir = self.test_dir / "src"
        self.src_dir.mkdir()
        
        # Write the strict CMakeLists.txt we use in production
        cmake_content = """cmake_minimum_required(VERSION 3.20)
project(data_rein_cpp_core VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# PON Compliance: Strict warnings
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror -Wpedantic")

add_executable(pon_engine src/main.cpp)
"""
        (self.test_dir / "CMakeLists.txt").write_text(cmake_content)
        
        yield
        
        # Cleanup is handled by pytest tmp_path

    def test_cpp_compilation_blocks_unused_variables(self):
        """
        Validates that an unused variable triggers -Wunused-variable and
        due to -Werror, causes the compilation to fail entirely.
        """
        bad_cpp_code = """
        int main() {
            int unused_var = 42; // Anti-pattern
            return 0;
        }
        """
        (self.src_dir / "main.cpp").write_text(bad_cpp_code)
        
        build_dir = self.test_dir / "build"
        build_dir.mkdir()
        
        # Configure
        config_result = subprocess.run(
            ["cmake", ".."], 
            cwd=str(build_dir), 
            capture_output=True, 
            text=True
        )
        assert config_result.returncode == 0, f"CMake configuration failed: {config_result.stderr}"
        
        # Build (Should fail!)
        build_result = subprocess.run(
            ["cmake", "--build", "."], 
            cwd=str(build_dir), 
            capture_output=True, 
            text=True
        )
        
        assert build_result.returncode != 0, "SECURITY FAILURE: C++ code with unused variables compiled successfully! The strict flags are missing."
        assert "unused variable" in build_result.stderr.lower() or "unused variable" in build_result.stdout.lower()
        
    def test_cpp_compilation_succeeds_with_clean_code(self):
        """
        Validates that completely clean, PON-compliant C++ code compiles successfully.
        """
        clean_cpp_code = """
        int main() {
            return 0;
        }
        """
        (self.src_dir / "main.cpp").write_text(clean_cpp_code)
        
        build_dir = self.test_dir / "build_clean"
        build_dir.mkdir()
        
        subprocess.run(["cmake", ".."], cwd=str(build_dir), capture_output=True)
        build_result = subprocess.run(["cmake", "--build", "."], cwd=str(build_dir), capture_output=True, text=True)
        
        assert build_result.returncode == 0, f"Compilation of clean code failed unexpectedly: {build_result.stderr}\n{build_result.stdout}"
