#!/usr/bin/env python3
"""
Targeted fix for dict iteration errors - handles multi-line comprehensions
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
    
    # Track variables that hold JSON data (dicts)
    json_var_lines = []  # List of (var_name, line_number) tuples
    
    # Pass 1: Find all load_json assignments
    for i, line in enumerate(lines):
        match = re.search(r'(\w+)\s*=\s*load_json\(["\']([^"\']+)["\']\)', line)
        if match:
            var_name = match.group(1)
            json_var_lines.append((var_name, i))
    
    # Pass 2: Find all iterations over these variables and add .values()
    for var_name, def_line in json_var_lines:
        # Look forward from the definition
        for i in range(def_line + 1, min(def_line + 100, len(lines))):
            line = lines[i]
            
            # Stop at next function/class
            if re.match(r'\s*(def|class)\s', line):
                break
            
            # Single-line pattern: for x in var_name:
            if re.search(rf'\bfor\s+\w+\s+in\s+{var_name}:', line):
                # Check if we're accessing items as dicts
                loop_match = re.search(rf'\bfor\s+(\w+)\s+in\s+{var_name}:', line)
                if loop_match:
                    loop_var = loop_match.group(1)
                    
                    # Check next few lines for dict access
                    accesses_as_dict = False
                    for j in range(i + 1, min(i + 20, len(lines))):
                        if f'{loop_var}[' in lines[j] or f'{loop_var}.get(' in lines[j]:
                            accesses_as_dict = True
                            break
                        if re.match(r'\s*(def|class|for|while)\s', lines[j]):
                            break
                    
                    if accesses_as_dict and '.values()' not in line:
                        lines[i] = line.replace(
                            f'for {loop_var} in {var_name}:',
                            f'for {loop_var} in {var_name}.values():'
                        )
                        fixed = True
            
            # Multi-line comprehension pattern: for x in var_name
            # (might be part of a list/dict comprehension that spans lines)
            # Match: "for x in var_name" at end of line OR "for x in var_name if"
            if re.search(rf'\bfor\s+\w+\s+in\s+{var_name}(\s*$|\s+if\b)', line):
                loop_match = re.search(rf'\bfor\s+(\w+)\s+in\s+{var_name}', line)
                if loop_match:
                    loop_var = loop_match.group(1)
                    
                    # Check surrounding lines for dict access
                    accesses_as_dict = False
                    # Look backwards (for the expression part of comprehension)
                    for j in range(max(0, i - 5), i):
                        if f'{loop_var}[' in lines[j] or f'{loop_var}.get(' in lines[j]:
                            accesses_as_dict = True
                            break
                    # Look forwards (for the if clause)
                    for j in range(i, min(i + 10, len(lines))):
                        if f'{loop_var}[' in lines[j] or f'{loop_var}.get(' in lines[j]:
                            accesses_as_dict = True
                            break
                        # Stop at closing bracket
                        if ']' in lines[j] and lines[j].strip().startswith(']'):
                            break
                    
                    if accesses_as_dict and '.values()' not in line:
                        lines[i] = line.replace(
                            f'for {loop_var} in {var_name}',
                            f'for {loop_var} in {var_name}.values()'
                        )
                        fixed = True
    
    # Pass 3: Fix data['table'] patterns
    for i, line in enumerate(lines):
        # Pattern: for loop_var in data['table']:
        match = re.search(r"for (\w+) in data\['([^']+)'\]:", line)
        if match:
            loop_var = match.group(1)
            table_name = match.group(2)
            
            # Check if loop_var is accessed as dict
            accesses_as_dict = False
            for j in range(i + 1, min(i + 20, len(lines))):
                if f'{loop_var}[' in lines[j] or f'{loop_var}.get(' in lines[j]:
                    accesses_as_dict = True
                    break
                if re.match(r'\s*(def|class|for|while)\s', lines[j]):
                    break
            
            if accesses_as_dict and '.values()' not in line:
                lines[i] = line.replace(
                    f"for {loop_var} in data['{table_name}']:",
                    f"for {loop_var} in data['{table_name}'].values():"
                )
                fixed = True
        
        # Multi-line: for loop_var in data['table']
        match = re.search(r"for (\w+) in data\['([^']+)'\]\s*$", line) or \
                re.search(r"for (\w+) in data\['([^']+)'\]\s+if\b", line)
        if match:
            loop_var = match.group(1)
            table_name = match.group(2)
            
            # Check surrounding lines
            accesses_as_dict = False
            for j in range(max(0, i - 5), min(i + 10, len(lines))):
                if f'{loop_var}[' in lines[j] or f'{loop_var}.get(' in lines[j]:
                    accesses_as_dict = True
                    break
            
            if accesses_as_dict and '.values()' not in line:
                lines[i] = line.replace(
                    f"for {loop_var} in data['{table_name}']",
                    f"for {loop_var} in data['{table_name}'].values()"
                )
                fixed = True
        
        # Pattern: for loop_var in data.get('table', []):
        match = re.search(r"for (\w+) in data\.get\('([^']+)', \[\]\):", line)
        if match:
            loop_var = match.group(1)
            table_name = match.group(2)
            
            # Check if loop_var is accessed as dict
            accesses_as_dict = False
            for j in range(i + 1, min(i + 20, len(lines))):
                if f'{loop_var}[' in lines[j] or f'{loop_var}.get(' in lines[j]:
                    accesses_as_dict = True
                    break
                if re.match(r'\s*(def|class|for|while)\s', lines[j]):
                    break
            
            if accesses_as_dict:
                lines[i] = line.replace(
                    f"for {loop_var} in data.get('{table_name}', []):",
                    f"for {loop_var} in data.get('{table_name}', {{}}).values():"
                )
                fixed = True
    
    # Pass 4: Fix double .values() calls
    for i, line in enumerate(lines):
        match = re.search(r'(\w+)\s*=\s*data\.get\(["\']([^"\']+)["\'],[^)]+\)\.values\(\)', line)
        if match:
            var_name = match.group(1)
            
            # Look for iteration over var_name with extra .values()
            for j in range(i + 1, min(i + 50, len(lines))):
                check_line = lines[j]
                
                if f'for {var_name} in {var_name}.values():' in check_line:
                    # Should just be: for var_name in var_name:
                    # But that's weird, so the original line shouldn't have .values()
                    # Let's remove .values() from the original assignment instead
                    lines[i] = lines[i].replace('.values()', '')
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
        # Restore original
        with open(tools_path, 'w') as f:
            f.write(original_content)
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
    print("DICT ITERATION FIXER V3 - Multi-line comprehensions")
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

