#!/usr/bin/env python3
"""
Simple and effective fix for Task definitions in test files.
This script fixes the specific pattern where Task definitions are missing actions=[].
"""

import os
import re
import ast
from pathlib import Path

REPO_ROOT = Path(__file__).parent

def fix_task_patterns(file_path: Path) -> bool:
    """Fix Task patterns by adding missing actions=[] parameters."""
    try:
        content = file_path.read_text()
        rel_path = file_path.relative_to(REPO_ROOT)
        
        print(f"Fixing Task patterns in {rel_path}...")
        
        # Use regex to find and fix all Task definitions that are missing actions=[]
        # Pattern: instruction=("..."), Action( -> instruction=("..."), actions=[ Action(
        
        # First, find all Task blocks that need fixing
        lines = content.split('\n')
        new_lines = []
        i = 0
        fixes_applied = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Look for Task( lines
            if line.strip().startswith('Task('):
                # Check if this Task needs fixing
                task_start = i
                instruction_found = False
                actions_found = False
                instruction_end_line = None
                
                # Look ahead to find the instruction and check for actions
                j = i + 1
                while j < len(lines) and j < i + 50:
                    current_line = lines[j]
                    if 'instruction=' in current_line:
                        instruction_found = True
                        # Find where instruction ends
                        k = j
                        while k < len(lines) and k < j + 10:
                            if '),' in lines[k]:
                                instruction_end_line = k
                                break
                            k += 1
                        break
                    if 'actions=[' in current_line:
                        actions_found = True
                        break
                    j += 1
                
                # If we found instruction but no actions, we need to add actions=[]
                if instruction_found and not actions_found and instruction_end_line is not None:
                    # Add the actions=[] parameter after the instruction
                    original_line = lines[instruction_end_line]
                    lines[instruction_end_line] = original_line.replace('),', '),\n        actions=[')
                    fixes_applied += 1
                    
                    # Find the first Action line after this and fix its indentation
                    for k in range(instruction_end_line + 1, min(instruction_end_line + 20, len(lines))):
                        if 'Action(' in lines[k] and not lines[k].strip().startswith('Action('):
                            # This Action line needs proper indentation
                            lines[k] = '            ' + lines[k].strip()
                            break
            
            new_lines.append(line)
            i += 1
        
        new_content = '\n'.join(new_lines)
        
        # Check if syntax is valid
        try:
            ast.parse(new_content)
            file_path.write_text(new_content)
            print(f"  ✓ Fixed {fixes_applied} Task definitions in {rel_path}")
            return True
        except SyntaxError as e:
            print(f"  ✗ Still has syntax error in {rel_path}: {e}")
            return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Fix all Task definitions in both test files."""
    files_to_fix = [
        "tau/tau_bench/envs/github_mcp_6/tasks_test.py",
        "tau/tau_bench/envs/github_mcp_2/tasks_test.py"
    ]
    
    fixed_files = 0
    failed_files = 0
    
    print("Fixing Task patterns in test files...")
    
    for file_path_str in files_to_fix:
        file_path = REPO_ROOT / file_path_str
        
        if not file_path.exists():
            print(f"File not found: {file_path_str}")
            continue
        
        if fix_task_patterns(file_path):
            fixed_files += 1
        else:
            failed_files += 1
    
    print(f"\n=== Summary ===")
    print(f"Files attempted: {len(files_to_fix)}")
    print(f"Files fixed: {fixed_files}")
    print(f"Files that still need manual attention: {failed_files}")

if __name__ == "__main__":
    main()