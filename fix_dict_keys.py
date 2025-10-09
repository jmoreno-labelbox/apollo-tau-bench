#!/usr/bin/env python3
"""
Fix dictionary keys that were incorrectly converted to {key}: format.
They should be "key": format.
"""

import re

def fix_dict_keys(content):
    """
    Fix patterns like:
    {key}: value -> "key": value
    This should only apply to dictionary keys, not dict values
    """
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Pattern: {identifier}: (where identifier can contain letters, numbers, underscores)
        # This pattern matches dictionary keys that are incorrectly formatted
        # We need to be careful to only match keys, not values
        
        # Look for patterns like:
        # {name}: "value"
        # {outputs}: [
        # {annotator}: 0
        
        # Pattern: whitespace + {identifier}: + anything
        # Check if line has the pattern
        match = re.match(r'^(\s*){([a-zA-Z_][a-zA-Z0-9_]*)}:\s*(.*)$', line)
        if match:
            indent = match.group(1)
            key = match.group(2)
            rest = match.group(3)
            line = f'{indent}"{key}": {rest}'
        else:
            # Also check for patterns in the middle of lines (less common)
            # Like: }, {key}: value
            line = re.sub(r'([,\s]){([a-zA-Z_][a-zA-Z0-9_]*)}:\s*', r'\1"\2": ', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_malformed_dict_values(content):
    """
    Fix malformed dict values that have backslash escapes in the wrong place.
    Pattern: {key}: \\value\", ...
    Should be: "key": "value", ...
    """
    # Fix patterns like: {account_id}: \acc_chk_1001\", \"balance\": 5230.5
    # This is: {key}: \text\", \"key2\": value
    # Should be: "key": "text", "key2": value
    
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Pattern: {key}: \text\"
        # This happens when the value was partially unescaped
        
        # Look for: : \text\"
        # Replace with: : "text"
        line = re.sub(r':\s*\\([^\\]+)\\",\s*\\"', r': "\1", "', line)
        
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
        content = fix_dict_keys(content)
        content = fix_malformed_dict_values(content)
        
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
    print("FIXING DICTIONARY KEYS")
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

