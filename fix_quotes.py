#!/usr/bin/env python3
"""
Fix unterminated string literals - only add quotes where actually missing.
"""

import re
from pathlib import Path
import sys

def fix_file(file_path: Path):
    """Fix unterminated strings."""
    lines = file_path.read_text(encoding='utf-8').split('\n')
    fixed = []
    changes = 0
    
    for i, line in enumerate(lines):
        # Skip lines that already end correctly
        if line.rstrip().endswith(('"', '",', '")', '"}', '"]:',  '"]', "'")):
            fixed.append(line)
            continue
        
        # Check if line opens a string but doesn't close it
        # Pattern: "key": "value  (odd quotes after colon)
        if ': "' in line:
            # Count quotes after the colon
            after_colon = line.split(': "', 1)[-1]
            quote_count = after_colon.count('"')
            
            # Odd number means unclosed
            if quote_count == 0:
                # Next line check
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    # If next line closes something, we need a quote
                    if re.match(r'^\s*[}\])]', next_line):
                        line = line.rstrip() + '"'
                        changes += 1
        
        fixed.append(line)
    
    return '\n'.join(fixed), changes

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fix_quotes.py <file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    content, changes = fix_file(file_path)
    
    if changes:
        file_path.write_text(content, encoding='utf-8')
        print(f"Fixed {changes} unterminated strings")
    else:
        print("No changes needed")

