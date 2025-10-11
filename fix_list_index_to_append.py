#!/usr/bin/env python3
"""
Fix list[len(list)] = value back to list.append(value).
"""

from pathlib import Path
import re

def fix_file(file_path: Path):
    """Replace list[len(list)] = value with list.append(value)."""
    content = file_path.read_text(encoding='utf-8')
    
    # Pattern: var_name[len(var_name)] = value
    # Replace with: var_name.append(value)
    pattern = r'(\w+)\[len\(\1\)\] = (.+)'
    
    def replacer(match):
        var_name = match.group(1)
        value = match.group(2)
        return f'{var_name}.append({value})'
    
    new_content, count = re.subn(pattern, replacer, content)
    
    if count > 0:
        file_path.write_text(new_content, encoding='utf-8')
        return count
    
    return 0

tau_envs = Path("tau/tau_bench/envs")
py_files = [f for f in tau_envs.rglob("*.py") if '__pycache__' not in str(f)]

total_changes = 0
files_fixed = 0

for py_file in py_files:
    changes = fix_file(py_file)
    if changes > 0:
        print(f"✓ {py_file.relative_to(tau_envs)}: {changes} fix(es)")
        total_changes += changes
        files_fixed += 1

print(f"\nFixed {files_fixed} files with {total_changes} total changes")

