#include <iostream>
#include <cassert>
#include <vector>
#include <memory>

// SAFETY & SECURITY TEST: Bounds checking and smart pointer usage.

void test_bounds() {
    std::vector<int> safe_buffer = {1, 2, 3};
    // Using .at() enforces bounds checking, unlike []
    try {
        [[maybe_unused]] int val = safe_buffer.at(5);
        assert(false); // Should not reach here
    } catch (const std::out_of_range&) {
        // Expected
    }
}

void test_memory_safety() {
    std::unique_ptr<int> ptr = std::make_unique<int>(42);
    assert(*ptr == 42);
    // ptr is automatically freed. No raw pointer leaks.
}

int main() {
    test_bounds();
    test_memory_safety();
    std::cout << "[PASS] Safety & Security: Bounds checks and memory safety validated." << std::endl;
    return 0;
}
