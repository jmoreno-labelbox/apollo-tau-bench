#!/usr/bin/env python3
"""
Find all undefined variables in tools.py files by analyzing variable usage
"""

from pathlib import Path
import re
import ast

def find_undefined_in_file(file_path):
    """Find variables that are used but never assigned in a file"""
    try:
        content = file_path.read_text()
        tree = ast.parse(content, filename=str(file_path))
        
        undefined = []
        
        # Walk through all functions
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Get all variable names used in this function
                used_vars = set()
                assigned_vars = set()
                
                for child in ast.walk(node):
                    # Find assignments
                    if isinstance(child, ast.Assign):
                        for target in child.targets:
                            if isinstance(target, ast.Name):
                                assigned_vars.add(target.id)
                    
                    # Find usage
                    if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load):
                        used_vars.add(child.id)
                
                # Find undefined (used but not assigned, excluding function params and builtins)
                params = {arg.arg for arg in node.args.args} if hasattr(node.args, 'args') else set()
                builtins = {'True', 'False', 'None', 'len', 'str', 'int', 'float', 'list', 'dict', 'set', 'tuple', 'range', 'enumerate', 'zip', 'sum', 'max', 'min', 'any', 'all', 'next', 'isinstance', 'bool', 'abs', 'round', 'sorted'}
                
                undefined_in_func = used_vars - assigned_vars - params - builtins
                
                if undefined_in_func:
                    for var in undefined_in_func:
                        # Get line number where it's used
                        for line_num, line in enumerate(content.split('\n'), 1):
                            if re.search(rf'\b{var}\b', line) and not re.search(rf'{var}\s*=', line):
                                undefined.append((line_num, var, node.name))
                                break
        
        return undefined
    except:
        return []

def main():
    base = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    all_undefined = []
    
    for env_dir in sorted(base.iterdir()):
        if env_dir.is_dir() and not env_dir.name.startswith('_'):
            tools_file = env_dir / "tools.py"
            if tools_file.exists():
                undefined = find_undefined_in_file(tools_file)
                if undefined:
                    for line_num, var, func_name in undefined:
                        all_undefined.append((env_dir.name, line_num, var, func_name))
    
    print("=" * 70)
    print(f"UNDEFINED VARIABLES FOUND: {len(all_undefined)}")
    print("=" * 70)
    print()
    
    # Group by variable name to see patterns
    from collections import defaultdict
    by_var = defaultdict(list)
    
    for env, line, var, func in all_undefined:
        by_var[var].append(f"{env}:{line} in {func}()")
    
    # Show most common
    for var, locs in sorted(by_var.items(), key=lambda x: len(x[1]), reverse=True)[:30]:
        print(f"{var}: {len(locs)} occurrences")
        for loc in locs[:3]:
            print(f"  {loc}")
        if len(locs) > 3:
            print(f"  ... and {len(locs) - 3} more")
        print()

if __name__ == "__main__":
    main()

