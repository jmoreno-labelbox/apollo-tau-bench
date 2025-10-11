#!/usr/bin/env python3
"""
Fix STR NO GET errors in recipes_3 by updating specific files.
This script fixes the remaining files that use data.get("table", []) in for loops.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

def fix_str_no_get_in_file(file_path: Path) -> bool:
    """Fix STR NO GET errors in a specific file."""
    try:
        content = file_path.read_text()
        rel_path = file_path.relative_to(REPO_ROOT)
        
        print(f"Fixing {rel_path}...")
        
        # Fix pattern: for x in data.get("table", []) -> for x in list(data.get("table", {}).values())
        original_content = content
        
        # Pattern 1: for x in data.get("table", [])
        content = re.sub(
            r'for\s+(\w+)\s+in\s+data\.get\("([^"]+)",\s*\[\])',
            r'for \1 in list(data.get("\2", {}).values())',
            content
        )
        
        # Pattern 2: [x for x in data.get("table", []) if condition]
        content = re.sub(
            r'\[([^]]*)\s+for\s+(\w+)\s+in\s+data\.get\("([^"]+)",\s*\[\])',
            r'[\1 for \2 in list(data.get("\3", {}).values())',
            content
        )
        
        # Check if any changes were made
        if content == original_content:
            print(f"  ⏭️  No changes needed in {rel_path}")
            return True
        
        # Check if syntax is valid
        try:
            ast.parse(content)
            file_path.write_text(content)
            print(f"  ✓ Fixed {rel_path}")
            return True
        except SyntaxError as e:
            print(f"  ✗ Still has syntax error in {rel_path}: {e}")
            return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Fix STR NO GET errors in all remaining recipes_3 files."""
    files_to_fix = [
        "tau/tau_bench/envs/recipes_3/tools/upsert_grocery_list_items_for_plan_by_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/update_order_status_by_plan_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/update_meal_plan_entry_notes_by_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/update_meal_plan_entry_notes.py",
        "tau/tau_bench/envs/recipes_3/tools/update_grocery_list_with_substitutes_by_plan_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/update_grocery_list_with_substitutes.py",
        "tau/tau_bench/envs/recipes_3/tools/propose_substitute_products.py",
        "tau/tau_bench/envs/recipes_3/tools/log_order_placed_by_plan_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/log_order_delivered_by_plan_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/log_meal_plan_create_by_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/log_meal_history_create_by_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/log_inventory_consume_by_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/log_grocery_list_create_by_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/list_recipe_ingredients.py",
        "tau/tau_bench/envs/recipes_3/tools/list_recent_meal_history.py",
        "tau/tau_bench/envs/recipes_3/tools/list_household_members.py",
        "tau/tau_bench/envs/recipes_3/tools/get_order_details_by_plan_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/get_order_details.py",
        "tau/tau_bench/envs/recipes_3/tools/get_meal_plan_by_household_and_week.py",
        "tau/tau_bench/envs/recipes_3/tools/get_household_staple_ingredient_id.py",
        "tau/tau_bench/envs/recipes_3/tools/get_household_by_primary_user.py",
        "tau/tau_bench/envs/recipes_3/tools/get_grocery_list_details_by_plan_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/get_grocery_list_details.py",
        "tau/tau_bench/envs/recipes_3/tools/get_grocery_list_by_source_plan.py",
        "tau/tau_bench/envs/recipes_3/tools/get_grocery_list_by_plan_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/flag_pantry_staples_on_list_by_plan_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/flag_pantry_staples_on_list.py",
        "tau/tau_bench/envs/recipes_3/tools/flag_overlap_last_month_on_list_by_plan_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/flag_overlap_last_month_on_list.py",
        "tau/tau_bench/envs/recipes_3/tools/create_order_for_plan_list_by_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/create_grocery_list_for_plan_by_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/compute_household_servings.py",
        "tau/tau_bench/envs/recipes_3/tools/check_store_inventory_for_plan_by_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/check_store_inventory_for_list.py",
        "tau/tau_bench/envs/recipes_3/tools/categorize_grocery_list_sections_by_plan_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/categorize_grocery_list_sections.py",
        "tau/tau_bench/envs/recipes_3/tools/add_order_items_from_list.py",
        "tau/tau_bench/envs/recipes_3/tools/add_order_items_for_plan_by_keys.py",
        "tau/tau_bench/envs/recipes_3/tools/add_meal_plan_entries_by_keys.py"
    ]
    
    fixed_files = 0
    failed_files = 0
    no_change_files = 0
    
    print("Fixing STR NO GET errors in remaining recipes_3 files...")
    
    for file_path_str in files_to_fix:
        file_path = REPO_ROOT / file_path_str
        
        if not file_path.exists():
            print(f"File not found: {file_path_str}")
            continue
        
        if fix_str_no_get_in_file(file_path):
            fixed_files += 1
        else:
            failed_files += 1
    
    print(f"\n=== Summary ===")
    print(f"Files attempted: {len(files_to_fix)}")
    print(f"Files fixed: {fixed_files}")
    print(f"Files that still need manual attention: {failed_files}")

if __name__ == "__main__":
    main()
