#!/usr/bin/env python3
"""
Fixed version - handles each invoke() function separately in files with multiple classes.
"""

import argparse
import ast
import re
import sys
from typing import Set, Optional, List, Tuple


def normalize_param_name(name: str) -> str:
    """Convert parameter name to valid Python identifier."""
    name = re.sub(r'[^\w]', '_', name)
    if name and name[0].isdigit():
        name = '_' + name
    return name


class InvokeRefactorer:
    """Refactor a single invoke function."""
    
    def __init__(self, source: str, start_line: int, end_line: int, kwargs_name: str):
        self.source = source
        self.start_line = start_line
        self.end_line = end_line
        self.kwargs_name = kwargs_name
        self.keys = set()
    
    def extract_keys(self):
        """Extract kwargs keys used within this specific function."""
        # Get just the function source
        lines = self.source.split('\n')
        func_source = '\n'.join(lines[self.start_line-1:self.end_line])
        
        try:
            tree = ast.parse(func_source)
            for node in ast.walk(tree):
                # kwargs.get("key")
                if isinstance(node, ast.Call):
                    if (isinstance(node.func, ast.Attribute) and
                        node.func.attr == "get" and
                        isinstance(node.func.value, ast.Name) and
                        node.func.value.id == self.kwargs_name):
                        if node.args and isinstance(node.args[0], ast.Constant):
                            self.keys.add(str(node.args[0].value))
                
                # kwargs["key"]
                elif isinstance(node, ast.Subscript):
                    if (isinstance(node.value, ast.Name) and
                        node.value.id == self.kwargs_name and
                        isinstance(node.slice, ast.Constant)):
                        self.keys.add(str(node.slice.value))
        except:
            pass


def find_all_invoke_functions(source: str) -> List[Tuple[int, int, Optional[str]]]:
    """
    Find all invoke() functions and their line ranges and **kwargs parameter name.
    Returns: [(start_line, end_line, kwargs_name), ...]
    """
    results = []
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "invoke":
                kwargs_name = None
                if node.args.kwarg:
                    kwargs_name = node.args.kwarg.arg
                if kwargs_name:  # Only process if it has **kwargs
                    start_line = node.lineno
                    end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 50
                    results.append((start_line, end_line, kwargs_name))
    except:
        pass
    return results


def refactor_file(source: str) -> str:
    """Refactor all invoke() functions in the file."""
    
    invoke_funcs = find_all_invoke_functions(source)
    if not invoke_funcs:
        return source
    
    # Process each invoke function from bottom to top (to preserve line numbers)
    for start_line, end_line, kwargs_name in reversed(invoke_funcs):
        refactorer = InvokeRefactorer(source, start_line, end_line, kwargs_name)
        refactorer.extract_keys()
        
        if not refactorer.keys:
            # Just remove **kwargs
            lines = source.split('\n')
            sig_line = lines[start_line - 1]
            sig_line = re.sub(r',\s*\*\*' + re.escape(kwargs_name) + r'\s*\)', ')', sig_line)
            lines[start_line - 1] = sig_line
            source = '\n'.join(lines)
            continue
        
        # Create parameters
        param_mapping = {key: normalize_param_name(key) for key in refactorer.keys}
        params_list = ", ".join(f"{param}=None" for param in sorted(set(param_mapping.values())))
        
        # Get the function source
        lines = source.split('\n')
        func_lines = lines[start_line-1:end_line]
        func_source = '\n'.join(func_lines)
        
        # Replace signature
        pattern = r'(def\s+invoke\s*\([^)]*?),\s*\*\*' + re.escape(kwargs_name) + r'\s*\)'
        replacement = r'\1, ' + params_list + ')'
        func_source = re.sub(pattern, replacement, func_source, count=1)
        
        # Replace kwargs.get() calls - longest first
        sorted_keys = sorted(refactorer.keys, key=len, reverse=True)
        for original_key in sorted_keys:
            param_name = param_mapping[original_key]
            escaped_key = re.escape(original_key)
            escaped_kwargs = re.escape(kwargs_name)
            
            # kwargs.get("key", default)
            pattern = escaped_kwargs + r'\.get\(\s*["\']' + escaped_key + r'["\']\s*,\s*([^)]+)\)'
            replacement = f'({param_name} if {param_name} is not None else \\1)'
            func_source = re.sub(pattern, replacement, func_source)
            
            # kwargs.get("key")
            pattern = escaped_kwargs + r'\.get\(\s*["\']' + escaped_key + r'["\']\s*\)'
            func_source = re.sub(pattern, param_name, func_source)
            
            # kwargs["key"]
            pattern = escaped_kwargs + r'\[\s*["\']' + escaped_key + r'["\']\s*\]'
            func_source = re.sub(pattern, param_name, func_source)
        
        # Replace in source
        lines[start_line-1:end_line] = func_source.split('\n')
        source = '\n'.join(lines)
    
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
        sys.exit(1)


if __name__ == "__main__":
    main()

