#!/usr/bin/env python3
"""
Find missing private functions that can be imported from domains_warrior.
This script identifies tool files that use private functions but don't define them,
and suggests importing them from the appropriate warrior domain.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

# Common private functions from warrior domains
WARRIOR_FUNCTIONS = {
    "_tbl": "Get table from data, creating empty list if not exists",
    "_max_id": "Find maximum integer value for given key in items list", 
    "_index_by": "Index records by a key field",
    "_require": "Find first item in list where key matches value",
    "_parse_json_list_ids": "Parse JSON string to list of integers",
    "_json_dump": "Pretty print JSON with consistent formatting",
    "_next_numeric_id": "Generate next numeric ID from existing records",
    "_fail": "Create error response JSON",
    "_assert_table": "Assert table exists and is a list"
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

def find_warrior_domain_for_function(func_name: str, file_path: Path) -> str:
    """Find which warrior domain contains the function."""
    # Extract environment name from path
    path_parts = file_path.parts
    env_name = None
    for part in path_parts:
        if part.startswith(('recipes_', 'social_media_advertising_', 'academic_search_', 
                          'airline_', 'banking_services_', 'career_planner_', 
                          'consulting_accounting_', 'data_science_', 'dev_ops_',
                          'digital_commerce_', 'figma_gmail_mcp_pipeline_', 'file_system_',
                          'github_mcp_', 'it_help_desk_', 'logistics_supply_chain_',
                          'new_hire_mcp_', 'org_chart_', 'project_management_', 'rbac_',
                          'real_estate_sales_', 'retail_', 'retail_point_of_sale_and_inventory_system_',
                          'smart_home_', 'sports_analytics_')):
            env_name = part
            break
    
    if not env_name:
        return "unknown"
    
    # Map environment names to warrior domain folder names
    # This maps the exact environment names to their corresponding warrior domain folders
    domain_mapping = {
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
    
    # Return the mapped domain name
    return domain_mapping.get(env_name, "unknown")

def analyze_file(file_path: Path) -> Dict:
    """Analyze a single file for missing private functions."""
    missing_functions = find_undefined_functions(file_path)
    
    if not missing_functions:
        return None
    
    # Find warrior domain for this file
    warrior_domain = find_warrior_domain_for_function(list(missing_functions)[0], file_path)
    
    return {
        'file': str(file_path),
        'missing_functions': missing_functions,
        'warrior_domain': warrior_domain,
        'suggested_import': f"from domains_warrior.{warrior_domain}.variations.variation_1.tools import {', '.join(sorted(missing_functions))}"
    }

def main():
    """Find missing private functions across all tool files."""
    tau_dir = REPO_ROOT / "tau"
    
    if not tau_dir.exists():
        print(f"tau directory not found: {tau_dir}")
        return
    
    all_issues = []
    files_with_issues = 0
    total_files = 0
    
    print("Scanning for missing private functions...")
    
    # Find all Python tool files
    for py_file in tau_dir.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
            
        total_files += 1
        analysis = analyze_file(py_file)
        
        if analysis:
            files_with_issues += 1
            all_issues.append(analysis)
            
            print(f"\n{py_file.relative_to(tau_dir)}:")
            print(f"  Missing functions: {', '.join(sorted(analysis['missing_functions']))}")
            print(f"  Warrior domain: {analysis['warrior_domain']}")
            print(f"  Suggested import: {analysis['suggested_import']}")
    
    print(f"\n=== Summary ===")
    print(f"Total files scanned: {total_files}")
    print(f"Files with missing functions: {files_with_issues}")
    
    # Group by missing function
    function_counts = {}
    for issue in all_issues:
        for func in issue['missing_functions']:
            function_counts[func] = function_counts.get(func, 0) + 1
    
    if function_counts:
        print(f"\n=== Most Common Missing Functions ===")
        for func, count in sorted(function_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{func}: {count} files")

if __name__ == "__main__":
    main()
