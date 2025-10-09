#!/usr/bin/env python3
"""
Comprehensive fix for all remaining 55 syntax errors.
"""

import json
import re
import shutil
from pathlib import Path


def load_errors():
    with open('syntax_errors.json', 'r') as f:
        return json.load(f)['all_errors']


def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()


def write_file(filepath, lines):
    with open(filepath, 'w') as f:
        f.writelines(lines)


def backup_file(filepath):
    backup = f"{filepath}.backup_final"
    try:
        shutil.copy2(filepath, backup)
    except:
        pass


def fix_dict_values_in_literal(lines, line_num):
    """Fix: "key": dict.get("x", {}).values()), -> "key": list(dict.get("x", {}).values()),"""
    idx = line_num - 1
    line = lines[idx]
    
    # Pattern: "key": something.get("x", {}).values()),
    if '.values()),' in line and '"' in line and ':' in line:
        # Wrap the .get().values() part with list()
        pattern = r'(\w+\.get\([^)]+\{[^}]*\}\)\.values\(\))'
        match = re.search(pattern, line)
        if match:
            old = match.group(1) + ')'
            new = 'list(' + match.group(1) + ')'
            fixed = line.replace(old, new)
            if fixed != line:
                lines[idx] = fixed
                return True
    
    return False


def fix_multiline_avg_progress(lines, line_num):
    """Fix avg_progress = ( with sum missing closing paren"""
    idx = line_num - 1
    
    # Find the sum line after avg_progress
    for i in range(idx, min(len(lines), idx + 10)):
        if 'sum(' in lines[i] and '.values()' in lines[i]:
            # Check next line for division
            if i + 1 < len(lines) and '/' in lines[i + 1]:
                # Add closing paren to sum line
                if lines[i].count('(') > lines[i].count(')'):
                    lines[i] = lines[i].rstrip() + ')\n'
                    return True
    return False


def fix_round_with_sum(lines, line_num):
    """Fix round( with inner sum missing paren"""
    idx = line_num - 1
    
    # Look ahead for sum with division
    for i in range(idx, min(len(lines), idx + 8)):
        if 'sum(' in lines[i] and '.values()' in lines[i]:
            if i + 1 < len(lines) and '/' in lines[i + 1]:
                if lines[i].count('(') > lines[i].count(')'):
                    lines[i] = lines[i].rstrip() + ')\n'
                    return True
    return False


def fix_fstring_nested_quotes(lines, line_num):
    """Fix f-string with data.get("x") -> data.get('x')"""
    idx = line_num - 1
    line = lines[idx]
    
    if 'f"' in line and 'data.get("' in line:
        fixed = re.sub(r'data\.get\("([^"]+)"', r"data.get('\1'", line)
        fixed = re.sub(r'data\.get\("([^"]+)",\s*\{\}\)', r"data.get('\1', {})", fixed)
        if fixed != line:
            lines[idx] = fixed
            return True
    return False


def fix_missing_comma_in_string(lines, line_num):
    """Fix: "number": \"555-999-8888\" missing comma"""
    idx = line_num - 1
    
    # Check if this is about previous line missing comma
    if idx > 0:
        prev_line = lines[idx - 1]
        # If previous line ends with }" without comma
        if prev_line.rstrip().endswith('}"') and not prev_line.rstrip().endswith('},'):
            lines[idx - 1] = prev_line.rstrip() + ',\n'
            return True
    return False


def fix_unclosed_paren_simple(lines, line_num):
    """Fix simple unclosed parenthesis at end of line"""
    idx = line_num - 1
    line = lines[idx]
    
    # Skip if line is just closing bracket
    if line.strip() in ['', ')', ']', '}', '),', '],', '},']:
        return False
    
    # Count parens
    open_p = line.count('(')
    close_p = line.count(')')
    
    if open_p > close_p:
        # Check if it's a line that should have closing paren
        if any(x in line for x in ['.values()', 'sum(', 'min(', 'max(', 'all(', 'any(', 'round(', 'sorted(', 'join(']):
            missing = open_p - close_p
            lines[idx] = line.rstrip() + ')' * missing + '\n'
            return True
    
    return False


def fix_extra_closing_paren(lines, line_num):
    """Fix unmatched extra ) like .values())): or ))"""
    idx = line_num - 1
    line = lines[idx]
    
    # Pattern: .values())):
    if '.values())):' in line:
        fixed = line.replace('.values())):', '.values()):')
        if fixed != line:
            lines[idx] = fixed
            return True
    
    # Pattern: extra ) at end before :
    if ')' in line and ':' in line:
        # Count parens before :
        before_colon = line.split(':')[0]
        if before_colon.count(')') > before_colon.count('('):
            # Remove one )
            fixed = before_colon[:-1] + before_colon[-1:].replace(')', '', 1) + ':' + ':'.join(line.split(':')[1:])
            lines[idx] = fixed
            return True
    
    return False


def fix_abs_sum_missing_paren(lines, line_num):
    """Fix: if abs(sum(...)) != ..."""
    idx = line_num - 1
    line = lines[idx]
    
    if 'abs(sum(' in line and '!=' in line:
        # Check if sum is missing closing paren before !=
        before_ne = line.split('!=')[0]
        sum_start = before_ne.find('sum(')
        if sum_start != -1:
            # Count parens after sum(
            parens_part = before_ne[sum_start:]
            if parens_part.count('(') > parens_part.count(')'):
                # Add closing paren before !=
                fixed = line.replace(' !=', ') !=', 1)
                lines[idx] = fixed
                return True
    
    return False


def fix_unclosed_brace(lines, line_num):
    """Fix: payload = {"key": ..."""
    idx = line_num - 1
    line = lines[idx]
    
    if 'payload = {' in line or line.strip().startswith('{'):
        # Check if missing closing brace
        if line.count('{') > line.count('}'):
            # Check if it's single line that should close
            if '.values())' in line and not line.rstrip().endswith('}'):
                lines[idx] = line.rstrip() + '}\n'
                return True
    
    return False


def fix_if_statement_missing_paren(lines, line_num):
    """Fix: if statement preceded by line with unclosed paren"""
    idx = line_num - 1
    line = lines[idx]
    
    if line.strip().startswith('if ') and idx > 0:
        prev_line = lines[idx - 1]
        if prev_line.count('(') > prev_line.count(')'):
            lines[idx - 1] = prev_line.rstrip() + ')\n'
            return True
    
    return False


def fix_specific_patterns(lines, line_num, error_msg, filepath):
    """Fix specific known error patterns"""
    
    # avg_progress = ( or avg_daily_sales = round(
    if 'avg_progress' in error_msg or 'avg_daily_sales' in error_msg:
        return fix_multiline_avg_progress(lines, line_num) or fix_round_with_sum(lines, line_num)
    
    # F-string issues
    if 'f-string' in error_msg:
        return fix_fstring_nested_quotes(lines, line_num)
    
    # Missing comma
    if 'Perhaps you forgot a comma' in error_msg:
        return fix_missing_comma_in_string(lines, line_num)
    
    # Dict .values() in dict literal
    if 'does not match' in error_msg and '{' in error_msg:
        return fix_dict_values_in_literal(lines, line_num)
    
    # abs(sum(...))
    if 'abs(sum' in error_msg or 'abs(sum' in lines[line_num - 1]:
        return fix_abs_sum_missing_paren(lines, line_num)
    
    # Unclosed brace
    if "'{' was never closed" in error_msg:
        return fix_unclosed_brace(lines, line_num)
    
    # if statement issues
    if lines[line_num - 1].strip().startswith('if '):
        return fix_if_statement_missing_paren(lines, line_num)
    
    # Extra closing paren
    if 'unmatched' in error_msg:
        return fix_extra_closing_paren(lines, line_num)
    
    # General unclosed paren
    if 'was never closed' in error_msg:
        return fix_unclosed_paren_simple(lines, line_num)
    
    return False


def fix_file(filepath, errors):
    """Fix all errors in a file"""
    lines = read_file(filepath)
    backup_file(filepath)
    
    fixes = []
    
    # Sort by line number descending to fix from bottom up
    for error in sorted(errors, key=lambda x: x['line'], reverse=True):
        line_num = error['line']
        error_msg = error['error']
        
        if fix_specific_patterns(lines, line_num, error_msg, filepath):
            fixes.append(line_num)
    
    if fixes:
        write_file(filepath, lines)
        return len(fixes)
    
    return 0


def main():
    print("🔧 Final Comprehensive Fix for All Remaining Errors")
    print("=" * 80)
    
    errors = load_errors()
    print(f"Loaded {len(errors)} errors\n")
    
    # Group by file
    from collections import defaultdict
    by_file = defaultdict(list)
    for e in errors:
        by_file[e['filepath']].append(e)
    
    total_fixes = 0
    files_fixed = 0
    
    for filepath in sorted(by_file.keys()):
        file_errors = by_file[filepath]
        print(f"\n📄 {filepath}")
        print(f"   {len(file_errors)} error(s)...")
        
        fixes = fix_file(filepath, file_errors)
        if fixes > 0:
            total_fixes += fixes
            files_fixed += 1
            print(f"   ✅ Fixed {fixes} error(s)")
        else:
            print(f"   ⚠️  No automatic fix available")
    
    print(f"\n{'=' * 80}")
    print("📊 FINAL SUMMARY")
    print(f"{'=' * 80}")
    print(f"Files processed:  {len(by_file)}")
    print(f"Files fixed:      {files_fixed}")
    print(f"Errors fixed:     {total_fixes}")
    print(f"Remaining:        {len(errors) - total_fixes}")
    print(f"Success rate:     {(total_fixes / len(errors) * 100):.1f}%")
    print(f"\n💾 Backups: .backup_final")
    print(f"✅ Re-run find_unused_code.py --syntax-errors-only to verify")
    print(f"{'=' * 80}\n")


if __name__ == '__main__':
    main()

