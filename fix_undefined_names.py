#!/usr/bin/env python3
"""
Fix undefined name errors in tool files.
Handles: load_json, kwargs, and other missing imports/functions.
"""

import ast
from pathlib import Path
import sys

def find_undefined_names(file_path: Path):
    """Find undefined names in a file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        tree = ast.parse(content)
        
        defined = set()
        referenced = set()
        
        # Collect defined names
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                defined.add(node.name)
            elif isinstance(node, ast.ClassDef):
                defined.add(node.name)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    defined.add(alias.asname if alias.asname else alias.name)
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    defined.add(alias.asname if alias.asname else alias.name)
        
        # Collect referenced names
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                referenced.add(node.id)
        
        # Undefined = referenced but not defined
        undefined = referenced - defined
        
        # Filter out builtins
        builtins = {'str', 'int', 'list', 'dict', 'set', 'tuple', 'bool', 'None', 'True', 'False', 
                   'len', 'range', 'enumerate', 'isinstance', 'any', 'all', 'max', 'min', 'sum'}
        undefined = undefined - builtins
        
        return undefined
        
    except Exception as e:
        return set()

def fix_load_json(file_path: Path):
    """Add import json if load_json is used but not defined."""
    content = file_path.read_text(encoding='utf-8')
    
    if 'load_json' in content and 'import json' not in content:
        # Add import json at the top
        lines = content.split('\n')
        
        # Find where to insert (after existing imports or at start)
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('import ') or line.startswith('from '):
                insert_idx = i + 1
        
        lines.insert(insert_idx, 'import json')
        file_path.write_text('\n'.join(lines), encoding='utf-8')
        return True
    
    return False

def fix_kwargs_not_defined(file_path: Path):
    """Fix cases where kwargs is used but not in function signature."""
    content = file_path.read_text(encoding='utf-8')
    
    # If kwargs.get() is used but function doesn't have **kwargs
    if 'kwargs.get(' in content or 'kwargs[' in content:
        lines = content.split('\n')
        fixed = False
        
        for i, line in enumerate(lines):
            # Find function definitions
            if 'def invoke(' in line and '**kwargs' not in line:
                # Add **kwargs to signature
                if line.rstrip().endswith('):'):
                    # Replace ): with , **kwargs):
                    lines[i] = line.rstrip()[:-2] + ', **kwargs):'
                    fixed = True
                    print(f"  Added **kwargs to function at line {i+1}")
        
        if fixed:
            file_path.write_text('\n'.join(lines), encoding='utf-8')
            return True
    
    return False

def process_env(env_dir: Path):
    """Process all tool files in an environment."""
    changes = 0
    
    # Check main tools.py
    tools_py = env_dir / "tools.py"
    if tools_py.exists():
        undefined = find_undefined_names(tools_py)
        
        if 'load_json' in undefined:
            if fix_load_json(tools_py):
                print(f"  Fixed load_json in {tools_py.name}")
                changes += 1
        
        if 'kwargs' in undefined:
            if fix_kwargs_not_defined(tools_py):
                print(f"  Fixed kwargs in {tools_py.name}")
                changes += 1
    
    # Check individual tool files
    tools_dir = env_dir / "tools"
    if tools_dir.exists():
        for tool_file in tools_dir.glob("*.py"):
            if tool_file.name == '__init__.py':
                continue
            
            undefined = find_undefined_names(tool_file)
            
            if 'load_json' in undefined:
                if fix_load_json(tool_file):
                    print(f"  Fixed load_json in tools/{tool_file.name}")
                    changes += 1
            
            if 'kwargs' in undefined:
                if fix_kwargs_not_defined(tool_file):
                    print(f"  Fixed kwargs in tools/{tool_file.name}")
                    changes += 1
    
    return changes

def main():
    # Target environments with undefined name errors
    envs_to_fix = [
        'banking_services_1',
        'banking_services_4',
        'recipes_4'
    ]
    
    tau_envs = Path("tau/tau_bench/envs")
    
    print("Fixing undefined name errors\n")
    print("="*60)
    
    total_changes = 0
    
    for env_name in envs_to_fix:
        env_dir = tau_envs / env_name
        if not env_dir.exists():
            print(f"✗ {env_name}: not found")
            continue
        
        print(f"\n{env_name}:")
        changes = process_env(env_dir)
        total_changes += changes
        
        if changes == 0:
            print(f"  No changes needed")
    
    print(f"\n{'='*60}")
    print(f"Total fixes applied: {total_changes}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

