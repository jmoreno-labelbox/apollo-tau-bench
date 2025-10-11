#!/usr/bin/env python3
"""Check syntax of all Python files."""

import ast
from pathlib import Path
import sys

def check_file(file_path):
    """Check if file has valid syntax."""
    try:
        content = file_path.read_text(encoding='utf-8')
        ast.parse(content)
        return True, None
    except SyntaxError as e:
        return False, f"Line {e.lineno}: {e.msg}"
    except Exception as e:
        return False, str(e)

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
py_files = [f for f in target.rglob("*.py") 
            if '__pycache__' not in str(f) 
            and 'domains_apollo' not in str(f)
            and 'domains_warrior' not in str(f)]

print(f"Checking {len(py_files)} files...\n")

errors = []
for f in py_files:
    ok, err = check_file(f)
    if not ok:
        errors.append((f, err))
        print(f"✗ {f}")
        print(f"  {err}\n")

print(f"\n{'='*60}")
print(f"Total: {len(py_files)} files")
print(f"Errors: {len(errors)} files")
print(f"Clean: {len(py_files) - len(errors)} files")
print(f"{'='*60}")

if errors:
    print("\nFiles with errors:")
    for f, _ in errors:
        print(f"  {f}")

