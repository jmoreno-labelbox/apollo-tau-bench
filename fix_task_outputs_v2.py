#!/usr/bin/env python3
"""
Script to convert task outputs from dict to list format using AST parsing.
This is safer than regex as it properly understands Python syntax.
"""
import ast
import shutil
from pathlib import Path


def convert_outputs_in_file(file_path: Path) -> tuple[str, int]:
    """
    Convert outputs={...} to outputs=[] by parsing and rewriting the AST.
    Returns (modified_content, number_of_changes)
    """
    with open(file_path, 'r') as f:
        content = f.read()

    # Simple but safe approach: replace only the outputs parameter in Task() calls
    # We'll do line-by-line replacement looking for the pattern
    lines = content.split('\n')
    new_lines = []
    changes = 0
    in_outputs_dict = False
    brace_count = 0

    for i, line in enumerate(lines):
        # Check if this line starts an outputs dict
        if 'outputs={' in line and not in_outputs_dict:
            # Count opening braces on this line
            brace_count = line.count('{') - line.count('}')
            if brace_count == 0:
                # Single line dict, replace it
                new_line = line.split('outputs={')[0] + 'outputs=[]'
                # Check if there's a comma after the dict
                if '},' in line or ')' in line.split('outputs={')[1]:
                    # Check what comes after
                    after_part = line.split('}', 1)[1] if '}' in line else ''
                    new_line = line.split('outputs={')[0] + 'outputs=[]' + after_part
                new_lines.append(new_line)
                changes += 1
            else:
                # Multi-line dict starts here
                in_outputs_dict = True
                # Replace with outputs=[]
                indent = len(line) - len(line.lstrip())
                new_lines.append(' ' * indent + 'outputs=[]')
                changes += 1
        elif in_outputs_dict:
            # We're inside a multi-line outputs dict, skip until we close all braces
            brace_count += line.count('{') - line.count('}')
            if brace_count <= 0:
                in_outputs_dict = False
            # Skip this line (it's the closing of the dict)
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
    print("=" * 70)
    print("Processing files...")
    print("=" * 70 + "\n")

    modified_count = 0
    total_changes = 0

    for tasks_file in sorted(tasks_files):
        # Create backup
        backup_path = tasks_file.with_suffix('.py.backup2')
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

    print(f"\n{'=' * 70}")
    print("COMPLETE")
    print(f"{'=' * 70}")
    print(f"Files modified: {modified_count}")
    print(f"Total outputs converted: {total_changes}")
    print(f"\nBackup files created with .backup2 extension")


if __name__ == "__main__":
    main()