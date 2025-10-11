#!/usr/bin/env python3
"""
Fix all Task syntax errors in test files by adding missing actions=[] parameters.
This script fixes the pattern where Task( is missing the actions=[] parameter.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

def fix_task_syntax_errors(file_path: Path) -> bool:
    """Fix Task syntax errors by adding missing actions=[] parameters."""
    try:
        content = file_path.read_text()
        rel_path = file_path.relative_to(REPO_ROOT)
        
        print(f"Fixing {rel_path}...")
        
        # Fix pattern: Task( ... instruction=... ), Action( -> Task( ... instruction=... ), actions=[ Action(
        # This pattern occurs when Task is missing the actions=[] parameter
        
        # Find all Task( blocks that are missing actions=[]
        lines = content.split('\n')
        fixed_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Look for Task( lines
            if line.strip().startswith('Task('):
                # Check if this Task is missing actions=[]
                task_start = i
                instruction_found = False
                actions_found = False
                
                # Look ahead to find the instruction and check for actions
                j = i + 1
                while j < len(lines) and not line.strip().endswith(')'):
                    if 'instruction=' in lines[j]:
                        instruction_found = True
                    if 'actions=[' in lines[j]:
                        actions_found = True
                        break
                    j += 1
                
                # If we found instruction but no actions, we need to add actions=[]
                if instruction_found and not actions_found:
                    # Find where to insert actions=[]
                    insert_pos = None
                    for k in range(i, min(i + 20, len(lines))):
                        if 'instruction=' in lines[k] and '),' in lines[k]:
                            insert_pos = k
                            break
                    
                    if insert_pos is not None:
                        # Add the actions=[] parameter
                        lines[insert_pos] = lines[insert_pos].replace('),', '),\n        actions=[')
                        # Find the first Action line and fix its indentation
                        for k in range(insert_pos + 1, min(insert_pos + 10, len(lines))):
                            if 'Action(' in lines[k]:
                                lines[k] = '            ' + lines[k].strip()
                                break
            
            fixed_lines.append(line)
            i += 1
        
        new_content = '\n'.join(fixed_lines)
        
        # Check if syntax is valid
        try:
            ast.parse(new_content)
            file_path.write_text(new_content)
            print(f"  ✓ Fixed {rel_path}")
            return True
        except SyntaxError as e:
            print(f"  ✗ Still has syntax error in {rel_path}: {e}")
            return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Fix Task syntax errors in both test files."""
    files_to_fix = [
        "tau/tau_bench/envs/github_mcp_6/tasks_test.py",
        "tau/tau_bench/envs/github_mcp_2/tasks_test.py"
    ]
    
    fixed_files = 0
    failed_files = 0
    
    print("Fixing Task syntax errors in test files...")
    
    for file_path_str in files_to_fix:
        file_path = REPO_ROOT / file_path_str
        
        if not file_path.exists():
            print(f"File not found: {file_path_str}")
            continue
        
        if fix_task_syntax_errors(file_path):
            fixed_files += 1
        else:
            failed_files += 1
    
    print(f"\n=== Summary ===")
    print(f"Files attempted: {len(files_to_fix)}")
    print(f"Files fixed: {fixed_files}")
    print(f"Files that still need manual attention: {failed_files}")

if __name__ == "__main__":
    main()
