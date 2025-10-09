#!/usr/bin/env python3
"""
Comprehensive fix for str_get_error across all 9 affected environments.

The bug: Table getter functions return dicts without converting to lists.
The fix: Make each table getter call _convert_db_to_list.
"""

from pathlib import Path
import re

# All environments with str_get_error and their table getter patterns
FIXES = [
    {
        'env': 'dev_ops_1',
        'old': 'def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:\n    return data.setdefault(name, [])',
        'new': 'def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:\n    table = data.setdefault(name, [])\n    return _convert_db_to_list(table)',
    },
    {
        'env': 'dev_ops_6',
        'old': 'def _table(db: dict[str, Any], name: str) -> list[dict[str, Any]]:\n    pass\n    return db.get(name, [])',
        'new': 'def _table(db: dict[str, Any], name: str) -> list[dict[str, Any]]:\n    pass\n    table = db.get(name, [])\n    return _convert_db_to_list(table)',
    },
    {
        'env': 'digital_commerce_1',
        # This one might not have a table getter - need to check individual tool methods
        'pattern': 'data.get(',
    },
    {
        'env': 'figma_gmail_mcp_pipeline_5',
        'old': 'def _safe_table(data: dict[str, Any], table: str) -> list[dict[str, Any]]:\n    """Retrieve or generate a list table."""\n    return data.setdefault(table, [])',
        'new': 'def _safe_table(data: dict[str, Any], table: str) -> list[dict[str, Any]]:\n    """Retrieve or generate a list table."""\n    tbl = data.setdefault(table, [])\n    return _convert_db_to_list(tbl)',
    },
    {
        'env': 'it_help_desk_2',
        'pattern': 'data.get(',
    },
    {
        'env': 'it_help_desk_4', 
        'pattern': 'data.get(',
    },
    {
        'env': 'it_help_desk_6',
        'pattern': 'data.get(',
    },
    {
        'env': 'rbac_3',
        'pattern': 'data.get(',
    },
    {
        'env': 'recipes_3',
        'old': 'def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:\n    pass\n    return data.setdefault(name, [])',
        'new': 'def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:\n    pass\n    table = data.setdefault(name, [])\n    return _convert_db_to_list(table)',
    },
]

def fix_environment(env_info):
    """Fix one environment"""
    env_name = env_info['env']
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    tools_file = base_path / env_name / "tools.py"
    
    if not tools_file.exists():
        return f"❌ {env_name}: tools.py not found"
    
    content = tools_file.read_text()
    
    # If we have a specific old/new pattern, use it
    if 'old' in env_info and 'new' in env_info:
        if env_info['old'] not in content:
            return f"⚠️  {env_name}: Pattern not found"
        
        new_content = content.replace(env_info['old'], env_info['new'])
        tools_file.write_text(new_content)
        return f"✅ {env_name}: Fixed"
    
    # Otherwise, we need manual investigation
    return f"⚠️  {env_name}: Needs manual fix (uses inline data.get)"

def main():
    print("=" * 70)
    print("COMPREHENSIVE FIX FOR str_get_error")
    print("=" * 70)
    print()
    
    results = []
    for env_info in FIXES:
        result = fix_environment(env_info)
        results.append(result)
        print(result)
    
    print()
    print("=" * 70)
    fixed_count = sum(1 for r in results if r.startswith("✅"))
    print(f"FIXED {fixed_count} / {len(FIXES)} ENVIRONMENTS")
    print("=" * 70)

if __name__ == "__main__":
    main()

