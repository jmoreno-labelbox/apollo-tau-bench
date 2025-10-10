#!/usr/bin/env python3
"""
Fix Pattern 4 (Undefined Variables) and Pattern 5 (Logic Bugs)

Pattern 4: Add missing helper functions/variables (4 environments)
Pattern 5: Fix logic bugs (1 environment)
"""

import os
import sys
from pathlib import Path

TAU_BASE = Path("tau/tau_bench/envs")


def fix_data_science_3():
    """Fix: Add _fixed_now_iso() function"""
    env_name = "data_science_3"
    print(f"\n{'='*80}")
    print(f"🔧 Fixing: {env_name}")
    print(f"{'='*80}")
    print("Issue: name '_fixed_now_iso' is not defined")
    print("Fix: Add datetime helper function")
    
    # Check if it's modular tools
    tools_dir = TAU_BASE / env_name / "tools"
    if tools_dir.exists():
        # Add to __init__.py or individual tool files
        init_file = tools_dir / "__init__.py"
        if init_file.exists():
            with open(init_file, 'r') as f:
                content = f.read()
            
            if '_fixed_now_iso' not in content:
                # Add import and function
                helper_code = '''
from datetime import datetime

def _fixed_now_iso():
    """Return current time in ISO format."""
    return datetime.now().isoformat()
'''
                # Insert after imports
                lines = content.split('\n')
                insert_idx = 0
                for i, line in enumerate(lines):
                    if line.startswith('import ') or line.startswith('from '):
                        insert_idx = i + 1
                
                lines.insert(insert_idx, helper_code)
                new_content = '\n'.join(lines)
                
                # Backup and write
                with open(str(init_file) + '.backup', 'w') as f:
                    f.write(content)
                with open(init_file, 'w') as f:
                    f.write(new_content)
                
                print("✅ Added _fixed_now_iso() to tools/__init__.py")
                return True
    else:
        # Single tools.py file
        tools_file = TAU_BASE / env_name / "tools.py"
        if tools_file.exists():
            with open(tools_file, 'r') as f:
                content = f.read()
            
            if '_fixed_now_iso' not in content:
                # Add function at top after imports
                helper_code = '''
def _fixed_now_iso():
    """Return current time in ISO format."""
    from datetime import datetime
    return datetime.now().isoformat()
'''
                # Insert after imports
                lines = content.split('\n')
                insert_idx = 0
                for i, line in enumerate(lines):
                    if line.startswith('import ') or line.startswith('from '):
                        insert_idx = i + 1
                
                lines.insert(insert_idx, helper_code)
                new_content = '\n'.join(lines)
                
                # Backup and write
                with open(str(tools_file) + '.backup', 'w') as f:
                    f.write(content)
                with open(tools_file, 'w') as f:
                    f.write(new_content)
                
                print("✅ Added _fixed_now_iso() to tools.py")
                return True
    
    print("⚠️  Could not locate tools file")
    return False


def fix_banking_services_5():
    """Fix: Add get_next_account_id() function"""
    env_name = "banking_services_5"
    print(f"\n{'='*80}")
    print(f"🔧 Fixing: {env_name}")
    print(f"{'='*80}")
    print("Issue: name 'get_next_account_id' is not defined")
    print("Fix: Add ID generation helper function")
    
    tools_dir = TAU_BASE / env_name / "tools"
    helper_code = '''
def get_next_account_id(data, account_type='checking'):
    """Generate next account ID."""
    accounts = data.get('accounts', {})
    max_id = 0
    for acc_id in accounts.keys():
        if account_type in acc_id:
            try:
                num = int(acc_id.split('_')[-1])
                max_id = max(max_id, num)
            except (ValueError, IndexError):
                pass
    return f"acc_{account_type}_{max_id + 1}"
'''
    
    if tools_dir.exists():
        init_file = tools_dir / "__init__.py"
        if init_file.exists():
            with open(init_file, 'r') as f:
                content = f.read()
            
            if 'get_next_account_id' not in content:
                lines = content.split('\n')
                insert_idx = 0
                for i, line in enumerate(lines):
                    if line.startswith('import ') or line.startswith('from '):
                        insert_idx = i + 1
                
                lines.insert(insert_idx, helper_code)
                new_content = '\n'.join(lines)
                
                with open(str(init_file) + '.backup', 'w') as f:
                    f.write(content)
                with open(init_file, 'w') as f:
                    f.write(new_content)
                
                print("✅ Added get_next_account_id() to tools/__init__.py")
                return True
    else:
        tools_file = TAU_BASE / env_name / "tools.py"
        if tools_file.exists():
            with open(tools_file, 'r') as f:
                content = f.read()
            
            if 'get_next_account_id' not in content:
                lines = content.split('\n')
                insert_idx = 0
                for i, line in enumerate(lines):
                    if line.startswith('import ') or line.startswith('from '):
                        insert_idx = i + 1
                
                lines.insert(insert_idx, helper_code)
                new_content = '\n'.join(lines)
                
                with open(str(tools_file) + '.backup', 'w') as f:
                    f.write(content)
                with open(tools_file, 'w') as f:
                    f.write(new_content)
                
                print("✅ Added get_next_account_id() to tools.py")
                return True
    
    print("⚠️  Could not locate tools file")
    return False


def fix_dev_ops_6():
    """Fix: Initialize _table variable"""
    env_name = "dev_ops_6"
    print(f"\n{'='*80}")
    print(f"🔧 Fixing: {env_name}")
    print(f"{'='*80}")
    print("Issue: name '_table' is not defined")
    print("Fix: Initialize _table variable")
    
    tools_dir = TAU_BASE / env_name / "tools"
    init_code = '\n_table = {}  # Global table storage\n'
    
    if tools_dir.exists():
        init_file = tools_dir / "__init__.py"
        if init_file.exists():
            with open(init_file, 'r') as f:
                content = f.read()
            
            if '_table' not in content:
                lines = content.split('\n')
                # Add after imports
                insert_idx = 0
                for i, line in enumerate(lines):
                    if line.startswith('import ') or line.startswith('from '):
                        insert_idx = i + 1
                
                lines.insert(insert_idx, init_code)
                new_content = '\n'.join(lines)
                
                with open(str(init_file) + '.backup', 'w') as f:
                    f.write(content)
                with open(init_file, 'w') as f:
                    f.write(new_content)
                
                print("✅ Added _table = {} to tools/__init__.py")
                return True
    else:
        tools_file = TAU_BASE / env_name / "tools.py"
        if tools_file.exists():
            with open(tools_file, 'r') as f:
                content = f.read()
            
            if '_table' not in content:
                lines = content.split('\n')
                insert_idx = 0
                for i, line in enumerate(lines):
                    if line.startswith('import ') or line.startswith('from '):
                        insert_idx = i + 1
                
                lines.insert(insert_idx, init_code)
                new_content = '\n'.join(lines)
                
                with open(str(tools_file) + '.backup', 'w') as f:
                    f.write(content)
                with open(tools_file, 'w') as f:
                    f.write(new_content)
                
                print("✅ Added _table = {} to tools.py")
                return True
    
    print("⚠️  Could not locate tools file")
    return False


def fix_recipes_3():
    """Fix: Add _json import/variable"""
    env_name = "recipes_3"
    print(f"\n{'='*80}")
    print(f"🔧 Fixing: {env_name}")
    print(f"{'='*80}")
    print("Issue: name '_json' is not defined")
    print("Fix: Add json import or initialize _json variable")
    
    tools_dir = TAU_BASE / env_name / "tools"
    
    if tools_dir.exists():
        init_file = tools_dir / "__init__.py"
        if init_file.exists():
            with open(init_file, 'r') as f:
                content = f.read()
            
            # Check if it's trying to use json module as _json
            if '_json' in content and 'import json' not in content:
                # Add import json
                lines = content.split('\n')
                lines.insert(0, 'import json')
                new_content = '\n'.join(lines)
                
                with open(str(init_file) + '.backup', 'w') as f:
                    f.write(content)
                with open(init_file, 'w') as f:
                    f.write(new_content)
                
                print("✅ Added 'import json' to tools/__init__.py")
                return True
            elif 'import json' not in content:
                lines = content.split('\n')
                lines.insert(0, 'import json')
                new_content = '\n'.join(lines)
                
                with open(str(init_file) + '.backup', 'w') as f:
                    f.write(content)
                with open(init_file, 'w') as f:
                    f.write(new_content)
                
                print("✅ Added 'import json' to tools/__init__.py")
                return True
    else:
        tools_file = TAU_BASE / env_name / "tools.py"
        if tools_file.exists():
            with open(tools_file, 'r') as f:
                content = f.read()
            
            if 'import json' not in content:
                lines = content.split('\n')
                lines.insert(0, 'import json')
                new_content = '\n'.join(lines)
                
                with open(str(tools_file) + '.backup', 'w') as f:
                    f.write(content)
                with open(tools_file, 'w') as f:
                    f.write(new_content)
                
                print("✅ Added 'import json' to tools.py")
                return True
    
    print("⚠️  Could not locate tools file or already has json import")
    return False


def fix_airline():
    """Fix Pattern 5: Payment validation logic bug"""
    env_name = "airline"
    print(f"\n{'='*80}")
    print(f"🔧 Fixing: {env_name} (Pattern 5 - Logic Bug)")
    print(f"{'='*80}")
    print("Issue: Payment validation incorrectly includes insurance cost")
    print("Fix: Only add insurance cost when explicitly requested")
    print("⚠️  This requires manual review of payment validation logic")
    print("    File: tau/tau_bench/envs/airline/tools.py")
    print("    Look for: payment validation that always adds insurance")
    return False  # Manual fix required


def main():
    print("=" * 80)
    print("🔧 FIX PATTERN 4 (Undefined Variables) & PATTERN 5 (Logic Bugs)")
    print("=" * 80)
    print()
    
    results = {}
    
    # Pattern 4 fixes
    print("\n🟡 PATTERN 4: Undefined Variables (4 environments)")
    print("=" * 80)
    
    results['data_science_3'] = fix_data_science_3()
    results['banking_services_5'] = fix_banking_services_5()
    results['dev_ops_6'] = fix_dev_ops_6()
    results['recipes_3'] = fix_recipes_3()
    
    # Pattern 5 fix
    print("\n🟢 PATTERN 5: Logic Bugs (1 environment)")
    print("=" * 80)
    results['airline'] = fix_airline()
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 SUMMARY")
    print("=" * 80)
    print()
    
    fixed = [k for k, v in results.items() if v]
    manual = [k for k, v in results.items() if not v]
    
    print(f"✅ Automatically fixed: {len(fixed)} environments")
    for env in fixed:
        print(f"   • {env}")
    print()
    
    if manual:
        print(f"📋 Requires manual fix: {len(manual)} environments")
        for env in manual:
            print(f"   • {env}")
        print()
    
    print("=" * 80)
    print("🎯 NEXT STEPS")
    print("=" * 80)
    print()
    print("1. Test the fixed environments:")
    if fixed:
        print(f"   cd tau && PYTHONPATH=. python3 run.py --env {fixed[0]} --end-index 1")
    print()
    print("2. Run error analysis:")
    envs_str = ' '.join(fixed[:3])
    print(f"   python3 run_error_analysis_all_envs.py --run-tests --envs {envs_str}")
    print()
    print("3. Manual fixes:")
    print("   • airline: Review tau/tau_bench/envs/airline/tools.py")
    print("     Look for payment validation logic")
    print()
    print("=" * 80)
    
    return len(fixed)


if __name__ == "__main__":
    fixed_count = main()
    sys.exit(0 if fixed_count > 0 else 1)

