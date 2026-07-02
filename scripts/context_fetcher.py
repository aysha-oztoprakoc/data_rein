#!/usr/bin/env python3
import os
import glob
import time
from datetime import datetime

BRAIN_DIR = os.path.expanduser("~/.gemini/antigravity-cli/brain")
OUTPUT_PATH = os.path.expanduser("~/data_rein/knowledge_base/SHARED_CONTEXT.md")

def get_latest_file(pattern):
    files = glob.glob(pattern)
    if not files:
        return None
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

def read_file(path):
    if not path or not os.path.exists(path):
        return "No data found."
    with open(path, "r") as f:
        return f.read()

def main():
    print("Fetching latest AI persona context...")
    
    walk_pattern = os.path.join(BRAIN_DIR, "*", "walkthrough.md")
    plan_pattern = os.path.join(BRAIN_DIR, "*", "implementation_plan.md")
    
    latest_walk = get_latest_file(walk_pattern)
    latest_plan = get_latest_file(plan_pattern)
    
    walk_content = read_file(latest_walk)
    plan_content = read_file(latest_plan)
    
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    output = f"""# SHARED PERSONA CONTEXT
> Synchronized at: {now_str}
> Source: Antigravity Architect Brain

This document contains the latest architectural changes, historical context, and technical implementation plans across the Data Harness ecosystem. All agent personas MUST read and align with this context before making decisions.

## 1. Master Walkthrough (Historical Context)
{walk_content}

---

## 2. Master Implementation Plan (Current Goals)
{plan_content}
"""
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        f.write(output)
        
    print(f"Context successfully synchronized to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
