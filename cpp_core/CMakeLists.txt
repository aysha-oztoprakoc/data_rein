cmake_minimum_required(VERSION 3.20)
project(data_rein_cpp_core VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# PON Compliance: Strict warnings (Pedantic Wall)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror -Wpedantic")

add_executable(pon_engine src/main.cpp)

# Enable CTest
enable_testing()

# Add native test executables
add_executable(test_performance tests/test_performance.cpp)
add_executable(test_safety_security tests/test_safety_security.cpp)
add_executable(test_stability tests/test_stability.cpp)

# Register tests
add_test(NAME PerformanceTest COMMAND test_performance)
add_test(NAME SafetySecurityTest COMMAND test_safety_security)
add_test(NAME StabilityTest COMMAND test_stability)
