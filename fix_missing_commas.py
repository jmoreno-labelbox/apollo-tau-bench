#!/usr/bin/env python3
"""
Fix missing commas after strings in tasks_test.py files.
Handles: instruction strings, kwargs values, outputs array items.
"""

import re
from pathlib import Path
import sys

def fix_missing_commas(content: str) -> str:
    """Fix various missing comma patterns."""
    
    # Fix 1: instruction=("...") missing comma before actions
    content = re.sub(
        r'(instruction=\("([^"]|"")*"\))\n(\s+)(actions=)',
        r'\1,\n\3\4',
        content
    )
    
    # Fix 2: instruction="..." missing comma before actions
    content = re.sub(
        r'(instruction="([^"]|\\")*")\n(\s+)(actions=)',
        r'\1,\n\3\4',
        content
    )
    
    # Fix 3: "key": "value  (missing closing quote)
    # Look for patterns like "message": "text\n with no closing quote
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Check for unterminated string in kwargs
        if re.search(r'"[^"]+": "[^"]*$', line):
            # Line ends with an open quote, need to add closing quote
            # But only if next line doesn't continue the string
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                # If next line starts with more content (not a closing bracket/paren), close the string
                if not re.match(r'^\s*[}\])]', next_line):
                    line = line.rstrip() + '"'
        
        fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    # Fix 4: outputs array items missing commas
    # "item1"  \n  "item2"  ->  "item1",\n  "item2"
    content = re.sub(
        r'("[^"]*")\n(\s+)("+)',
        r'\1,\n\2\3',
        content
    )
    
    # Fix 5: kwargs dict values missing closing quotes
    # "key": "value}\n  ->  "key": "value"}\n
    content = re.sub(
        r'("[\w_]+": ")([^"]*)\n',
        lambda m: m.group(1) + m.group(2) + '"\n' if not m.group(2).endswith('"') else m.group(0),
        content
    )
    
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix_missing_commas.py <file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    print(f"Fixing missing commas in {file_path}")
    
    content = file_path.read_text(encoding='utf-8')
    original_len = len(content)
    
    fixed_content = fix_missing_commas(content)
    
    if fixed_content != content:
        file_path.write_text(fixed_content, encoding='utf-8')
        print(f"✓ Fixed and saved ({len(fixed_content) - original_len:+d} chars)")
    else:
        print("No changes needed")

if __name__ == "__main__":
    main()

