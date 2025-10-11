#!/usr/bin/env python3
"""
Fix recipes_2 tools to remove redundant list().values() calls.
Since data loader now returns lists, tools should just use data.get(..., []).
"""

import re
import sys
from pathlib import Path


def fix_list_values_pattern(source: str) -> tuple[str, int]:
    """
    Replace: list(data.get("table", {}).values())
    With: data.get("table", [])
    """
    # Pattern: list(data.get("table_name", {}).values())
    pattern = r'list\(data\.get\("([^"]+)",\s*\{\}\)\.values\(\)\)'
    replacement = r'data.get("\1", [])'
    
    new_source, count = re.subn(pattern, replacement, source)
    return new_source, count


def main():
    tools_dir = Path("tau/tau_bench/envs/recipes_2/tools")
    
    if not tools_dir.exists():
        print(f"Error: {tools_dir} not found")
        sys.exit(1)
    
    modified_count = 0
    total_replacements = 0
    
    for tool_file in tools_dir.glob("*.py"):
        if tool_file.name == "__init__.py":
            continue
        
        source = tool_file.read_text(encoding='utf-8')
        new_source, count = fix_list_values_pattern(source)
        
        if count > 0:
            tool_file.write_text(new_source, encoding='utf-8')
            print(f"✓ {tool_file.name}: {count} replacements")
            modified_count += 1
            total_replacements += count
    
    print(f"\nModified {modified_count} files, {total_replacements} total replacements")


if __name__ == "__main__":
    main()

