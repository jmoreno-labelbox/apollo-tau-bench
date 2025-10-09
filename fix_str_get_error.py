#!/usr/bin/env python3
"""
Fix the str_get_error bug in 9 environments.

The bug: _get_table doesn't call _convert_db_to_list, so it returns dicts as-is.
The fix: Make _get_table use _convert_db_to_list to convert dict tables to lists.
"""

from pathlib import Path

# All environments with str_get_error
AFFECTED_ENVS = [
    'dev_ops_1',
    'dev_ops_6', 
    'digital_commerce_1',
    'figma_gmail_mcp_pipeline_5',
    'it_help_desk_2',
    'it_help_desk_4',
    'it_help_desk_6',
    'rbac_3',
    'recipes_3'
]

OLD_GET_TABLE = """def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:
    pass
    return data.setdefault(name, [])"""

NEW_GET_TABLE = """def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:
    pass
    table = data.setdefault(name, [])
    return _convert_db_to_list(table)"""

def main():
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    print("=" * 70)
    print("FIXING str_get_error IN 9 ENVIRONMENTS")
    print("=" * 70)
    print()
    
    fixed_count = 0
    
    for env_name in AFFECTED_ENVS:
        tools_file = base_path / env_name / "tools.py"
        
        if not tools_file.exists():
            print(f"❌ {env_name}: tools.py not found")
            continue
        
        # Read file
        content = tools_file.read_text()
        
        # Check if old code exists
        if OLD_GET_TABLE not in content:
            print(f"⚠️  {env_name}: Old _get_table not found (may already be fixed or has different format)")
            # Try to find the line
            if "def _get_table" in content:
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if "def _get_table" in line:
                        print(f"    Found at line {i+1}: {line}")
                        if i+1 < len(lines):
                            print(f"    Next lines: {lines[i+1]}, {lines[i+2]}")
            continue
        
        # Replace
        new_content = content.replace(OLD_GET_TABLE, NEW_GET_TABLE)
        
        # Write back
        tools_file.write_text(new_content)
        
        print(f"✅ {env_name}: Fixed _get_table")
        fixed_count += 1
    
    print()
    print("=" * 70)
    print(f"FIXED {fixed_count} / {len(AFFECTED_ENVS)} ENVIRONMENTS")
    print("=" * 70)

if __name__ == "__main__":
    main()
