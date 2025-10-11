#!/usr/bin/env python3
"""
AST-based refactoring that properly handles each invoke method separately.
"""

import argparse
import ast
import re
import sys
from typing import Set


def normalize_param_name(name: str) -> str:
    """Convert to valid Python identifier."""
    name = re.sub(r'[^\w]', '_', name)
    if name and name[0].isdigit():
        name = '_' + name
    return name


def extract_kwargs_from_function_ast(func_node: ast.FunctionDef, kwargs_name: str) -> Set[str]:
    """Extract kwargs keys from a specific function AST node."""
    keys = set()
    
    for node in ast.walk(func_node):
        # kwargs.get("key")
        if isinstance(node, ast.Call):
            if (isinstance(node.func, ast.Attribute) and
                node.func.attr == "get" and
                isinstance(node.func.value, ast.Name) and
                node.func.value.id == kwargs_name):
                if node.args and isinstance(node.args[0], ast.Constant):
                    keys.add(str(node.args[0].value))
        
        # kwargs["key"]
        elif isinstance(node, ast.Subscript):
            if (isinstance(node.value, ast.Name) and
                node.value.id == kwargs_name and
                isinstance(node.slice, ast.Constant)):
                keys.add(str(node.slice.value))
    
    return keys


def refactor_file(source: str) -> str:
    """Refactor file using AST to properly scope each function."""
    
    try:
        tree = ast.parse(source)
    except:
        return source
    
    # Find all invoke functions with their source locations and kwargs usage
    refactorings = []  # List of (line_num, old_sig, new_sig, kwargs_name, keys)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "invoke":
            if node.args.kwarg:
                kwargs_name = node.args.kwarg.arg
                keys = extract_kwargs_from_function_ast(node, kwargs_name)
                
                # Get the line with the function signature
                line_num = node.lineno
                refactorings.append((line_num, kwargs_name, keys))
    
    if not refactorings:
        return source
    
    # Apply refactorings from bottom to top (preserve line numbers)
    lines = source.split('\n')
    
    for line_num, kwargs_name, keys in reversed(sorted(refactorings)):
        line_idx = line_num - 1
        original_line = lines[line_idx]
        
        # Check if this line actually has the def invoke signature
        if 'def invoke' not in original_line:
            continue
        
        if not keys:
            # Just remove **kwargs
            new_line = re.sub(
                r',\s*\*\*' + re.escape(kwargs_name) + r'\s*\)',
                ')',
                original_line
            )
            lines[line_idx] = new_line
        else:
            # Add explicit parameters
            param_mapping = {key: normalize_param_name(key) for key in keys}
            params_list = ", ".join(f"{param}=None" for param in sorted(set(param_mapping.values())))
            
            new_line = re.sub(
                r',\s*\*\*' + re.escape(kwargs_name) + r'\s*\)',
                f', {params_list})',
                original_line
            )
            lines[line_idx] = new_line
            
            # Now replace kwargs.get() usage in the function body
            # Find the function body (all indented lines after the def until next def/class)
            func_indent = len(original_line) - len(original_line.lstrip())
            body_start = line_idx + 1
            body_end = body_start
            
            while body_end < len(lines):
                line = lines[body_end]
                if line.strip():
                    line_indent = len(line) - len(line.lstrip())
                    if line_indent <= func_indent and (line.lstrip().startswith('def ') or 
                                                       line.lstrip().startswith('class ') or
                                                       line.lstrip().startswith('@')):
                        break
                body_end += 1
            
            # Replace kwargs.get() in body
            for original_key in sorted(keys, key=len, reverse=True):
                param_name = param_mapping[original_key]
                escaped_key = re.escape(original_key)
                escaped_kwargs = re.escape(kwargs_name)
                
                for i in range(body_start, body_end):
                    # kwargs.get("key", default)
                    pattern = escaped_kwargs + r'\.get\(\s*["\']' + escaped_key + r'["\']\s*,\s*([^)]+)\)'
                    replacement = f'({param_name} if {param_name} is not None else \\1)'
                    lines[i] = re.sub(pattern, replacement, lines[i])
                    
                    # kwargs.get("key")
                    pattern = escaped_kwargs + r'\.get\(\s*["\']' + escaped_key + r'["\']\s*\)'
                    lines[i] = re.sub(pattern, param_name, lines[i])
                    
                    # kwargs["key"]
                    pattern = escaped_kwargs + r'\[\s*["\']' + escaped_key + r'["\']\s*\]'
                    lines[i] = re.sub(pattern, param_name, lines[i])
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()
    
    try:
        with open(args.path, "r") as f:
            original = f.read()
        
        refactored = refactor_file(original)
        
        if args.stdout:
            print(refactored)
        else:
            if refactored != original:
                with open(args.path, "w") as f:
                    f.write(refactored)
                print(f"✓ {args.path}")
            else:
                print(f"- {args.path}")
    except Exception as e:
        print(f"✗ {args.path}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

