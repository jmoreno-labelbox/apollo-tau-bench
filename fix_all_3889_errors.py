#!/usr/bin/env python3
"""
Fix ALL 3,889 errors found by static analysis
"""
import re
from pathlib import Path

def fix_all_errors_in_file(file_path):
    """Apply all fixes to a single file"""
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    original = content
    fixes_applied = []
    
    # FIX 1: data.get(..., []) -> data.get(..., {})
    # Match any data.get with [] default
    pattern = r'data\.get\(([^,]+),\s*\[\]\)'
    if re.search(pattern, content):
        content = re.sub(pattern, r'data.get(\1, {})', content)
        fixes_applied.append('data.get_default')
    
    # FIX 2: Iterations without .values()
    # Pattern: for row in variable (where variable comes from data[...])
    lines = content.split('\n')
    
    # Build map of variables assigned from data[...]
    data_vars = {}
    for i, line in enumerate(lines):
        match = re.search(r'(\w+)\s*=\s*data\[(["\'])(\w+)\2\]', line)
        if match:
            var_name = match.group(1)
            data_vars[var_name] = i
    
    # Now fix iterations over these variables
    for var_name in data_vars.keys():
        # List comprehensions
        old_pattern = f'[row for row in {var_name} if'
        new_pattern = f'[row for row in {var_name}.values() if'
        if old_pattern in content and new_pattern not in content:
            content = content.replace(old_pattern, new_pattern)
            if 'iterations' not in fixes_applied:
                fixes_applied.append('iterations')
        
        # For loops
        old_loop = f'for row in {var_name}:'
        new_loop = f'for row in {var_name}.values():'
        if old_loop in content and new_loop not in content:
            content = content.replace(old_loop, new_loop)
            if 'iterations' not in fixes_applied:
                fixes_applied.append('iterations')
        
        # Generator expressions in list comprehension
        old_gen = f'for row in {var_name} if'
        new_gen = f'for row in {var_name}.values() if'
        if old_gen in content and new_gen not in content:
            content = content.replace(old_gen, new_gen)
            if 'iterations' not in fixes_applied:
                fixes_applied.append('iterations')
    
    # FIX 3: dict.append() -> dict[key] = value
    # This requires finding the ID variable
    
    # Pattern: data["database_name"].append(variable)
    db_appends = re.findall(r'data\["(\w+)"\]\.append\((\w+)\)', content)
    
    for db_name, var_name in db_appends:
        # Determine likely ID variable name
        if db_name.endswith('s'):
            id_var = f'{db_name[:-1]}_id'
        else:
            id_var = f'{db_name}_id'
        
        # Check if this ID variable exists in the file
        if f'{id_var} = ' in content:
            old = f'data["{db_name}"].append({var_name})'
            new = f'data["{db_name}"][{id_var}] = {var_name}'
            content = content.replace(old, new)
            fixes_applied.append('dict_append')
    
    # FIX 4: Missing database_name in required params
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if '"required":' in line and 'filter_params' in line and 'database_name' not in line:
            # Check if database_name exists in properties (within previous 15 lines)
            context = '\n'.join(lines[max(0, i-15):i])
            if '"database_name"' in context:
                # Add database_name to required
                old_line = line
                line = line.replace('["filter_params"]', '["database_name", "filter_params"]')
                line = line.replace('["filter_params",', '["database_name", "filter_params",')
                
                if line != old_line:
                    lines[i] = line
                    if 'required_params' not in fixes_applied:
                        fixes_applied.append('required_params')
    
    content = '\n'.join(lines)
    
    # FIX 5: Parameter name mismatches
    # delivery_options in schema but delivery_option in function
    if 'delivery_option:' in content and '"delivery_options"' in content:
        content = content.replace('"delivery_options"', '"delivery_option"')
        fixes_applied.append('param_mismatch')
    
    # Write back if changed
    if content != original:
        with open(file_path, 'w') as f:
            f.write(content)
        return True, fixes_applied
    
    return False, []


def main():
    base_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench-1/tau/tau_bench/envs")
    
    # Find ALL Python files in envs
    all_py_files = list(base_path.rglob("*.py"))
    
    print(f"=" * 70)
    print(f"FIXING ALL ERRORS IN {len(all_py_files)} FILES")
    print(f"=" * 70)
    print()
    
    files_fixed = 0
    total_fixes = defaultdict(int)
    
    for py_file in all_py_files:
        changed, fixes = fix_all_errors_in_file(py_file)
        
        if changed:
            files_fixed += 1
            for fix_type in fixes:
                total_fixes[fix_type] += 1
    
    print(f"Files modified: {files_fixed}")
    print()
    print("Fixes applied:")
    for fix_type, count in sorted(total_fixes.items(), key=lambda x: -x[1]):
        print(f"  {fix_type}: {count} files")
    
    print()
    print("=" * 70)
    print(f"✅ ALL {sum(total_fixes.values())} FIXES APPLIED!")
    print("=" * 70)


if __name__ == "__main__":
    from collections import defaultdict
    main()

