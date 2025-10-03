#!/usr/bin/env python3
"""
Script to convert task outputs from dict to list format.
Simple and robust approach: track brace nesting.
"""

import shutil
from pathlib import Path


def convert_outputs_in_file(file_path: Path) -> tuple[str, int]:
    """
    Convert outputs={...} to outputs=[] by tracking brace nesting.
    Returns (modified_content, number_of_changes)
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    changes = 0
    in_outputs_dict = False
    brace_count = 0
    outputs_start_indent = 0
    
    for line in lines:
        stripped = line.lstrip()
        
        # Check if this line starts an outputs dict
        if stripped.startswith('outputs={') and not in_outputs_dict:
            # Calculate initial brace balance
            brace_count = line.count('{') - line.count('}')
            
            if brace_count == 0:
                # Single line dict - replace entire line
                indent = len(line) - len(stripped)
                new_lines.append(' ' * indent + 'outputs=[]')
                changes += 1
            else:
                # Multi-line dict starts here
                in_outputs_dict = True
                outputs_start_indent = len(line) - len(stripped)
                # Replace with outputs=[]
                new_lines.append(' ' * outputs_start_indent + 'outputs=[]')
                changes += 1
        elif in_outputs_dict:
            # We're inside a multi-line outputs dict
            brace_count += line.count('{') - line.count('}')
            
            if brace_count <= 0:
                # Dict is closed, exit mode
                in_outputs_dict = False
            # Skip all lines inside the dict
            continue
        else:
            # Normal line, keep it
            new_lines.append(line)
    
    return '\n'.join(new_lines), changes


def main():
    """Main function to process all tasks_test.py files."""
    domains_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains")
    
    # Find all tasks_test.py files
    tasks_files = list(domains_path.glob("*/variations/*/tasks_test.py"))
    
    print(f"Found {len(tasks_files)} tasks_test.py files\n")
    print("="*70)
    print("Processing files...")
    print("="*70 + "\n")
    
    modified_count = 0
    total_changes = 0
    
    for tasks_file in sorted(tasks_files):
        # Create backup
        backup_path = tasks_file.with_suffix('.py.backup3')
        shutil.copy2(tasks_file, backup_path)
        
        # Convert
        new_content, changes = convert_outputs_in_file(tasks_file)
        
        if changes > 0:
            # Write modified content
            with open(tasks_file, 'w') as f:
                f.write(new_content)
            
            rel_path = tasks_file.relative_to(Path.cwd())
            print(f"✓ {rel_path}: {changes} outputs converted")
            modified_count += 1
            total_changes += changes
    
    print(f"\n{'='*70}")
    print("COMPLETE")
    print(f"{'='*70}")
    print(f"Files modified: {modified_count}")
    print(f"Total outputs converted: {total_changes}")
    print(f"\nBackup files created with .backup3 extension")


if __name__ == "__main__":
    main()

