#!/usr/bin/env python3
"""
Fix missing private functions by importing them from the correct warrior domain variations.
This script maps missing functions to their actual locations in warrior domains.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

# Function mapping: function_name -> (domain, variation)
FUNCTION_MAPPING = {
    # Recipes functions
    '_household_for_user': ('recipes', 'variation_5'),
    '_latest_list_for_household': ('recipes', 'variation_5'),
    '_latest_order_for_household': ('recipes', 'variation_5'),
    '_latest_meal_plan_for_household': ('recipes', 'variation_5'),
    '_all_recipe_ids_filtered': ('recipes', 'variation_5'),
    '_decode_filter_token': ('recipes', 'variation_5'),
    '_parse_json_list_ids': ('recipes', 'variation_1'),
    '_collect_recipe_ingredients': ('recipes', 'variation_1'),
    '_next_week_start_date_for_household': ('recipes', 'variation_5'),
    '_plan_week_dates': ('recipes', 'variation_1'),
    '_recipe_by_id': ('recipes', 'variation_1'),
    '_recent_recipe_ids': ('recipes', 'variation_5'),
    '_pick_target_from_member': ('recipes', 'variation_5'),
    '_ids_from_kwargs_or_defaults': ('recipes', 'variation_5'),
    
    # Digital commerce functions
    '_slugify': ('digital_commerce', 'variation_1'),
    '_err': ('digital_commerce', 'variation_1'),
    '_ensure_table': ('digital_commerce', 'variation_1'),
    '_find_one': ('digital_commerce', 'variation_1'),
    '_ensure_audit_log': ('digital_commerce', 'variation_1'),
    
    # Figma Gmail MCP Pipeline functions
    '_j': ('figma_gmail_mcp_pipeline', 'variation_3'),
    '_err': ('figma_gmail_mcp_pipeline', 'variation_3'),
    '_get_config_json': ('figma_gmail_mcp_pipeline', 'variation_1'),
    '_index_by': ('figma_gmail_mcp_pipeline', 'variation_1'),
    '_safe_table': ('figma_gmail_mcp_pipeline', 'variation_1'),
    '_get_next_id': ('figma_gmail_mcp_pipeline', 'variation_6'),
    
    # GitHub MCP functions
    '_repos': ('github_mcp', 'variation_7'),
    '_auth': ('github_mcp', 'variation_2'),
    
    # Banking services functions
    '_get_next_id': ('banking_services', 'variation_6'),
    '_convert_db_to_list': ('banking_services', 'variation_1'),
    
    # Data science functions
    '_fixed_now_iso': ('data_science', 'variation_3'),
    
    # Sports analytics functions
    '_today_iso': ('sports_analytics', 'variation_1'),
    
    # New hire MCP functions
    '_render_template': ('new_hire_mcp', 'variation_1'),
    '_fixed_ts': ('new_hire_mcp', 'variation_3'),
    '_ensure_list': ('new_hire_mcp', 'variation_2'),
    '_find_by_key': ('new_hire_mcp', 'variation_2'),
    '_slug': ('new_hire_mcp', 'variation_2'),
    
    # Airline functions
    '_norm': ('airline', 'variation_2'),
    '_j': ('airline', 'variation_2'),
    
    # RBAC functions
    '_eq': ('rbac', 'variation_1'),
    '_parse_iso': ('rbac', 'variation_1'),
    
    # Smart home functions
    '_now_iso': ('smart_home', 'variation_1'),
    
    # Real estate sales functions
    '_index_by': ('real_estate_sales', 'variation_1'),
    '_latest': ('real_estate_sales', 'variation_7'),
    '_err': ('real_estate_sales', 'variation_7'),
    
    # Dev ops functions
    '_idx_by_id': ('dev_ops', 'variation_1'),
    '_err': ('dev_ops', 'variation_6'),
    '_get_next_id': ('dev_ops', 'variation_3'),
    
    # IT Help Desk functions
    '_get_next_id': ('it_help_desk', 'variation_4'),
    
    # Consulting accounting functions
    '_fixed_now_iso': ('consulting_accounting', 'variation_4'),
}

# Domain mapping from environment names to warrior domain folders
DOMAIN_MAPPING = {
    'recipes_1': 'recipes',
    'recipes_2': 'recipes', 
    'recipes_3': 'recipes',
    'recipes_4': 'recipes',
    'recipes_5': 'recipes',
    
    'social_media_advertising_1': 'social_media_advertising',
    'social_media_advertising_2': 'social_media_advertising',
    'social_media_advertising_3': 'social_media_advertising',
    'social_media_advertising_4': 'social_media_advertising',
    'social_media_advertising_5': 'social_media_advertising',
    'social_media_advertising_6': 'social_media_advertising',
    
    'academic_search_1': 'academic_search',
    'academic_search_2': 'academic_search',
    'academic_search_3': 'academic_search',
    'academic_search_4': 'academic_search',
    'academic_search_5': 'academic_search',
    
    'airline_1': 'airline',
    'airline_2': 'airline',
    'airline_3': 'airline',
    'airline_4': 'airline',
    'airline_5': 'airline',
    
    'banking_services_1': 'banking_services',
    'banking_services_2': 'banking_services',
    'banking_services_4': 'banking_services',
    'banking_services_5': 'banking_services',
    'banking_services_6': 'banking_services',
    
    'career_planner_1': 'career_planner',
    'career_planner_2': 'career_planner',
    'career_planner_3': 'career_planner',
    'career_planner_4': 'career_planner',
    'career_planner_5': 'career_planner',
    
    'consulting_accounting_1': 'consulting_accounting',
    'consulting_accounting_2': 'consulting_accounting',
    'consulting_accounting_4': 'consulting_accounting',
    'consulting_accounting_5': 'consulting_accounting',
    'consulting_accounting_6': 'consulting_accounting',
    
    'data_science_1': 'data_science',
    'data_science_2': 'data_science',
    'data_science_3': 'data_science',
    'data_science_4': 'data_science',
    'data_science_5': 'data_science',
    'data_science_6': 'data_science',
    
    'dev_ops_1': 'dev_ops',
    'dev_ops_2': 'dev_ops',
    'dev_ops_3': 'dev_ops',
    'dev_ops_4': 'dev_ops',
    'dev_ops_5': 'dev_ops',
    'dev_ops_6': 'dev_ops',
    
    'digital_commerce_1': 'digital_commerce',
    'digital_commerce_2': 'digital_commerce',
    'digital_commerce_3': 'digital_commerce',
    'digital_commerce_4': 'digital_commerce',
    'digital_commerce_5': 'digital_commerce',
    
    'figma_gmail_mcp_pipeline_1': 'figma_gmail_mcp_pipeline',
    'figma_gmail_mcp_pipeline_2': 'figma_gmail_mcp_pipeline',
    'figma_gmail_mcp_pipeline_3': 'figma_gmail_mcp_pipeline',
    'figma_gmail_mcp_pipeline_4': 'figma_gmail_mcp_pipeline',
    'figma_gmail_mcp_pipeline_5': 'figma_gmail_mcp_pipeline',
    'figma_gmail_mcp_pipeline_6': 'figma_gmail_mcp_pipeline',
    
    'file_system_1': 'file_system',
    'file_system_7': 'file_system',
    'file_system_8': 'file_system',
    'file_system_9': 'file_system',
    
    'github_mcp_1': 'github_mcp',
    'github_mcp_2': 'github_mcp',
    'github_mcp_5': 'github_mcp',
    'github_mcp_6': 'github_mcp',
    'github_mcp_7': 'github_mcp',
    
    'it_help_desk_2': 'it_help_desk',
    'it_help_desk_4': 'it_help_desk',
    'it_help_desk_5': 'it_help_desk',
    'it_help_desk_6': 'it_help_desk',
    
    'logistics_supply_chain_1': 'logistics_supply_chain',
    'logistics_supply_chain_2': 'logistics_supply_chain',
    'logistics_supply_chain_3': 'logistics_supply_chain',
    'logistics_supply_chain_5': 'logistics_supply_chain',
    'logistics_supply_chain_6': 'logistics_supply_chain',
    
    'new_hire_mcp_1': 'new_hire_mcp',
    'new_hire_mcp_2': 'new_hire_mcp',
    'new_hire_mcp_3': 'new_hire_mcp',
    'new_hire_mcp_4': 'new_hire_mcp',
    'new_hire_mcp_5': 'new_hire_mcp',
    
    'org_chart_1': 'org_chart',
    'org_chart_2': 'org_chart',
    'org_chart_3': 'org_chart',
    'org_chart_4': 'org_chart',
    'org_chart_5': 'org_chart',
    
    'project_management_1': 'project_management',
    'project_management_2': 'project_management',
    'project_management_3': 'project_management',
    'project_management_4': 'project_management',
    'project_management_5': 'project_management',
    
    'rbac_1': 'rbac',
    'rbac_2': 'rbac',
    'rbac_3': 'rbac',
    'rbac_4': 'rbac',
    'rbac_5': 'rbac',
    
    'real_estate_sales_1': 'real_estate_sales',
    'real_estate_sales_2': 'real_estate_sales',
    'real_estate_sales_3': 'real_estate_sales',
    'real_estate_sales_4': 'real_estate_sales',
    'real_estate_sales_7': 'real_estate_sales',
    
    'retail_1': 'retail',
    'retail_2': 'retail',
    'retail_3': 'retail',
    'retail_4': 'retail',
    'retail_5': 'retail',
    'retail_6': 'retail',
    
    'retail_point_of_sale_and_inventory_system_1': 'retail_point_of_sale_and_inventory_system',
    'retail_point_of_sale_and_inventory_system_2': 'retail_point_of_sale_and_inventory_system',
    'retail_point_of_sale_and_inventory_system_4': 'retail_point_of_sale_and_inventory_system',
    'retail_point_of_sale_and_inventory_system_5': 'retail_point_of_sale_and_inventory_system',
    'retail_point_of_sale_and_inventory_system_6': 'retail_point_of_sale_and_inventory_system',
    
    'smart_home_1': 'smart_home',
    'smart_home_2': 'smart_home',
    'smart_home_3': 'smart_home',
    'smart_home_4': 'smart_home',
    'smart_home_5': 'smart_home',
    
    'sports_analytics_2': 'sports_analytics',
    'sports_analytics_3': 'sports_analytics',
    'sports_analytics_4': 'sports_analytics',
    'sports_analytics_5': 'sports_analytics'
}

def find_undefined_functions(file_path: Path) -> Set[str]:
    """Find which private functions are used but not defined in a file."""
    try:
        content = file_path.read_text()
        
        # Parse the file to find function calls
        try:
            tree = ast.parse(content)
        except SyntaxError:
            return set()
        
        used_functions = set()
        defined_functions = set()
        
        # Find function definitions
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('_'):
                defined_functions.add(node.name)
        
        # Find function calls
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id.startswith('_'):
                    used_functions.add(node.func.id)
        
        # Return functions that are used but not defined
        missing = used_functions - defined_functions
        return missing
        
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return set()

def get_warrior_domain(file_path: Path) -> str:
    """Get the warrior domain for a file based on its path."""
    # Extract environment name from path
    path_parts = file_path.parts
    env_name = None
    for part in path_parts:
        if any(part.startswith(prefix) for prefix in [
            'recipes_', 'social_media_advertising_', 'academic_search_', 
            'airline_', 'banking_services_', 'career_planner_', 
            'consulting_accounting_', 'data_science_', 'dev_ops_',
            'digital_commerce_', 'figma_gmail_mcp_pipeline_', 'file_system_',
            'github_mcp_', 'it_help_desk_', 'logistics_supply_chain_',
            'new_hire_mcp_', 'org_chart_', 'project_management_', 'rbac_',
            'real_estate_sales_', 'retail_', 'retail_point_of_sale_and_inventory_system_',
            'smart_home_', 'sports_analytics_'
        ]):
            env_name = part
            break
    
    if not env_name:
        return None
    
    return DOMAIN_MAPPING.get(env_name)

def add_correct_imports_to_file(file_path: Path, missing_functions: Set[str], warrior_domain: str) -> bool:
    """Add correct import statements for missing functions to a file."""
    try:
        content = file_path.read_text()
        
        # Group functions by their source variation
        imports_by_variation = {}
        
        for func in missing_functions:
            if func in FUNCTION_MAPPING:
                domain, variation = FUNCTION_MAPPING[func]
                if domain == warrior_domain:  # Only import from the same domain
                    if variation not in imports_by_variation:
                        imports_by_variation[variation] = []
                    imports_by_variation[variation].append(func)
        
        if not imports_by_variation:
            return False
        
        # Create import statements
        import_lines = []
        for variation, functions in imports_by_variation.items():
            functions_list = ', '.join(sorted(functions))
            import_line = f"from domains_warrior.{warrior_domain}.variations.{variation}.tools import {functions_list}"
            import_lines.append(import_line)
        
        # Find where to insert the imports (after existing imports)
        lines = content.split('\n')
        insert_index = 0
        
        # Find the last import line
        for i, line in enumerate(lines):
            if line.strip().startswith(('import ', 'from ')):
                insert_index = i + 1
        
        # Insert the imports
        for import_line in import_lines:
            lines.insert(insert_index, import_line)
            insert_index += 1
        
        # Write back to file
        new_content = '\n'.join(lines)
        file_path.write_text(new_content)
        
        return True
        
    except Exception as e:
        print(f"Error adding imports to {file_path}: {e}")
        return False

def main():
    """Fix missing private functions by adding correct imports from warrior domains."""
    tau_dir = REPO_ROOT / "tau"
    
    if not tau_dir.exists():
        print(f"tau directory not found: {tau_dir}")
        return
    
    fixed_files = 0
    total_files = 0
    errors = 0
    
    print("Fixing missing private function imports with correct warrior domain sources...")
    
    # Find all Python tool files
    for py_file in tau_dir.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
            
        total_files += 1
        missing_functions = find_undefined_functions(py_file)
        
        if missing_functions:
            warrior_domain = get_warrior_domain(py_file)
            
            if warrior_domain:
                print(f"Fixing {py_file.relative_to(tau_dir)}: {', '.join(sorted(missing_functions))}")
                if add_correct_imports_to_file(py_file, missing_functions, warrior_domain):
                    fixed_files += 1
                else:
                    errors += 1
            else:
                print(f"Unknown domain for {py_file.relative_to(tau_dir)}")
                errors += 1
    
    print(f"\n=== Summary ===")
    print(f"Total files scanned: {total_files}")
    print(f"Files fixed: {fixed_files}")
    print(f"Errors: {errors}")

if __name__ == "__main__":
    main()
