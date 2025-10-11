#!/usr/bin/env python3
"""
Fix invalid "dictionary" type in JSON schemas - should be "object".
"""

from pathlib import Path

def fix_file(file_path: Path):
    """Replace 'dictionary' with 'object' in type fields."""
    content = file_path.read_text(encoding='utf-8')
    
    if '"type": "dictionary"' in content:
        new_content = content.replace('"type": "dictionary"', '"type": "object"')
        file_path.write_text(new_content, encoding='utf-8')
        return True
    
    return False

tau_envs = Path("tau/tau_bench/envs")
py_files = [f for f in tau_envs.rglob("*.py") if '__pycache__' not in str(f)]

fixed = 0
for py_file in py_files:
    if fix_file(py_file):
        print(f"✓ {py_file.relative_to(tau_envs)}")
        fixed += 1

print(f"\nFixed {fixed} files")

