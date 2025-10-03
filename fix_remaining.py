#!/usr/bin/env python3
"""Fix the final 16 remaining issues."""

import shutil
from pathlib import Path


def rename_sports_analytics_directory():
    """Rename sports-analytics to sports_analytics for proper Python imports."""
    old_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains/sports-analytics")
    new_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains/sports_analytics")
    
    if old_path.exists() and not new_path.exists():
        old_path.rename(new_path)
        print(f"✓ Renamed sports-analytics → sports_analytics")
        return True
    return False


def restore_broken_files():
    """Restore files that got broken by the conversion script."""
    domains_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains")
    
    broken_files = [
        "consulting_accounting/variations/variation_5/tasks_test.py",
        "github_mcp/variations/variation_2/tasks_test.py",
        "project_management/variations/variation_4/tasks_test.py",
        "rbac/variations/variation_1/tasks_test.py",
        "social_media_advertising/variations/variation_3/tasks_test.py",
        "banking_services/variations/variation_2/tasks_test.py",
        "file_system/variations/variation_1/tasks_test.py",
    ]
    
    restored = 0
    for file_path_str in broken_files:
        file_path = domains_path / file_path_str
        backup_v3 = file_path.with_suffix('.py.backup3')
        backup_fix = file_path.with_suffix('.py.backup_fix')
        
        # Try to restore from the oldest good backup
        if backup_v3.exists():
            shutil.copy2(backup_v3, file_path)
            restored += 1
            print(f"  ✓ Restored {file_path_str} from backup3")
        elif backup_fix.exists():
            shutil.copy2(backup_fix, file_path)
            restored += 1
            print(f"  ✓ Restored {file_path_str} from backup_fix")
    
    return restored


def fix_career_planner_tasks():
    """Fix career_planner variations with init issues."""
    domains_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains")
    
    for var in ['variation_4', 'variation_5']:
        tasks_file = domains_path / f"career_planner/variations/{var}/tasks_test.py"
        backup = tasks_file.with_suffix('.py.backup3')
        
        if backup.exists():
            shutil.copy2(backup, tasks_file)
            print(f"  ✓ Restored career_planner/{var}/tasks_test.py")


def fix_rbac_variation_4():
    """Fix rbac/variation_4 init issue."""
    domains_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains")
    tasks_file = domains_path / "rbac/variations/variation_4/tasks_test.py"
    backup = tasks_file.with_suffix('.py.backup3')
    
    if backup.exists():
        shutil.copy2(backup, tasks_file)
        print(f"  ✓ Restored rbac/variation_4/tasks_test.py")


def check_github_mcp_variation_7():
    """Check github_mcp/variation_7 structure."""
    domains_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains")
    var_path = domains_path / "github_mcp/variations/variation_7"
    
    # Check if tools.py exists
    if not (var_path / "tools.py").exists():
        print(f"  ! github_mcp/variation_7 has no tools.py file")
        # Check what files exist
        if (var_path / "tools").exists():
            print(f"    Files in tools/: {list((var_path / 'tools').glob('*.py'))[:5]}")
        return False
    return True


def main():
    print("="*70)
    print("FIXING REMAINING 16 ISSUES")
    print("="*70 + "\n")
    
    # Fix 1: Rename sports-analytics directory
    print("Fix 1: Rename sports-analytics directory...")
    if rename_sports_analytics_directory():
        print()
    else:
        print("  - Already renamed or doesn't exist\n")
    
    # Fix 2: Restore broken files
    print("Fix 2: Restore files broken by conversion script...")
    restored = restore_broken_files()
    print(f"  Restored {restored} files\n")
    
    # Fix 3: Fix career_planner init issues
    print("Fix 3: Fix career_planner variations...")
    fix_career_planner_tasks()
    print()
    
    # Fix 4: Fix rbac/variation_4
    print("Fix 4: Fix rbac/variation_4...")
    fix_rbac_variation_4()
    print()
    
    # Fix 5: Check github_mcp/variation_7
    print("Fix 5: Check github_mcp/variation_7...")
    check_github_mcp_variation_7()
    print()
    
    print("="*70)
    print("FIXES COMPLETE - Run test_all_envs.py again!")
    print("="*70)


if __name__ == "__main__":
    main()

