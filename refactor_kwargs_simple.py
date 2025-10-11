#!/usr/bin/env python3
"""
Simple line-based refactoring - process each invoke function independently.
"""

import argparse
import re
import sys
from typing import Set, Dict


def normalize_param_name(name: str) -> str:
    """Convert to valid Python identifier."""
    name = re.sub(r'[^\w]', '_', name)
    if name and name[0].isdigit():
        name = '_' + name
    return name


def extract_kwargs_keys(text: str, kwargs_name: str) -> Set[str]:
    """Extract all kwargs.get() keys from text."""
    keys = set()
    
    # Pattern: kwargs.get("key"
    pattern = re.escape(kwargs_name) + r'\.get\(\s*["\']([^"\']+)["\']'
    for match in re.finditer(pattern, text):
        keys.add(match.group(1))
    
    # Pattern: kwargs["key"]
    pattern = re.escape(kwargs_name) + r'\[\s*["\']([^"\']+)["\']\s*\]'
    for match in re.finditer(pattern, text):
        keys.add(match.group(1))
    
    return keys


def refactor_single_function(func_text: str, kwargs_name: str) -> str:
    """Refactor a single invoke function."""
    
    # Extract keys used in this function
    keys = extract_kwargs_keys(func_text, kwargs_name)
    
    if not keys:
        # Just remove **kwargs
        func_text = re.sub(
            r',\s*\*\*' + re.escape(kwargs_name) + r'\s*\)',
            ')',
            func_text,
            count=1
        )
        return func_text
    
    # Create parameter mapping
    param_mapping = {key: normalize_param_name(key) for key in keys}
    params_list = ", ".join(f"{param}=None" for param in sorted(set(param_mapping.values())))
    
    # Replace **kwargs in signature (only first occurrence)
    func_text = re.sub(
        r',\s*\*\*' + re.escape(kwargs_name) + r'\s*\)',
        f', {params_list})',
        func_text,
        count=1
    )
    
    # Replace kwargs.get() calls - longest keys first
    for original_key in sorted(keys, key=len, reverse=True):
        param_name = param_mapping[original_key]
        escaped_key = re.escape(original_key)
        escaped_kwargs = re.escape(kwargs_name)
        
        # kwargs.get("key", default)
        pattern = escaped_kwargs + r'\.get\(\s*["\']' + escaped_key + r'["\']\s*,\s*([^)]+)\)'
        replacement = f'({param_name} if {param_name} is not None else \\1)'
        func_text = re.sub(pattern, replacement, func_text)
        
        # kwargs.get("key")
        pattern = escaped_kwargs + r'\.get\(\s*["\']' + escaped_key + r'["\']\s*\)'
        func_text = re.sub(pattern, param_name, func_text)
        
        # kwargs["key"]
        pattern = escaped_kwargs + r'\[\s*["\']' + escaped_key + r'["\']\s*\]'
        func_text = re.sub(pattern, param_name, func_text)
    
    return func_text


def refactor_file(source: str) -> str:
    """Process file by finding each invoke function and refactoring it."""
    
    # Find all def invoke(..., **kwargs patterns
    lines = source.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line has "def invoke" with **kwargs
        if re.search(r'def\s+invoke\s*\([^)]*\*\*\w+\s*\)', line):
            # Extract kwargs_name
            match = re.search(r'\*\*(\w+)', line)
            if match:
                kwargs_name = match.group(1)
                
                # Find the end of this function (next def or class, or end of file)
                func_start = i
                func_end = i + 1
                
                # Simple heuristic: find next line at same or lower indentation with 'def ' or 'class '
                base_indent = len(line) - len(line.lstrip())
                
                while func_end < len(lines):
                    next_line = lines[func_end]
                    if next_line.strip():  # Non-empty line
                        next_indent = len(next_line) - len(next_line.lstrip())
                        if next_indent <= base_indent and (next_line.lstrip().startswith('def ') or 
                                                          next_line.lstrip().startswith('class ') or
                                                          next_line.lstrip().startswith('@')):
                            break
                    func_end += 1
                
                # Extract and refactor this function
                func_lines = lines[func_start:func_end]
                func_text = '\n'.join(func_lines)
                refactored = refactor_single_function(func_text, kwargs_name)
                
                # Replace in source
                refactored_lines = refactored.split('\n')
                lines[func_start:func_end] = refactored_lines
                
                # Continue from after this function
                i = func_start + len(refactored_lines)
                continue
        
        i += 1
    
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

