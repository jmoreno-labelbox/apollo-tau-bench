#!/usr/bin/env python3
"""
Add missing helper function imports to tool files.
For banking_services_4: adds `from . import load_json` to files that use it.
"""

import argparse
import sys
from pathlib import Path


def needs_load_json_import(source: str) -> bool:
    """Check if file uses load_json but doesn't import it."""
    uses_load_json = "load_json(" in source
    has_import = ("from . import load_json" in source or 
                  "from tau_bench.envs.banking_services_4.tools import load_json" in source or
                  "import load_json" in source)
    return uses_load_json and not has_import


def add_load_json_import(source: str) -> str:
    """Add `from . import load_json` after other imports."""
    lines = source.split('\n')
    
    # Find the last import line
    last_import_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith(('import ', 'from ')):
            last_import_idx = i
    
    if last_import_idx == -1:
        # No imports found, add at the beginning after copyright
        for i, line in enumerate(lines):
            if not line.strip().startswith('#') and line.strip():
                last_import_idx = i - 1
                break
    
    # Insert the import after the last import
    lines.insert(last_import_idx + 1, "from . import load_json")
    
    return '\n'.join(lines)


def fix_file(file_path: Path) -> bool:
    """Fix a single file. Returns True if modified."""
    try:
        source = file_path.read_text(encoding='utf-8')
        original = source
        
        # Check if fix is needed
        if needs_load_json_import(source):
            source = add_load_json_import(source)
        
        if source != original:
            file_path.write_text(source, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Directory containing tool files")
    args = parser.parse_args()
    
    path = Path(args.path)
    files = list(path.glob("*.py"))
    
    modified_count = 0
    for file_path in files:
        if file_path.name == "__init__.py":
            continue  # Skip __init__.py
            
        if fix_file(file_path):
            print(f"✓ {file_path.name}")
            modified_count += 1
    
    print(f"\nModified {modified_count}/{len(files)-1} files")  # -1 for __init__.py


if __name__ == "__main__":
    main()

