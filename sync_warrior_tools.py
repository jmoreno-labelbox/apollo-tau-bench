#!/usr/bin/env python3
"""
Script to sync tools.py files from domains_warrior to tau/tau_bench/envs

Maps:
  domains_warrior/<domain>/variations/variation_<N>/tools.py
  → tau/tau_bench/envs/<domain>_<N>/tools.py
"""

import os
import shutil
from pathlib import Path
from typing import List, Tuple


def find_warrior_tools() -> List[Tuple[Path, str, int]]:
    """
    Find all tools.py files in domains_warrior.
    
    Returns:
        List of (tools_path, domain, variation_number)
    """
    warrior_dir = Path("domains_warrior")
    tools_files = []
    
    if not warrior_dir.exists():
        print(f"❌ Error: {warrior_dir} directory not found!")
        return []
    
    # Iterate through each domain
    for domain_dir in warrior_dir.iterdir():
        if not domain_dir.is_dir():
            continue
        
        domain_name = domain_dir.name
        variations_dir = domain_dir / "variations"
        
        if not variations_dir.exists():
            continue
        
        # Iterate through variations
        for variation_dir in variations_dir.iterdir():
            if not variation_dir.is_dir():
                continue
            
            # Extract variation number (e.g., "variation_1" -> 1)
            if not variation_dir.name.startswith("variation_"):
                continue
            
            try:
                variation_num = int(variation_dir.name.split("_")[1])
            except (IndexError, ValueError):
                print(f"⚠️  Skipping {variation_dir}: invalid variation name")
                continue
            
            # Check if tools.py exists
            tools_path = variation_dir / "tools.py"
            if tools_path.exists():
                tools_files.append((tools_path, domain_name, variation_num))
    
    return tools_files


def get_target_path(domain: str, variation_num: int) -> Path:
    """
    Get the target path in tau/tau_bench/envs.
    
    Args:
        domain: Domain name (e.g., "banking_services")
        variation_num: Variation number (e.g., 6)
    
    Returns:
        Path to target tools.py
    """
    env_name = f"{domain}_{variation_num}"
    return Path(f"tau/tau_bench/envs/{env_name}/tools.py")


def sync_tools(dry_run: bool = True) -> None:
    """
    Sync tools.py files from domains_warrior to tau/tau_bench/envs.
    
    Args:
        dry_run: If True, only show what would be done without making changes
    """
    tools_files = find_warrior_tools()
    
    if not tools_files:
        print("No tools.py files found in domains_warrior")
        return
    
    print(f"Found {len(tools_files)} tools.py files in domains_warrior\n")
    
    copied = 0
    skipped = 0
    errors = []
    
    for source_path, domain, variation_num in sorted(tools_files):
        target_path = get_target_path(domain, variation_num)
        
        # Check if target directory exists
        if not target_path.parent.exists():
            print(f"⚠️  Skipping {domain}_{variation_num}: target directory doesn't exist")
            print(f"   Missing: {target_path.parent}")
            skipped += 1
            continue
        
        # Show what will be done
        status = "📋 WOULD COPY" if dry_run else "📝 COPYING"
        print(f"{status}: {source_path.relative_to('domains_warrior')}")
        print(f"         → {target_path}")
        
        if not dry_run:
            try:
                # Backup existing file
                if target_path.exists():
                    backup_path = target_path.with_suffix('.py.backup')
                    shutil.copy2(target_path, backup_path)
                    print(f"   💾 Backed up existing file to {backup_path.name}")
                
                # Copy the file
                shutil.copy2(source_path, target_path)
                print(f"   ✅ Copied successfully")
                copied += 1
            except Exception as e:
                error_msg = f"Error copying {source_path} to {target_path}: {e}"
                errors.append(error_msg)
                print(f"   ❌ {error_msg}")
        else:
            copied += 1
        
        print()
    
    # Summary
    print("=" * 60)
    if dry_run:
        print(f"DRY RUN SUMMARY:")
        print(f"  Would copy: {copied} files")
        print(f"  Would skip: {skipped} files (target dir missing)")
        print(f"\nTo actually perform the sync, run:")
        print(f"  python3 sync_warrior_tools.py --execute")
    else:
        print(f"SYNC COMPLETE:")
        print(f"  ✅ Copied: {copied} files")
        print(f"  ⚠️  Skipped: {skipped} files")
        if errors:
            print(f"  ❌ Errors: {len(errors)}")
            for error in errors:
                print(f"     - {error}")
    print("=" * 60)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Sync tools.py files from domains_warrior to tau/tau_bench/envs"
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually perform the sync (default is dry-run)"
    )
    parser.add_argument(
        "--domain",
        type=str,
        help="Only sync a specific domain (e.g., banking_services)"
    )
    
    args = parser.parse_args()
    
    if not args.execute:
        print("🔍 DRY RUN MODE - No files will be modified")
        print("   Use --execute to actually perform the sync\n")
    else:
        print("⚠️  EXECUTE MODE - Files will be modified!")
        print("   Existing files will be backed up with .backup extension\n")
    
    sync_tools(dry_run=not args.execute)


if __name__ == "__main__":
    main()

