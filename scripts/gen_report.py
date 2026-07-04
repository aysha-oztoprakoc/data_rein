import subprocess
import shutil
import os

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True)
    except Exception as e:
        return str(e)

def generate():
    report = []
    report.append("===================================")
    report.append("       OMARCHY NIX REPORT")
    report.append("===================================\n")
    
    report.append("--- OS ---")
    report.append(run_cmd("cat /etc/os-release"))
    
    report.append("--- KERNEL ---")
    report.append(run_cmd("uname -r"))
    
    report.append("--- CPU ---")
    report.append(run_cmd("lscpu | grep 'Model name'"))
    
    report.append("--- RAM ---")
    report.append(run_cmd("free -h"))
    
    report.append("--- GPU ---")
    report.append(run_cmd("lspci | grep VGA"))
    
    report.append("--- INSTALLED PACKAGES ---")
    report.append(run_cmd("pacman -Q"))
    
    content = "\n".join(report)
    
    kb_path = "/home/amdy/data_rein/knowledge_base/omarchy-nix.txt"
    dl_path = "/home/amdy/Downloads/omarchy-nix.txt"
    
    with open(kb_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    os.makedirs(os.path.dirname(dl_path), exist_ok=True)
    shutil.copy(kb_path, dl_path)
    print(f"Successfully generated {kb_path} and {dl_path}")

if __name__ == "__main__":
    generate()
