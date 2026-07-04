import os
import shutil
from pathlib import Path

def migrate():
    base = Path('/home/amdy/data_rein')
    src = base / 'src' / 'data_harness'
    
    # Create directories
    (src / 'services').mkdir(parents=True, exist_ok=True)
    (src / 'extraction').mkdir(parents=True, exist_ok=True)
    (src / 'cli').mkdir(parents=True, exist_ok=True)
    (base / 'tools').mkdir(parents=True, exist_ok=True)
    
    # Move python_core/services -> src/data_harness/services
    old_services = base / 'python_core' / 'services'
    if old_services.exists():
        for item in old_services.iterdir():
            if item.name != '__pycache__':
                shutil.move(str(item), str(src / 'services' / item.name))
                
    # Move extraction_pipeline -> src/data_harness/extraction
    old_ext = base / 'extraction_pipeline'
    if old_ext.exists():
        for item in old_ext.iterdir():
            if item.name != '__pycache__':
                shutil.move(str(item), str(src / 'extraction' / item.name))
                
    # Create __init__.py files
    (src / '__init__.py').touch()
    (src / 'services' / '__init__.py').touch()
    (src / 'extraction' / '__init__.py').touch()
    (src / 'cli' / '__init__.py').touch()
    
    # Remove old dirs if empty
    try:
        if old_services.exists():
            os.rmdir(old_services)
        if (base / 'python_core').exists():
            os.rmdir(base / 'python_core')
        if old_ext.exists():
            os.rmdir(old_ext)
    except OSError:
        pass

    print("Migration structural move complete.")

if __name__ == '__main__':
    migrate()
