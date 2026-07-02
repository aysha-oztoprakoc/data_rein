#!/bin/bash
set -e

# Setup Arena
python3 /home/amdy/data_rein/scripts/generate_mock_internet.py

echo "============================================="
echo " THE SCRAPER BATTLE BENCHMARK"
echo "============================================="

# 1. Compile C++ with Pedantic Wall mode
echo "[*] Compiling C++20 Pedantic Engine..."
cd /home/amdy/data_rein/cpp_core
g++ -std=c++20 -Wall -Wextra -Wpedantic -O3 tests/test_scraper_benchmark.cpp -o scraper_benchmark_cpp

# 2. Run C++ Battle
echo ""
echo "---------------------------------------------"
echo " >>> GLADIATOR 1: C++20 (Wall) <<<"
echo "---------------------------------------------"
time ./scraper_benchmark_cpp

# 3. Run Python Battle
echo ""
echo "---------------------------------------------"
echo " >>> GLADIATOR 2: Python 3.11 <<<"
echo "---------------------------------------------"
time python3 /home/amdy/data_rein/python_core/tests/scraper_benchmark.py

echo ""
echo "============================================="
echo " BATTLE CONCLUDED. REVIEW METRICS ABOVE."
echo "============================================="
