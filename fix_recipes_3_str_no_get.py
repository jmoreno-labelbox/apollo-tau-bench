#!/usr/bin/env python3
"""
Fix STR NO GET errors in recipes_3 environment.
This script changes data.get("table", []) to list(data.get("table", {}).values()) in for loops.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

def fix_str_no_get_in_file(file_path: Path) -> bool:
    """Fix STR NO GET errors in a file."""
    try:
        content = file_path.read_text()
        rel_path = file_path.relative_to(REPO_ROOT)
        
        print(f"Fixing {rel_path}...")
        
        # Fix the pattern: for x in data.get("table", []) -> for x in list(data.get("table", {}).values())
        pattern = r'for\s+(\w+)\s+in\s+data\.get\("([^"]+)",\s*\[\])'
        replacement = r'for \1 in list(data.get("\2", {}).values())'
        
        fixed_content = re.sub(pattern, replacement, content)
        
        # Check if syntax is valid
        try:
            ast.parse(fixed_content)
            file_path.write_text(fixed_content)
            print(f"  ✓ Fixed {rel_path}")
            return True
        except SyntaxError as e:
            print(f"  ✗ Still has syntax error in {rel_path}: {e}")
            return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Fix STR NO GET errors in all recipes_3 tool files."""
    recipes_3_dir = REPO_ROOT / "tau/tau_bench/envs/recipes_3/tools"
    
    if not recipes_3_dir.exists():
        print(f"recipes_3 tools directory not found: {recipes_3_dir}")
        return
    
    # Find all Python files in the tools directory
    py_files = list(recipes_3_dir.glob("*.py"))
    
    fixed_files = 0
    failed_files = 0
    
    print("Fixing STR NO GET errors in recipes_3...")
    
    for file_path in py_files:
        if file_path.name == "__init__.py":
            continue
        
        if fix_str_no_get_in_file(file_path):
            fixed_files += 1
        else:
            failed_files += 1
    
    print(f"\n=== Summary ===")
    print(f"Files attempted: {len(py_files)}")
    print(f"Files fixed: {fixed_files}")
    print(f"Files that still need manual attention: {failed_files}")

if __name__ == "__main__":
    main()
