#!/usr/bin/env python3
"""
Automatically fix Pattern 1: 'str' object has no attribute 'get' errors.

This script identifies and fixes the common bug where code iterates over
dictionary keys instead of values, causing 'str' object errors.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

# List of 19 environments with Pattern 1 errors
PATTERN1_ENVS = [
    "consulting_accounting_1",
    "consulting_accounting_4",
    "data_science_2",
    "data_science_5",
    "dev_ops_5",
    "digital_commerce_2",
    "figma_gmail_mcp_pipeline_2",
    "file_system_9",
    "logistics_supply_chain_5",
    "new_hire_mcp_3",
    "project_management_2",
    "rbac_2",
    "real_estate_sales_1",
    "real_estate_sales_4",
    "recipes_1",
    "retail_3",
    "social_media_advertising_2",
    "sports_analytics_2",
    "sports_analytics_3",
]

TAU_BASE = Path("tau/tau_bench/envs")


def find_dict_iterations(content, filename):
    """Find problematic dictionary iterations in code."""
    issues = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Pattern: for X in data['key'] or for X in data.get('key')
        # Without .values()
        patterns = [
            r'for\s+(\w+)\s+in\s+data\[([\'"][^\'"]+[\'"]\)\]',  # data['key']
            r'for\s+(\w+)\s+in\s+data\.get\(([\'"][^\'"]+[\'"])[^\)]*\)',  # data.get('key')
            r'for\s+(\w+)\s+in\s+(\w+)\[([\'"][^\'"]+[\'"]\)\]',  # var['key']
            r'for\s+(\w+)\s+in\s+(\w+)\.get\(([\'"][^\'"]+[\'"])[^\)]*\)',  # var.get('key')
        ]
        
        for pattern in patterns:
            match = re.search(pattern, line)
            if match and '.values()' not in line and 'list(' not in line:
                # Check if this might be iterating over keys
                # Look for .get() usage on the iteration variable in nearby lines
                var_name = match.group(1)
                
                # Check next 10 lines for var.get() usage
                for j in range(i, min(i + 10, len(lines))):
                    if f'{var_name}.get(' in lines[j] or f'{var_name}[' in lines[j]:
                        issues.append({
                            'line_num': i,
                            'line': line,
                            'var': var_name,
                            'issue': 'Missing .values() - likely iterating over keys'
                        })
                        break
    
    return issues


def fix_dict_iteration(content):
    """Fix dictionary iteration issues."""
    lines = content.split('\n')
    fixed_lines = []
    changes = []
    
    for i, line in enumerate(lines, 1):
        original_line = line
        
        # Fix pattern: for X in data['key']: -> for X in data['key'].values():
        # But only if not already using .values() or list()
        if 'for ' in line and ' in ' in line and '.values()' not in line and 'list(' not in line:
            # Check if this looks like dict iteration
            var_match = re.search(r'for\s+(\w+)\s+in\s+', line)
            if var_match:
                var_name = var_match.group(1)
                
                # Check if next few lines use .get() on this variable
                has_get_usage = False
                for j in range(i, min(i + 10, len(lines))):
                    if f'{var_name}.get(' in lines[j] or f'{var_name}["' in lines[j] or f"{var_name}['" in lines[j]:
                        has_get_usage = True
                        break
                
                if has_get_usage:
                    # Apply fixes
                    # Pattern 1: data['key'] -> data['key'].values()
                    new_line = re.sub(
                        r'(for\s+\w+\s+in\s+data\[[\'"][^\'"]+[\'"])\](\s*:)',
                        r'\1].values()\2',
                        line
                    )
                    
                    # Pattern 2: data.get('key') -> data.get('key').values()
                    if new_line == line:
                        new_line = re.sub(
                            r'(for\s+\w+\s+in\s+data\.get\([^)]+\))(\s*:)',
                            r'\1.values()\2',
                            line
                        )
                    
                    # Pattern 3: var['key'] -> var['key'].values()
                    if new_line == line:
                        new_line = re.sub(
                            r'(for\s+\w+\s+in\s+\w+\[[\'"][^\'"]+[\'"])\](\s*:)',
                            r'\1].values()\2',
                            line
                        )
                    
                    # Pattern 4: var.get('key') -> var.get('key').values()
                    if new_line == line:
                        new_line = re.sub(
                            r'(for\s+\w+\s+in\s+\w+\.get\([^)]+\))(\s*:)',
                            r'\1.values()\2',
                            line
                        )
                    
                    if new_line != line:
                        changes.append({
                            'line_num': i,
                            'old': line,
                            'new': new_line
                        })
                        line = new_line
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), changes


def test_environment(env_name):
    """Test if an environment loads successfully."""
    try:
        result = subprocess.run(
            ['python3', '-c', f'from tau_bench.envs import get_env; get_env("{env_name}")'],
            cwd='tau',
            capture_output=True,
            timeout=10,
            text=True
        )
        return result.returncode == 0, result.stderr
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)


def main():
    print("=" * 80)
    print("🔧 AUTO-FIX PATTERN 1: 'str' object has no attribute 'get'")
    print("=" * 80)
    print()
    print(f"Processing {len(PATTERN1_ENVS)} environments...")
    print()
    
    results = {
        'fixed': [],
        'already_ok': [],
        'failed': []
    }
    
    for env_name in PATTERN1_ENVS:
        print(f"📦 Processing: {env_name}")
        
        tools_path = TAU_BASE / env_name / "tools.py"
        
        if not tools_path.exists():
            print(f"   ⚠️  tools.py not found, checking tools/ directory...")
            tools_dir = TAU_BASE / env_name / "tools"
            if tools_dir.exists() and tools_dir.is_dir():
                print(f"   ℹ️  Has modular tools/ directory - skipping")
                results['already_ok'].append(env_name)
                continue
            else:
                print(f"   ❌ No tools.py or tools/ found")
                results['failed'].append((env_name, "No tools.py found"))
                continue
        
        # Read current content
        with open(tools_path, 'r') as f:
            original_content = f.read()
        
        # Find issues
        issues = find_dict_iterations(original_content, str(tools_path))
        
        if not issues:
            print(f"   ✅ No issues found (already fixed or different pattern)")
            results['already_ok'].append(env_name)
            continue
        
        print(f"   🔍 Found {len(issues)} potential issue(s)")
        
        # Apply fixes
        fixed_content, changes = fix_dict_iteration(original_content)
        
        if not changes:
            print(f"   ℹ️  No automatic fixes applied")
            results['already_ok'].append(env_name)
            continue
        
        print(f"   🔧 Applying {len(changes)} fix(es):")
        for change in changes[:3]:  # Show first 3 changes
            print(f"      Line {change['line_num']}:")
            print(f"        - {change['old'].strip()}")
            print(f"        + {change['new'].strip()}")
        if len(changes) > 3:
            print(f"      ... and {len(changes) - 3} more")
        
        # Backup original
        backup_path = tools_path.with_suffix('.py.backup_pattern1')
        with open(backup_path, 'w') as f:
            f.write(original_content)
        
        # Write fixed content
        with open(tools_path, 'w') as f:
            f.write(fixed_content)
        
        # Test if environment loads
        print(f"   🧪 Testing environment load...")
        success, error = test_environment(env_name)
        
        if success:
            print(f"   ✅ Fix successful! Environment loads correctly")
            results['fixed'].append(env_name)
        else:
            print(f"   ⚠️  Environment still has issues (may need manual fix)")
            print(f"      Error: {error[:100]}")
            results['failed'].append((env_name, error[:100]))
            
            # Restore backup if test fails
            print(f"   ↩️  Restoring backup...")
            with open(backup_path, 'r') as f:
                original = f.read()
            with open(tools_path, 'w') as f:
                f.write(original)
        
        print()
    
    # Summary
    print("=" * 80)
    print("📊 SUMMARY")
    print("=" * 80)
    print()
    print(f"✅ Successfully fixed:  {len(results['fixed'])} environments")
    if results['fixed']:
        for env in results['fixed']:
            print(f"   • {env}")
    print()
    
    print(f"✓  Already OK:          {len(results['already_ok'])} environments")
    if results['already_ok'][:5]:
        for env in results['already_ok'][:5]:
            print(f"   • {env}")
        if len(results['already_ok']) > 5:
            print(f"   ... and {len(results['already_ok']) - 5} more")
    print()
    
    print(f"❌ Failed/Needs manual: {len(results['failed'])} environments")
    if results['failed']:
        for env, error in results['failed']:
            print(f"   • {env}: {error}")
    print()
    
    print("=" * 80)
    print("🎯 NEXT STEPS")
    print("=" * 80)
    print()
    
    if results['fixed']:
        print("1. Test the fixed environments:")
        print(f"   cd tau && PYTHONPATH=. python3 run.py --env {results['fixed'][0]} --end-index 1")
        print()
        print("2. Run error analysis:")
        print(f"   python3 run_error_analysis_all_envs.py --run-tests --envs {' '.join(results['fixed'][:3])}")
        print()
    
    if results['failed']:
        print("3. Manually investigate failures:")
        for env, _ in results['failed'][:3]:
            print(f"   ./investigate_failure.sh {env}")
        print()
    
    print("4. View all backups:")
    print("   find tau/tau_bench/envs -name '*.backup_pattern1'")
    print()
    
    return len(results['fixed'])


if __name__ == "__main__":
    sys.exit(0 if main() > 0 else 1)

