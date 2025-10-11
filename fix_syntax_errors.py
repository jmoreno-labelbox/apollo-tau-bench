#!/usr/bin/env python3
"""
Fix syntax errors in files that had function definitions added.
This script identifies and fixes common syntax issues from incomplete function extraction.
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Set, Dict, Tuple

REPO_ROOT = Path(__file__).parent

def has_syntax_errors(file_path: Path) -> bool:
    """Check if a file has syntax errors."""
    try:
        content = file_path.read_text()
        ast.parse(content)
        return False
    except SyntaxError:
        return True
    except Exception:
        return False

def fix_syntax_errors_in_file(file_path: Path) -> bool:
    """Fix common syntax errors in a file."""
    try:
        content = file_path.read_text()
        lines = content.split('\n')
        fixed_lines = []
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Fix incomplete function definitions (lines that just say "def")
            if line.strip() == 'def':
                # Remove this line and any following empty lines
                i += 1
                while i < len(lines) and lines[i].strip() == '':
                    i += 1
                continue
            
            # Fix lines that start with "def" but are incomplete
            if line.strip().startswith('def') and not line.strip().endswith(':'):
                # Skip this line
                i += 1
                continue
            
            # Fix lines that have incomplete function signatures
            if 'def ' in line and not line.strip().endswith(':'):
                # Try to find the complete function definition
                complete_line = line
                j = i + 1
                while j < len(lines) and not complete_line.strip().endswith(':'):
                    if lines[j].strip() == '':
                        j += 1
                        continue
                    complete_line += ' ' + lines[j].strip()
                    j += 1
                
                if complete_line.strip().endswith(':'):
                    fixed_lines.append(complete_line)
                    i = j
                    continue
                else:
                    # Skip incomplete function
                    i = j
                    continue
            
            fixed_lines.append(line)
            i += 1
        
        # Join lines and check if syntax is now valid
        new_content = '\n'.join(fixed_lines)
        
        try:
            ast.parse(new_content)
            # Syntax is valid, write the fixed content
            file_path.write_text(new_content)
            return True
        except SyntaxError as e:
            print(f"  Still has syntax error after fix attempt: {e}")
            return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def fix_common_patterns(file_path: Path) -> bool:
    """Fix common syntax patterns that cause errors."""
    try:
        content = file_path.read_text()
        
        # Fix incomplete function definitions
        content = re.sub(r'^def\s*$', '', content, flags=re.MULTILINE)
        
        # Fix lines that have "def" but no colon
        content = re.sub(r'^def\s+[^:]*$', '', content, flags=re.MULTILINE)
        
        # Remove empty lines that might be left over
        lines = content.split('\n')
        cleaned_lines = []
        
        for i, line in enumerate(lines):
            # Skip empty lines that follow incomplete function definitions
            if line.strip() == '' and i > 0 and lines[i-1].strip() == '':
                continue
            cleaned_lines.append(line)
        
        # Remove trailing empty lines
        while cleaned_lines and cleaned_lines[-1].strip() == '':
            cleaned_lines.pop()
        
        new_content = '\n'.join(cleaned_lines)
        
        # Check if syntax is valid
        try:
            ast.parse(new_content)
            file_path.write_text(new_content)
            return True
        except SyntaxError:
            return False
        
    except Exception as e:
        print(f"Error fixing patterns in {file_path}: {e}")
        return False

def main():
    """Fix syntax errors in all affected files."""
    tau_dir = REPO_ROOT / "tau"
    
    if not tau_dir.exists():
        print(f"tau directory not found: {tau_dir}")
        return
    
    files_with_errors = []
    total_files = 0
    
    print("Scanning for files with syntax errors...")
    
    # Find all Python tool files
    for py_file in tau_dir.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
            
        total_files += 1
        
        if has_syntax_errors(py_file):
            files_with_errors.append(py_file)
    
    print(f"Found {len(files_with_errors)} files with syntax errors")
    
    fixed_files = 0
    failed_files = 0
    
    for file_path in files_with_errors:
        print(f"\nFixing {file_path.relative_to(tau_dir)}:")
        
        # Try the general syntax fix first
        if fix_syntax_errors_in_file(file_path):
            print("  ✓ Fixed with general syntax fix")
            fixed_files += 1
        elif fix_common_patterns(file_path):
            print("  ✓ Fixed with pattern matching")
            fixed_files += 1
        else:
            print("  ✗ Could not fix automatically")
            failed_files += 1
    
    print(f"\n=== Summary ===")
    print(f"Total files scanned: {total_files}")
    print(f"Files with syntax errors: {len(files_with_errors)}")
    print(f"Files fixed: {fixed_files}")
    print(f"Files that need manual attention: {failed_files}")
    
    if failed_files > 0:
        print(f"\nFiles that need manual attention:")
        for file_path in files_with_errors:
            if has_syntax_errors(file_path):
                print(f"  - {file_path.relative_to(tau_dir)}")

if __name__ == "__main__":
    main()