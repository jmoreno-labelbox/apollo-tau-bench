#!/usr/bin/env python3
"""
Fix low-hanging fruit errors in tau environments:
1. str_no_get errors - Pattern 1: Dict vs list bug
2. dict_no_append errors - Pattern 5: Use dict assignment instead of append
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Any

# Environments with str_no_get errors (Pattern 1)
STR_NO_GET_ENVS = [
    'dev_ops_1', 'dev_ops_2', 'dev_ops_3', 'digital_commerce_5',
    'figma_gmail_mcp_pipeline_5', 'file_system_8', 'real_estate_sales_2',
    'real_estate_sales_4', 'recipes_3', 'recipes_5', 'retail_3',
    'retail_6', 'social_media_advertising_4'
]

# Environments with dict_no_append errors (Pattern 5)
DICT_NO_APPEND_ENVS = [
    'academic_search_4', 'file_system_9', 'recipes_2'
]

def fix_str_no_get_pattern(content: str) -> tuple[str, int]:
    """
    Fix Pattern 1: str object has no attribute 'get'
    Replace: data.get('key', {}).values()
    With: list(data.get('key', {}).values()) or data.get('key', [])
    """
    fixes_made = 0
    
    # Pattern 1: .get('key', {}).values() where key might be a list
    # This needs to be: list(data.get('key', {}).values()) if dict, or data.get('key', []) if list
    patterns = [
        # Pattern: variable.get('key', {}).values()
        (r"(\w+)\.get\('(\w+)',\s*\{\}\)\.values\(\)", r"list(\1.get('\2', {}).values()) if isinstance(\1.get('\2'), dict) else \1.get('\2', [])"),
        
        # Pattern: variable.get("key", {}).values()
        (r'(\w+)\.get\("(\w+)",\s*\{\}\)\.values\(\)', r'list(\1.get("\2", {}).values()) if isinstance(\1.get("\2"), dict) else \1.get("\2", [])'),
        
        # Simpler pattern: just wrap in list() for now
        (r"(\w+\.get\(['\"][\w_]+['\"],\s*\{\}\))\.values\(\)", r"list(\1.values())"),
    ]
    
    for pattern, replacement in patterns:
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            fixes_made += content.count(pattern.split('(')[0]) - new_content.count(pattern.split('(')[0])
            content = new_content
    
    return content, fixes_made

def fix_dict_no_append_pattern(content: str) -> tuple[str, int]:
    """
    Fix Pattern 5: dict object has no attribute 'append'
    Replace: dict_var.append(...)
    With: dict_var[key] = value or dict_var.update(...)
    """
    fixes_made = 0
    
    # This is trickier - we need to find dict.append() calls
    # Common pattern: some_dict.append({...})
    # Should be: some_dict[key] = {...} or some_dict.update({...})
    
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        # Look for pattern: dict_name.append({...})
        match = re.search(r'(\w+)\.append\((\{[^}]+\})\)', line)
        if match:
            dict_name = match.group(1)
            dict_value = match.group(2)
            
            # Try to extract a key from the dict
            key_match = re.search(r'["\'](\w+)["\']:\s*', dict_value)
            if key_match:
                key = key_match.group(1)
                # Replace with dictionary assignment
                new_line = line.replace(
                    f'{dict_name}.append({dict_value})',
                    f'{dict_name}.update({dict_value})'
                )
                new_lines.append(new_line)
                fixes_made += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    if fixes_made > 0:
        content = '\n'.join(new_lines)
    
    return content, fixes_made

def fix_tool_file(file_path: str, env_name: str, error_type: str) -> bool:
    """Fix a single tool file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  Error reading {file_path}: {e}")
        return False
    
    original_content = content
    total_fixes = 0
    
    # Apply fixes based on error type
    if error_type == 'str_no_get':
        content, fixes = fix_str_no_get_pattern(content)
        total_fixes += fixes
    elif error_type == 'dict_no_append':
        content, fixes = fix_dict_no_append_pattern(content)
        total_fixes += fixes
    
    # Write back if changes were made
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            if total_fixes > 0:
                print(f"  ✓ Fixed {total_fixes} issues in {file_path}")
            return True
        except Exception as e:
            print(f"  Error writing {file_path}: {e}")
            return False
    
    return False

def find_tool_files(env_name: str) -> List[str]:
    """Find all tool files in an environment"""
    env_path = Path(f'tau/tau_bench/envs/{env_name}/tools')
    if not env_path.exists():
        return []
    
    return [str(f) for f in env_path.glob('*.py') if f.name != '__init__.py']

def fix_str_no_get_errors():
    """Fix all str_no_get errors"""
    print("="*70)
    print("FIXING STR_NO_GET ERRORS (Pattern 1: Dict vs List Bug)")
    print("="*70)
    
    total_envs = len(STR_NO_GET_ENVS)
    fixed_envs = 0
    total_files_fixed = 0
    
    for env_name in STR_NO_GET_ENVS:
        print(f"\nProcessing {env_name}...")
        tool_files = find_tool_files(env_name)
        
        if not tool_files:
            print(f"  No tool files found for {env_name}")
            continue
        
        env_fixed = False
        for tool_file in tool_files:
            if fix_tool_file(tool_file, env_name, 'str_no_get'):
                env_fixed = True
                total_files_fixed += 1
        
        if env_fixed:
            fixed_envs += 1
            print(f"  ✓ Environment fixed")
        else:
            print(f"  No changes needed")
    
    print(f"\n{'='*70}")
    print(f"STR_NO_GET Summary: Fixed {fixed_envs}/{total_envs} environments ({total_files_fixed} files)")
    print(f"{'='*70}\n")
    
    return fixed_envs, total_files_fixed

def fix_dict_no_append_errors():
    """Fix all dict_no_append errors"""
    print("="*70)
    print("FIXING DICT_NO_APPEND ERRORS (Pattern 5: Dict Assignment)")
    print("="*70)
    
    total_envs = len(DICT_NO_APPEND_ENVS)
    fixed_envs = 0
    total_files_fixed = 0
    
    for env_name in DICT_NO_APPEND_ENVS:
        print(f"\nProcessing {env_name}...")
        tool_files = find_tool_files(env_name)
        
        if not tool_files:
            print(f"  No tool files found for {env_name}")
            continue
        
        env_fixed = False
        for tool_file in tool_files:
            if fix_tool_file(tool_file, env_name, 'dict_no_append'):
                env_fixed = True
                total_files_fixed += 1
        
        if env_fixed:
            fixed_envs += 1
            print(f"  ✓ Environment fixed")
        else:
            print(f"  No changes needed")
    
    print(f"\n{'='*70}")
    print(f"DICT_NO_APPEND Summary: Fixed {fixed_envs}/{total_envs} environments ({total_files_fixed} files)")
    print(f"{'='*70}\n")
    
    return fixed_envs, total_files_fixed

def main():
    """Main function"""
    print("\n" + "="*70)
    print("LOW-HANGING FRUIT FIX SCRIPT")
    print("="*70 + "\n")
    
    # Fix str_no_get errors
    str_envs, str_files = fix_str_no_get_errors()
    
    # Fix dict_no_append errors
    dict_envs, dict_files = fix_dict_no_append_errors()
    
    # Final summary
    print("\n" + "="*70)
    print("FINAL SUMMARY")
    print("="*70)
    print(f"Total environments fixed: {str_envs + dict_envs}")
    print(f"Total files modified: {str_files + dict_files}")
    print(f"\nBreakdown:")
    print(f"  - str_no_get: {str_envs} environments, {str_files} files")
    print(f"  - dict_no_append: {dict_envs} environments, {dict_files} files")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()

