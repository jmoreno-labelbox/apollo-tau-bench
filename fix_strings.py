#!/usr/bin/env python3
"""
Fix unterminated string literals using Python's tokenizer.
"""

import tokenize
import io
from pathlib import Path
import sys

def fix_unterminated_strings(file_path: Path):
    """Fix unterminated strings by trying to parse and fixing errors."""
    content = file_path.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    # Try to tokenize - this will fail on unterminated strings
    while True:
        try:
            tokens = list(tokenize.generate_tokens(io.StringIO('\n'.join(lines)).readline))
            # If we get here, no tokenize errors
            break
        except tokenize.TokenError as e:
            # Extract line number and error
            msg = str(e)
            if 'EOF in multi-line string' in msg or 'unterminated string' in msg.lower():
                # Find the line number from the error
                import re
                match = re.search(r'line (\d+)', msg)
                if match:
                    error_line = int(match.group(1)) - 1
                    if 0 <= error_line < len(lines):
                        # Add closing quote to this line
                        lines[error_line] = lines[error_line].rstrip() + '"'
                        print(f"Fixed line {error_line + 1}: added closing quote")
                        continue
            # Can't fix this error
            print(f"Unable to auto-fix: {e}")
            break
        except Exception as e:
            print(f"Error: {e}")
            break
    
    # Now try AST parse and fix any remaining issues
    import ast
    fixed_content = '\n'.join(lines)
    
    max_attempts = 50
    for attempt in range(max_attempts):
        try:
            ast.parse(fixed_content)
            # Success
            break
        except SyntaxError as e:
            if 'unterminated string' in str(e).lower() or 'EOF' in str(e):
                # Fix at the line
                if e.lineno and e.lineno <= len(lines):
                    lines[e.lineno - 1] = lines[e.lineno - 1].rstrip() + '"'
                    fixed_content = '\n'.join(lines)
                    print(f"Fixed line {e.lineno}: added closing quote")
                else:
                    break
            else:
                # Different error
                break
    
    return '\n'.join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix_strings.py <file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: {file_path} not found")
        sys.exit(1)
    
    print(f"Fixing unterminated strings in {file_path}\n")
    
    original = file_path.read_text(encoding='utf-8')
    fixed = fix_unterminated_strings(file_path)
    
    if fixed != original:
        file_path.write_text(fixed, encoding='utf-8')
        print(f"\n✓ File updated")
        
        # Final syntax check
        try:
            import ast
            ast.parse(fixed)
            print("✓ Syntax verified clean")
        except SyntaxError as e:
            print(f"✗ Remaining syntax error at line {e.lineno}: {e.msg}")
    else:
        print("No changes made")

if __name__ == "__main__":
    main()

