#!/usr/bin/env python3
"""
Fix syntax errors in Python files using Claude 4.5 Sonnet.
Sends entire file, gets back corrected version.
"""

import sys
from pathlib import Path
from anthropic import Anthropic

def fix_file_with_claude(file_path: Path, api_key: str):
    """Send file to Claude 4.5 Sonnet to fix all syntax errors."""
    print(f"\nProcessing: {file_path}")
    
    try:
        content = file_path.read_text(encoding='utf-8')
        
        client = Anthropic(api_key=api_key)
        
        prompt = f"""Fix all syntax errors in this Python file. Return ONLY the corrected Python code with no syntax errors. Do not include any explanations, markdown formatting, or code blocks. Just output the raw Python code that can be directly saved to the file.

{content}"""

        print(f"  Sending {len(content)} characters to Claude 4.5 Sonnet...")
        
        # Use streaming for large files
        fixed_content = ""
        with client.messages.stream(
            model="claude-sonnet-4-5",
            max_tokens=64000,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        ) as stream:
            for text in stream.text_stream:
                fixed_content += text
        
        # Write back
        file_path.write_text(fixed_content, encoding='utf-8')
        print(f"  ✓ Wrote {len(fixed_content)} characters back to file")
        
        # Verify syntax
        import ast
        try:
            ast.parse(fixed_content)
            print(f"  ✓ Syntax verified clean")
            return True
        except SyntaxError as e:
            print(f"  ✗ Still has syntax error at line {e.lineno}: {e.msg}")
            return False
            
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix_with_claude.py <file1> [file2 ...]")
        print("\nExample:")
        print("  python3 fix_with_claude.py tau/tau_bench/envs/retail_4/tasks_test.py")
        sys.exit(1)
    
    import os
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
    
    files = [Path(f) for f in sys.argv[1:]]
    
    print(f"Fixing {len(files)} files with Claude 4.5 Sonnet")
    
    fixed = 0
    failed = 0
    
    for file_path in files:
        if not file_path.exists():
            print(f"\n✗ File not found: {file_path}")
            failed += 1
            continue
        
        if fix_file_with_claude(file_path, api_key):
            fixed += 1
        else:
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Fixed: {fixed}")
    print(f"Failed: {failed}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

