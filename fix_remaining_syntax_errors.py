#!/usr/bin/env python3
"""
Enhanced script to fix remaining syntax errors with multi-line context awareness.
"""

import json
import re
import shutil
from pathlib import Path
from collections import defaultdict


def load_errors():
    """Load syntax errors from JSON."""
    with open('syntax_errors.json', 'r') as f:
        data = json.load(f)
    return data.get('all_errors', [])


def read_file_lines(filepath):
    """Read file and return lines."""
    try:
        with open(filepath, 'r') as f:
            return f.readlines()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None


def write_file_lines(filepath, lines):
    """Write lines to file."""
    try:
        with open(filepath, 'w') as f:
            f.writelines(lines)
        return True
    except Exception as e:
        print(f"Error writing {filepath}: {e}")
        return False


def fix_list_values_double_paren(lines, line_num):
    """Fix: list(...values())) -> list(...values())"""
    idx = line_num - 1
    line = lines[idx]
    
    if 'list(' in line and '.values())' in line and '.values()))' in line:
        fixed = line.replace('.values()))', '.values())')
        if fixed != line:
            lines[idx] = fixed
            return True, "Removed double closing paren after list(.values())"
    
    return False, None


def fix_missing_paren_before_bracket(lines, line_num):
    """Fix multi-line comprehension missing closing paren before ]"""
    idx = line_num - 1
    
    # Check previous line (where the paren issue is)
    if idx > 0:
        prev_line = lines[idx - 1]
        curr_line = lines[idx]
        
        # Pattern: previous line has unclosed paren, current is ]
        if curr_line.strip() == ']':
            open_count = prev_line.count('(')
            close_count = prev_line.count(')')
            
            if open_count > close_count:
                # Add missing closing parens
                missing = open_count - close_count
                lines[idx - 1] = prev_line.rstrip() + ')' * missing + '\n'
                return True, f"Added {missing} closing paren(s) before ]"
    
    return False, None


def fix_dict_values_in_dict_literal(lines, line_num):
    """Fix: {...}.values()) in dict literal -> list({...}.values())"""
    idx = line_num - 1
    line = lines[idx]
    
    # Pattern: "key": something.get("x", {}).values()),
    if '.values()),' in line and '"' in line and ':' in line:
        # Check if it's not already wrapped in list()
        if 'list(' not in line:
            # Find the part with .values())
            match = re.search(r'(\w+\.get\([^)]+\{[^}]*\}\)\.values\(\))', line)
            if match:
                old_part = match.group(1)
                new_part = f'list({old_part})'
                fixed = line.replace(old_part + ')', new_part)
                lines[idx] = fixed
                return True, "Wrapped .values() with list()"
    
    return False, None


def fix_unclosed_paren_in_comprehension(lines, line_num):
    """Fix unclosed parenthesis in list/generator comprehensions"""
    idx = line_num - 1
    
    # Look back for the start of comprehension
    if idx > 0:
        curr_line = lines[idx]
        
        # If current line is ] or ), check previous lines
        if curr_line.strip() in [']', ')', '])']:
            # Scan backwards to find unclosed parens
            for i in range(idx - 1, max(0, idx - 10), -1):
                check_line = lines[i]
                
                # Count parens in this line
                open_count = check_line.count('(')
                close_count = check_line.count(')')
                
                if open_count > close_count:
                    # Check if line ends with comprehension or similar
                    stripped = check_line.rstrip()
                    if any(stripped.endswith(pat) for pat in ['.values()', 'for tag in tags)', ' in p)']):
                        # Add missing closing parens
                        missing = open_count - close_count
                        lines[i] = check_line.rstrip() + ')' * missing + '\n'
                        return True, f"Added {missing} closing paren(s) in comprehension at line {i+1}"
    
    return False, None


def fix_missing_closing_paren_general(lines, line_num):
    """General fix for missing closing parentheses"""
    idx = line_num - 1
    line = lines[idx]
    
    # Skip if line is just whitespace or closing brackets
    if line.strip() in ['', ']', ')', '}', '],', '),', '},']:
        return False, None
    
    # Count parens
    open_count = line.count('(')
    close_count = line.count(')')
    
    if open_count > close_count:
        # Check if it's a line that should have closing paren
        if any(pattern in line for pattern in [
            '.values()',
            'all(',
            'any(',
            'sum(',
            'list(',
            'enumerate(',
            '_convert_db_to_list('
        ]):
            missing = open_count - close_count
            lines[idx] = line.rstrip() + ')' * missing + '\n'
            return True, f"Added {missing} closing paren(s)"
    
    return False, None


def fix_extra_closing_paren(lines, line_num):
    """Fix unmatched/extra closing parenthesis"""
    idx = line_num - 1
    line = lines[idx]
    
    # Pattern: .values())):  -> .values()):
    if '.values()):' in line and line.count('(') < line.count(')'):
        fixed = line.replace('.values())):', '.values()):')
        if fixed != line:
            lines[idx] = fixed
            return True, "Removed extra closing paren before :"
    
    # Pattern: .values()),  -> .values(),
    if '.values()),' in line:
        # Check if there's unmatched paren
        before_values = line.split('.values()')[0]
        if before_values.count('(') < before_values.count(')') + 1:
            fixed = line.replace('.values()),', '.values(),')
            lines[idx] = fixed
            return True, "Removed extra closing paren before comma"
    
    return False, None


def fix_fstring_quotes(lines, line_num):
    """Fix f-string with nested quotes"""
    idx = line_num - 1
    line = lines[idx]
    
    if 'f"' in line and 'data.get("' in line:
        # Replace inner double quotes with single quotes
        fixed = re.sub(r'data\.get\("([^"]+)"', r"data.get('\1'", line)
        fixed = re.sub(r'data\.get\("([^"]+)",\s*\{\}\)', r"data.get('\1', {})", fixed)
        if fixed != line:
            lines[idx] = fixed
            return True, "Fixed f-string nested quotes"
    
    return False, None


def fix_leading_zero_in_number(lines, line_num):
    """Fix leading zeros in numbers (e.g., 01 -> 1)"""
    idx = line_num - 1
    line = lines[idx]
    
    # Pattern: "key": 01, or similar
    match = re.search(r':\s+0(\d+),', line)
    if match:
        old = f'0{match.group(1)}'
        new = match.group(1)
        fixed = line.replace(f': {old},', f': {new},')
        lines[idx] = fixed
        return True, f"Fixed leading zero: {old} -> {new}"
    
    return False, None


def apply_fixes_to_file(filepath, error_infos):
    """Apply all fixes to a file"""
    lines = read_file_lines(filepath)
    if not lines:
        return 0
    
    # Create backup
    backup_path = f"{filepath}.backup_syntax2"
    try:
        shutil.copy2(filepath, backup_path)
    except:
        pass
    
    fixes_applied = 0
    
    # Group errors by line and try fixes
    for error_info in sorted(error_infos, key=lambda x: x['line'], reverse=True):
        line_num = error_info['line']
        error_msg = error_info['error']
        
        applied = False
        fix_msg = None
        
        # Try different fix strategies
        if 'list(' in ''.join(lines[max(0, line_num-2):line_num+1]) and '.values())' in error_msg:
            applied, fix_msg = fix_list_values_double_paren(lines, line_num)
        
        if not applied and ']' in error_msg and 'does not match' in error_msg:
            applied, fix_msg = fix_missing_paren_before_bracket(lines, line_num)
        
        if not applied and ')' in error_msg and 'does not match' in error_msg and '{' in error_msg:
            applied, fix_msg = fix_dict_values_in_dict_literal(lines, line_num)
        
        if not applied and '(' in error_msg and 'was never closed' in error_msg:
            applied, fix_msg = fix_missing_closing_paren_general(lines, line_num)
        
        if not applied and 'unmatched' in error_msg:
            applied, fix_msg = fix_extra_closing_paren(lines, line_num)
        
        if not applied and 'f-string' in error_msg:
            applied, fix_msg = fix_fstring_quotes(lines, line_num)
        
        if not applied and 'leading zeros' in error_msg:
            applied, fix_msg = fix_leading_zero_in_number(lines, line_num)
        
        if not applied:
            # Try unclosed paren in comprehension as last resort
            applied, fix_msg = fix_unclosed_paren_in_comprehension(lines, line_num)
        
        if applied:
            fixes_applied += 1
            print(f"   ✅ Line {line_num}: {fix_msg}")
    
    # Write back if fixes were applied
    if fixes_applied > 0:
        write_file_lines(filepath, lines)
    
    return fixes_applied


def main():
    print("🔧 Enhanced Syntax Error Fixer")
    print("=" * 80)
    
    errors = load_errors()
    print(f"Loaded {len(errors)} remaining syntax errors\n")
    
    # Group by file
    errors_by_file = defaultdict(list)
    for error in errors:
        errors_by_file[error['filepath']].append(error)
    
    print(f"Errors in {len(errors_by_file)} files\n")
    
    total_fixes = 0
    files_fixed = 0
    
    for filepath in sorted(errors_by_file.keys()):
        file_errors = errors_by_file[filepath]
        print(f"\n📄 {filepath}")
        print(f"   {len(file_errors)} error(s)")
        
        fixes = apply_fixes_to_file(filepath, file_errors)
        if fixes > 0:
            total_fixes += fixes
            files_fixed += 1
    
    print(f"\n{'=' * 80}")
    print("📊 SUMMARY")
    print(f"{'=' * 80}")
    print(f"Files processed:  {len(errors_by_file)}")
    print(f"Files fixed:      {files_fixed}")
    print(f"Total fixes:      {total_fixes}")
    print(f"Success rate:     {(total_fixes / len(errors) * 100):.1f}%")
    print(f"\n💾 Backup files created with .backup_syntax2 extension")
    print(f"✅ Re-run find_unused_code.py to verify")
    print(f"{'=' * 80}\n")


if __name__ == '__main__':
    main()

