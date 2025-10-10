#!/usr/bin/env python3
"""
Fix DICT NO APPEND errors in the 3 affected environments.

The issue: Code calls .append() on data that might be a dictionary instead of a list.
The fix: Ensure we're working with lists by converting dicts to lists when needed.
"""

from pathlib import Path
import re

# The 3 environments with DICT NO APPEND errors
ENVS_TO_FIX = [
    'consulting_accounting_2',
    'file_system_9', 
    'social_media_advertising_1'
]

def fix_dict_append_errors(content):
    """Fix DICT NO APPEND errors in tool content"""
    original_content = content
    
    # Pattern 1: data.setdefault("key", []).append(...)
    # This is the most common pattern causing the error
    content = re.sub(
        r'data\.setdefault\("([^"]+)",\s*\[\])\.append\(([^)]+)\)',
        r'data.setdefault("\1", []).append(\2) if isinstance(data.get("\1"), list) else data.setdefault("\1", []).extend([\2])',
        content
    )
    
    # Pattern 2: variable.append(...) where variable might be a dict
    # Look for patterns like: some_var.append(item) where some_var comes from data.get()
    content = re.sub(
        r'(\w+)\.append\(([^)]+)\)',
        r'\1.append(\2) if isinstance(\1, list) else \1.update({\2}) if isinstance(\1, dict) else \1.append(\2)',
        content
    )
    
    # Pattern 3: More specific fix for common patterns
    # Fix: data["key"].append() -> ensure it's a list first
    content = re.sub(
        r'data\["([^"]+)"\]\.append\(([^)]+)\)',
        r'data["\1"].append(\2) if isinstance(data["\1"], list) else data["\1"] = [data["\1"], \2]',
        content
    )
    
    # Pattern 4: Fix list comprehensions that might append to dicts
    # Look for: [item for item in data.get("key", []) if condition]
    content = re.sub(
        r'data\.get\("([^"]+)",\s*\[\]\)',
        r'list(data.get("\1", {}).values()) if isinstance(data.get("\1"), dict) else data.get("\1", [])',
        content
    )
    
    return content, content != original_content

def fix_tool_file(file_path):
    """Fix a single tool file"""
    try:
        content = file_path.read_text()
        new_content, changed = fix_dict_append_errors(content)
        
        if changed:
            file_path.write_text(new_content)
            return True
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def fix_environment(env_name):
    """Fix all tool files in an environment"""
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    env_path = base_path / env_name
    
    if not env_path.exists():
        return f"❌ {env_name}: Environment directory not found"
    
    tools_dir = env_path / "tools"
    if not tools_dir.exists():
        return f"❌ {env_name}: Tools directory not found"
    
    # Find all Python files in tools directory
    tool_files = list(tools_dir.glob("*.py"))
    if not tool_files:
        return f"❌ {env_name}: No tool files found"
    
    fixed_files = []
    for tool_file in tool_files:
        if fix_tool_file(tool_file):
            fixed_files.append(tool_file.name)
    
    if fixed_files:
        return f"✅ {env_name}: Fixed {len(fixed_files)} files: {', '.join(fixed_files)}"
    else:
        return f"⚠️  {env_name}: No files needed fixing"

def main():
    print("=" * 80)
    print("FIXING DICT NO APPEND ERRORS IN 3 ENVIRONMENTS")
    print("=" * 80)
    print()
    
    results = []
    for env_name in ENVS_TO_FIX:
        result = fix_environment(env_name)
        results.append(result)
        print(result)
    
    print()
    print("=" * 80)
    fixed_count = sum(1 for r in results if r.startswith("✅"))
    print(f"FIXED {fixed_count} / {len(ENVS_TO_FIX)} ENVIRONMENTS")
    print("=" * 80)
    
    if fixed_count > 0:
        print()
        print("🔧 FIXES APPLIED:")
        print("   • Fixed data.setdefault().append() patterns")
        print("   • Added type checking for .append() operations")
        print("   • Ensured lists are used instead of dicts for append operations")

if __name__ == "__main__":
    main()
