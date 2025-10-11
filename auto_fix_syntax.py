#!/usr/bin/env python3
"""
Automatically fix syntax errors in Python files using GPT-4o.
"""

import os
import re
import sys
import subprocess
from pathlib import Path
from openai import OpenAI
import argparse

def check_syntax(file_path: Path):
    """Check if file has syntax errors. Returns (has_error, error_message, line_number)."""
    try:
        result = subprocess.run(
            ["python3", "-m", "py_compile", str(file_path)],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return False, None, None
        
        # Parse error message
        error_msg = result.stderr
        # Extract line number from error
        match = re.search(r'line (\d+)', error_msg)
        line_num = int(match.group(1)) if match else None
        
        return True, error_msg, line_num
        
    except Exception as e:
        return True, str(e), None

def get_context_around_line(file_path: Path, line_num: int, context: int = 20):
    """Get lines around the error for context."""
    try:
        lines = file_path.read_text(encoding='utf-8').splitlines()
        start = max(0, line_num - context - 1)
        end = min(len(lines), line_num + context)
        
        context_lines = []
        for i in range(start, end):
            prefix = ">>> " if i == line_num - 1 else "    "
            context_lines.append(f"{prefix}{i+1:4d}: {lines[i]}")
        
        return "\n".join(context_lines), lines
    except Exception as e:
        return None, None

def fix_with_gpt(file_path: Path, error_msg: str, line_num: int, client: OpenAI):
    """Use GPT-4o to fix the syntax error."""
    context, all_lines = get_context_around_line(file_path, line_num, context=15)
    
    if context is None:
        return None
    
    prompt = f"""Fix this Python syntax error. The error is on line {line_num}.

Error message:
{error_msg}

Code context (>>> marks the error line):
{context}

Provide ONLY the fixed line {line_num} content, nothing else. Do not include line numbers or quotes."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Python syntax error fixer. Return only the corrected line of code, preserving indentation. No explanations, no line numbers, no quotes around the output."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=500,
            timeout=30.0
        )
        
        fixed_line = response.choices[0].message.content.strip()
        
        # Apply the fix
        all_lines[line_num - 1] = fixed_line
        return "\n".join(all_lines)
        
    except Exception as e:
        print(f"  GPT error: {e}")
        return None

def fix_file(file_path: Path, client: OpenAI):
    """Fix syntax errors in a file, iterating until clean."""
    print(f"\nFixing: {file_path}")
    
    iteration = 0
    while True:
        iteration += 1
        has_error, error_msg, line_num = check_syntax(file_path)
        
        if not has_error:
            print(f"  ✓ Syntax clean after {iteration} iteration(s)")
            return True
        
        if iteration > 50:
            print(f"  ✗ Too many errors (>50), stopping")
            return False
        
        if line_num is None:
            print(f"  ✗ Could not determine error line")
            return False
        
        print(f"  Iteration {iteration}: Fixing line {line_num}")
        
        fixed_content = fix_with_gpt(file_path, error_msg, line_num, client)
        
        if fixed_content is None:
            print(f"  ✗ Failed to generate fix")
            return False
        
        # Write the fix
        file_path.write_text(fixed_content, encoding='utf-8')
        print(f"  Applied fix to line {line_num}")

def main():
    parser = argparse.ArgumentParser(description="Auto-fix Python syntax errors using GPT-4o")
    parser.add_argument("files", nargs="+", help="Files to fix")
    args = parser.parse_args()
    
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)
    
    client = OpenAI(api_key=api_key)
    
    files_to_fix = [Path(f) for f in args.files]
    
    print(f"Fixing {len(files_to_fix)} files using GPT-4o")
    
    fixed = 0
    failed = 0
    
    for file_path in files_to_fix:
        if not file_path.exists():
            print(f"\n✗ File not found: {file_path}")
            failed += 1
            continue
        
        if fix_file(file_path, client):
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

