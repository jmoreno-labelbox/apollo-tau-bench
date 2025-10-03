#!/usr/bin/env python3
"""
Script to convert task outputs from dict to list format for Pydantic compatibility.

This changes outputs={...} to outputs=[] in all tasks_test.py files.
"""

import os
import shutil
from pathlib import Path
import re


def backup_file(file_path: Path) -> Path:
    """Create a backup of the file."""
    backup_path = file_path.with_suffix('.py.backup')
    shutil.copy2(file_path, backup_path)
    return backup_path


def convert_outputs_to_list(content: str) -> tuple[str, int]:
    """
    Convert outputs={...} to outputs=[] in task definitions.
    Returns (modified_content, number_of_changes)
    """
    # Pattern to match outputs={...} including nested braces
    # This matches from outputs={ to the closing }, handling nested content
    pattern = r'outputs=\{[^}]*(?:\{[^}]*\}[^}]*)*\}'
    
    # Count how many matches
    matches = re.findall(pattern, content, re.DOTALL)
    
    # Replace all matches with outputs=[]
    new_content = re.sub(pattern, 'outputs=[]', content, flags=re.DOTALL)
    
    return new_content, len(matches)


def process_tasks_file(file_path: Path, dry_run: bool = True) -> dict:
    """
    Process a single tasks_test.py file.
    
    Args:
        file_path: Path to the tasks_test.py file
        dry_run: If True, don't actually modify files
    
    Returns:
        Dict with processing info
    """
    with open(file_path, 'r') as f:
        original_content = f.read()
    
    # Convert outputs
    new_content, num_changes = convert_outputs_to_list(original_content)
    
    result = {
        'file': str(file_path.relative_to(Path.cwd())),
        'changes': num_changes,
        'modified': False
    }
    
    if num_changes > 0 and not dry_run:
        # Create backup
        backup_path = backup_file(file_path)
        result['backup'] = str(backup_path.relative_to(Path.cwd()))
        
        # Write modified content
        with open(file_path, 'w') as f:
            f.write(new_content)
        
        result['modified'] = True
    
    return result


def main():
    """Main function to process all tasks_test.py files."""
    domains_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains")
    
    # Find all tasks_test.py files
    tasks_files = list(domains_path.glob("*/variations/*/tasks_test.py"))
    
    print(f"Found {len(tasks_files)} tasks_test.py files\n")
    
    # First pass: dry run to show what will change
    print("="*70)
    print("DRY RUN - Analyzing files...")
    print("="*70)
    
    results = []
    total_changes = 0
    
    for tasks_file in sorted(tasks_files):
        result = process_tasks_file(tasks_file, dry_run=True)
        results.append(result)
        
        if result['changes'] > 0:
            total_changes += result['changes']
            print(f"✓ {result['file']}: {result['changes']} task(s) to convert")
    
    print(f"\n{'='*70}")
    print(f"SUMMARY: {total_changes} total task outputs will be converted")
    print(f"{'='*70}\n")
    
    if total_changes == 0:
        print("No changes needed!")
        return
    
    # Auto-proceed (backups will be created)
    print("Proceeding with conversion (backups will be created)...")
    
    # Second pass: actually modify files
    print(f"\n{'='*70}")
    print("Converting files...")
    print(f"{'='*70}\n")
    
    modified_count = 0
    backup_count = 0
    
    for tasks_file in sorted(tasks_files):
        result = process_tasks_file(tasks_file, dry_run=False)
        
        if result['modified']:
            modified_count += 1
            backup_count += 1
            print(f"✓ Modified: {result['file']}")
            print(f"  Backup: {result['backup']}")
    
    print(f"\n{'='*70}")
    print("COMPLETE")
    print(f"{'='*70}")
    print(f"Files modified: {modified_count}")
    print(f"Backups created: {backup_count}")
    print(f"\nBackup files have .backup extension")
    print(f"To restore: mv file.py.backup file.py")


if __name__ == "__main__":
    main()

