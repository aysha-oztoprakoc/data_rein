#include <iostream>
#include <cassert>
#include <chrono>
#include <thread>

// Pedantic test for sync debouncer logic
class SyncDebouncer {
    std::chrono::steady_clock::time_point last_sync;
    std::chrono::milliseconds threshold;
public:
    explicit SyncDebouncer(int ms) : last_sync(std::chrono::steady_clock::now()), threshold(ms) {}
    
    bool should_sync() {
        auto now = std::chrono::steady_clock::now();
        if (std::chrono::duration_cast<std::chrono::milliseconds>(now - last_sync) > threshold) {
            last_sync = now;
            return true;
        }
        return false;
    }
};

void test_debouncer() {
    SyncDebouncer debouncer(100);
    assert(debouncer.should_sync() == false);
    std::this_thread::sleep_for(std::chrono::milliseconds(120));
    assert(debouncer.should_sync() == true);
}

int main() {
    std::cout << "[test_sync_debouncer] Validating synchronous debouncing...\n";
    test_debouncer();
    std::cout << "[test_sync_debouncer] All tests passed.\n";
    return 0;
}
