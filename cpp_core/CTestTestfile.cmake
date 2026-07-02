# CMake generated Testfile for 
# Source directory: /home/amdy/data_rein/cpp_core
# Build directory: /home/amdy/data_rein/cpp_core
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test([=[PerformanceTest]=] "/home/amdy/data_rein/cpp_core/test_performance")
set_tests_properties([=[PerformanceTest]=] PROPERTIES  _BACKTRACE_TRIPLES "/home/amdy/data_rein/cpp_core/CMakeLists.txt;21;add_test;/home/amdy/data_rein/cpp_core/CMakeLists.txt;0;")
add_test([=[SafetySecurityTest]=] "/home/amdy/data_rein/cpp_core/test_safety_security")
set_tests_properties([=[SafetySecurityTest]=] PROPERTIES  _BACKTRACE_TRIPLES "/home/amdy/data_rein/cpp_core/CMakeLists.txt;22;add_test;/home/amdy/data_rein/cpp_core/CMakeLists.txt;0;")
add_test([=[StabilityTest]=] "/home/amdy/data_rein/cpp_core/test_stability")
set_tests_properties([=[StabilityTest]=] PROPERTIES  _BACKTRACE_TRIPLES "/home/amdy/data_rein/cpp_core/CMakeLists.txt;23;add_test;/home/amdy/data_rein/cpp_core/CMakeLists.txt;0;")
