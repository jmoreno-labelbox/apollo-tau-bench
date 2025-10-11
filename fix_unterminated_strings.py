#!/usr/bin/env python3
"""
Fix unterminated string literals in Python files.
Finds lines with unclosed quotes and adds the missing closing quote.
"""

import re
from pathlib import Path
import sys

def fix_unterminated_strings(content: str) -> str:
    """Fix unterminated string literals."""
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        original_line = line
        
        # Pattern 1: "key": "value  (missing closing quote before newline)
        # Check if line has an odd number of quotes after the last colon
        if '": "' in line:
            # Count quotes after the ": " pattern
            match = re.search(r': "([^"]*?)$', line)
            if match:
                # Line ends without closing quote
                line = line.rstrip() + '"'
        
        # Pattern 2: instruction=("text  (missing closing quote and paren)
        if 'instruction=("' in line and not line.rstrip().endswith('")'):
            if not line.rstrip().endswith('"'):
                line = line.rstrip() + '"'
        
        # Pattern 3: "message": "text  (in kwargs or outputs)
        if '"message": "' in line:
            # Count quotes in the value part
            parts = line.split('"message": "', 1)
            if len(parts) == 2:
                value_part = parts[1]
                # If value part has no closing quote
                if '"' not in value_part and not value_part.strip().endswith('"'):
                    line = line.rstrip() + '"'
        
        # Pattern 4: General kwargs value missing closing quote
        # "any_key": "any_value\n -> add closing quote
        match = re.search(r'"(\w+)": "([^"]*?)$', line)
        if match and i + 1 < len(lines):
            next_line = lines[i + 1]
            # If next line starts with closing bracket/paren/comma, add quote
            if re.match(r'^\s*[}\]),]', next_line):
                if not line.rstrip().endswith('"'):
                    line = line.rstrip() + '"'
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix_unterminated_strings.py <file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    print(f"Fixing unterminated strings in {file_path}")
    
    content = file_path.read_text(encoding='utf-8')
    fixed_content = fix_unterminated_strings(content)
    
    if fixed_content != content:
        # Count changes
        changes = sum(1 for a, b in zip(content.split('\n'), fixed_content.split('\n')) if a != b)
        file_path.write_text(fixed_content, encoding='utf-8')
        print(f"✓ Fixed {changes} lines")
        
        # Verify syntax
        try:
            import ast
            ast.parse(fixed_content)
            print("✓ Syntax verified clean")
        except SyntaxError as e:
            print(f"✗ Still has syntax error at line {e.lineno}: {e.msg}")
    else:
        print("No changes needed")

if __name__ == "__main__":
    main()

