#!/usr/bin/env python3
"""
Fix dict.append() errors - replace with proper dict assignment.
"""

from pathlib import Path
import re

def fix_dict_append(content: str) -> tuple[str, int]:
    """Fix patterns like dict_var.append(...) to dict_var[key] = value."""
    changes = 0
    
    # Pattern: some_dict.append({...})
    # Replace with proper dict assignment
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Check for .append( on a dict variable
        if '.append(' in line and not '[' in line.split('.append')[0]:
            # This might be dict.append() which is invalid
            # Need to convert to dict[key] = value
            # Common pattern: results.append(item) -> results[key] = item
            # Or: data.append(entry) -> data[len(data)] = entry
            
            match = re.search(r'(\w+)\.append\((.+)\)', line)
            if match:
                dict_name = match.group(1)
                value = match.group(2)
                
                # Try to extract a key if it's a dict being appended
                # Pattern: results.append({"id": "x", ...})
                key_match = re.search(r'\{"(\w+)":\s*"([^"]+)"', value)
                if key_match:
                    key_name = key_match.group(1)
                    key_value = key_match.group(2)
                    # Replace with dict assignment
                    indent = line[:len(line) - len(line.lstrip())]
                    new_line = f'{indent}{dict_name}["{key_value}"] = {value}'
                    fixed_lines.append(new_line)
                    changes += 1
                    continue
                else:
                    # Use index-based assignment
                    indent = line[:len(line) - len(line.lstrip())]
                    new_line = f'{indent}{dict_name}[len({dict_name})] = {value}'
                    fixed_lines.append(new_line)
                    changes += 1
                    continue
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), changes

envs_to_fix = [
    'academic_search_4',
    'consulting_accounting_1', 
    'file_system_9',
    'it_help_desk_6'
]

tau_envs = Path("tau/tau_bench/envs")

total = 0
for env_name in envs_to_fix:
    env_dir = tau_envs / env_name
    if not env_dir.exists():
        continue
    
    print(f"\n{env_name}:")
    
    # Check tools directory
    tools_dir = env_dir / "tools"
    if tools_dir.exists():
        for tool_file in tools_dir.glob("*.py"):
            if tool_file.name == '__init__.py':
                continue
            
            content = tool_file.read_text(encoding='utf-8')
            fixed, changes = fix_dict_append(content)
            
            if changes > 0:
                tool_file.write_text(fixed, encoding='utf-8')
                print(f"  ✓ Fixed {changes} append() calls in {tool_file.name}")
                total += 1

print(f"\nTotal files fixed: {total}")

