#!/usr/bin/env python3
"""
Fix '(' was never closed errors - add missing ) at end of lines
"""

from pathlib import Path

# Map of env -> (line_num, expected_fix)
FIXES = {
    'airline_1': (1521, '.values()', '.values())'),
    'consulting_accounting_1': (900, '.values()', '.values())'),
    'consulting_accounting_4': (1060, None, None),  # Needs manual check
    'dev_ops_2': (121, '.values()', '.values())'),
    'dev_ops_5': (2629, None, None),  # Needs manual check (has + 1 at end)
    'figma_gmail_mcp_pipeline_3': (116, '.values()', '.values())'),
    'file_system_7': (34, '.values()', '.values())'),
    'github_mcp_2': (685, '.values()', '.values())'),
    'new_hire_mcp_2': (None, None, None),
    'new_hire_mcp_4': (None, None, None),
    'new_hire_mcp_5': (None, None, None),
    'real_estate_sales_1': (None, None, None),
    'real_estate_sales_3': (None, None, None),
    'real_estate_sales_4': (None, None, None),
    'recipes_5': (None, None, None),
    'retail_6': (None, None, None),
}

def fix_line_in_file(file_path, line_num, old_ending, new_ending):
    """Replace old_ending with new_ending on a specific line"""
    lines = file_path.read_text().splitlines(keepends=True)
    
    if line_num <= len(lines):
        line = lines[line_num - 1]
        if old_ending in line:
            lines[line_num - 1] = line.replace(old_ending, new_ending)
            file_path.write_text(''.join(lines))
            return True
    
    return False

def main():
    base = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    print("=" * 70)
    print("FIXING UNCLOSED '(' ERRORS")
    print("=" * 70)
    print()
    
    fixed_count = 0
    for env, (line_num, old, new) in FIXES.items():
        if line_num is None or old is None or new is None:
            print(f"⚠️  {env}: Needs manual check")
            continue
            
        tools_file = base / env / "tools.py"
        if tools_file.exists():
            if fix_line_in_file(tools_file, line_num, old, new):
                print(f"✅ {env}: Line {line_num}")
                fixed_count += 1
            else:
                print(f"❌ {env}: Pattern not found on line {line_num}")
        else:
            print(f"❌ {env}: File not found")
    
    print()
    print("=" * 70)
    print(f"FIXED {fixed_count} FILES")
    print("=" * 70)

if __name__ == "__main__":
    main()

