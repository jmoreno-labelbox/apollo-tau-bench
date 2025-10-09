#!/usr/bin/env python3
"""
Comprehensive fix for ONLY academic_search 2, 3, 4, 5 (skip 1)
"""
import re
from pathlib import Path

def comprehensive_fix(file_path):
    """Fix all error patterns"""
    
    with open(file_path) as f:
        content = f.read()
    
    original = content
    
    # FIX 1: Find ALL variables from data and fix their iterations
    var_names = set()
    for match in re.finditer(r'(\w+)\s*=\s*data(?:\.get)?\(?"(\w+)"', content):
        var_names.add(match.group(1))
    
    for var in var_names:
        # All iteration patterns
        content = re.sub(rf'\[(\w+) for \1 in {var} if', rf'[\1 for \1 in {var}.values() if', content)
        content = re.sub(rf'\[(\w+) for \1 in {var}\]', rf'[\1 for \1 in {var}.values()]', content)
        content = re.sub(rf'for (\w+) in {var}:', rf'for \1 in {var}.values():', content)
        content = re.sub(rf'for (\w+) in {var} if', rf'for \1 in {var}.values() if', content)
        content = re.sub(rf'any\(([^)]+) for (\w+) in {var}\)', rf'any(\1 for \2 in {var}.values())', content)
        content = re.sub(rf'all\(([^)]+) for (\w+) in {var}\)', rf'all(\1 for \2 in {var}.values())', content)
    
    # FIX 2: Direct data iterations
    dbs = ['articles', 'users', 'projects', 'citations', 'funding_sources', 'submissions',
           'reviews', 'research_logs', 'notifications', 'subscriptions', 'user_preferences']
    
    for db in dbs:
        content = re.sub(rf'for (\w+) in data\["{db}"\]:', rf'for \1 in data["{db}"].values():', content)
        content = re.sub(rf'for (\w+) in data\.get\("{db}"', rf'for \1 in data.get("{db}"', content)
        # Then add .values() after the get
        content = re.sub(rf'for (\w+) in data\.get\("{db}", {{}}\):', rf'for \1 in data.get("{db}", {{}}).values():', content)
    
    # FIX 3: .append() on all dicts
    for db in dbs:
        id_var = f'{db[:-1]}_id' if db.endswith('s') else f'{db}_id'
        
        # Both data["db"].append and variable.append
        content = re.sub(rf'data\["{db}"\]\.append\((\w+)\)', rf'data["{db}"][{id_var}] = \1', content)
        content = re.sub(rf'{db}\.append\((\w+)\)', rf'data["{db}"][{id_var}] = \1', content)
    
    # FIX 4: data.get defaults
    content = re.sub(r'data\.get\(([^,]+),\s*\[\]\)', r'data.get(\1, {})', content)
    
    if content != original:
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    return False


# Fix ONLY academic_search 2, 3, 4, 5
base = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench-1/tau/tau_bench/envs")
envs_to_fix = ['academic_search_2', 'academic_search_3', 'academic_search_4', 'academic_search_5']

print("Comprehensive fix for academic_search 2-5 (skipping 1)...\n")

for env in envs_to_fix:
    tools_file = base / env / "tools.py"
    if tools_file.exists():
        fixed = comprehensive_fix(tools_file)
        print(f"{'✅' if fixed else '⚪'} {env}")

print("\n✅ Done!")

