#!/usr/bin/env python3
"""
Fix the remaining 5 environments by adding _get_table helper and updating direct accesses.
"""

from pathlib import Path
import re

ENVS_TO_FIX = ['it_help_desk_2', 'it_help_desk_4', 'it_help_desk_6', 'rbac_3', 'digital_commerce_1']

def add_get_table_helper(content):
    """Add _get_table helper function after _convert_db_to_list"""
    
    # Find where to insert (after _convert_db_to_list)
    pattern = r'(def _convert_db_to_list\(db\):.*?return db\n)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return None, "Could not find _convert_db_to_list"
    
    get_table_func = '''

def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:
    """Get table from data and convert from dict to list if needed."""
    table = data.get(name, [])
    return _convert_db_to_list(table)
'''
    
    insert_pos = match.end()
    new_content = content[:insert_pos] + get_table_func + content[insert_pos:]
    
    return new_content, None

def fix_direct_accesses(content):
    """Replace direct data["table"] or data.get("table") with _get_table calls"""
    
    # Pattern 1: data["table_name"] used in iteration contexts
    # Look for: for x in data["something"]
    content = re.sub(
        r'for\s+(\w+)\s+in\s+data\["(\w+)"\]',
        r'for \1 in _get_table(data, "\2")',
        content
    )
    
    # Pattern 2: _find_one(data["table"], ...)
    content = re.sub(
        r'_find_one\(data\["(\w+)"\]',
        r'_find_one(_get_table(data, "\1")',
        content
    )
    
    # Pattern 3: Similar patterns with other helper functions
    content = re.sub(
        r'(_\w+)\(data\["(\w+)"\]',
        r'\1(_get_table(data, "\2")',
        content
    )
    
    return content

def fix_environment(env_name):
    """Fix one environment"""
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    tools_file = base_path / env_name / "tools.py"
    
    if not tools_file.exists():
        return f"❌ {env_name}: tools.py not found"
    
    content = tools_file.read_text()
    
    # Check if already has _get_table
    if 'def _get_table' in content:
        return f"⚠️  {env_name}: Already has _get_table"
    
    # Step 1: Add _get_table helper
    new_content, error = add_get_table_helper(content)
    if error:
        return f"❌ {env_name}: {error}"
    
    # Step 2: Fix direct accesses
    new_content = fix_direct_accesses(new_content)
    
    # Write back
    tools_file.write_text(new_content)
    
    return f"✅ {env_name}: Added _get_table and fixed direct accesses"

def main():
    print("=" * 70)
    print("FIXING REMAINING 5 str_get_error ENVIRONMENTS")
    print("=" * 70)
    print()
    
    results = []
    for env_name in ENVS_TO_FIX:
        result = fix_environment(env_name)
        results.append(result)
        print(result)
    
    print()
    print("=" * 70)
    fixed_count = sum(1 for r in results if r.startswith("✅"))
    print(f"FIXED {fixed_count} / {len(ENVS_TO_FIX)} ENVIRONMENTS")
    print("=" * 70)

if __name__ == "__main__":
    main()

