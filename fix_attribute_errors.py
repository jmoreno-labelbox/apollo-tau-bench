#!/usr/bin/env python3
"""
Fix attribute errors in career_planner_1 and recipes_2.

1. career_planner_1: Remove double .values() calls (dict_values has no .values())
2. recipes_2: Remove .values() calls on lists (list has no .values())
"""

import argparse
import re
import sys
from pathlib import Path


def fix_double_values_call(source: str) -> tuple[str, list[str]]:
    """
    Fix pattern: users.values() where users is already dict_values.
    
    Pattern: 
        users = data.get("users", {}).values()
        for user in users.values():  # ERROR
    
    Fix:
        for user in users:  # Just iterate directly
    """
    changes = []
    lines = source.split('\n')
    
    # Track variables that are dict_values
    dict_values_vars = set()
    
    for i, line in enumerate(lines):
        # Pattern: var = something.values()
        match = re.search(r'(\w+)\s*=.*\.values\(\)', line)
        if match:
            var_name = match.group(1)
            dict_values_vars.add(var_name)
        
        # Pattern: for item in var.values() where var is dict_values
        for var_name in dict_values_vars:
            pattern = rf'(\s+for\s+\w+\s+in\s+){re.escape(var_name)}\.values\(\):'
            if re.search(pattern, line):
                new_line = re.sub(pattern, rf'\1{var_name}:', line)
                if new_line != line:
                    lines[i] = new_line
                    changes.append(f"Line {i+1}: Removed .values() call on dict_values object")
    
    return '\n'.join(lines), changes


def fix_list_values_call(source: str) -> tuple[str, list[str]]:
    """
    Fix pattern where .values() is called on a list.
    
    If data has been converted to list but code still calls .values(),
    the fix depends on context - flag for manual review.
    """
    changes = []
    lines = source.split('\n')
    
    # Track variables that are lists
    list_vars = set()
    
    for i, line in enumerate(lines):
        # Pattern: var = list(...)
        match = re.search(r'(\w+)\s*=\s*list\(', line)
        if match:
            var_name = match.group(1)
            list_vars.add(var_name)
        
        # Check if any list var has .values() called on it
        for var_name in list_vars:
            if f'{var_name}.values()' in line:
                changes.append(f"Line {i+1}: WARNING - .values() called on list variable '{var_name}'")
    
    return source, changes


def process_file(file_path: Path, env_name: str) -> tuple[bool, list[str]]:
    """Process a single file based on environment type."""
    try:
        source = file_path.read_text(encoding='utf-8')
        original = source
        all_changes = []
        
        if env_name == "career_planner_1":
            source, changes = fix_double_values_call(source)
            all_changes.extend(changes)
        elif env_name == "recipes_2":
            source, changes = fix_list_values_call(source)
            all_changes.extend(changes)
        
        if source != original:
            file_path.write_text(source, encoding='utf-8')
            return True, all_changes
        elif all_changes:  # Warnings but no fixes
            return False, all_changes
        return False, []
    except Exception as e:
        return False, [f"Error: {e}"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", choices=["career_planner_1", "recipes_2", "all"], 
                       default="all", help="Environment to fix")
    args = parser.parse_args()
    
    envs = ["career_planner_1", "recipes_2"] if args.env == "all" else [args.env]
    
    base_path = Path("tau/tau_bench/envs")
    
    for env_name in envs:
        print(f"\n=== Processing {env_name} ===")
        tools_dir = base_path / env_name / "tools"
        
        if not tools_dir.exists():
            print(f"✗ Tools directory not found: {tools_dir}")
            continue
        
        modified_count = 0
        warning_count = 0
        
        for tool_file in tools_dir.glob("*.py"):
            if tool_file.name == "__init__.py":
                continue
            
            modified, changes = process_file(tool_file, env_name)
            
            if modified:
                print(f"✓ {tool_file.name}")
                for change in changes:
                    print(f"  - {change}")
                modified_count += 1
            elif changes:
                print(f"⚠ {tool_file.name}")
                for change in changes:
                    print(f"  - {change}")
                warning_count += 1
        
        print(f"\nSummary for {env_name}:")
        print(f"  Modified: {modified_count} files")
        print(f"  Warnings: {warning_count} files")


if __name__ == "__main__":
    main()

