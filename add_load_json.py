#!/usr/bin/env python3
"""
Add load_json helper function to banking_services and recipes tool files.
"""

import os
from pathlib import Path

LOAD_JSON_CODE = """

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
        return json.load(f)
"""

def add_load_json_to_file(file_path: Path):
    """Add load_json function to a file if it's used but not defined."""
    content = file_path.read_text(encoding='utf-8')
    
    # Check if load_json is used but not defined
    if 'load_json(' in content and 'def load_json' not in content:
        lines = content.split('\n')
        
        # Find where to insert (after imports)
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('import ') or line.startswith('from '):
                insert_idx = i + 1
            elif line.strip() == '' and insert_idx > 0:
                insert_idx = i + 1
            elif (line.startswith('def ') or line.startswith('class ')) and insert_idx > 0:
                break
        
        lines.insert(insert_idx, LOAD_JSON_CODE)
        file_path.write_text('\n'.join(lines), encoding='utf-8')
        return True
    
    return False

def main():
    envs = ['banking_services_1', 'banking_services_4', 'recipes_4']
    tau_envs = Path("tau/tau_bench/envs")
    
    print("Adding load_json to environments that need it\n")
    
    total = 0
    for env_name in envs:
        env_dir = tau_envs / env_name
        tools_dir = env_dir / "tools"
        
        if not tools_dir.exists():
            continue
        
        print(f"{env_name}:")
        for tool_file in tools_dir.glob("*.py"):
            if tool_file.name == '__init__.py':
                continue
            
            if add_load_json_to_file(tool_file):
                print(f"  ✓ Added to {tool_file.name}")
                total += 1
    
    print(f"\nTotal files fixed: {total}")

if __name__ == "__main__":
    main()

