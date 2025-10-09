#!/usr/bin/env python3
"""
Fix ALL iteration bugs INCLUDING variables with type annotations
"""
import re
from pathlib import Path

def fix_all_patterns(file_path):
    with open(file_path) as f:
        content = f.read()
    
    original = content
    
    # Find variables assigned from data - with OR without type annotations
    # Pattern: var = data.get(...) OR var: type = data.get(...)
    var_names = set()
    
    for match in re.finditer(r'(\w+)(?:\s*:\s*\w+)?\s*=\s*data\.get\("(\w+)"', content):
        var_names.add(match.group(1))
    
    # Fix iterations
    for var in var_names:
        content = re.sub(rf'for (\w+) in {var}:', rf'for \1 in {var}.values():', content)
        content = re.sub(rf'for (\w+) in {var} if', rf'for \1 in {var}.values() if', content)
        content = re.sub(rf'\[(\w+) for \1 in {var} if', rf'[\1 for \1 in {var}.values() if', content)
        content = re.sub(rf'\[(\w+) for \1 in {var}\]', rf'[\1 for \1 in {var}.values()]', content)
    
    # Fix .append
    dbs = ['articles', 'reviews', 'projects', 'research_logs', 'submissions', 'citations']
    for db in dbs:
        id_var = f'{db[:-1]}_id' if db.endswith('s') else f'{db}_id'
        content = re.sub(rf'{db}\.append\((\w+)\)', rf'data["{db}"][{id_var}] = \1', content)
    
    if content != original:
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    return False

# Fix ALL files in academic_search 2-5
base = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench-1/tau/tau_bench/envs")

for env_num in [2, 3, 4, 5]:
    env_name = f"academic_search_{env_num}"
    env_dir = base / env_name
    
    if env_dir.exists():
        all_py = list(env_dir.rglob("*.py"))
        fixed = 0
        
        for py_file in all_py:
            if fix_all_patterns(py_file):
                fixed += 1
        
        print(f"✅ {env_name}: fixed {fixed} files")

print("\n✅ Done!")

