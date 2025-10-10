#!/usr/bin/env python3
"""
Fix the dict vs list bug in all tau-bench environments.

Bug: data.get('key', []) assumes data['key'] is a list, but it's actually a dict.
Fix: Use list(data.get('key', {}).values()) to convert dict.values() to list.

This script finds and fixes all occurrences across all environments.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple


def find_data_get_patterns(file_path: Path) -> List[Tuple[int, str]]:
    """Find all data.get(..., []) patterns in a file."""
    patterns = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                if 'data.get(' in line and ', []' in line:
                    patterns.append((line_num, line.rstrip()))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return patterns


def fix_file(file_path: Path, dry_run: bool = True) -> int:
    """
    Fix all data.get(..., []) patterns in a file.
    Returns number of fixes applied.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixes_applied = 0
        
        # List of common data keys that are stored as dicts in tau-bench
        dict_keys = [
            'articles', 'projects', 'users', 'research_logs', 'citations',
            'submissions', 'reviews', 'funding_sources', 'subscriptions',
            'notifications', 'accounts', 'transactions', 'customers',
            'products', 'orders', 'inventory', 'campaigns', 'ads',
            'servers', 'deployments', 'incidents', 'tickets', 'employees',
            'departments', 'tasks', 'milestones', 'properties', 'listings',
            'clients', 'appointments', 'recipes', 'ingredients', 'meals',
            'devices', 'automations', 'scenes', 'flights', 'reservations',
            'passengers', 'airports', 'aircraft', 'routes', 'schedules',
            'datasets', 'models', 'experiments', 'jobs', 'pipelines',
            'repositories', 'issues', 'pull_requests', 'commits', 'branches',
            'loans', 'beneficiaries', 'support_tickets', 'payment_methods',
            'permissions', 'roles', 'access_logs', 'audit_trails'
        ]
        
        # Fix each known dict key
        for key in dict_keys:
            old_pattern = f"data.get('{key}', [])"
            new_pattern = f"list(data.get('{key}', {{}}).values())"
            
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                fixes_applied += content.count(new_pattern) - original_content.count(new_pattern)
            
            # Also handle double quotes
            old_pattern_dq = f'data.get("{key}", [])'
            new_pattern_dq = f'list(data.get("{key}", {{}}).values())'
            
            if old_pattern_dq in content:
                content = content.replace(old_pattern_dq, new_pattern_dq)
                fixes_applied += content.count(new_pattern_dq) - original_content.count(new_pattern_dq)
        
        if content != original_content and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return fixes_applied
    
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return 0


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Fix dict vs list bug in all tau-bench environments")
    parser.add_argument("--execute", action="store_true", help="Actually fix files (default is dry run)")
    args = parser.parse_args()
    
    tau_envs = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    if not tau_envs.exists():
        print(f"❌ Directory not found: {tau_envs}")
        return
    
    print("🔍 Scanning all environments for dict vs list bug...")
    print()
    
    if not args.execute:
        print("📋 DRY RUN MODE - No files will be modified")
        print()
    
    env_dirs = sorted([d for d in tau_envs.iterdir() if d.is_dir() and d.name != "__pycache__"])
    
    total_files_scanned = 0
    total_files_with_issues = 0
    total_fixes = 0
    files_by_env = {}
    
    for env_dir in env_dirs:
        # Find all Python files in tools/ directory or tools.py
        py_files = []
        
        tools_dir = env_dir / "tools"
        if tools_dir.exists() and tools_dir.is_dir():
            py_files.extend(tools_dir.glob("*.py"))
        
        tools_file = env_dir / "tools.py"
        if tools_file.exists():
            py_files.append(tools_file)
        
        env_fixes = 0
        env_files_with_issues = []
        
        for py_file in py_files:
            if py_file.name == "__init__.py":
                continue
            
            total_files_scanned += 1
            patterns = find_data_get_patterns(py_file)
            
            if patterns:
                fixes = fix_file(py_file, dry_run=not args.execute)
                if fixes > 0:
                    total_files_with_issues += 1
                    env_fixes += fixes
                    env_files_with_issues.append((py_file.name, fixes))
        
        if env_fixes > 0:
            files_by_env[env_dir.name] = (env_fixes, env_files_with_issues)
            total_fixes += env_fixes
    
    # Print results
    print("=" * 80)
    print("📊 RESULTS")
    print("=" * 80)
    print()
    
    if files_by_env:
        print(f"Environments with issues: {len(files_by_env)}")
        print()
        
        for env_name, (env_fixes, files) in sorted(files_by_env.items()):
            print(f"📁 {env_name}: {env_fixes} fixes in {len(files)} files")
            for file_name, file_fixes in files[:3]:  # Show first 3 files
                print(f"   - {file_name}: {file_fixes} fixes")
            if len(files) > 3:
                print(f"   ... and {len(files) - 3} more files")
        print()
    
    print(f"Total files scanned:     {total_files_scanned}")
    print(f"Files with issues:       {total_files_with_issues}")
    print(f"Total fixes applied:     {total_fixes}")
    print()
    
    if not args.execute:
        print("=" * 80)
        print("📝 This was a DRY RUN - no files were modified")
        print()
        print("To actually apply fixes, run:")
        print("  python3 fix_dict_vs_list_bug.py --execute")
        print("=" * 80)
    else:
        print("=" * 80)
        print("✅ All fixes applied successfully!")
        print()
        print("Next steps:")
        print("  1. Test a few environments:")
        print("     cd tau")
        print("     python3 run.py --env academic_search_2 --end-index 1")
        print("     python3 run.py --env banking_services_2 --end-index 1")
        print()
        print("  2. Run comprehensive tests across multiple domains")
        print("=" * 80)


if __name__ == "__main__":
    main()

