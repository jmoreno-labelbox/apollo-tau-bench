#!/usr/bin/env python3
"""
Remove incorrect imports that don't exist in warrior domains.
This script removes import statements for functions that don't actually exist.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

def remove_incorrect_imports(file_path: Path) -> bool:
    """Remove import lines that reference non-existent warrior functions."""
    try:
        content = file_path.read_text()
        lines = content.split('\n')
        
        # Find and remove lines that import from domains_warrior
        new_lines = []
        removed_imports = []
        
        for line in lines:
            if 'from domains_warrior.' in line and 'import' in line:
                removed_imports.append(line.strip())
                print(f"  Removing: {line.strip()}")
            else:
                new_lines.append(line)
        
        if removed_imports:
            # Write back to file
            new_content = '\n'.join(new_lines)
            file_path.write_text(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Remove incorrect warrior domain imports."""
    tau_dir = REPO_ROOT / "tau"
    
    if not tau_dir.exists():
        print(f"tau directory not found: {tau_dir}")
        return
    
    fixed_files = 0
    total_files = 0
    
    print("Removing incorrect warrior domain imports...")
    
    # Find all Python tool files
    for py_file in tau_dir.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
            
        total_files += 1
        
        # Check if file has domains_warrior imports
        try:
            content = py_file.read_text()
            if 'from domains_warrior.' in content:
                print(f"\nProcessing {py_file.relative_to(tau_dir)}:")
                if remove_incorrect_imports(py_file):
                    fixed_files += 1
        except Exception as e:
            print(f"Error reading {py_file}: {e}")
    
    print(f"\n=== Summary ===")
    print(f"Total files scanned: {total_files}")
    print(f"Files fixed: {fixed_files}")

if __name__ == "__main__":
    main()
