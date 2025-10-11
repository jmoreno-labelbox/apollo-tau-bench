#!/usr/bin/env python3
"""
Fix duplicate 'body' keys in CreateIssue kwargs.
Keeps the second body value and removes the first.
"""

import re
from pathlib import Path
import sys

def fix_duplicate_body(content: str) -> tuple[str, int]:
    """Remove duplicate body keys in kwargs dicts."""
    
    # Pattern: "body": "text1", "body": "text2"
    # Keep text2, remove first body
    pattern = r'"body": "[^"]*",\s*"body": '
    
    def replacer(match):
        # Just replace with "body": (keeping the second one)
        return '"body": '
    
    new_content, count = re.subn(pattern, replacer, content)
    
    return new_content, count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix_duplicate_body.py <file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: {file_path} not found")
        sys.exit(1)
    
    print(f"Fixing duplicate 'body' keys in {file_path}\n")
    
    content = file_path.read_text(encoding='utf-8')
    fixed_content, changes = fix_duplicate_body(content)
    
    if changes > 0:
        file_path.write_text(fixed_content, encoding='utf-8')
        print(f"✓ Fixed {changes} duplicate body keys")
        
        # Verify syntax
        try:
            import ast
            ast.parse(fixed_content)
            print("✓ Syntax verified clean")
        except SyntaxError as e:
            print(f"✗ Still has syntax error at line {e.lineno}: {e.msg}")
    else:
        print("No duplicate body keys found")

if __name__ == "__main__":
    main()


