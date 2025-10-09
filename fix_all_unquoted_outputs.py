#!/usr/bin/env python3
"""Fix all unquoted key-value pairs in tasks.py outputs arrays."""

import re
import shutil


def fix_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Backup
    shutil.copy2(filepath, filepath + ".backup_outputs")
    
    fixed_count = 0
    for i, line in enumerate(lines):
        # Pattern: "key": "value", OR "key": number,
        # Need to wrap in escaped quotes
        
        # Check if line is in outputs array context (has leading spaces and looks like a dict entry)
        if re.match(r'\s+"[^"]+": ', line):
            # Pattern 1: "key": "value",  -> "\"key\": \"value\"",
            if re.match(r'^(\s+)"([^"]+)": "([^"]+)",?$', line):
                match = re.match(r'^(\s+)"([^"]+)": "([^"]+)"(,?)$', line)
                if match:
                    indent, key, value, comma = match.groups()
                    # Check if not already escaped
                    if not line.strip().startswith('"\\'):
                        lines[i] = f'{indent}"\\\"{key}\\\": \\\"{value}\\\""{comma}\n'
                        fixed_count += 1
            
            # Pattern 2: "key": number,  -> "\"key\": number",
            elif re.match(r'^(\s+)"([^"]+)": ([\d.]+)(,?)$', line):
                match = re.match(r'^(\s+)"([^"]+)": ([\d.]+)(,?)$', line)
                if match:
                    indent, key, value, comma = match.groups()
                    # Check if not already escaped
                    if not line.strip().startswith('"\\'):
                        lines[i] = f'{indent}"\\\"{key}\\\": {value}"{comma}\n'
                        fixed_count += 1
    
    if fixed_count > 0:
        with open(filepath, 'w') as f:
            f.writelines(lines)
        return fixed_count
    return 0


def main():
    print("🔧 Fixing unquoted outputs in tasks.py files...")
    print("=" * 60)
    
    files = [
        "tau/tau_bench/envs/airline_3/tasks.py",
        "tau/tau_bench/envs/retail_2/tasks.py",
    ]
    
    total_fixed = 0
    for filepath in files:
        try:
            fixed = fix_file(filepath)
            if fixed > 0:
                print(f"✅ {filepath}: fixed {fixed} lines")
                total_fixed += fixed
            else:
                print(f"⚠️  {filepath}: no changes")
        except Exception as e:
            print(f"❌ {filepath}: {e}")
    
    print("=" * 60)
    print(f"✅ Total lines fixed: {total_fixed}")


if __name__ == '__main__':
    main()

