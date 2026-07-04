import os
from pathlib import Path

def update_tests():
    tests_dir = Path('/home/amdy/data_rein/tests')
    if not tests_dir.exists():
        return
        
    for py_file in tests_dir.rglob('*.py'):
        content = py_file.read_text()
        new_content = content.replace('python_core', 'src.data_harness')
        new_content = new_content.replace('extraction_pipeline', 'src.data_harness.extraction')
        if new_content != content:
            py_file.write_text(new_content)
            print(f"Updated {py_file.name}")
            
    print("Tests imports updated.")

if __name__ == '__main__':
    update_tests()
