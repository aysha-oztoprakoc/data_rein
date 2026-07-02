#!/bin/bash
set -e

echo "============================================="
echo " DATA-REIN KAD 1.1 PEDANTIC TEST SUITE"
echo "============================================="

echo "[1/2] Building and Running C++20 Pedantic Wall Tests..."
cd /home/amdy/data_rein/cpp_core/tests

for test_file in test_mqtt_stability.cpp test_sync_debouncer.cpp test_lifecycle_security.cpp test_services_pedantic.cpp test_extraction.cpp; do
    echo "Compiling $test_file..."
    g++ -std=c++20 -Wall -Wextra -Wpedantic -Werror -O3 "$test_file" -o "${test_file%.cpp}"
    echo "Running ${test_file%.cpp}..."
    ./"${test_file%.cpp}"
done

echo "[2/3] Running Python AI Pedantic Tests..."
cd /home/amdy/data_rein
source .venv/bin/activate || true
PYTHONPATH=src pytest -v tests/test_ai_training_pon.py tests/test_data_nexus.py tests/test_nexus_deduplication.py tests/test_nexus_scraper.py

echo "============================================="
echo "[3/3] Running Stress Battery (Endurance & Performance)..."
cd /home/amdy/data_rein/cpp_core/tests
echo "Compiling test_stress_battery.cpp..."
g++ -std=c++20 -Wall -Wextra -Wpedantic -Werror -O3 test_stress_battery.cpp -o test_stress_battery -pthread
echo "Running test_stress_battery..."
./test_stress_battery

cd /home/amdy/data_rein
PYTHONPATH=src pytest -v tests/test_stress_battery.py

echo "============================================="
echo " ALL TESTS PASSED. PEDANTIC WALL SECURED."
echo "============================================="
