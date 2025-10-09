#!/usr/bin/env python3
"""
Fix dict_append_error by replacing .append() with dict assignment where appropriate
"""

from pathlib import Path
import re

AFFECTED_ENVS = [
    'airline_2', 'banking_services_5', 'banking_services_6', 'career_planner_1',
    'career_planner_2', 'career_planner_3', 'career_planner_4', 'career_planner_5',
    'consulting_accounting_1', 'consulting_accounting_2', 'consulting_accounting_5',
    'data_science_2', 'data_science_4', 'dev_ops_4', 'figma_gmail_mcp_pipeline_1',
    'file_system_7', 'file_system_8', 'file_system_9', 'github_mcp_2', 'github_mcp_7',
    'it_help_desk_2', 'it_help_desk_4', 'new_hire_mcp_4', 'new_hire_mcp_5',
    'rbac_5', 'recipes_1', 'social_media_advertising_1', 'social_media_advertising_5',
    'sports_analytics_2', 'sports_analytics_4'
]

def fix_append_patterns(content):
    """
    Find patterns like:
      table = data.setdefault("table_name", [])
      new_id = _some_id_func(...)
      rec = {...}
      table.append(rec)
    
    And change to:
      table[new_id] = rec
    """
    lines = content.split('\n')
    modified = False
    
    for i in range(len(lines)):
        line = lines[i]
        
        # Look for .append( pattern
        if '.append(' in line:
            # Check if this is appending a record with an ID
            # Common patterns: table.append(rec), table.append(new_row), table.append(record)
            match = re.match(r'(\s*)(\w+)\.append\((\w+)\)', line)
            if match:
                indent, table_name, record_name = match.groups()
                
                # Look backwards to find the ID variable
                id_var = None
                for j in range(i-1, max(0, i-10), -1):
                    # Look for patterns like: new_id = ..., record_id = ..., etc.
                    id_match = re.search(r'(\w*id\w*)\s*=', lines[j], re.IGNORECASE)
                    if id_match:
                        id_var = id_match.group(1)
                        break
                
                if id_var:
                    # Replace .append() with dict assignment
                    lines[i] = f'{indent}{table_name}[{id_var}] = {record_name}'
                    modified = True
                    print(f'  Line {i+1}: {table_name}.append({record_name}) → {table_name}[{id_var}] = {record_name}')
    
    return '\n'.join(lines) if modified else None

def main():
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    print("=" * 70)
    print("FIXING dict_append_error - REPLACING .append() WITH DICT ASSIGNMENT")
    print("=" * 70)
    print()
    
    fixed_count = 0
    
    for env_name in AFFECTED_ENVS:
        tools_file = base_path / env_name / "tools.py"
        
        if not tools_file.exists():
            print(f"❌ {env_name}: tools.py not found")
            continue
        
        content = tools_file.read_text()
        
        print(f"\n{env_name}:")
        new_content = fix_append_patterns(content)
        
        if new_content:
            tools_file.write_text(new_content)
            print(f"✅ {env_name}: Fixed")
            fixed_count += 1
        else:
            print(f"⚠️  {env_name}: No .append() patterns found or already fixed")
    
    print()
    print("=" * 70)
    print(f"FIXED {fixed_count} / {len(AFFECTED_ENVS)} ENVIRONMENTS")
    print("=" * 70)

if __name__ == "__main__":
    main()

