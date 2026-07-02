import os
import pathlib

def replace_in_file(filepath, old_str, new_str):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if old_str in content:
            content = content.replace(old_str, new_str)
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
    except UnicodeDecodeError:
        # Ignore binary files like PDFs or sqlite databases
        pass
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    return False

def main():
    root_dir = pathlib.Path(os.path.expanduser("~/data_rein"))
    
    old_str = "data_rein"
    new_str = "data_rein"
    
    count = 0
    # Walk through all directories and files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude git, venv, pycache, etc.
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        for filename in filenames:
            if filename.startswith('.') or filename.endswith('.pdf') or filename.endswith('.png') or filename.endswith('.jsonl') or filename == 'vault.json':
                continue
                
            file_path = os.path.join(dirpath, filename)
            
            # Don't replace inside this script itself
            if filename == "rename_project.py":
                continue
                
            if replace_in_file(file_path, old_str, new_str):
                count += 1
                
    print(f"Global renaming complete. Modified {count} files.")

if __name__ == "__main__":
    main()
