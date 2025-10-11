#!/usr/bin/env python3
"""
Fix STR NO GET errors in recipes_3 environment by fixing specific patterns.
This script fixes the most common patterns that cause STR NO GET errors.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

def fix_str_no_get_patterns(file_path: Path) -> bool:
    """Fix STR NO GET patterns in a file."""
    try:
        content = file_path.read_text()
        rel_path = file_path.relative_to(REPO_ROOT)
        
        print(f"Fixing {rel_path}...")
        
        # Fix pattern 1: for x in data.get("table", []) -> for x in list(data.get("table", {}).values())
        content = re.sub(
            r'for\s+(\w+)\s+in\s+data\.get\("([^"]+)",\s*\[\])',
            r'for \1 in list(data.get("\2", {}).values())',
            content
        )
        
        # Fix pattern 2: [x for x in data.get("table", []) -> [x for x in list(data.get("table", {}).values())
        content = re.sub(
            r'\[([^]]*)\s+for\s+(\w+)\s+in\s+data\.get\("([^"]+)",\s*\[\])',
            r'[\1 for \2 in list(data.get("\3", {}).values())',
            content
        )
        
        # Fix pattern 3: data.get("table", []) in other contexts
        content = re.sub(
            r'data\.get\("([^"]+)",\s*\[\])',
            r'list(data.get("\1", {}).values())',
            content
        )
        
        # Check if syntax is valid
        try:
            ast.parse(content)
            file_path.write_text(content)
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
        
        if fix_str_no_get_patterns(file_path):
            fixed_files += 1
        else:
            failed_files += 1
    
    print(f"\n=== Summary ===")
    print(f"Files attempted: {len(py_files)}")
    print(f"Files fixed: {fixed_files}")
    print(f"Files that still need manual attention: {failed_files}")

if __name__ == "__main__":
    main()
