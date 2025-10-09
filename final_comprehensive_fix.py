#!/usr/bin/env python3
"""
FINAL COMPREHENSIVE FIX - Catch ALL iteration patterns including nested loops
"""
import re
from pathlib import Path

# ALL possible database variable names in the codebase
DB_VAR_NAMES = [
    'users', 'orders', 'products', 'couriers', 'suppliers', 'tracking', 'supply_orders',
    'flights', 'passengers', 'aircraft', 'crew', 'routes', 'airports', 'maintenance',
    'accounts', 'transactions', 'customers', 'loans', 'deposits', 'payments', 'cards',
    'projects', 'articles', 'citations', 'reviews', 'submissions', 'notifications',
    'files', 'directories', 'tasks', 'logs', 'permissions', 'archives', 'metadata',
    'repositories', 'issues', 'pull_requests', 'commits', 'branches', 'releases',
    'candidates', 'employees', 'departments', 'positions', 'applications', 'interviews',
    'roles', 'permissions', 'policies', 'sessions', 'audit_logs', 'access_controls',
    'listings', 'agents', 'offers', 'showings', 'contracts', 'properties', 'inspections',
    'recipes', 'ingredients', 'meal_plans', 'grocery_lists', 'households', 'members',
    'campaigns', 'ad_sets', 'ads', 'creatives', 'audiences', 'budgets', 'metrics',
    'teams', 'players', 'games', 'venues', 'stats', 'matches', 'umpires', 'pitches',
    'invoices', 'expenses', 'revenue', 'clients', 'timesheet', 'reports', 'budgets',
    'tickets', 'assets', 'incidents', 'changes', 'configurations', 'monitors', 'alerts',
    'deployments', 'pipelines', 'builds', 'releases', 'containers', 'services', 'pods',
    'inventory', 'shipments', 'warehouses', 'carriers', 'routes', 'orders_fulfilled'
]

def fix_file(file_path):
    """Apply ALL possible fixes to a file"""
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    original = content
    
    # Fix ANY variable that's assigned from data[...] and then iterated without .values()
    for var_name in DB_VAR_NAMES:
        # Pattern 1: for X in var_name where var_name = data["..."]
        # Only fix if this variable is assigned from data in this file
        if f'{var_name} = data[' in content or f'{var_name} = data.get(' in content:
            # Fix list comprehensions
            content = re.sub(
                f'\\[row for row in {var_name} if',
                f'[row for row in {var_name}.values() if',
                content
            )
            content = re.sub(
                f'\\[(\w+) for \\1 in {var_name} if',
                f'[\\1 for \\1 in {var_name}.values() if',
                content
            )
            
            # Fix regular for loops - be careful to only match start of line patterns
            content = re.sub(
                f'for (\\w+) in {var_name}:',
                f'for \\1 in {var_name}.values():',
                content
            )
            
            # Fix generator expressions
            content = re.sub(
                f'\\((\w+) for \\1 in {var_name} if',
                f'(\\1 for \\1 in {var_name}.values() if',
                content
            )
    
    if content != original:
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    
    return False

def main():
    base = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench-1/tau/tau_bench/envs")
    all_py_files = list(base.rglob("*.py"))
    
    print(f"Fixing ALL iteration patterns in {len(all_py_files)} files...")
    print()
    
    fixed = 0
    for py_file in all_py_files:
        if fix_file(py_file):
            fixed += 1
    
    print(f"=" * 70)
    print(f"✅ Fixed {fixed} files with iteration issues")
    print(f"=" * 70)

if __name__ == "__main__":
    main()

