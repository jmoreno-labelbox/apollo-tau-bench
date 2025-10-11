#!/usr/bin/env python3
"""
Fix missing commas after instruction= strings in tasks_test.py files.
"""

import re
from pathlib import Path
import sys

def fix_instruction_commas(file_path: Path):
    """Fix missing commas after instruction strings."""
    content = file_path.read_text(encoding='utf-8')
    
    def replacer(match):
        instruction = match.group(1)
        indent = match.group(2)
        actions = match.group(3)
        return f'{instruction},\n{indent}{actions}'
    
    # Pattern 1: instruction="..." (no parens)
    pattern1 = r'(instruction="[^"]*")\n(\s+)(actions=\[)'
    new_content = re.sub(pattern1, replacer, content)
    
    # Pattern 2: instruction=("...") (with parens)
    pattern2 = r'(instruction=\("([^"]|"[^)])*"\))\n(\s+)(actions=\[)'
    new_content = re.sub(pattern2, replacer, new_content)
    
    # Pattern 3: instruction=("""...""") (triple quotes with parens)
    pattern3 = r'(instruction=\(""".*?"""\))\n(\s+)(actions=\[)'
    new_content = re.sub(pattern3, replacer, new_content, flags=re.DOTALL)
    
    # Pattern 4: instruction="""...""" (triple quotes no parens)
    pattern4 = r'(instruction=""".*?""")\n(\s+)(actions=\[)'
    new_content = re.sub(pattern4, replacer, new_content, flags=re.DOTALL)
    
    if new_content != content:
        file_path.write_text(new_content, encoding='utf-8')
        return True
    return False

def main():
    if len(sys.argv) > 1:
        files = [Path(f) for f in sys.argv[1:]]
    else:
        # Default: all tasks_test.py in tau/tau_bench/envs
        base = Path("tau/tau_bench/envs")
        files = list(base.glob("*/tasks_test.py"))
    
    print(f"Fixing {len(files)} files...")
    
    fixed = 0
    for f in files:
        if f.exists() and fix_instruction_commas(f):
            print(f"✓ Fixed: {f}")
            fixed += 1
    
    print(f"\nFixed {fixed} files")

if __name__ == "__main__":
    main()

