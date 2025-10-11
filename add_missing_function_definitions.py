#!/usr/bin/env python3
"""
Extract and add missing private function definitions directly to tool files.
This script copies function definitions from warrior domains without importing.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

# Function mapping: function_name -> (domain, variation, file_path)
FUNCTION_MAPPING = {
    # Recipes functions
    '_household_for_user': ('recipes', 'variation_5', 'domains_warrior/recipes/variations/variation_5/tools.py'),
    '_latest_list_for_household': ('recipes', 'variation_5', 'domains_warrior/recipes/variations/variation_5/tools.py'),
    '_latest_order_for_household': ('recipes', 'variation_5', 'domains_warrior/recipes/variations/variation_5/tools.py'),
    '_latest_meal_plan_for_household': ('recipes', 'variation_5', 'domains_warrior/recipes/variations/variation_5/tools.py'),
    '_all_recipe_ids_filtered': ('recipes', 'variation_5', 'domains_warrior/recipes/variations/variation_5/tools.py'),
    '_decode_filter_token': ('recipes', 'variation_5', 'domains_warrior/recipes/variations/variation_5/tools.py'),
    '_parse_json_list_ids': ('recipes', 'variation_1', 'domains_warrior/recipes/variations/variation_1/tools.py'),
    '_collect_recipe_ingredients': ('recipes', 'variation_1', 'domains_warrior/recipes/variations/variation_1/tools.py'),
    '_next_week_start_date_for_household': ('recipes', 'variation_5', 'domains_warrior/recipes/variations/variation_5/tools.py'),
    '_plan_week_dates': ('recipes', 'variation_1', 'domains_warrior/recipes/variations/variation_1/tools.py'),
    '_recipe_by_id': ('recipes', 'variation_1', 'domains_warrior/recipes/variations/variation_1/tools.py'),
    '_recent_recipe_ids': ('recipes', 'variation_5', 'domains_warrior/recipes/variations/variation_5/tools.py'),
    '_pick_target_from_member': ('recipes', 'variation_5', 'domains_warrior/recipes/variations/variation_5/tools.py'),
    '_ids_from_kwargs_or_defaults': ('recipes', 'variation_5', 'domains_warrior/recipes/variations/variation_5/tools.py'),
    
    # Digital commerce functions
    '_slugify': ('digital_commerce', 'variation_1', 'domains_warrior/digital_commerce/variations/variation_1/tools.py'),
    '_err': ('digital_commerce', 'variation_1', 'domains_warrior/digital_commerce/variations/variation_1/tools.py'),
    '_ensure_table': ('digital_commerce', 'variation_1', 'domains_warrior/digital_commerce/variations/variation_1/tools.py'),
    '_find_one': ('digital_commerce', 'variation_1', 'domains_warrior/digital_commerce/variations/variation_1/tools.py'),
    '_ensure_audit_log': ('digital_commerce', 'variation_1', 'domains_warrior/digital_commerce/variations/variation_1/tools.py'),
    
    # Figma Gmail MCP Pipeline functions
    '_j': ('figma_gmail_mcp_pipeline', 'variation_3', 'domains_warrior/figma_gmail_mcp_pipeline/variations/variation_3/tools.py'),
    '_err': ('figma_gmail_mcp_pipeline', 'variation_3', 'domains_warrior/figma_gmail_mcp_pipeline/variations/variation_3/tools.py'),
    '_get_config_json': ('figma_gmail_mcp_pipeline', 'variation_1', 'domains_warrior/figma_gmail_mcp_pipeline/variations/variation_1/tools.py'),
    '_index_by': ('figma_gmail_mcp_pipeline', 'variation_1', 'domains_warrior/figma_gmail_mcp_pipeline/variations/variation_1/tools.py'),
    '_safe_table': ('figma_gmail_mcp_pipeline', 'variation_1', 'domains_warrior/figma_gmail_mcp_pipeline/variations/variation_1/tools.py'),
    '_get_next_id': ('figma_gmail_mcp_pipeline', 'variation_6', 'domains_warrior/figma_gmail_mcp_pipeline/variations/variation_6/tools.py'),
    
    # GitHub MCP functions
    '_repos': ('github_mcp', 'variation_7', 'domains_warrior/github_mcp/variations/variation_7/tools.py'),
    '_auth': ('github_mcp', 'variation_2', 'domains_warrior/github_mcp/variations/variation_2/tools.py'),
    
    # Banking services functions
    '_get_next_id': ('banking_services', 'variation_6', 'domains_warrior/banking_services/variations/variation_6/tools.py'),
    '_convert_db_to_list': ('banking_services', 'variation_1', 'domains_warrior/banking_services/variations/variation_1/tools.py'),
    
    # Data science functions
    '_fixed_now_iso': ('data_science', 'variation_3', 'domains_warrior/data_science/variations/variation_3/tools.py'),
    
    # Sports analytics functions
    '_today_iso': ('sports_analytics', 'variation_1', 'domains_warrior/sports_analytics/variations/variation_1/tools.py'),
    
    # New hire MCP functions
    '_render_template': ('new_hire_mcp', 'variation_1', 'domains_warrior/new_hire_mcp/variations/variation_1/tools.py'),
    '_fixed_ts': ('new_hire_mcp', 'variation_3', 'domains_warrior/new_hire_mcp/variations/variation_3/tools.py'),
    '_ensure_list': ('new_hire_mcp', 'variation_2', 'domains_warrior/new_hire_mcp/variations/variation_2/tools.py'),
    '_find_by_key': ('new_hire_mcp', 'variation_2', 'domains_warrior/new_hire_mcp/variations/variation_2/tools.py'),
    '_slug': ('new_hire_mcp', 'variation_2', 'domains_warrior/new_hire_mcp/variations/variation_2/tools.py'),
    
    # Airline functions
    '_norm': ('airline', 'variation_2', 'domains_warrior/airline/variations/variation_2/tools.py'),
    '_j': ('airline', 'variation_2', 'domains_warrior/airline/variations/variation_2/tools.py'),
    
    # RBAC functions
    '_eq': ('rbac', 'variation_1', 'domains_warrior/rbac/variations/variation_1/tools.py'),
    '_parse_iso': ('rbac', 'variation_1', 'domains_warrior/rbac/variations/variation_1/tools.py'),
    
    # Smart home functions
    '_now_iso': ('smart_home', 'variation_1', 'domains_warrior/smart_home/variations/variation_1/tools.py'),
    
    # Real estate sales functions
    '_index_by': ('real_estate_sales', 'variation_1', 'domains_warrior/real_estate_sales/variations/variation_1/tools.py'),
    '_latest': ('real_estate_sales', 'variation_7', 'domains_warrior/real_estate_sales/variations/variation_7/tools.py'),
    '_err': ('real_estate_sales', 'variation_7', 'domains_warrior/real_estate_sales/variations/variation_7/tools.py'),
    
    # Dev ops functions
    '_idx_by_id': ('dev_ops', 'variation_1', 'domains_warrior/dev_ops/variations/variation_1/tools.py'),
    '_err': ('dev_ops', 'variation_6', 'domains_warrior/dev_ops/variations/variation_6/tools.py'),
    '_get_next_id': ('dev_ops', 'variation_3', 'domains_warrior/dev_ops/variations/variation_3/tools.py'),
    
    # IT Help Desk functions
    '_get_next_id': ('it_help_desk', 'variation_4', 'domains_warrior/it_help_desk/variations/variation_4/tools.py'),
    
    # Consulting accounting functions
    '_fixed_now_iso': ('consulting_accounting', 'variation_4', 'domains_warrior/consulting_accounting/variations/variation_4/tools.py'),
}

def extract_function_definition(file_path: Path, function_name: str) -> str:
    """Extract a function definition from a warrior domain file."""
    try:
        content = file_path.read_text()
        
        # Find the function definition
        pattern = rf'^def {re.escape(function_name)}\(.*?^def |^class |\Z'
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        
        if match:
            func_def = match.group(0).rstrip()
            # Remove the trailing 'def ' or 'class ' from the next definition
            if func_def.endswith('def '):
                func_def = func_def[:-4]
            elif func_def.endswith('class '):
                func_def = func_def[:-6]
            
            return func_def.strip()
        
        return None
        
    except Exception as e:
        print(f"Error extracting function from {file_path}: {e}")
        return None

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

def add_function_definitions_to_file(file_path: Path, missing_functions: Set[str]) -> bool:
    """Add function definitions directly to a file."""
    try:
        content = file_path.read_text()
        
        # Remove any existing warrior domain imports
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            if 'from domains_warrior.' in line and 'import' in line:
                continue  # Skip warrior domain imports
            new_lines.append(line)
        
        # Extract function definitions
        function_definitions = []
        for func in missing_functions:
            if func in FUNCTION_MAPPING:
                domain, variation, warrior_file = FUNCTION_MAPPING[func]
                warrior_path = REPO_ROOT / warrior_file
                
                if warrior_path.exists():
                    func_def = extract_function_definition(warrior_path, func)
                    if func_def:
                        function_definitions.append(func_def)
                        print(f"  Adding function: {func}")
        
        if not function_definitions:
            return False
        
        # Find where to insert the function definitions (after imports, before classes)
        insert_index = 0
        for i, line in enumerate(new_lines):
            if line.strip().startswith(('import ', 'from ')):
                insert_index = i + 1
        
        # Insert function definitions
        for func_def in function_definitions:
            new_lines.insert(insert_index, func_def)
            new_lines.insert(insert_index + 1, '')  # Add blank line
            insert_index += 2
        
        # Write back to file
        new_content = '\n'.join(new_lines)
        file_path.write_text(new_content)
        
        return True
        
    except Exception as e:
        print(f"Error adding function definitions to {file_path}: {e}")
        return False

def main():
    """Add missing private function definitions directly to tool files."""
    tau_dir = REPO_ROOT / "tau"
    
    if not tau_dir.exists():
        print(f"tau directory not found: {tau_dir}")
        return
    
    fixed_files = 0
    total_files = 0
    errors = 0
    
    print("Adding missing private function definitions directly to tool files...")
    
    # Find all Python tool files
    for py_file in tau_dir.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
            
        total_files += 1
        missing_functions = find_undefined_functions(py_file)
        
        if missing_functions:
            print(f"\nFixing {py_file.relative_to(tau_dir)}: {', '.join(sorted(missing_functions))}")
            if add_function_definitions_to_file(py_file, missing_functions):
                fixed_files += 1
            else:
                errors += 1
    
    print(f"\n=== Summary ===")
    print(f"Total files scanned: {total_files}")
    print(f"Files fixed: {fixed_files}")
    print(f"Errors: {errors}")

if __name__ == "__main__":
    main()
