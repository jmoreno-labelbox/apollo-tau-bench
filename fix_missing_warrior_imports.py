#!/usr/bin/env python3
"""
Fix missing private functions by importing them from the correct warrior domains.
This script automatically adds the necessary import statements to tool files.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

# Domain mapping from environment names to warrior domain folders
DOMAIN_MAPPING = {
    # Recipes environments
    'recipes_1': 'recipes',
    'recipes_2': 'recipes', 
    'recipes_3': 'recipes',
    'recipes_4': 'recipes',
    'recipes_5': 'recipes',
    
    # Social media advertising environments
    'social_media_advertising_1': 'social_media_advertising',
    'social_media_advertising_2': 'social_media_advertising',
    'social_media_advertising_3': 'social_media_advertising',
    'social_media_advertising_4': 'social_media_advertising',
    'social_media_advertising_5': 'social_media_advertising',
    'social_media_advertising_6': 'social_media_advertising',
    
    # Academic search environments
    'academic_search_1': 'academic_search',
    'academic_search_2': 'academic_search',
    'academic_search_3': 'academic_search',
    'academic_search_4': 'academic_search',
    'academic_search_5': 'academic_search',
    
    # Airline environments
    'airline_1': 'airline',
    'airline_2': 'airline',
    'airline_3': 'airline',
    'airline_4': 'airline',
    'airline_5': 'airline',
    
    # Banking services environments
    'banking_services_1': 'banking_services',
    'banking_services_2': 'banking_services',
    'banking_services_4': 'banking_services',
    'banking_services_5': 'banking_services',
    'banking_services_6': 'banking_services',
    
    # Career planner environments
    'career_planner_1': 'career_planner',
    'career_planner_2': 'career_planner',
    'career_planner_3': 'career_planner',
    'career_planner_4': 'career_planner',
    'career_planner_5': 'career_planner',
    
    # Consulting accounting environments
    'consulting_accounting_1': 'consulting_accounting',
    'consulting_accounting_2': 'consulting_accounting',
    'consulting_accounting_4': 'consulting_accounting',
    'consulting_accounting_5': 'consulting_accounting',
    'consulting_accounting_6': 'consulting_accounting',
    
    # Data science environments
    'data_science_1': 'data_science',
    'data_science_2': 'data_science',
    'data_science_3': 'data_science',
    'data_science_4': 'data_science',
    'data_science_5': 'data_science',
    'data_science_6': 'data_science',
    
    # Dev ops environments
    'dev_ops_1': 'dev_ops',
    'dev_ops_2': 'dev_ops',
    'dev_ops_3': 'dev_ops',
    'dev_ops_4': 'dev_ops',
    'dev_ops_5': 'dev_ops',
    'dev_ops_6': 'dev_ops',
    
    # Digital commerce environments
    'digital_commerce_1': 'digital_commerce',
    'digital_commerce_2': 'digital_commerce',
    'digital_commerce_3': 'digital_commerce',
    'digital_commerce_4': 'digital_commerce',
    'digital_commerce_5': 'digital_commerce',
    
    # Figma Gmail MCP Pipeline environments
    'figma_gmail_mcp_pipeline_1': 'figma_gmail_mcp_pipeline',
    'figma_gmail_mcp_pipeline_2': 'figma_gmail_mcp_pipeline',
    'figma_gmail_mcp_pipeline_3': 'figma_gmail_mcp_pipeline',
    'figma_gmail_mcp_pipeline_4': 'figma_gmail_mcp_pipeline',
    'figma_gmail_mcp_pipeline_5': 'figma_gmail_mcp_pipeline',
    'figma_gmail_mcp_pipeline_6': 'figma_gmail_mcp_pipeline',
    
    # File system environments
    'file_system_1': 'file_system',
    'file_system_7': 'file_system',
    'file_system_8': 'file_system',
    'file_system_9': 'file_system',
    
    # GitHub MCP environments
    'github_mcp_1': 'github_mcp',
    'github_mcp_2': 'github_mcp',
    'github_mcp_5': 'github_mcp',
    'github_mcp_6': 'github_mcp',
    'github_mcp_7': 'github_mcp',
    
    # IT Help Desk environments
    'it_help_desk_2': 'it_help_desk',
    'it_help_desk_4': 'it_help_desk',
    'it_help_desk_5': 'it_help_desk',
    'it_help_desk_6': 'it_help_desk',
    
    # Logistics Supply Chain environments
    'logistics_supply_chain_1': 'logistics_supply_chain',
    'logistics_supply_chain_2': 'logistics_supply_chain',
    'logistics_supply_chain_3': 'logistics_supply_chain',
    'logistics_supply_chain_5': 'logistics_supply_chain',
    'logistics_supply_chain_6': 'logistics_supply_chain',
    
    # New Hire MCP environments
    'new_hire_mcp_1': 'new_hire_mcp',
    'new_hire_mcp_2': 'new_hire_mcp',
    'new_hire_mcp_3': 'new_hire_mcp',
    'new_hire_mcp_4': 'new_hire_mcp',
    'new_hire_mcp_5': 'new_hire_mcp',
    
    # Org Chart environments
    'org_chart_1': 'org_chart',
    'org_chart_2': 'org_chart',
    'org_chart_3': 'org_chart',
    'org_chart_4': 'org_chart',
    'org_chart_5': 'org_chart',
    
    # Project Management environments
    'project_management_1': 'project_management',
    'project_management_2': 'project_management',
    'project_management_3': 'project_management',
    'project_management_4': 'project_management',
    'project_management_5': 'project_management',
    
    # RBAC environments
    'rbac_1': 'rbac',
    'rbac_2': 'rbac',
    'rbac_3': 'rbac',
    'rbac_4': 'rbac',
    'rbac_5': 'rbac',
    
    # Real Estate Sales environments
    'real_estate_sales_1': 'real_estate_sales',
    'real_estate_sales_2': 'real_estate_sales',
    'real_estate_sales_3': 'real_estate_sales',
    'real_estate_sales_4': 'real_estate_sales',
    'real_estate_sales_7': 'real_estate_sales',
    
    # Retail environments
    'retail_1': 'retail',
    'retail_2': 'retail',
    'retail_3': 'retail',
    'retail_4': 'retail',
    'retail_5': 'retail',
    'retail_6': 'retail',
    
    # Retail Point of Sale and Inventory System environments
    'retail_point_of_sale_and_inventory_system_1': 'retail_point_of_sale_and_inventory_system',
    'retail_point_of_sale_and_inventory_system_2': 'retail_point_of_sale_and_inventory_system',
    'retail_point_of_sale_and_inventory_system_4': 'retail_point_of_sale_and_inventory_system',
    'retail_point_of_sale_and_inventory_system_5': 'retail_point_of_sale_and_inventory_system',
    'retail_point_of_sale_and_inventory_system_6': 'retail_point_of_sale_and_inventory_system',
    
    # Smart Home environments
    'smart_home_1': 'smart_home',
    'smart_home_2': 'smart_home',
    'smart_home_3': 'smart_home',
    'smart_home_4': 'smart_home',
    'smart_home_5': 'smart_home',
    
    # Sports Analytics environments
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

def add_import_to_file(file_path: Path, missing_functions: Set[str], warrior_domain: str) -> bool:
    """Add import statement for missing functions to a file."""
    try:
        content = file_path.read_text()
        
        # Create the import statement
        functions_list = ', '.join(sorted(missing_functions))
        import_line = f"from domains_warrior.{warrior_domain}.variations.variation_1.tools import {functions_list}\n"
        
        # Find where to insert the import (after existing imports)
        lines = content.split('\n')
        insert_index = 0
        
        # Find the last import line
        for i, line in enumerate(lines):
            if line.strip().startswith(('import ', 'from ')):
                insert_index = i + 1
        
        # Insert the import
        lines.insert(insert_index, import_line)
        
        # Write back to file
        new_content = '\n'.join(lines)
        file_path.write_text(new_content)
        
        return True
        
    except Exception as e:
        print(f"Error adding import to {file_path}: {e}")
        return False

def main():
    """Fix missing private functions by adding imports from warrior domains."""
    tau_dir = REPO_ROOT / "tau"
    
    if not tau_dir.exists():
        print(f"tau directory not found: {tau_dir}")
        return
    
    fixed_files = 0
    total_files = 0
    errors = 0
    
    print("Fixing missing private function imports...")
    
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
                if add_import_to_file(py_file, missing_functions, warrior_domain):
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
