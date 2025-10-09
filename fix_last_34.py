#!/usr/bin/env python3
"""
Final fix for the last 34 syntax errors with manual inspection of each pattern.
"""

import json
import re
import shutil


def load_errors():
    with open('syntax_errors.json', 'r') as f:
        return json.load(f)['all_errors']


def read_file(fp):
    with open(fp, 'r') as f:
        return f.readlines()


def write_file(fp, lines):
    shutil.copy2(fp, f"{fp}.backup_last")
    with open(fp, 'w') as f:
        f.writelines(lines)


def fix_line(lines, idx, error_msg):
    """Apply targeted fixes based on error pattern"""
    line = lines[idx]
    original = line
    
    # Fix 1: "key": (...values()), "next" -> "key": list(...values()), "next"
    if '.values()),' in line and ':' in line and '"' in line:
        pattern = r':\s+\(([^)]+\.values\(\))\),'
        if re.search(pattern, line):
            fixed = re.sub(pattern, r': list(\1),', line)
            if fixed != line:
                lines[idx] = fixed
                return True, "Wrapped .values() with list()"
    
    # Fix 2: _convert_db_to_list(...values() missing closing paren (deeper in file)
    if '_convert_db_to_list(' in line and '.values()' in line:
        if line.rstrip().endswith('.values()'):
            lines[idx] = line.rstrip() + ')\n'
            return True, "Added closing ) to _convert_db_to_list"
    
    # Fix 3: enumerate(...values(): missing closing paren
    if 'enumerate(' in line and '.values():' in line:
        lines[idx] = line.replace('.values():', '.values()):')
        return True, "Added closing ) to enumerate"
    
    # Fix 4: sum(...values() missing closing paren
    if 'sum(' in line and '.values()' in line and line.rstrip().endswith('.values()'):
        lines[idx] = line.rstrip() + ')\n'
        return True, "Added closing ) to sum"
    
    # Fix 5: Extra closing paren at end like :)
    if line.rstrip().endswith(':)'):
        lines[idx] = line.replace(':)', ':')
        return True, "Removed extra ) before :"
    
    # Fix 6: cid.values() + len(...) should be cid) + len(...)
    if 'cid.values()' in line and '+ len(' in line:
        lines[idx] = line.replace('cid.values()', 'cid)')
        return True, "Fixed cid.values() to cid)"
    
    # Fix 7: supplier_categories.values() and) should be supplier_categories.values()))
    if '.values() and)' in line:
        lines[idx] = line.replace('.values() and)', '.values()))')
        return True, "Fixed .values() and) to .values()))"
    
    # Fix 8: avg_order_value = () should be avg_order_value = 0 or removed
    if 'avg_order_value = ()' in line:
        lines[idx] = line.replace('avg_order_value = ()', 'avg_order_value = 0.0')
        return True, "Fixed () to 0.0"
    
    # Fix 9: if checks else False) - extra paren
    if 'if checks else False)' in line and not 'all(' in line:
        lines[idx] = line.replace('if checks else False)', 'if checks else False')
        return True, "Removed extra ) after False"
    
    # Fix 10: Missing comma before line - check previous line
    if 'Perhaps you forgot a comma' in error_msg and idx > 0:
        prev = lines[idx - 1]
        # Check if prev line ends with " without comma
        if prev.rstrip().endswith('"') and not prev.rstrip().endswith('",'):
            if '":' in prev:  # It's a dict key-value
                lines[idx - 1] = prev.rstrip() + ',\n'
                return True, "Added missing comma to previous line"
    
    # Fix 11: String literal issues - check if line has unbalanced quotes
    if 'invalid syntax' in error_msg and '"' in line:
        # shipping manager," should be "shipping manager",
        if line.strip().endswith('manager,"'):
            lines[idx] = line.replace('manager,', '"shipping manager",')
            return True, "Fixed string quote"
        # "#W4817420"," should be "#W4817420",
        if '"#W' in line and ',"' in line:
            lines[idx] = line.replace(',"', ',')
            return True, "Removed extra quote"
    
    # Fix 12: unmatched ')' at end of comprehension
    if ')' in line and 'unmatched' in error_msg:
        # Look for patterns like .values()):
        if '.values())):' in line:
            lines[idx] = line.replace('.values())):', '.values()):')
            return True, "Removed extra ) before :"
        # Just ) at end
        if line.strip() == ')':
            # Check previous line needs closing
            if idx > 0 and lines[idx-1].count('(') > lines[idx-1].count(')'):
                # The ) is actually needed, so the issue might be elsewhere
                return False, None
    
    # Fix 13: Invalid syntax on simple assignment - previous line issue
    if 'invalid syntax at "total_hours +=' in error_msg or 'invalid syntax at "member_cost =' in error_msg:
        if idx > 0:
            prev = lines[idx - 1]
            if prev.count('(') > prev.count(')'):
                lines[idx - 1] = prev.rstrip() + ')\n'
                return True, "Added closing ) to previous line"
    
    # Fix 14: Another pattern of .values() that needs list() wrap in dict context
    if '".values()),' in line and not 'list(' in line:
        # Pattern: something.get("x", {}).values()),
        pattern = r'(\w+\.get\([^)]+,\s*\{\}\)\.values\(\))\),'
        match = re.search(pattern, line)
        if match:
            old = match.group(0)
            new = 'list(' + match.group(1) + ')),'
            lines[idx] = line.replace(old, new)
            return True, "Wrapped .values() with list()"
    
    return False, None


def fix_file(filepath, errors):
    """Fix all errors in file"""
    lines = read_file(filepath)
    fixes = []
    
    # Sort by line desc to fix from bottom
    for error in sorted(errors, key=lambda x: x['line'], reverse=True):
        idx = error['line'] - 1
        fixed, msg = fix_line(lines, idx, error['error'])
        if fixed:
            fixes.append((error['line'], msg))
    
    if fixes:
        write_file(filepath, lines)
        return fixes
    return None


def main():
    print("🔧 Final Fix for Last 34 Errors")
    print("=" * 80)
    
    errors = load_errors()
    print(f"Loaded {len(errors)} errors\n")
    
    from collections import defaultdict
    by_file = defaultdict(list)
    for e in errors:
        by_file[e['filepath']].append(e)
    
    total_fixed = 0
    files_fixed = 0
    
    for fp in sorted(by_file.keys()):
        file_errors = by_file[fp]
        print(f"\n📄 {fp}")
        print(f"   {len(file_errors)} error(s)")
        
        fixes = fix_file(fp, file_errors)
        if fixes:
            files_fixed += 1
            total_fixed += len(fixes)
            for line, msg in fixes:
                print(f"   ✅ Line {line}: {msg}")
        else:
            print(f"   ⚠️  Manual review needed")
    
    print(f"\n{'=' * 80}")
    print("📊 SUMMARY")
    print(f"{'=' * 80}")
    print(f"Files processed:  {len(by_file)}")
    print(f"Files fixed:      {files_fixed}")
    print(f"Errors fixed:     {total_fixed}")
    print(f"Remaining:        {len(errors) - total_fixed}")
    print(f"Success rate:     {(total_fixed / len(errors) * 100):.1f}%")
    print(f"\n💾 Backups: .backup_last")
    print(f"✅ Re-run checker to verify")
    print(f"{'=' * 80}\n")


if __name__ == '__main__':
    main()

