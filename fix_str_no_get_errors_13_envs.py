#!/usr/bin/env python3
"""
Fix STR NO GET errors in the 13 affected environments.

The issue: Tools use data.get("table", []) when data["table"] is a dict.
When iterating over a dict, you get keys (strings), not values (dicts).
Calling .get() on a string causes "'str' object has no attribute 'get'".

The fix: Change data.get("table", []) to list(data.get("table", {}).values())
"""

from pathlib import Path
import re

# The 13 environments with STR NO GET errors
ENVS_TO_FIX = [
    'airline_1',
    'airline_2', 
    'dev_ops_4',
    'figma_gmail_mcp_pipeline_1',
    'it_help_desk_4',
    'logistics_supply_chain_2',
    'new_hire_mcp_4',
    'project_management_5',
    'recipes_2',
    'retail_point_of_sale_and_inventory_system_1',
    'social_media_advertising_4',
    'social_media_advertising_5',
    'sports_analytics_5'
]

def fix_tool_file(file_path):
    """Fix a single tool file"""
    try:
        content = file_path.read_text()
        original_content = content
        
        # Pattern 1: data.get("table", []) used in iteration contexts
        # Look for: for x in data.get("something", [])
        content = re.sub(
            r'for\s+(\w+)\s+in\s+data\.get\("([^"]+)",\s*\[\]\)',
            r'for \1 in list(data.get("\2", {}).values())',
            content
        )
        
        # Pattern 2: Variable assignment with data.get("table", [])
        # Look for: variable = data.get("something", [])
        content = re.sub(
            r'(\w+)\s*=\s*data\.get\("([^"]+)",\s*\[\]\)',
            r'\1 = list(data.get("\2", {}).values())',
            content
        )
        
        # Pattern 3: Direct usage in function calls
        # Look for: function(data.get("something", []))
        content = re.sub(
            r'(\w+)\(data\.get\("([^"]+)",\s*\[\]\)',
            r'\1(list(data.get("\2", {}).values())',
            content
        )
        
        # Pattern 4: More complex patterns with multiple parameters
        # Look for: function(param1, data.get("something", []), param2)
        content = re.sub(
            r'(\w+)\(([^,)]*),\s*data\.get\("([^"]+)",\s*\[\]\)([^)]*)\)',
            r'\1(\2, list(data.get("\3", {}).values())\4)',
            content
        )
        
        # Only write if content changed
        if content != original_content:
            file_path.write_text(content)
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
    print("FIXING STR NO GET ERRORS IN 13 ENVIRONMENTS")
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
        print("   • Changed data.get('table', []) to list(data.get('table', {}).values())")
        print("   • This ensures iteration over dict values instead of keys")
        print("   • Prevents 'str' object has no attribute 'get' errors")

if __name__ == "__main__":
    main()
