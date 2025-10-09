#!/usr/bin/env python3
"""
Fix malformed outputs arrays in task files.
"""

import re

def fix_outputs_in_airline_retail(content, filename):
    """
    Fix outputs arrays in airline and retail files where items are like:
    {key:value:more:values} -> "key:value:more:values"
    """
    if 'airline' not in filename and 'retail' not in filename:
        return content
    
    lines = content.split('\n')
    fixed_lines = []
    in_outputs = False
    
    for line in lines:
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
        
        # If we're in an outputs array, fix the items
        if in_outputs:
            # Pattern: {identifier:value:more:values} -> "identifier:value:more:values"
            match = re.match(r'^(\s*)\{([^}]+)\}(,?)$', line)
            if match:
                indent = match.group(1)
                content_str = match.group(2)
                comma = match.group(3)
                line = f'{indent}"{content_str}"{comma}'
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_escaped_quotes_in_outputs(content):
    """
    Fix partially escaped quotes in outputs arrays like:
    "key": "value", "balance\": 5230.5 -> {"key": "value", "balance": 5230.5}
    """
    lines = content.split('\n')
    fixed_lines = []
    in_outputs = False
    
    for line in lines:
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
        
        # If we're in an outputs array, fix the items
        if in_outputs:
            # Fix escaped quotes: \"key\" -> "key"
            line = re.sub(r'\\"', '"', line)
            
            # If the line has key-value pairs but no opening brace, add braces
            # Pattern: spaces + "key": value, "key2": value,
            if re.match(r'^\s+"[^"]+":.*,\s*$', line):
                # Check if it doesn't already start with {
                if not re.match(r'^\s*\{', line):
                    # Add braces around the content
                    match = re.match(r'^(\s+)(.+)(,\s*)$', line)
                    if match:
                        indent = match.group(1)
                        content_str = match.group(2).rstrip(',').strip()
                        line = f'{indent}{{{content_str}}},'
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_file(filepath):
    """Fix a single file."""
    print(f"\nProcessing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        content = original_content
        
        # Apply fixes
        content = fix_outputs_in_airline_retail(content, filepath)
        content = fix_escaped_quotes_in_outputs(content)
        
        # Check if changes were made
        if content != original_content:
            orig_lines = original_content.split('\n')
            new_lines = content.split('\n')
            changes = sum(1 for o, n in zip(orig_lines, new_lines) if o != n)
            
            print(f"  ✓ Fixed {changes} lines")
            
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
    print("FIXING OUTPUTS ARRAYS")
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

