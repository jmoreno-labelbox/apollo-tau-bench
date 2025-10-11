#!/usr/bin/env python3
"""
Robust kwargs refactoring - preserves all kwargs.get() calls but adds parameters.
Converts: def invoke(data, **kwargs) -> def invoke(data, key1=None, key2=None)
And leaves: key1 = kwargs.get("key1") -> key1 = key1 (which simplifies to just using key1)
"""

import argparse
import ast
import re
import sys
from typing import Set, Optional


def normalize_param_name(name: str) -> str:
    """Convert parameter name to valid Python identifier."""
    # Replace spaces and special chars with underscores
    name = re.sub(r'[^\w]', '_', name)
    # Ensure it doesn't start with a number
    if name and name[0].isdigit():
        name = '_' + name
    return name


def extract_kwargs_keys(source: str, kwargs_name: str) -> Set[str]:
    """Extract all unique keys accessed from kwargs."""
    try:
        tree = ast.parse(source)
    except:
        return set()
    
    keys = set()
    
    for node in ast.walk(tree):
        # kwargs.get("key", ...)
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


def find_kwargs_param_name(source: str) -> Optional[str]:
    """Find **kwargs parameter name in invoke function."""
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "invoke":
                if node.args.kwarg:
                    return node.args.kwarg.arg
    except:
        pass
    return None


def refactor_file(source: str) -> str:
    """Refactor invoke() function to use explicit parameters."""
    
    kwargs_name = find_kwargs_param_name(source)
    if not kwargs_name:
        return source
    
    keys = extract_kwargs_keys(source, kwargs_name)
    if not keys:
        # Just remove unused **kwargs
        source = re.sub(
            r',\s*\*\*' + re.escape(kwargs_name) + r'\s*\)',
            ')',
            source
        )
        return source
    
    # Create normalized parameter names
    param_mapping = {}  # original_key -> normalized_param_name
    for key in keys:
        normalized = normalize_param_name(key)
        param_mapping[key] = normalized
    
    # Build parameter list string
    params_list = ", ".join(f"{param}=None" for param in sorted(set(param_mapping.values())))
    
    # Step 1: Replace **kwargs in signature
    # Match: def invoke(data: Dict[str, Any], **kwargs) -> str:
    pattern = r'(def\s+invoke\s*\([^)]*?),\s*\*\*' + re.escape(kwargs_name) + r'\s*\)'
    replacement = r'\1, ' + params_list + ')'
    source = re.sub(pattern, replacement, source, count=1)
    
    # Step 2: Replace kwargs.get("key") with the parameter name
    # Sort by length (longest first) to avoid partial replacements
    sorted_keys = sorted(keys, key=len, reverse=True)
    
    for original_key in sorted_keys:
        param_name = param_mapping[original_key]
        escaped_key = re.escape(original_key)
        escaped_kwargs = re.escape(kwargs_name)
        
        # Pattern: kwargs.get("key", default) -> param_name if param_name is not None else default
        # But for simplicity: kwargs.get("key", default) -> (param_name if param_name is not None else default)
        # Actually even simpler: just use param_name since we set all defaults to None
        
        # First handle kwargs.get("key", default)
        pattern = escaped_kwargs + r'\.get\(\s*["\']' + escaped_key + r'["\']\s*,\s*([^)]+)\)'
        replacement = f'({param_name} if {param_name} is not None else \\1)'
        source = re.sub(pattern, replacement, source)
        
        # Then handle kwargs.get("key") without default
        pattern = escaped_kwargs + r'\.get\(\s*["\']' + escaped_key + r'["\']\s*\)'
        source = re.sub(pattern, param_name, source)
        
        # Handle kwargs["key"]
        pattern = escaped_kwargs + r'\[\s*["\']' + escaped_key + r'["\']\s*\]'
        source = re.sub(pattern, param_name, source)
    
    return source


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


if __name__ == "__main__":
    main()

