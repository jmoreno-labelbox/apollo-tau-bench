#!/usr/bin/env python3
"""
Add 'import os' to files that use os but don't import it.
"""

from pathlib import Path
import re

def fix_file(file_path: Path):
    """Add import os if needed."""
    content = file_path.read_text(encoding='utf-8')
    
    # Check if os is used but not imported
    uses_os = bool(re.search(r'\bos\.', content))
    has_import = 'import os' in content
    
    if uses_os and not has_import:
        lines = content.split('\n')
        
        # Find where to insert (after other imports or at top)
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('import ') or line.startswith('from '):
                insert_idx = i + 1
            elif line.strip() == '' and insert_idx == 0:
                continue
            elif insert_idx > 0:
                break
        
        lines.insert(insert_idx, 'import os')
        file_path.write_text('\n'.join(lines), encoding='utf-8')
        return True
    
    return False

def main():
    tau_envs = Path("tau/tau_bench/envs")
    
    print("Adding 'import os' to files that use os...\n")
    
    py_files = [f for f in tau_envs.rglob("*.py") if '__pycache__' not in str(f)]
    
    fixed = 0
    for py_file in py_files:
        if fix_file(py_file):
            rel_path = py_file.relative_to(tau_envs)
            print(f"✓ {rel_path}")
            fixed += 1
    
    print(f"\nFixed {fixed} files")

if __name__ == "__main__":
    main()

