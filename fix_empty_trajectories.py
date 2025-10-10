#!/usr/bin/env python3
"""
Fix Pattern 2: Empty Trajectories (Initialization Failures)

This script tests each environment with empty trajectories to identify
and fix import errors, syntax errors, and missing components.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

# 18 environments with empty trajectory issues
EMPTY_TRAJECTORY_ENVS = [
    "airline_2",
    "banking_services_6",
    "consulting_accounting_5",
    "dev_ops_1",
    "dev_ops_2",
    "digital_commerce_3",
    "figma_gmail_mcp_pipeline_4",
    "it_help_desk_5",
    "project_management_1",
    "project_management_5",
    "real_estate_sales_7",
    "recipes_4",
    "retail_1",
    "retail_4",
    "retail_point_of_sale_and_inventory_system_4",
    "retail_point_of_sale_and_inventory_system_5",
    "retail_point_of_sale_and_inventory_system_6",
    "social_media_advertising_5",
]

TAU_BASE = Path("tau/tau_bench/envs")


def test_python_syntax(file_path: Path) -> Tuple[bool, str]:
    """Test if a Python file has syntax errors."""
    if not file_path.exists():
        return False, "File not found"
    
    try:
        result = subprocess.run(
            ['python3', '-m', 'py_compile', str(file_path)],
            capture_output=True,
            timeout=5,
            text=True
        )
        if result.returncode == 0:
            return True, "OK"
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)


def test_import_module(env_name: str, module_name: str) -> Tuple[bool, str]:
    """Test if a module can be imported."""
    try:
        result = subprocess.run(
            ['python3', '-c', f'import sys; sys.path.insert(0, "."); from tau_bench.envs.{env_name} import {module_name}'],
            cwd='tau',
            capture_output=True,
            timeout=10,
            text=True
        )
        if result.returncode == 0:
            return True, "OK"
        else:
            error = result.stderr.strip()
            # Extract the most relevant error line
            if error:
                lines = error.split('\n')
                for line in reversed(lines):
                    if 'Error' in line or 'cannot import' in line or 'No module' in line:
                        return False, line
                return False, error[-200:] if len(error) > 200 else error
            return False, "Unknown import error"
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)


def test_env_load(env_name: str) -> Tuple[bool, str]:
    """Test if environment can be loaded via get_env()."""
    try:
        result = subprocess.run(
            ['python3', '-c', f'from tau_bench.envs import get_env; env = get_env("{env_name}", None, None, None, None, None)'],
            cwd='tau',
            capture_output=True,
            timeout=10,
            text=True
        )
        if result.returncode == 0:
            return True, "Environment loads successfully"
        else:
            error = result.stderr.strip()
            if error:
                lines = error.split('\n')
                # Find the most relevant error
                for line in reversed(lines):
                    if any(keyword in line for keyword in ['Error', 'cannot import', 'No module', 'undefined', 'not defined']):
                        return False, line
                return False, error[-300:] if len(error) > 300 else error
            return False, "Unknown error"
    except subprocess.TimeoutExpired:
        return False, "Timeout during environment load"
    except Exception as e:
        return False, str(e)


def check_environment(env_name: str) -> Dict:
    """Comprehensively check an environment."""
    print(f"\n{'='*80}")
    print(f"🔍 Checking: {env_name}")
    print(f"{'='*80}")
    
    env_path = TAU_BASE / env_name
    result = {
        'env_name': env_name,
        'exists': env_path.exists(),
        'checks': {},
        'issues': [],
        'status': 'unknown'
    }
    
    if not env_path.exists():
        result['status'] = 'missing'
        result['issues'].append('Environment directory not found')
        print(f"❌ Environment directory not found: {env_path}")
        return result
    
    # Check file structure
    files_to_check = ['__init__.py', 'env.py', 'tasks_test.py']
    has_tools_py = (env_path / 'tools.py').exists()
    has_tools_dir = (env_path / 'tools').exists() and (env_path / 'tools').is_dir()
    
    if not has_tools_py and not has_tools_dir:
        result['issues'].append('No tools.py or tools/ directory found')
        print(f"⚠️  No tools.py or tools/ directory")
    
    # Check syntax for key files
    for file_name in files_to_check:
        file_path = env_path / file_name
        if file_path.exists():
            success, msg = test_python_syntax(file_path)
            result['checks'][file_name] = {'syntax': success, 'message': msg}
            if success:
                print(f"  ✅ {file_name}: Syntax OK")
            else:
                print(f"  ❌ {file_name}: Syntax Error")
                print(f"     {msg[:100]}")
                result['issues'].append(f'{file_name}: {msg[:100]}')
    
    # Check tools.py syntax if it exists
    if has_tools_py:
        success, msg = test_python_syntax(env_path / 'tools.py')
        result['checks']['tools.py'] = {'syntax': success, 'message': msg}
        if success:
            print(f"  ✅ tools.py: Syntax OK")
        else:
            print(f"  ❌ tools.py: Syntax Error")
            print(f"     {msg[:100]}")
            result['issues'].append(f'tools.py: {msg[:100]}')
    
    # Test imports
    for module in ['env', 'tools']:
        success, msg = test_import_module(env_name, module)
        result['checks'][f'import_{module}'] = {'success': success, 'message': msg}
        if success:
            print(f"  ✅ import {module}: OK")
        else:
            print(f"  ❌ import {module}: Failed")
            print(f"     {msg[:150]}")
            result['issues'].append(f'import {module}: {msg[:150]}')
    
    # Test environment load
    success, msg = test_env_load(env_name)
    result['checks']['env_load'] = {'success': success, 'message': msg}
    if success:
        print(f"  ✅ Environment load: OK")
        result['status'] = 'working'
    else:
        print(f"  ❌ Environment load: Failed")
        print(f"     {msg[:150]}")
        result['issues'].append(f'env_load: {msg[:150]}')
        result['status'] = 'broken'
    
    return result


def main():
    print("=" * 80)
    print("🔧 FIX PATTERN 2: Empty Trajectories (Initialization Failures)")
    print("=" * 80)
    print()
    print(f"Testing {len(EMPTY_TRAJECTORY_ENVS)} environments...")
    print()
    
    results = []
    
    for env_name in EMPTY_TRAJECTORY_ENVS:
        result = check_environment(env_name)
        results.append(result)
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 SUMMARY")
    print("=" * 80)
    print()
    
    working = [r for r in results if r['status'] == 'working']
    broken = [r for r in results if r['status'] == 'broken']
    missing = [r for r in results if r['status'] == 'missing']
    
    print(f"✅ Working:  {len(working)} environments")
    for r in working:
        print(f"   • {r['env_name']}")
    print()
    
    print(f"❌ Broken:   {len(broken)} environments")
    for r in broken:
        print(f"   • {r['env_name']}")
        if r['issues']:
            for issue in r['issues'][:2]:
                print(f"     - {issue[:80]}")
    print()
    
    if missing:
        print(f"⚠️  Missing:  {len(missing)} environments")
        for r in missing:
            print(f"   • {r['env_name']}")
        print()
    
    # Categorize issues
    print("=" * 80)
    print("🔍 ISSUE CATEGORIES")
    print("=" * 80)
    print()
    
    import_errors = []
    syntax_errors = []
    other_errors = []
    
    for r in broken:
        for issue in r['issues']:
            if 'import' in issue.lower() or 'no module' in issue.lower():
                import_errors.append((r['env_name'], issue))
            elif 'syntax' in issue.lower():
                syntax_errors.append((r['env_name'], issue))
            else:
                other_errors.append((r['env_name'], issue))
    
    if import_errors:
        print(f"📦 Import Errors: {len(import_errors)}")
        for env, issue in import_errors[:5]:
            print(f"   • {env}: {issue[:100]}")
        if len(import_errors) > 5:
            print(f"   ... and {len(import_errors) - 5} more")
        print()
    
    if syntax_errors:
        print(f"⚠️  Syntax Errors: {len(syntax_errors)}")
        for env, issue in syntax_errors[:5]:
            print(f"   • {env}: {issue[:100]}")
        if len(syntax_errors) > 5:
            print(f"   ... and {len(syntax_errors) - 5} more")
        print()
    
    if other_errors:
        print(f"❓ Other Errors: {len(other_errors)}")
        for env, issue in other_errors[:5]:
            print(f"   • {env}: {issue[:100]}")
        if len(other_errors) > 5:
            print(f"   ... and {len(other_errors) - 5} more")
        print()
    
    # Next steps
    print("=" * 80)
    print("🎯 NEXT STEPS")
    print("=" * 80)
    print()
    
    if working:
        print("✅ Some environments are already working!")
        print("   These may have been fixed by previous changes.")
        print()
    
    if broken:
        print(f"🔧 Fix the {len(broken)} broken environments:")
        print()
        for r in broken[:3]:
            print(f"   {r['env_name']}:")
            if r['issues']:
                main_issue = r['issues'][0]
                print(f"      Issue: {main_issue[:120]}")
                print(f"      Command: ./investigate_failure.sh {r['env_name']}")
            print()
        
        if len(broken) > 3:
            print(f"   ... and {len(broken) - 3} more environments")
        print()
    
    print("=" * 80)
    
    return len(working), len(broken)


if __name__ == "__main__":
    working, broken = main()
    sys.exit(0 if broken == 0 else 1)

