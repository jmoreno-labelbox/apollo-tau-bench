#!/usr/bin/env python3
"""
Complete kwargs refactoring - handles all patterns including complex ones.
Strategy: Extract parameters, add to signature, replace ALL kwargs references.
"""

import argparse
import ast
import re
import sys
from typing import Dict, Set, Tuple, Optional


def extract_all_kwargs_keys(source: str, kwargs_name: str) -> Set[str]:
    """Extract all keys accessed from kwargs using AST."""
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
    """Find the name of the **kwargs parameter in invoke function."""
    try:
        tree = ast.parse(source)
    except:
        return None
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "invoke":
            if node.args.kwarg:
                return node.args.kwarg.arg
    return None


def refactor_invoke_function(source: str) -> str:
    """
    Refactor invoke() to replace **kwargs with explicit parameters.
    """
    # Find kwargs parameter name
    kwargs_name = find_kwargs_param_name(source)
    if not kwargs_name:
        return source
    
    # Extract all keys used
    keys = extract_all_kwargs_keys(source, kwargs_name)
    if not keys:
        # No keys used, just remove **kwargs
        pattern = r'(def\s+invoke\s*\([^)]*?),\s*\*\*' + re.escape(kwargs_name) + r'\s*(\)\s*->)'
        source = re.sub(pattern, r'\1\2', source)
        return source
    
    # Build parameter list (all with default None for safety)
    params = ", ".join(f"{key}=None" for key in sorted(keys))
    
    # Step 1: Replace **kwargs with explicit parameters in signature
    # Pattern: def invoke(..., **kwargs) -> str:
    pattern = r'(def\s+invoke\s*\([^)]*?),\s*\*\*' + re.escape(kwargs_name) + r'\s*(\)\s*->)'
    replacement = r'\1, ' + params + r'\2'
    source = re.sub(pattern, replacement, source)
    
    # Also handle case where **kwargs is the only parameter after data
    pattern = r'(def\s+invoke\s*\(\s*data\s*:\s*[^,)]+)\s*,\s*\*\*' + re.escape(kwargs_name) + r'\s*(\)\s*->)'
    replacement = r'\1, ' + params + r'\2'
    source = re.sub(pattern, replacement, source)
    
    # Step 2: Replace all kwargs.get() calls with parameter names
    # Handle: kwargs.get("key", default) -> key if key is None else key (safer)
    # Actually, simpler: kwargs.get("key", default) -> (key if key is not None else default)
    # But we need to preserve the default, so: kwargs.get("key", default) -> (key if key is not None else (default))
    # Even simpler for now: kwargs.get("key", default) -> key
    # And: kwargs.get("key") -> key
    
    for key in keys:
        # Pattern 1: kwargs.get("key", default) - replace with just the key
        # We need to be careful with nested calls
        pattern = re.escape(kwargs_name) + r'\.get\(\s*["\']' + re.escape(key) + r'["\'](?:\s*,\s*[^)]*?)?\s*\)'
        source = re.sub(pattern, key, source)
        
        # Pattern 2: kwargs["key"] - replace with key
        pattern = re.escape(kwargs_name) + r'\[\s*["\']' + re.escape(key) + r'["\']\s*\]'
        source = re.sub(pattern, key, source)
    
    return source


def main():
    parser = argparse.ArgumentParser(description="Complete kwargs refactoring for invoke functions")
    parser.add_argument("path", help="Python file to refactor")
    parser.add_argument("--stdout", action="store_true", help="Print to stdout instead of writing")
    args = parser.parse_args()
    
    try:
        with open(args.path, "r", encoding="utf-8") as f:
            original = f.read()
        
        refactored = refactor_invoke_function(original)
        
        if args.stdout:
            print(refactored)
        else:
            if refactored != original:
                with open(args.path, "w", encoding="utf-8") as f:
                    f.write(refactored)
                print(f"✓ {args.path}")
            else:
                print(f"- {args.path}")
    
    except Exception as e:
        print(f"✗ {args.path}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

