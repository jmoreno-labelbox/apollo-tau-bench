#!/usr/bin/env python3
"""
Quick script to check for missing imports in tau/**/tools/*.py files
"""

import ast
from pathlib import Path
from typing import Set, List, Dict, Any

def check_file_imports(file_path: str) -> Dict[str, Any]:
    """Check a Python file for missing imports"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {'error': f"Could not read file: {e}"}
    
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        return {'error': f"Syntax error: {e}"}
    
    # Find existing imports
    existing_imports = set()
    typing_imports = set()
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                existing_imports.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                existing_imports.add(node.module.split('.')[0])
                if node.module == 'typing':
                    for alias in node.names:
                        typing_imports.add(alias.name)
            for alias in node.names:
                existing_imports.add(alias.name)
    
    # Find used names
    used_names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used_names.add(node.id)
        elif isinstance(node, ast.Attribute):
            if isinstance(node.value, ast.Name):
                used_names.add(node.value.id)
    
    # Check for missing standard library imports
    stdlib_modules = {
        'json', 'os', 'sys', 're', 'datetime', 'time', 'random',
        'math', 'collections', 'itertools', 'functools', 'operator',
        'pathlib', 'uuid', 'hashlib', 'base64', 'urllib', 'copy',
        'requests', 'subprocess', 'threading', 'multiprocessing'
    }
    
    missing_stdlib = []
    for module in stdlib_modules:
        if module in used_names and module not in existing_imports:
            missing_stdlib.append(module)
    
    # Check for missing typing imports
    typing_types = {
        'Any', 'Dict', 'List', 'Optional', 'Union', 'Tuple', 'Set',
        'Callable', 'Type', 'TypeVar', 'Generic', 'Iterable', 'Iterator'
    }
    
    missing_typing = []
    for typ in typing_types:
        if typ in used_names and typ not in typing_imports:
            missing_typing.append(typ)
    
    # Check for missing helper functions
    helper_functions = {
        '_error', '_ok', '_match', '_find_one', '_apply_update', 
        '_apply_delete', '_get_table', '_convert_db_to_list'
    }
    
    defined_functions = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            defined_functions.add(node.name)
    
    missing_helpers = []
    for helper in helper_functions:
        if helper in used_names and helper not in defined_functions and helper not in existing_imports:
            missing_helpers.append(helper)
    
    if missing_stdlib or missing_typing or missing_helpers:
        return {
            'file': file_path,
            'missing_stdlib': sorted(missing_stdlib),
            'missing_typing': sorted(missing_typing),
            'missing_helpers': sorted(missing_helpers)
        }
    
    return None

def find_tau_tools_files() -> List[str]:
    """Find all tau/**/tools/*.py files"""
    tau_tools_files = []
    tau_dir = Path('tau')
    
    if not tau_dir.exists():
        print("tau directory not found")
        return tau_tools_files
    
    for tools_dir in tau_dir.rglob('tools'):
        if tools_dir.is_dir():
            for py_file in tools_dir.glob('*.py'):
                if py_file.name != '__init__.py':
                    tau_tools_files.append(str(py_file))
    
    return sorted(tau_tools_files)

def main():
    """Main function"""
    print("Checking for missing imports in tau/**/tools/*.py files...\n")
    
    tau_files = find_tau_tools_files()
    print(f"Scanning {len(tau_files)} Python files...")
    
    files_with_issues = []
    total_stdlib = 0
    total_typing = 0
    total_helpers = 0
    
    for file_path in tau_files:
        result = check_file_imports(file_path)
        
        if result and 'error' not in result:
            files_with_issues.append(result)
            total_stdlib += len(result['missing_stdlib'])
            total_typing += len(result['missing_typing'])
            total_helpers += len(result['missing_helpers'])
    
    print(f"\n{'='*70}")
    print(f"RESULTS:")
    print(f"{'='*70}")
    
    if not files_with_issues:
        print("✅ No missing imports found! All files are good.")
    else:
        print(f"❌ Found {len(files_with_issues)} files with missing imports:")
        print(f"   - Standard library imports: {total_stdlib}")
        print(f"   - Typing imports: {total_typing}")
        print(f"   - Helper functions: {total_helpers}")
        print(f"\nFirst 10 files with issues:\n")
        
        for i, result in enumerate(files_with_issues[:10]):
            print(f"{i+1}. {result['file']}")
            if result['missing_stdlib']:
                print(f"   Missing stdlib: {', '.join(result['missing_stdlib'])}")
            if result['missing_typing']:
                print(f"   Missing typing: {', '.join(result['missing_typing'])}")
            if result['missing_helpers']:
                print(f"   Missing helpers: {', '.join(result['missing_helpers'])}")
            print()
        
        if len(files_with_issues) > 10:
            print(f"... and {len(files_with_issues) - 10} more files with issues\n")
    
    print(f"{'='*70}")

if __name__ == "__main__":
    main()

