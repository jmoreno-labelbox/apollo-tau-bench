#!/usr/bin/env python3
"""
Fix missing variable references after kwargs refactoring.
Specifically handles _validate_inputs(kwargs, ...) calls where kwargs no longer exists.
"""

import argparse
import ast
import re
import sys
from pathlib import Path
from typing import List, Set


def extract_invoke_params(source: str) -> List[str]:
    """Extract parameter names from invoke() function signature."""
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "invoke":
                params = []
                # Skip 'data' and 'self' parameters
                for arg in node.args.args:
                    if arg.arg not in ('self', 'data'):
                        params.append(arg.arg)
                return params
    except:
        pass
    return []


def fix_validate_inputs_call(source: str) -> str:
    """
    Fix _validate_inputs(kwargs, ...) calls by replacing with explicit param dict.
    """
    lines = source.split('\n')
    
    # Find invoke function and extract its parameters
    invoke_params = extract_invoke_params(source)
    if not invoke_params:
        return source  # No params to fix
    
    # Build the kwargs dict string
    kwargs_dict_items = [f'"{param}": {param}' for param in invoke_params]
    kwargs_dict = '{' + ', '.join(kwargs_dict_items) + '}'
    
    # Find and replace _validate_inputs(kwargs, ...) calls
    result_lines = []
    for line in lines:
        # Pattern: _validate_inputs(kwargs, param_definitions)
        if '_validate_inputs(kwargs,' in line:
            # Replace kwargs with the explicit dict
            new_line = line.replace('_validate_inputs(kwargs,', f'_validate_inputs({kwargs_dict},')
            result_lines.append(new_line)
        else:
            result_lines.append(line)
    
    return '\n'.join(result_lines)


def add_error_messages_if_missing(source: str) -> str:
    """Add ERROR_MESSAGES constant if it's referenced but not defined."""
    if 'ERROR_MESSAGES' in source and 'ERROR_MESSAGES = {' not in source:
        # Find a good place to insert it (after imports, before first class/function)
        lines = source.split('\n')
        insert_idx = 0
        
        # Find last import or first empty line after imports
        for i, line in enumerate(lines):
            if line.strip().startswith(('import ', 'from ')):
                insert_idx = i + 1
            elif insert_idx > 0 and not line.strip():
                insert_idx = i + 1
                break
        
        error_messages = '''
ERROR_MESSAGES = {
    "REQUIRED_PARAMETER": "Required parameter '{param}' is missing.",
    "INVALID_PARAMETER_TYPE": "Parameter '{param}' must be of type {expected_type}.",
    "NOT_FOUND": "{entity} with ID {entity_id} not found.",
    "OPERATION_FAILED": "Operation failed: {reason}",
}
'''
        lines.insert(insert_idx, error_messages)
        return '\n'.join(lines)
    
    return source


def fix_file(file_path: Path) -> bool:
    """Fix a single file. Returns True if modified."""
    try:
        source = file_path.read_text(encoding='utf-8')
        original = source
        
        # Apply fixes
        source = fix_validate_inputs_call(source)
        source = add_error_messages_if_missing(source)
        
        if source != original:
            file_path.write_text(source, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="File or directory to fix")
    args = parser.parse_args()
    
    path = Path(args.path)
    
    if path.is_file():
        files = [path]
    else:
        files = list(path.rglob("*.py"))
    
    modified_count = 0
    for file_path in files:
        if fix_file(file_path):
            print(f"✓ {file_path}")
            modified_count += 1
        else:
            print(f"- {file_path}")
    
    print(f"\nModified {modified_count}/{len(files)} files")


if __name__ == "__main__":
    main()

