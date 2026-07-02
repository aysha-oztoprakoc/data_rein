import os
import time

MOCK_DIR = "/tmp/nexus_internet_mock"

def parse_payload(filepath: str) -> bool:
    """Parses a payload and returns False if it violates security constraints."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Security Constraint: Detect RCE patterns
            if "$(rm -rf" in content or "<script>" in content:
                return False
                
            # RAM Constraint Check (mock memory boundary)
            if len(content) > 100000:
                return False
                
            return True
    except Exception:
        return False

def main():
    print("Starting Python Scraper Benchmark (Pedantic Mode)...")
    start_time = time.time()
    
    success_count = 0
    threats_blocked = 0
    
    # Process sequentially for strict CPU time comparison against C++
    files = [os.path.join(MOCK_DIR, f) for f in os.listdir(MOCK_DIR) if f.endswith(".html")]
    
    for filepath in files:
        if parse_payload(filepath):
            success_count += 1
        else:
            threats_blocked += 1
            
    elapsed = time.time() - start_time
    print(f"Python Engine Completed in {elapsed:.4f} seconds.")
    print(f"Successfully Parsed: {success_count}")
    print(f"Threats/Anomalies Blocked: {threats_blocked}")

if __name__ == "__main__":
    main()
