import os
from pathlib import Path

def fix_imports():
    src_dir = Path('/home/amdy/data_rein/src/data_harness')
    for py_file in src_dir.rglob('*.py'):
        content = py_file.read_text()
        
        # Replace 'services.xxx' with 'src.data_harness.services.xxx'
        new_content = content.replace('from services.', 'from src.data_harness.services.')
        new_content = new_content.replace('import services.', 'import src.data_harness.services.')
        
        # Replace 'extraction_pipeline.xxx' with 'src.data_harness.extraction.xxx'
        new_content = new_content.replace('from extraction_pipeline', 'from src.data_harness.extraction')
        new_content = new_content.replace('import extraction_pipeline', 'import src.data_harness.extraction')
        
        if new_content != content:
            py_file.write_text(new_content)
            print(f"Fixed imports in {py_file}")

if __name__ == '__main__':
    fix_imports()
