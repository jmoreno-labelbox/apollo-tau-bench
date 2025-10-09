#!/usr/bin/env python3
"""
Automated fix script for common syntax errors in tau/ directory

This script fixes:
1. Future import ordering issues
2. Duplicate dictionary keys
3. Simple indentation issues
4. Relative import issues

Run with --dry-run to see what would be changed without making changes
"""

import sys
import re
import argparse
from pathlib import Path
from typing import List, Tuple

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def fix_future_import_order(file_path: Path, dry_run: bool = False) -> bool:
    """Fix files where 'from __future__ import' is not on line 1"""
    content = file_path.read_text()
    lines = content.split('\n')
    
    # Find the __future__ import line
    future_line_idx = None
    future_line = None
    for i, line in enumerate(lines):
        if line.strip().startswith('from __future__ import'):
            future_line_idx = i
            future_line = line
            break
    
    if future_line_idx is None:
        return False
    
    if future_line_idx == 0:
        return False  # Already on line 1
    
    # Remove the future import from its current position
    lines.pop(future_line_idx)
    
    # Insert it at the beginning
    lines.insert(0, future_line)
    
    if not dry_run:
        file_path.write_text('\n'.join(lines))
        print(f"{Colors.GREEN}✓{Colors.END} Fixed: {file_path}")
    else:
        print(f"{Colors.YELLOW}Would fix:{Colors.END} {file_path}")
    
    return True

def fix_relative_imports(file_path: Path, dry_run: bool = False) -> bool:
    """Fix imports that should be relative (from rules import -> from .rules import)"""
    content = file_path.read_text()
    
    # Check if this is in digital_commerce_4
    if 'digital_commerce_4' not in str(file_path):
        return False
    
    # Look for 'from rules import'
    if 'from rules import' not in content:
        return False
    
    # Replace with relative import
    new_content = content.replace('from rules import', 'from .rules import')
    
    if not dry_run:
        file_path.write_text(new_content)
        print(f"{Colors.GREEN}✓{Colors.END} Fixed: {file_path}")
    else:
        print(f"{Colors.YELLOW}Would fix:{Colors.END} {file_path}")
    
    return True

def fix_duplicate_dict_key(file_path: Path, dry_run: bool = False) -> bool:
    """Fix duplicate dictionary key in openai.py"""
    if 'openai.py' not in str(file_path):
        return False
    
    content = file_path.read_text()
    lines = content.split('\n')
    
    # Find lines with the duplicate key
    duplicate_key = '"gpt-4o-2024-08-06"'
    found_indices = []
    
    for i, line in enumerate(lines):
        if duplicate_key in line and 'PRICE_PER_INPUT_TOKEN_MAP' in '\n'.join(lines[max(0, i-5):i+1]):
            found_indices.append(i)
    
    if len(found_indices) <= 1:
        return False  # No duplicate
    
    # Keep the first occurrence, remove subsequent ones
    for idx in reversed(found_indices[1:]):
        if not dry_run:
            lines.pop(idx)
            print(f"{Colors.GREEN}✓{Colors.END} Removed duplicate key at line {idx+1}: {file_path}")
        else:
            print(f"{Colors.YELLOW}Would remove:{Colors.END} duplicate key at line {idx+1} in {file_path}")
    
    if not dry_run:
        file_path.write_text('\n'.join(lines))
    
    return True

def fix_create_log_entry_indentation(file_path: Path, dry_run: bool = False) -> bool:
    """Fix the specific indentation issue in create_log_entry.py"""
    if 'create_log_entry.py' not in str(file_path):
        return False
    
    content = file_path.read_text()
    
    # The problematic pattern
    bad_pattern = """users, articles, logs = (
            data.get("users", {}).values()),
            data.get("articles", {}).values()),
            data.get("research_logs", {}).values()),
        )"""
    
    good_pattern = """users, articles, logs = (
            data.get("users", {}).values(),
            data.get("articles", {}).values(),
            data.get("research_logs", {}).values()
        )"""
    
    if bad_pattern not in content:
        return False
    
    new_content = content.replace(bad_pattern, good_pattern)
    
    if not dry_run:
        file_path.write_text(new_content)
        print(f"{Colors.GREEN}✓{Colors.END} Fixed: {file_path}")
    else:
        print(f"{Colors.YELLOW}Would fix:{Colors.END} {file_path}")
    
    return True

def fix_line_continuation_in_strings(file_path: Path, dry_run: bool = False) -> bool:
    """Fix line continuation character issues in strings"""
    content = file_path.read_text()
    
    # Look for patterns like \"You are
    # This is a simple heuristic - may need manual review
    if '\\"' not in content and '\\n' in content:
        return False
    
    # Check if this file has the specific issue
    # Looking for backslash before You in strings
    pattern = r'\\You are'
    
    if not re.search(pattern, content):
        return False
    
    # For now, just report these - they need manual inspection
    print(f"{Colors.YELLOW}⚠{Colors.END}  Needs manual review (line continuation): {file_path}")
    return False

def main():
    parser = argparse.ArgumentParser(description='Fix common syntax errors in tau/ directory')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be fixed without making changes')
    parser.add_argument('--verbose', action='store_true',
                       help='Show verbose output')
    args = parser.parse_args()
    
    print(f"\n{Colors.BOLD}TAU Syntax Error Auto-Fix{Colors.END}")
    print("="*70)
    
    if args.dry_run:
        print(f"{Colors.YELLOW}DRY RUN MODE - No changes will be made{Colors.END}\n")
    
    tau_path = Path("tau/tau_bench")
    if not tau_path.exists():
        print(f"{Colors.RED}Error: tau/tau_bench directory not found{Colors.END}")
        return 1
    
    fixed_counts = {
        'future_imports': 0,
        'relative_imports': 0,
        'duplicate_keys': 0,
        'indentation': 0,
        'line_continuation': 0
    }
    
    # Fix future import ordering (airline_5/tools/*.py)
    print(f"\n{Colors.BOLD}1. Fixing future import ordering...{Colors.END}")
    airline5_tools = Path("tau/tau_bench/envs/airline_5/tools")
    if airline5_tools.exists():
        for py_file in airline5_tools.glob("*.py"):
            if fix_future_import_order(py_file, args.dry_run):
                fixed_counts['future_imports'] += 1
    
    # Fix relative imports
    print(f"\n{Colors.BOLD}2. Fixing relative imports...{Colors.END}")
    for py_file in tau_path.rglob("*.py"):
        if fix_relative_imports(py_file, args.dry_run):
            fixed_counts['relative_imports'] += 1
    
    # Fix duplicate dictionary key
    print(f"\n{Colors.BOLD}3. Fixing duplicate dictionary keys...{Colors.END}")
    openai_file = Path("tau/tau_bench/model_utils/model/openai.py")
    if openai_file.exists():
        if fix_duplicate_dict_key(openai_file, args.dry_run):
            fixed_counts['duplicate_keys'] += 1
    
    # Fix create_log_entry.py indentation
    print(f"\n{Colors.BOLD}4. Fixing indentation issues...{Colors.END}")
    create_log_entry = Path("tau/tau_bench/envs/academic_search_1/tools/create_log_entry.py")
    if create_log_entry.exists():
        if fix_create_log_entry_indentation(create_log_entry, args.dry_run):
            fixed_counts['indentation'] += 1
    
    # Report line continuation issues (manual review needed)
    print(f"\n{Colors.BOLD}5. Checking line continuation issues (manual review needed)...{Colors.END}")
    line_continuation_files = [
        "tau/tau_bench/envs/airline_3/tasks.py",
        "tau/tau_bench/envs/digital_commerce_3/tools/configure_shipping_rules.py",
        "tau/tau_bench/envs/project_management_1/tools/create_project.py",
        "tau/tau_bench/envs/project_management_1/tools/create_rotation_schedule.py",
        "tau/tau_bench/envs/project_management_4/tools/update_buffer_consumption.py",
        "tau/tau_bench/envs/rbac_1/tools/create_role.py",
        "tau/tau_bench/envs/retail_1/tools/create_bulk_order.py",
    ]
    for file_path in line_continuation_files:
        p = Path(file_path)
        if p.exists():
            fix_line_continuation_in_strings(p, args.dry_run)
    
    # Summary
    print(f"\n{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}SUMMARY{Colors.END}")
    print(f"{'='*70}")
    
    total_fixed = sum(fixed_counts.values())
    
    if args.dry_run:
        print(f"\nWould fix {total_fixed} issues:")
    else:
        print(f"\nFixed {total_fixed} issues:")
    
    for category, count in fixed_counts.items():
        if count > 0:
            print(f"  {Colors.GREEN}✓{Colors.END} {category.replace('_', ' ').title()}: {count}")
    
    print(f"\n{Colors.YELLOW}Note:{Colors.END} Some issues require manual review:")
    print(f"  - Unterminated string literals (2 files)")
    print(f"  - Line continuation character issues (13 files)")
    print(f"  - Other syntax errors (1 file)")
    print(f"\nRun verify_tau_lint_fixes.py to check remaining issues.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

