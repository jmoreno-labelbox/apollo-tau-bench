#!/usr/bin/env python3
"""
Fix all remaining syntax errors by rewriting corrupted files.
This script identifies the correct content and rewrites each file.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

def extract_valid_content(content: str) -> str:
    """Extract valid Python content from corrupted file."""
    lines = content.split('\n')
    valid_lines = []
    
    # Find the first valid class definition
    in_valid_class = False
    brace_count = 0
    
    for line in lines:
        # Skip problematic lines
        if line.strip() in ['class', 'def']:
            continue
        
        # Skip incomplete definitions
        if line.strip().startswith('class') and not line.strip().endswith(':'):
            continue
        
        if line.strip().startswith('def') and not line.strip().endswith(':'):
            continue
        
        # Skip lines with just braces or brackets
        if line.strip() in ['{', '}', '[', ']', '(', ')']:
            continue
        
        # If we find a valid class definition, start collecting
        if line.strip().startswith('class ') and line.strip().endswith(':'):
            in_valid_class = True
        
        if in_valid_class:
            valid_lines.append(line)
    
    return '\n'.join(valid_lines)

def fix_file_by_rewriting(file_path: Path) -> bool:
    """Fix a file by rewriting it with valid content."""
    try:
        content = file_path.read_text()
        rel_path = file_path.relative_to(REPO_ROOT)
        
        print(f"Fixing {rel_path}...")
        
        # Extract valid content
        valid_content = extract_valid_content(content)
        
        if not valid_content.strip():
            print(f"  ✗ No valid content found in {rel_path}")
            return False
        
        # Add necessary imports if missing
        if 'from tau_bench.envs.tool import Tool' not in valid_content:
            valid_content = 'from tau_bench.envs.tool import Tool\n\n' + valid_content
        
        # Check if syntax is valid
        try:
            ast.parse(valid_content)
            file_path.write_text(valid_content)
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
    
    print("Fixing all remaining syntax errors by rewriting...")
    
    for file_path_str in files_to_fix:
        file_path = REPO_ROOT / file_path_str
        
        if not file_path.exists():
            print(f"File not found: {file_path_str}")
            continue
        
        if fix_file_by_rewriting(file_path):
            fixed_files += 1
        else:
            failed_files += 1
    
    print(f"\n=== Summary ===")
    print(f"Files attempted: {len(files_to_fix)}")
    print(f"Files fixed: {fixed_files}")
    print(f"Files that still need manual attention: {failed_files}")

if __name__ == "__main__":
    main()
