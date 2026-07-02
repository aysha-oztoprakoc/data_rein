import os
import sys
import json
import urllib.request
import pathlib

def read_file(filepath):
    path = pathlib.Path(filepath).expanduser()
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def main():
    print("Initiating Failsafe: Handoff to Local Odysseus (Ollama)...")
    
    # Read the current task list and implementation plan
    # Using the standard workspace locations (assuming they might be in data_rein if already moved)
    # Actually, we should pass the state directly to the local model.
    # The Antigravity artifacts are stored in ~/.gemini/antigravity-cli/brain/dfc1bfe0-ad36-4387-94cd-5017d9ec2a86/
    
    task_file = "~/.gemini/antigravity-cli/brain/dfc1bfe0-ad36-4387-94cd-5017d9ec2a86/task.md"
    plan_file = "~/.gemini/antigravity-cli/brain/dfc1bfe0-ad36-4387-94cd-5017d9ec2a86/implementation_plan.md"
    
    task_content = read_file(task_file)
    plan_content = read_file(plan_file)
    
    if not task_content:
        task_content = "Task file not found. Assume partial completion of data_rein migration."
        
    prompt = f"""[URGENT HANDOFF]
You are Odysseus, the local Data-Harness AI agent. The cloud-based Antigravity agent has exhausted its token quota or was interrupted. 
You must immediately take over the execution of the ongoing architectural refactoring.

Here is the Implementation Plan that was approved:
{plan_content}

Here is the current execution state checklist:
{task_content}

INSTRUCTIONS:
1. Review the checklist to identify what was left incomplete.
2. If the directory rename (data_rein -> data_rein) is incomplete, finish it.
3. If the RAG pipeline ingestion is incomplete, finish it.
4. Execute the tests to validate the environment.
5. Provide a terminal output summarizing your actions to the user.
"""

    data = {
        "model": "qwen2.5-coder:7b", # Or whichever default Ollama model is available
        "prompt": prompt,
        "stream": True
    }
    
    req = urllib.request.Request("http://localhost:11434/api/generate")
    req.add_header('Content-Type', 'application/json')
    
    try:
        response = urllib.request.urlopen(req, json.dumps(data).encode('utf-8'))
        for line in response:
            if line:
                decoded_line = json.loads(line.decode('utf-8'))
                sys.stdout.write(decoded_line.get("response", ""))
                sys.stdout.flush()
    except Exception as e:
        print(f"\n[ERROR] Failed to contact local Ollama instance: {e}")
        print("Please ensure Ollama is running and Odysseus is available.")

if __name__ == "__main__":
    main()
