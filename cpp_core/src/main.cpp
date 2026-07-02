#include <iostream>
#include <functional>
#include <vector>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <queue>
#include <memory>

// PON Architecture: Zero-polling, Reactive Event Loop
class EventQueue {
public:
    void push(std::function<void()> task) {
        std::lock_guard<std::mutex> lock(mutex_);
        tasks_.push(std::move(task));
        cv_.notify_one();
    }

    void process_one() {
        std::function<void()> task;
        {
            std::unique_lock<std::mutex> lock(mutex_);
            cv_.wait(lock, [this]() { return !tasks_.empty() || stop_; });
            if (stop_ && tasks_.empty()) return;
            
            task = std::move(tasks_.front());
            tasks_.pop();
        }
        if (task) {
            task();
        }
    }

    void stop() {
        std::lock_guard<std::mutex> lock(mutex_);
        stop_ = true;
        cv_.notify_all();
    }
    
    bool is_stopped() {
        std::lock_guard<std::mutex> lock(mutex_);
        return stop_ && tasks_.empty();
    }

private:
    std::queue<std::function<void()>> tasks_;
    std::mutex mutex_;
    std::condition_variable cv_;
    bool stop_{false};
};

// Global Event Queue (Engine core)
EventQueue g_engine_queue;

// Base Attribute (FBE)
template <typename T>
class Attribute {
public:
    explicit Attribute(T initial_value) : value_(std::move(initial_value)) {}

    void set(T new_value) {
        {
            std::lock_guard<std::mutex> lock(mutex_);
            if (value_ == new_value) return;
            value_ = std::move(new_value);
        }
        notify();
    }

    T get() const {
        std::lock_guard<std::mutex> lock(mutex_);
        return value_;
    }

    void subscribe(std::function<void(const T&)> callback) {
        std::lock_guard<std::mutex> lock(mutex_);
        callbacks_.push_back(std::move(callback));
    }

private:
    void notify() {
        T current_value = get();
        std::vector<std::function<void(const T&)>> callbacks_copy;
        {
            std::lock_guard<std::mutex> lock(mutex_);
            callbacks_copy = callbacks_;
        }
        for (const auto& cb : callbacks_copy) {
            g_engine_queue.push([cb, current_value]() {
                cb(current_value);
            });
        }
    }

    T value_;
    mutable std::mutex mutex_;
    std::vector<std::function<void(const T&)>> callbacks_;
};

int main() {
    std::cout << "[PON Engine] C++ Pedantic Wall initialized." << std::endl;
    std::cout << "[PON Engine] Starting reactive event loop..." << std::endl;

    // Define Fact Base Elements (Attributes)
    Attribute<int> system_status(0); // 0 = idle, 1 = running, 2 = shutdown

    // Define Rules/Methods (Subscribers)
    system_status.subscribe([](const int& status) {
        std::cout << "[Method] System status changed to: " << status << std::endl;
        if (status == 2) {
            std::cout << "[Rule] Shutdown requested. Halting engine." << std::endl;
            g_engine_queue.stop();
        }
    });

    // Simulate external instigation (e.g., from network/MQTT) in a detached thread
    std::thread ext_thread([&system_status]() {
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
        system_status.set(1);
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
        system_status.set(2);
    });
    ext_thread.detach();

    // Zero-polling Main Event Loop (100% blocking on condition_variable)
    while (!g_engine_queue.is_stopped()) {
        g_engine_queue.process_one();
    }

    std::cout << "[PON Engine] Clean shutdown achieved." << std::endl;
    return 0;
}
