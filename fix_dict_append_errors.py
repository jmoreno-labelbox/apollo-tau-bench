#!/usr/bin/env python3
"""
Fix dict_append_error by correcting _convert_db_to_list in all affected environments
"""

from pathlib import Path

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

OLD_CODE = """def _convert_db_to_list(db):
    \"\"\"Convert database from dict format to list format.\"\"\"
    if isinstance(db, dict):
        return list(db)
    return db"""

NEW_CODE = """def _convert_db_to_list(db):
    \"\"\"Convert database from dict format to list format.\"\"\"
    if isinstance(db, dict):
        return list(db.values())
    return db"""

def main():
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    print("=" * 70)
    print("FIXING dict_append_error BY CORRECTING _convert_db_to_list")
    print("=" * 70)
    print()
    
    fixed_count = 0
    
    for env_name in AFFECTED_ENVS:
        tools_file = base_path / env_name / "tools.py"
        
        if not tools_file.exists():
            print(f"❌ {env_name}: tools.py not found")
            continue
        
        content = tools_file.read_text()
        
        if OLD_CODE not in content:
            print(f"⚠️  {env_name}: Old _convert_db_to_list not found (may already be fixed)")
            continue
        
        # Replace
        new_content = content.replace(OLD_CODE, NEW_CODE)
        tools_file.write_text(new_content)
        
        print(f"✅ {env_name}: Fixed _convert_db_to_list")
        fixed_count += 1
    
    print()
    print("=" * 70)
    print(f"FIXED {fixed_count} / {len(AFFECTED_ENVS)} ENVIRONMENTS")
    print("=" * 70)

if __name__ == "__main__":
    main()

