#!/usr/bin/env python3
"""
Find and fix all outputs array items that are missing braces.
"""

import re

def fix_unbraced_output_items(content):
    """
    Fix outputs array items that are missing braces.
    Pattern: spaces + "key": "value" (without surrounding braces)
    Fix: spaces + {"key": "value"}
    """
    lines = content.split('\n')
    fixed_lines = []
    in_outputs = False
    fixed_count = 0
    
    for i, line in enumerate(lines):
        # Detect if we're entering an outputs array
        if re.search(r'"outputs":\s*\[', line):
            in_outputs = True
            fixed_lines.append(line)
            continue
        
        # Detect if we're exiting an outputs array
        if in_outputs and re.match(r'\s*\]', line):
            in_outputs = False
            fixed_lines.append(line)
            continue
        
        # If we're in an outputs array, check if the line needs fixing
        if in_outputs:
            # Check if line starts with spaces + " (not spaces + {)
            # Pattern: spaces + "key": value (where value can be string, number, etc.)
            match = re.match(r'^(\s+)"([^"]+)":\s*(.+)$', line)
            if match and not line.strip().startswith('{'):
                indent = match.group(1)
                key = match.group(2)
                value = match.group(3)
                
                # Check if value ends with a comma
                if value.endswith(','):
                    value = value[:-1]
                    line = f'{indent}{{"{key}": {value}}},'
                else:
                    line = f'{indent}{{"{key}": {value}}}'
                
                fixed_count += 1
                print(f"  Line {i+1}: Fixed unbraced output item")
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), fixed_count

def fix_file(filepath):
    """Fix a single file."""
    print(f"\nProcessing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        content, fixed_count = fix_unbraced_output_items(original_content)
        
        if content != original_content:
            print(f"  ✓ Fixed {fixed_count} unbraced output items")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✅ File updated successfully")
            return True
        else:
            print(f"  ℹ️  No changes needed")
            return False
            
    except Exception as e:
        print(f"  ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function."""
    files_to_fix = [
        "tau/tau_bench/envs/airline_3/tasks.py",
        "tau/tau_bench/envs/retail_2/tasks.py",
        "tau/tau_bench/envs/banking_services_6/tasks.py",
        "tau/tau_bench/envs/github_mcp_2/tasks.py",
    ]
    
    print("=" * 80)
    print("FIXING UNBRACED OUTPUT ITEMS")
    print("=" * 80)
    
    fixed_count = 0
    for filepath in files_to_fix:
        if fix_file(filepath):
            fixed_count += 1
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: Fixed {fixed_count} out of {len(files_to_fix)} files")
    print("=" * 80)

if __name__ == "__main__":
    main()

