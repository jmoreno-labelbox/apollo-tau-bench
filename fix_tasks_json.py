#!/usr/bin/env python3
"""Fix JSON formatting issues in tasks.py files."""

import re
import shutil


def fix_airline_3():
    """Fix airline_3/tasks.py outputs format."""
    file = "tau/tau_bench/envs/airline_3/tasks.py"
    with open(file, 'r') as f:
        content = f.read()
    
    # Backup
    shutil.copy2(file, file + ".backup_json")
    
    # Replace pattern: "key": "value" -> "\"key\": \"value\""
    # In outputs arrays, fix unquoted key-value pairs
    pattern = r'(\s+)"(\w+)":\s+"([^"]+)"(,?)\n'
    replacement = r'\1"\\\"\2\\\": \\\"\3\\\""\4\n'
    
    content = re.sub(pattern, replacement, content)
    
    with open(file, 'w') as f:
        f.write(content)
    
    print(f"✅ Fixed {file}")


def fix_retail_2():
    """Fix retail_2/tasks.py."""
    file = "tau/tau_bench/envs/retail_2/tasks.py"
    with open(file, 'r') as f:
        lines = f.readlines()
    
    # Backup
    shutil.copy2(file, file + ".backup_json")
    
    # Line 76: ""audited_order_id": "#W4817420"," -> "\"audited_order_id\": \"#W4817420\","
    if len(lines) > 75:
        line = lines[75]
        if '"audited_order_id": "#W4817420",' in line:
            lines[75] = line.replace('"audited_order_id": "#W4817420",', '"\\\"audited_order_id\\\": \\\"#W4817420\\\"",')
    
    with open(file, 'w') as f:
        f.writelines(lines)
    
    print(f"✅ Fixed {file}")


def fix_retail_5():
    """Fix retail_5/tasks.py."""
    file = "tau/tau_bench/envs/retail_5/tasks.py"
    with open(file, 'r') as f:
        lines = f.readlines()
    
    # Backup
    shutil.copy2(file, file + ".backup_json")
    
    # Line 2964: "annotator": shipping manager," -> "annotator": "shipping manager",
    if len(lines) > 2963:
        line = lines[2963]
        if 'shipping manager,' in line:
            lines[2963] = line.replace('shipping manager,', '"shipping manager",')
    
    with open(file, 'w') as f:
        f.writelines(lines)
    
    print(f"✅ Fixed {file}")


def fix_data_science_6():
    """Fix data_science_6/tasks.py."""
    file = "tau/tau_bench/envs/data_science_6/tasks.py"
    with open(file, 'r') as f:
        lines = f.readlines()
    
    # Backup
    shutil.copy2(file, file + ".backup_json")
    
    # Line 2823: Check for missing comma before it
    if len(lines) > 2822:
        prev_line = lines[2821]
        curr_line = lines[2822]
        if not prev_line.rstrip().endswith(','):
            lines[2821] = prev_line.rstrip() + ',\n'
    
    with open(file, 'w') as f:
        f.writelines(lines)
    
    print(f"✅ Fixed {file}")


def main():
    print("🔧 Fixing tasks.py JSON formatting issues...")
    print("=" * 60)
    
    try:
        fix_airline_3()
    except Exception as e:
        print(f"❌ airline_3: {e}")
    
    try:
        fix_retail_2()
    except Exception as e:
        print(f"❌ retail_2: {e}")
    
    try:
        fix_retail_5()
    except Exception as e:
        print(f"❌ retail_5: {e}")
    
    try:
        fix_data_science_6()
    except Exception as e:
        print(f"❌ data_science_6: {e}")
    
    print("=" * 60)
    print("✅ Done!")


if __name__ == '__main__':
    main()

