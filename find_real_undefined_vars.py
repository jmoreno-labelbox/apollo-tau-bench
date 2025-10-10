#!/usr/bin/env python3
"""
Find real undefined variables - ones that will cause runtime errors
"""

from pathlib import Path
import re

def find_undefined_in_content(content, filename):
    """Find variables used but never defined"""
    undefined = []
    
    # Pattern 1: My bug - _id_var = _get_next_id(...) but code uses original var
    id_var_pattern = r'_id_var = _get_next_id\([^,]+, "(\w+)"'
    matches = re.findall(id_var_pattern, content)
    for var_name in matches:
        # Check if var_name is used in non-string context
        usage = re.search(rf'(?<!")(?<!\.)\b{var_name}\b(?!")', content)
        if usage:
            undefined.append(f"{var_name} (created by _get_next_id)")
    
    # Pattern 2: Variable used in assignment but never created
    # Like: data["table"][undefined_var] = value
    dict_assign = re.findall(r'data\["[^"]+"\]\[(\w+)\] =', content)
    for var in dict_assign:
        if var.startswith('new_') or var in ['key', 'i', 'idx']:
            continue  # These are usually defined
        # Check if this variable is assigned anywhere
        if not re.search(rf'\b{var}\s*=', content):
            undefined.append(f"{var} (used in dict assignment)")
    
    # Pattern 3: Common undefined from my edits
    common_undefined = ['matching_data', 'filtered_data', 'cancelled_data', 'fulfilled_data', 
                        'active_data', 'pending_data', 'found_data', 'not_found_data',
                        'supplier_data', 'eligible_data']
    for var in common_undefined:
        if var in content and not re.search(rf'\b{var}\s*=', content):
            undefined.append(f"{var} (never assigned)")
    
    return undefined

def main():
    base = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    all_undefined = {}
    
    for env_dir in sorted(base.iterdir()):
        if env_dir.is_dir() and not env_dir.name.startswith('_'):
            tools_file = env_dir / "tools.py"
            if tools_file.exists():
                content = tools_file.read_text()
                undefined = find_undefined_in_content(content, tools_file.name)
                if undefined:
                    all_undefined[env_dir.name] = undefined
    
    total = sum(len(v) for v in all_undefined.values())
    
    print("=" * 70)
    print(f"REAL UNDEFINED VARIABLES: {total}")
    print("=" * 70)
    print()
    
    for env, vars in sorted(all_undefined.items()):
        print(f"{env}:")
        for var in vars:
            print(f"  - {var}")
        print()
    
    print("=" * 70)
    print(f"Total: {total} undefined variables in {len(all_undefined)} environments")
    print("=" * 70)

if __name__ == "__main__":
    main()

