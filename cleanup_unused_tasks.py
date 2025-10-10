#!/usr/bin/env python3
"""
Script to remove unused tasks.py files from tau/tau_bench/envs/

The runtime environment uses tasks_test.py files (with uppercase TASKS, Task/Action objects),
while tasks.py files are unused leftovers with the wrong format (lowercase tasks, plain dicts).

This script:
1. Finds all tasks.py files in tau/tau_bench/envs/*/
2. Verifies they're not imported by env.py
3. Deletes them
4. Reports what was deleted

Usage:
    python3 cleanup_unused_tasks.py            # Preview only (no deletion)
    python3 cleanup_unused_tasks.py --delete   # Actually delete the files
"""

import os
import sys
import argparse
from pathlib import Path


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Remove unused tasks.py files from tau/tau_bench/envs/")
    parser.add_argument("--delete", action="store_true", help="Actually delete the files (default is preview only)")
    args = parser.parse_args()
    
    # Base directory
    base_dir = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    if not base_dir.exists():
        print(f"❌ Error: Directory not found: {base_dir}")
        sys.exit(1)
    
    # Find all tasks.py files (but not tasks_test.py)
    tasks_files = list(base_dir.glob("*/tasks.py"))
    
    if not tasks_files:
        print("✅ No tasks.py files found to clean up!")
        return
    
    print(f"Found {len(tasks_files)} tasks.py files to remove\n")
    
    # Verify none are imported by checking env.py files
    print("🔍 Verifying tasks.py files are not imported...")
    for tasks_file in tasks_files:
        env_dir = tasks_file.parent
        env_file = env_dir / "env.py"
        
        if env_file.exists():
            content = env_file.read_text()
            # Check if it imports from tasks (not tasks_test)
            if "from tau_bench.envs." in content and ".tasks import" in content:
                # Extract the import line
                for line in content.split("\n"):
                    if ".tasks import" in line and "tasks_test" not in line:
                        print(f"⚠️  WARNING: {env_dir.name}/env.py imports from tasks.py!")
                        print(f"   Line: {line.strip()}")
                        response = input("   Continue anyway? (y/n): ")
                        if response.lower() != 'y':
                            print("❌ Aborted")
                            sys.exit(1)
    
    print("✅ Verification complete: No env.py files import tasks.py\n")
    
    # List files
    print("The following files will be DELETED:" if args.delete else "Found unused tasks.py files:")
    for tasks_file in sorted(tasks_files):
        print(f"  - {tasks_file.relative_to(base_dir.parent.parent)}")
    
    print(f"\nTotal: {len(tasks_files)} files")
    
    if not args.delete:
        print("\n📝 This is a PREVIEW. No files were deleted.")
        print("   To actually delete these files, run:")
        print("   python3 cleanup_unused_tasks.py --delete")
        return
    
    # Delete files
    print("\n🗑️  Deleting files...")
    deleted_count = 0
    errors = []
    
    for tasks_file in tasks_files:
        try:
            tasks_file.unlink()
            deleted_count += 1
            print(f"  ✓ Deleted: {tasks_file.relative_to(base_dir.parent.parent)}")
        except Exception as e:
            errors.append((tasks_file, e))
            print(f"  ✗ Error deleting {tasks_file.relative_to(base_dir.parent.parent)}: {e}")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"✅ Successfully deleted {deleted_count}/{len(tasks_files)} files")
    
    if errors:
        print(f"❌ Failed to delete {len(errors)} files:")
        for file, error in errors:
            print(f"  - {file.relative_to(base_dir.parent.parent)}: {error}")
    
    print(f"\n📝 Note: The runtime uses tasks_test.py files (already correct)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()

