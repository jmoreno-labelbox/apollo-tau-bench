#!/usr/bin/env python3
"""
Fix unterminated strings by finding lines that should end with quotes but don't.
"""

import re
from pathlib import Path
import sys

def fix_file(file_path: Path):
    """Fix unterminated strings in the file."""
    content = file_path.read_text(encoding='utf-8')
    lines = content.split('\n')
    fixed_lines = []
    changes = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this line contains an instruction=( with an opening quote
        if 'instruction=(' in line and '="' in line:
            # This starts an instruction block
            # Find the closing )
            j = i + 1
            instruction_lines = [line]
            
            while j < len(lines):
                instruction_lines.append(lines[j])
                # Found the closing )
                if re.match(r'^\s+\),?\s*$', lines[j]):
                    # Check if the line before has a closing quote
                    prev_line = instruction_lines[-2] if len(instruction_lines) > 1 else instruction_lines[0]
                    
                    # If previous line doesn't end with a quote, add one
                    if not prev_line.rstrip().endswith('"'):
                        # Add quote to the last content line
                        instruction_lines[-2] = instruction_lines[-2].rstrip() + '"'
                        changes += 1
                        print(f"  Fixed line {i + len(instruction_lines) - 2}: added closing quote")
                    
                    # Add all instruction lines to fixed
                    fixed_lines.extend(instruction_lines)
                    i = j + 1
                    break
                j += 1
            else:
                # Didn't find closing paren, just add as-is
                fixed_lines.append(line)
                i += 1
        
        # Check for kwargs values that aren't closed
        elif '": "' in line and not re.search(r'": "[^"]*"', line):
            # Has opening quote for value but no closing quote
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                # If next line starts with closing bracket/paren, add quote
                if re.match(r'^\s*[}\])]', next_line):
                    line = line.rstrip() + '"'
                    changes += 1
                    print(f"  Fixed line {i + 1}: added closing quote to kwargs value")
            
            fixed_lines.append(line)
            i += 1
        
        # Check outputs array string items missing closing quotes
        elif re.match(r'^\s+["\']', line) and not line.rstrip().endswith(('",', '"', "',", "'")):
            # Starts with a quote but doesn't end properly
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                # If next line is a closing bracket or another string, add quote
                if re.match(r'^\s*[\])]', next_line) or re.match(r'^\s+["\']', next_line):
                    if not line.rstrip().endswith('"') and '"' in line:
                        line = line.rstrip() + '"'
                        changes += 1
                        print(f"  Fixed line {i + 1}: added closing quote to output item")
            
            fixed_lines.append(line)
            i += 1
        
        else:
            fixed_lines.append(line)
            i += 1
    
    return '\n'.join(fixed_lines), changes

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix_unterminated_strings_v2.py <file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    print(f"Fixing unterminated strings in {file_path}\n")
    
    fixed_content, changes = fix_file(file_path)
    
    if changes > 0:
        file_path.write_text(fixed_content, encoding='utf-8')
        print(f"\n✓ Fixed {changes} unterminated strings")
        
        # Verify syntax
        try:
            import ast
            ast.parse(fixed_content)
            print("✓ Syntax verified clean")
        except SyntaxError as e:
            print(f"✗ Still has syntax error at line {e.lineno}: {e.msg}")
    else:
        print("No unterminated strings found")

if __name__ == "__main__":
    main()

