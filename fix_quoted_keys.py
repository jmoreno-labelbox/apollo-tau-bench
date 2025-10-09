#!/usr/bin/env python3
"""
Fix improperly quoted keys and values in Python dictionary structures.
Transforms patterns like:
  "\"name\": \"value\"" -> "name": "value"
"""

import re
import sys

def fix_escaped_quotes_in_dicts(content):
    """
    Fix patterns like:
    "\"name\": \"value\"" -> "name": "value"
    "\"key\": value" -> "key": value
    """
    # This pattern matches strings like: "\"key\": \"value\""
    # and converts them to: "key": "value"
    
    # Pattern: "\"{escaped_content}\"" -> "{unescaped_content}"
    # We need to be careful to only match these within dictionary contexts
    
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        original_line = line
        
        # Check if this line contains the pattern "\"...\"..."
        # Common patterns:
        # 1. "\"key\": \"value\"" -> "key": "value"
        # 2. "\"key\": value" -> "key": value  (where value is not a string)
        
        # Pattern 1: Full string key-value pair
        # "\"crew_id\": \"CM015\""  ->  "crew_id": "CM015"
        line = re.sub(r'"\\"([^"\\]+)\\":\s*\\"([^"\\]+)\\""', r'"\1": "\2"', line)
        
        # Pattern 2: String key with non-string value
        # "\"annotator\": 0" -> "annotator": 0
        line = re.sub(r'"\\"([^"\\]+)\\":\s*([^",}\]]+)"', r'"\1": \2', line)
        
        # Pattern 3: If the line still has just a closing quote
        # Sometimes we have: "\"key\": value",  where value itself needs no quotes
        # This is already handled by pattern 2
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_malformed_outputs(content):
    """
    Fix malformed outputs arrays like:
    "\"type\": \"Work\", "number": \"098-765-4741\""
    ->
    {"type": "Work", "number": "098-765-4741"}
    """
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Check if we're in an outputs array and have a malformed entry
        # Pattern: spaces + "\"key\": \"value\", "key2": ...
        match = re.match(r'^(\s+)"(\\"[^"]+\\": \\"[^"]+\\"|[^"]+)"(.*)$', line)
        if match:
            indent = match.group(1)
            content_str = match.group(2)
            rest = match.group(3)
            
            # Remove the outer quotes and unescape
            content_str = content_str.replace('\\"', '"')
            
            # Remove outer quotes if present
            if content_str.startswith('"') and content_str.endswith('"'):
                content_str = content_str[1:-1]
            
            # Wrap in braces
            line = f'{indent}{{{content_str}}}{rest}'
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_file(filepath):
    """Fix a single file."""
    print(f"\nProcessing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        content = original_content
        
        # Apply fixes in order
        content = fix_escaped_quotes_in_dicts(content)
        content = fix_malformed_outputs(content)
        
        # Check if changes were made
        if content != original_content:
            # Calculate number of changes
            orig_lines = original_content.split('\n')
            new_lines = content.split('\n')
            changes = sum(1 for o, n in zip(orig_lines, new_lines) if o != n)
            
            print(f"  ✓ Fixed {changes} lines")
            
            # Save the file
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
    print("FIXING QUOTED KEYS IN PYTHON FILES")
    print("=" * 80)
    
    fixed_count = 0
    for filepath in files_to_fix:
        if fix_file(filepath):
            fixed_count += 1
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: Fixed {fixed_count} out of {len(files_to_fix)} files")
    print("=" * 80)
    print("\nRun the syntax checker to verify:")
    print("  python find_unused_code.py --syntax-errors-only")

if __name__ == "__main__":
    main()
