#!/usr/bin/env python3
"""
Auto-fix common syntax errors in tools.py files
"""

from pathlib import Path
import re

# Patterns to fix
FIXES = [
    # Pattern 1: for x in dict.values()): -> for x in dict.values():
    {
        'pattern': r'for \w+ in \w+\.values\(\)\):',
        'replacement': lambda m: m.group(0)[:-2] + ':',  # Remove one )
        'description': 'Remove extra ) after .values() in for loops'
    },
    # Pattern 2: list(...).values() -> list(...).values())
    {
        'pattern': r'list\(\{[^}]+\}\.values\(\)\n',
        'replacement': lambda m: m.group(0)[:-1] + ')\n',
        'description': 'Add missing ) after list().values()'
    },
]

def fix_file(file_path):
    """Try to auto-fix common patterns in a file"""
    try:
        content = file_path.read_text()
        original = content
        fixes_applied = []
        
        # Apply each fix pattern
        for fix in FIXES:
            matches = list(re.finditer(fix['pattern'], content))
            if matches:
                for match in matches:
                    fixes_applied.append(f"{fix['description']}: {match.group(0)[:50]}")
                content = re.sub(fix['pattern'], fix['replacement'], content)
        
        if content != original:
            file_path.write_text(content)
            return True, fixes_applied
        
        return False, []
    except Exception as e:
        return False, [f"Error: {e}"]

def main():
    base = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    # Read syntax error report
    with open('syntax_errors_report.txt') as f:
        lines = f.readlines()
    
    # Extract environment names
    envs_with_errors = []
    for i, line in enumerate(lines):
        if line.strip() and not line.startswith(' '):
            envs_with_errors.append(line.strip())
    
    print(f"Found {len(envs_with_errors)} environments with syntax errors")
    print()
    
    fixed_count = 0
    for env in envs_with_errors[:10]:  # Start with first 10
        tools_file = base / env / "tools.py"
        if tools_file.exists():
            was_fixed, fixes = fix_file(tools_file)
            if was_fixed:
                print(f"✅ {env}: Applied {len(fixes)} fixes")
                fixed_count += 1
            else:
                print(f"⚠️  {env}: No auto-fixes applied")
    
    print()
    print(f"Auto-fixed {fixed_count} files")

if __name__ == "__main__":
    main()

