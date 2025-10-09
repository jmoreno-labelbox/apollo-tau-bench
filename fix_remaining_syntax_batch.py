#!/usr/bin/env python3
"""
Batch fix remaining common syntax patterns
"""

from pathlib import Path
import re

def fix_file(file_path):
    """Apply multiple fix patterns to a file"""
    content = file_path.read_text()
    original = content
    fixes_applied = []
    
    # Pattern 1: Remove extra ) before : in for loops  
    # for x in y.values()): -> for x in y.values():
    if re.search(r'\.values\(\)\)\s*:', content):
        content = re.sub(r'\.values\(\)\)\s*:', r'.values():', content)
        fixes_applied.append("Removed extra ) before :")
    
    # Pattern 2: Add missing ) at end of lines with .values(
    # Look for lines ending with .values() that should have another )
    # This is tricky - need to be careful
    
    # Pattern 3: Fix mismatched brackets - common pattern
    # .values()), -> .values(),
    if ')),  ' in content or 'values()), ' in content:
        content = re.sub(r'\.values\(\)\),', r'.values(),', content)
        fixes_applied.append("Fixed .values()), to .values(),")
    
    if content != original:
        file_path.write_text(content)
        return True, fixes_applied
    
    return False, []

def main():
    base = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    #Read all envs with errors
    env_names = sorted([d.name for d in base.iterdir() 
                       if d.is_dir() and not d.name.startswith('_') and d.name != '__pycache__'])
    
    print("="*70)
    print("BATCH FIXING REMAINING SYNTAX ERRORS")
    print("="*70)
    print()
    
    fixed_count = 0
    for env in env_names:
        tools_file = base / env / "tools.py"
        if tools_file.exists():
            was_fixed, fixes = fix_file(tools_file)
            if was_fixed:
                print(f"✅ {env}: {', '.join(fixes)}")
                fixed_count += 1
    
    print()
    print("="*70)
    print(f"Applied fixes to {fixed_count} files")
    print("="*70)

if __name__ == "__main__":
    main()

