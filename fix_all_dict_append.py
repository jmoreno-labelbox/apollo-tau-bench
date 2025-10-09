#!/usr/bin/env python3
"""
Fix all dict_append_error by replacing .append() with dict assignment
"""

from pathlib import Path
import re

def fix_dict_append_in_file(file_path):
    """
    Replace pattern: data.setdefault("table", []).append(record)
    With: table = data.setdefault("table", {}); table[f"{len(table)}"] = record
    """
    content = file_path.read_text()
    lines = content.split('\n')
    modified = False
    
    for i in range(len(lines)):
        # Pattern: data.setdefault("table_name", []).append(record_var)
        match = re.match(r'(\s*)data\.setdefault\("(\w+)", \[\]\)\.append\((\w+)\)', lines[i])
        if match:
            indent, table_name, record_var = match.groups()
            # Replace with dict assignment
            lines[i] = f'{indent}table = data.setdefault("{table_name}", {{}})'
            lines.insert(i+1, f'{indent}key = f"{{len(table)}}"')
            lines.insert(i+2, f'{indent}table[key] = {record_var}')
            modified = True
            print(f'  Line {i+1}: Fixed {table_name}.append({record_var})')
    
    if modified:
        file_path.write_text('\n'.join(lines))
        return True
    return False

def main():
    base = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    envs = ['career_planner_4', 'consulting_accounting_5', 'consulting_accounting_2', 
            'data_science_4', 'banking_services_6', 'data_science_2', 'dev_ops_4',
            'sports_analytics_2', 'career_planner_5', 'career_planner_3', 'rbac_5',
            'social_media_advertising_1', 'banking_services_5', 'career_planner_2',
            'career_planner_1', 'new_hire_mcp_4', 'recipes_1', 'social_media_advertising_5',
            'figma_gmail_mcp_pipeline_1', 'file_system_7', 'github_mcp_7',
            'file_system_8', 'file_system_9']
    
    print("=" * 70)
    print("FIXING ALL dict_append_error")
    print("=" * 70)
    print()
    
    fixed_count = 0
    for env in envs:
        tools_file = base / env / "tools.py"
        if tools_file.exists():
            print(f"{env}:")
            if fix_dict_append_in_file(tools_file):
                print(f"✅ {env}: Fixed")
                fixed_count += 1
            else:
                print(f"⚠️  {env}: No patterns found")
        else:
            print(f"❌ {env}: File not found")
    
    print()
    print("=" * 70)
    print(f"FIXED {fixed_count} / {len(envs)} FILES")
    print("=" * 70)

if __name__ == "__main__":
    main()

