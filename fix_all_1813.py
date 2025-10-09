#!/usr/bin/env python3
"""
Fix all 1,813 errors found by direct tool testing
"""
import re
from pathlib import Path

base = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench-1/tau/tau_bench/envs")
all_py_files = list(base.rglob("*.py"))

print(f"Fixing all patterns in {len(all_py_files)} files...")
print()

fixed_count = 0

for py_file in all_py_files:
    with open(py_file) as f:
        content = f.read()
    
    original = content
    
    # FIX 1: Find variables assigned from data.get
    var_names = set()
    for match in re.finditer(r'(\w+)(?:\s*:\s*[\w\[\]]+)?\s*=\s*data\.get\("(\w+)"', content):
        var_names.add(match.group(1))
    
    # Fix iterations
    for var in var_names:
        content = re.sub(rf'for (\w+) in {var}:', rf'for \1 in {var}.values():', content)
        content = re.sub(rf'for (\w+) in {var} if', rf'for \1 in {var}.values() if', content)
        content = re.sub(rf'\[(\w+) for \1 in {var} if', rf'[\1 for \1 in {var}.values() if', content)
        content = re.sub(rf'\[(\w+) for \1 in {var}\]', rf'[\1 for \1 in {var}.values()]', content)
        content = re.sub(rf'any\(([^)]+) for (\w+) in {var}\)', rf'any(\1 for \2 in {var}.values())', content)
        content = re.sub(rf'all\(([^)]+) for (\w+) in {var}\)', rf'all(\1 for \2 in {var}.values())', content)
    
    # FIX 2: .append() on dicts - find ID variable and use dict assignment
    # Common database names
    db_names = re.findall(r'(\w+)\s*=\s*data\.get\("(\w+)"', content)
    for var_name, db_name in db_names:
        id_var = f'{db_name[:-1]}_id' if db_name.endswith('s') else f'{db_name}_id'
        
        if f'{id_var} = ' in content or f'{id_var}:' in content:
            content = re.sub(rf'{var_name}\.append\((\w+)\)', rf'data["{db_name}"][{id_var}] = \1', content)
            content = re.sub(rf'data\["{db_name}"\]\.append\((\w+)\)', rf'data["{db_name}"][{id_var}] = \1', content)
    
    if content != original:
        with open(py_file, 'w') as f:
            f.write(content)
        fixed_count += 1

print(f"✅ Fixed {fixed_count} files")
print()
print("Now run: python3 direct_tool_test_all.py")

