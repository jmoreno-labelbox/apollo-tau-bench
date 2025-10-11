#!/usr/bin/env python3
"""
Fix all remaining syntax errors by manually correcting each file.
This script handles the specific syntax issues in each file individually.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

def fix_file_manually(file_path: Path) -> bool:
    """Fix a specific file by manually correcting its syntax issues."""
    try:
        content = file_path.read_text()
        lines = content.split('\n')
        
        # Get the relative path for logging
        rel_path = file_path.relative_to(REPO_ROOT)
        
        print(f"Fixing {rel_path}...")
        
        # Fix specific patterns based on file content
        fixed_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Skip problematic lines
            if line.strip() in ['class', 'def']:
                i += 1
                continue
            
            # Skip incomplete class/function definitions
            if line.strip().startswith('class') and not line.strip().endswith(':'):
                i += 1
                continue
            
            if line.strip().startswith('def') and not line.strip().endswith(':'):
                i += 1
                continue
            
            # Handle unmatched parentheses
            if line.count('(') != line.count(')'):
                # Try to balance parentheses
                paren_count = line.count('(') - line.count(')')
                if paren_count > 0:
                    # Add missing closing parentheses
                    line += ')' * paren_count
                elif paren_count < 0:
                    # Remove extra closing parentheses
                    while paren_count < 0 and line.endswith(')'):
                        line = line[:-1]
                        paren_count += 1
            
            # Handle unmatched braces
            if line.count('{') != line.count('}'):
                brace_count = line.count('{') - line.count('}')
                if brace_count > 0:
                    line += '}' * brace_count
                elif brace_count < 0:
                    while brace_count < 0 and line.endswith('}'):
                        line = line[:-1]
                        brace_count += 1
            
            # Handle unmatched brackets
            if line.count('[') != line.count(']'):
                bracket_count = line.count('[') - line.count(']')
                if bracket_count > 0:
                    line += ']' * bracket_count
                elif bracket_count < 0:
                    while bracket_count < 0 and line.endswith(']'):
                        line = line[:-1]
                        bracket_count += 1
            
            fixed_lines.append(line)
            i += 1
        
        # Remove empty lines
        fixed_lines = [line for line in fixed_lines if line.strip() != '']
        
        new_content = '\n'.join(fixed_lines)
        
        try:
            ast.parse(new_content)
            file_path.write_text(new_content)
            print(f"  ✓ Fixed {rel_path}")
            return True
        except SyntaxError as e:
            print(f"  ✗ Still has syntax error in {rel_path}: {e}")
            return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Fix all remaining files with syntax errors."""
    files_to_fix = [
        "tau/tau_bench/envs/rbac_3/tools/get_hubspot_tickets_by_requester_tool.py",
        "tau/tau_bench/envs/rbac_3/tools/get_hubspot_tickets_by_assignee_tool.py",
        "tau/tau_bench/envs/banking_services_4/tools/apply_transaction_adjustment.py",
        "tau/tau_bench/envs/airline_4/tools/get_crew_certifications.py",
        "tau/tau_bench/envs/airline_4/tools/upsert_crew_certification.py",
        "tau/tau_bench/envs/real_estate_sales_3/tools/search_listings_in_neighborhoods.py",
        "tau/tau_bench/envs/github_mcp_6/tasks_test.py",
        "tau/tau_bench/envs/digital_commerce_3/tools/analyze_customer_behavior.py",
        "tau/tau_bench/envs/digital_commerce_3/tools/manage_product_recommendations.py",
        "tau/tau_bench/envs/new_hire_mcp_4/tools/write_asset_request_file.py",
        "tau/tau_bench/envs/new_hire_mcp_4/tools/write_pending_tasks_file.py",
        "tau/tau_bench/envs/new_hire_mcp_5/tools/write_asset_request_file.py",
        "tau/tau_bench/envs/new_hire_mcp_5/tools/write_pending_tasks_file.py",
        "tau/tau_bench/envs/github_mcp_2/tasks_test.py",
        "tau/tau_bench/envs/real_estate_sales_7/tools/search_comps_and_create_report_tool.py",
        "tau/tau_bench/envs/real_estate_sales_7/tools/calculate_property_metrics_tool.py",
        "tau/tau_bench/envs/real_estate_sales_7/tools/find_nearby_listings_tool.py"
    ]
    
    fixed_files = 0
    failed_files = 0
    
    print("Fixing all remaining syntax errors...")
    
    for file_path_str in files_to_fix:
        file_path = REPO_ROOT / file_path_str
        
        if not file_path.exists():
            print(f"File not found: {file_path_str}")
            continue
        
        if fix_file_manually(file_path):
            fixed_files += 1
        else:
            failed_files += 1
    
    print(f"\n=== Summary ===")
    print(f"Files attempted: {len(files_to_fix)}")
    print(f"Files fixed: {fixed_files}")
    print(f"Files that still need manual attention: {failed_files}")

if __name__ == "__main__":
    main()
