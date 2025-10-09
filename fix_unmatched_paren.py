#!/usr/bin/env python3
"""
Fix all 'unmatched )' syntax errors - typically .values()): -> .values():
"""

from pathlib import Path
import re

ENVS_TO_FIX = [
    'academic_search_5', 'airline_4', 'banking_services_2', 'consulting_accounting_6',
    'digital_commerce_2', 'digital_commerce_3', 'figma_gmail_mcp_pipeline_4',
    'github_mcp_5', 'github_mcp_6', 'logistics_supply_chain_3', 'logistics_supply_chain_5',
    'logistics_supply_chain_6', 'new_hire_mcp_1', 'org_chart_5', 'project_management_1',
    'rbac_4', 'rbac_5', 'real_estate_sales_2', 'retail_2', 'retail_5',
    'retail_point_of_sale_and_inventory_system_6', 'smart_home_2', 'smart_home_3', 'smart_home_5'
]

def fix_file(file_path):
    """Fix unmatched ) errors - pattern: .values()): -> .values():"""
    content = file_path.read_text()
    original = content
    
    # Fix pattern: for x in something.values()): -> for x in something.values():
    content = re.sub(r'\.values\(\)\)\s*:', r'.values():', content)
    
    # Fix pattern: something.values()): in other contexts
    content = re.sub(r'\.values\(\)\)\)', r'.values())', content)
    
    if content != original:
        file_path.write_text(content)
        return True
    return False

def main():
    base = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    print("=" * 70)
    print("FIXING UNMATCHED ')' ERRORS")
    print("=" * 70)
    print()
    
    fixed_count = 0
    for env in ENVS_TO_FIX:
        tools_file = base / env / "tools.py"
        if tools_file.exists():
            if fix_file(tools_file):
                print(f"✅ {env}")
                fixed_count += 1
            else:
                print(f"⚠️  {env}: No changes")
        else:
            print(f"❌ {env}: File not found")
    
    print()
    print("=" * 70)
    print(f"FIXED {fixed_count} / {len(ENVS_TO_FIX)} FILES")
    print("=" * 70)

if __name__ == "__main__":
    main()

