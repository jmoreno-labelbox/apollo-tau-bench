#!/usr/bin/env python3
"""
Targeted fix for dict iteration errors - handles both data['table'] and load_json() patterns
"""
import sys
import json
import re
import ast
from pathlib import Path
from typing import Dict, List

sys.path.insert(0, str(Path(__file__).parent / "tau"))


def fix_environment(env_name: str, base_path: Path) -> bool:
    """Fix dict iteration errors in a specific environment"""
    
    tools_path = base_path / env_name / "tools.py"
    
    if not tools_path.exists():
        return False
    
    with open(tools_path) as f:
        content = f.read()
    
    original_content = content
    lines = content.split('\n')
    fixed = False
    
    # Pattern 1: var = load_json("file.json") followed by iteration
    # Should add .values() to any iteration over that variable
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a load_json assignment
        match = re.search(r'(\w+)\s*=\s*load_json\(["\']([^"\']+)["\']\)', line)
        if match:
            var_name = match.group(1)
            
            # Look ahead for iterations over this variable in the next 50 lines
            for j in range(i + 1, min(i + 50, len(lines))):
                check_line = lines[j]
                
                # Pattern: for x in var_name:
                iter_match = re.search(rf'for (\w+) in {var_name}:', check_line)
                if iter_match:
                    loop_var = iter_match.group(1)
                    
                    # Check if loop_var is accessed as a dict (e.g., loop_var["field"])
                    # in the next few lines
                    accesses_as_dict = False
                    for k in range(j + 1, min(j + 15, len(lines))):
                        if f'{loop_var}[' in lines[k] or f'{loop_var}.get(' in lines[k]:
                            accesses_as_dict = True
                            break
                        # Stop at next def/class
                        if re.match(r'\s*(def|class)\s', lines[k]):
                            break
                    
                    if accesses_as_dict:
                        # Change to .values()
                        lines[j] = check_line.replace(
                            f'for {loop_var} in {var_name}:',
                            f'for {loop_var} in {var_name}.values():'
                        )
                        fixed = True
                
                # Pattern: [expr for x in var_name]
                comp_match = re.search(rf'\[([^\]]+) for (\w+) in {var_name}[\]\s]', check_line)
                if comp_match:
                    expr = comp_match.group(1)
                    loop_var = comp_match.group(2)
                    
                    # Check if loop_var is accessed as dict in the expression
                    if f'{loop_var}[' in expr or f'{loop_var}.get(' in expr:
                        lines[j] = check_line.replace(
                            f'for {loop_var} in {var_name}',
                            f'for {loop_var} in {var_name}.values()'
                        )
                        fixed = True
                
                # Stop looking if we hit another function/class definition
                if re.match(r'\s*(def|class)\s', check_line):
                    break
        
        i += 1
    
    # Pattern 2: for x in data['table']:
    for i, line in enumerate(lines):
        # Pattern: for loop_var in data['table']:
        match = re.search(r"for (\w+) in data\['([^']+)'\]:", line)
        if match:
            loop_var = match.group(1)
            table_name = match.group(2)
            
            # Check if loop_var is accessed as dict
            accesses_as_dict = False
            for j in range(i + 1, min(i + 15, len(lines))):
                if f'{loop_var}[' in lines[j] or f'{loop_var}.get(' in lines[j]:
                    accesses_as_dict = True
                    break
                if re.match(r'\s*(def|class)\s', lines[j]):
                    break
            
            if accesses_as_dict:
                lines[i] = line.replace(
                    f"for {loop_var} in data['{table_name}']:",
                    f"for {loop_var} in data['{table_name}'].values():"
                )
                fixed = True
        
        # Pattern: for loop_var in data.get('table', []):
        match = re.search(r"for (\w+) in data\.get\('([^']+)', \[\]\):", line)
        if match:
            loop_var = match.group(1)
            table_name = match.group(2)
            
            # Check if loop_var is accessed as dict
            accesses_as_dict = False
            for j in range(i + 1, min(i + 15, len(lines))):
                if f'{loop_var}[' in lines[j] or f'{loop_var}.get(' in lines[j]:
                    accesses_as_dict = True
                    break
                if re.match(r'\s*(def|class)\s', lines[j]):
                    break
            
            if accesses_as_dict:
                lines[i] = line.replace(
                    f"for {loop_var} in data.get('{table_name}', []):",
                    f"for {loop_var} in data.get('{table_name}', {{}}).values():"
                )
                fixed = True
        
        # Pattern: list comprehension
        match = re.search(r"\[([^\]]+) for (\w+) in data\['([^']+)'\]", line)
        if match:
            expr = match.group(1)
            loop_var = match.group(2)
            table_name = match.group(3)
            
            if f'{loop_var}[' in expr or f'{loop_var}.get(' in expr:
                lines[i] = line.replace(
                    f"for {loop_var} in data['{table_name}']",
                    f"for {loop_var} in data['{table_name}'].values()"
                )
                fixed = True
    
    # Pattern 3: Check for places where we're iterating over data.get().values() but calling .values() again
    # accounts = data.get("accounts", {}).values()
    # for account in accounts.values():  # ERROR - accounts is already a values view
    for i, line in enumerate(lines):
        match = re.search(r'(\w+)\s*=\s*data\.get\(["\']([^"\']+)["\'],[^)]+\)\.values\(\)', line)
        if match:
            var_name = match.group(1)
            
            # Look for iteration over var_name
            for j in range(i + 1, min(i + 50, len(lines))):
                check_line = lines[j]
                
                # If we iterate and call .values() again, that's wrong
                if f'for {var_name} in {var_name}.values():' in check_line:
                    # Remove the extra .values()
                    lines[j] = check_line.replace(
                        f'for {var_name} in {var_name}.values():',
                        f'for {var_name} in {var_name}:'
                    )
                    fixed = True
                
                if re.match(r'\s*(def|class)\s', check_line):
                    break
    
    if not fixed:
        return False
    
    new_content = '\n'.join(lines)
    
    # Verify it's valid Python
    try:
        ast.parse(new_content)
        with open(tools_path, 'w') as f:
            f.write(new_content)
        return True
    except SyntaxError as e:
        print(f"  ⚠️  Fix created invalid Python: {e}")
        return False


def main():
    """Main entry point"""
    
    # Load test results
    results_file = Path('direct_tool_test_results.json')
    if not results_file.exists():
        print("❌ direct_tool_test_results.json not found")
        return
    
    with open(results_file) as f:
        results = json.load(f)
    
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    # Find environments with dict iteration errors
    dict_iteration_errors = {}
    for env_name, errors in results.items():
        if not errors:
            continue
        
        tools_with_issue = []
        for error in errors:
            if error.get('tool') != 'LOAD_ERROR':
                error_msg = error['error']
                if ("string indices must be integers" in error_msg or
                    "'str' object has no attribute 'get'" in error_msg):
                    tools_with_issue.append(error['tool'])
        
        if tools_with_issue:
            dict_iteration_errors[env_name] = tools_with_issue
    
    print("=" * 70)
    print("DICT ITERATION FIXER V2")
    print("=" * 70)
    print(f"Found {len(dict_iteration_errors)} environments with dict iteration errors")
    print()
    
    fixed_count = 0
    for env_name, tool_names in dict_iteration_errors.items():
        print(f"  Fixing {env_name} ({len(tool_names)} tools)...", end=" ")
        
        if fix_environment(env_name, base_path):
            print("✅ FIXED")
            fixed_count += 1
        else:
            print("❌ Could not fix")
    
    print()
    print("=" * 70)
    print(f"✅ Fixed {fixed_count}/{len(dict_iteration_errors)} environments")
    print("=" * 70)
    print()
    print("Run: python direct_tool_test_all.py to verify")


if __name__ == "__main__":
    main()

