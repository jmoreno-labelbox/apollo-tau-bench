#!/usr/bin/env python3
"""
Final pass to fix remaining complex multi-line syntax errors.
"""

import json
import re
import shutil
from pathlib import Path


def load_errors():
    with open('syntax_errors.json', 'r') as f:
        return json.load(f)['all_errors']


def read_lines(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()


def write_lines(filepath, lines):
    with open(filepath, 'w') as f:
        f.writelines(lines)


def fix_multi_line_sum_division(lines, line_num, error_msg):
    """Fix multi-line sum(...) / division where sum is missing closing paren"""
    idx = line_num - 1
    
    # Check if this line has division and previous line has unclosed sum
    if idx > 0 and '/' in lines[idx]:
        prev_idx = idx - 1
        # Look back for the sum( line
        while prev_idx >= 0 and prev_idx > idx - 5:
            prev_line = lines[prev_idx]
            if 'sum(' in prev_line and '.values()' in prev_line:
                # Check if it's missing closing paren for sum
                if prev_line.count('(') > prev_line.count(')'):
                    # Add closing paren before newline
                    lines[prev_idx] = prev_line.rstrip() + ')\n'
                    return True, f"Added closing paren to sum() at line {prev_idx+1}"
            prev_idx -= 1
    
    return False, None


def fix_enumerate_missing_closing_paren(lines, line_num):
    """Fix for i, x in enumerate(x.values():"""
    idx = line_num - 1
    line = lines[idx]
    
    if 'enumerate(' in line and '.values():' in line:
        fixed = line.replace('.values():', '.values()):')
        if fixed != line:
            lines[idx] = fixed
            return True, "Added closing paren to enumerate"
    
    return False, None


def fix_capacity_limit_calculation(lines, line_num):
    """Fix capacity_limit = avg_velocity * 0.8 - usually prev line missing paren"""
    idx = line_num - 1
    
    if idx > 0 and 'capacity_limit' in lines[idx]:
        # Check previous line for unclosed paren
        prev_line = lines[idx - 1]
        if prev_line.count('(') > prev_line.count(')'):
            lines[idx - 1] = prev_line.rstrip() + ')\n'
            return True, f"Added closing paren at line {idx}"
    
    return False, None


def fix_leading_zero(lines, line_num):
    """Fix leading zero like 01 -> 1"""
    idx = line_num - 1
    line = lines[idx]
    
    # Pattern: pra-01 or similar with leading zero
    match = re.search(r':\s+(\w+)-0(\d+),', line)
    if match:
        prefix = match.group(1)
        num = match.group(2)
        old = f'{prefix}-0{num}'
        new = f'{prefix}-{num}'
        fixed = line.replace(old, new)
        if fixed != line:
            lines[idx] = fixed
            return True, f"Fixed leading zero: {old} -> {new}"
    
    return False, None


def fix_fstring_dashboard(lines, line_num):
    """Fix f-string with nested quotes in dashboard ID"""
    idx = line_num - 1
    line = lines[idx]
    
    if 'f"SNAP' in line and 'data.get(' in line:
        # Fix inner quotes
        fixed = re.sub(r'data\.get\("([^"]+)"', r"data.get('\1'", line)
        if fixed != line:
            lines[idx] = fixed
            return True, "Fixed f-string nested quotes"
    
    return False, None


def fix_split_transaction_sum(lines, line_num):
    """Fix if abs(sum(s['amount'] for s in splits) != ..."""
    idx = line_num - 1
    line = lines[idx]
    
    if 'abs(sum(' in line and 'for s in splits' in line and '!=' in line:
        # Check if missing closing paren for sum
        before_ne = line.split('!=')[0]
        if before_ne.count('(') > before_ne.count(')'):
            # Add closing paren before !=
            fixed = line.replace(' !=', ') !=')
            lines[idx] = fixed
            return True, "Added closing paren in abs(sum(...))"
    
    return False, None


def fix_find_by_id_unmatched(lines, line_num):
    """Fix _find_by_id(data.get(...).values()), arg) patterns"""
    idx = line_num - 1
    line = lines[idx]
    
    if '_find_by_id(' in line and '.values()),' in line:
        # Pattern: _find_by_id(data.get(...).values()), arg)
        # Should be: _find_by_id(data.get(...).values(), arg)
        fixed = line.replace('.values()),', '.values(),')
        if fixed != line:
            lines[idx] = fixed
            return True, "Fixed _find_by_id unmatched paren"
    
    return False, None


def fix_payload_dict_unclosed_brace(lines, line_num):
    """Fix payload = {"key": value, ..."""
    idx = line_num - 1
    line = lines[idx]
    
    if 'payload = {' in line:
        # Count braces
        if line.count('{') > line.count('}'):
            # This is start of multi-line dict, probably OK
            # But check if values() is causing issue
            if '.values()}' in line:
                # Should be .values())}
                fixed = line.replace('.values()}', '.values())}')
                lines[idx] = fixed
                return True, "Fixed dict closing brace"
    
    return False, None


def fix_round_sum_multi_line(lines, line_num):
    """Fix round((...) where sum inside is missing paren"""
    idx = line_num - 1
    
    # Check if this is the line with round(
    if 'round(' in lines[idx]:
        # Look ahead for the issue
        for i in range(idx, min(len(lines), idx + 10)):
            if 'sum(' in lines[i] and '.values()' in lines[i]:
                # Check if next line has division
                if i + 1 < len(lines) and '/' in lines[i + 1]:
                    # sum line is missing closing paren
                    if lines[i].count('(') > lines[i].count(')'):
                        lines[i] = lines[i].rstrip() + ')\n'
                        return True, f"Added closing paren to sum() at line {i+1}"
    
    return False, None


def apply_fixes(filepath, errors):
    lines = read_lines(filepath)
    
    # Backup
    backup = f"{filepath}.backup_syntax3"
    try:
        shutil.copy2(filepath, backup)
    except:
        pass
    
    fixes = 0
    
    for error in sorted(errors, key=lambda x: x['line'], reverse=True):
        line_num = error['line']
        error_msg = error['error']
        
        fixed = False
        msg = None
        
        if 'avg_daily_sales' in error_msg or 'avg_progress' in error_msg:
            fixed, msg = fix_multi_line_sum_division(lines, line_num, error_msg)
        elif 'round(' in error_msg:
            fixed, msg = fix_round_sum_multi_line(lines, line_num)
        elif 'enumerate' in error_msg:
            fixed, msg = fix_enumerate_missing_closing_paren(lines, line_num)
        elif 'capacity_limit' in error_msg:
            fixed, msg = fix_capacity_limit_calculation(lines, line_num)
        elif 'leading zeros' in error_msg:
            fixed, msg = fix_leading_zero(lines, line_num)
        elif 'f-string' in error_msg and 'SNAP' in error_msg:
            fixed, msg = fix_fstring_dashboard(lines, line_num)
        elif 'abs(sum' in error_msg:
            fixed, msg = fix_split_transaction_sum(lines, line_num)
        elif '_find_by_id' in error_msg or '_find_by_id' in lines[line_num-1]:
            fixed, msg = fix_find_by_id_unmatched(lines, line_num)
        elif 'payload = {' in error_msg:
            fixed, msg = fix_payload_dict_unclosed_brace(lines, line_num)
        
        if fixed:
            fixes += 1
            print(f"   ✅ Line {line_num}: {msg}")
    
    if fixes > 0:
        write_lines(filepath, lines)
    
    return fixes


def main():
    print("🔧 Final Syntax Error Fix Pass")
    print("=" * 80)
    
    errors = load_errors()
    print(f"Loaded {len(errors)} remaining errors\n")
    
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
        print(f"   {len(file_errors)} error(s)")
        
        fixes = apply_fixes(filepath, file_errors)
        if fixes > 0:
            total_fixes += fixes
            files_fixed += 1
    
    print(f"\n{'=' * 80}")
    print("📊 SUMMARY")
    print(f"{'=' * 80}")
    print(f"Files processed: {len(by_file)}")
    print(f"Files fixed:     {files_fixed}")
    print(f"Total fixes:     {total_fixes}")
    print(f"Success rate:    {(total_fixes / len(errors) * 100):.1f}%")
    print(f"\n💾 Backups: .backup_syntax3")
    print(f"✅ Re-run checker to verify")
    print(f"{'=' * 80}\n")


if __name__ == '__main__':
    main()

