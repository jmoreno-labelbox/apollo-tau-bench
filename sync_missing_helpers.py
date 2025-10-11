#!/usr/bin/env python3
"""
Sync missing helper functions and classes from domains_warrior to tau/tau_bench/envs.

Finds undefined functions/classes in tau/**/tools/*.py files and copies them from
the corresponding domains_warrior source files.
"""

import ast
import re
from pathlib import Path
from typing import Set, Dict, Optional, Tuple

REPO_ROOT = Path(__file__).parent
TAU_ENVS = REPO_ROOT / "tau" / "tau_bench" / "envs"
DOMAINS_WARRIOR = REPO_ROOT / "domains_warrior"


def parse_domain_and_variation(env_name: str) -> Tuple[Optional[str], Optional[int]]:
    """Extract domain and variation number from env name like 'recipes_1'."""
    match = re.match(r'^(.+)_(\d+)$', env_name)
    if match:
        return match.group(1), int(match.group(2))
    return None, None


def find_undefined_names(file_path: Path) -> Set[str]:
    """Find all referenced but undefined names in a Python file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        tree = ast.parse(content)
    except Exception as e:
        print(f"  Error parsing {file_path}: {e}")
        return set()
    
    defined = set()
    referenced = set()
    
    # Collect defined names
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            defined.add(node.name)
        elif isinstance(node, ast.ClassDef):
            defined.add(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    defined.add(target.id)
    
    # Collect referenced names
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            referenced.add(node.id)
    
    # Find undefined (referenced but not defined, and not builtins/imports)
    undefined = referenced - defined
    
    # Filter to likely helpers (private functions or CamelCase classes)
    helpers = {
        name for name in undefined
        if name.startswith('_') or (name[0].isupper() and not name.isupper())
    }
    
    return helpers


def extract_definition(source_file: Path, name: str) -> Optional[str]:
    """Extract function or class definition from source file."""
    try:
        content = source_file.read_text(encoding='utf-8')
        tree = ast.parse(content)
        lines = content.splitlines()
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name == name:
                start_line = node.lineno - 1
                end_line = node.end_lineno
                definition_lines = lines[start_line:end_line]
                return '\n'.join(definition_lines)
        
        return None
    except Exception as e:
        print(f"  Error extracting {name} from {source_file}: {e}")
        return None


def add_helper_to_file(target_file: Path, helper_name: str, helper_code: str) -> bool:
    """Add helper function/class to target file after imports."""
    try:
        content = target_file.read_text(encoding='utf-8')
        lines = content.splitlines()
        
        # Find where to insert (after imports, before first function/class)
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('import ') or line.startswith('from '):
                insert_idx = i + 1
            elif line.strip() == '' and insert_idx > 0:
                insert_idx = i + 1
            elif (line.startswith('def ') or line.startswith('class ')) and insert_idx > 0:
                break
        
        # Insert the helper code
        lines.insert(insert_idx, '\n\n' + helper_code + '\n')
        
        new_content = '\n'.join(lines)
        target_file.write_text(new_content, encoding='utf-8')
        return True
        
    except Exception as e:
        print(f"  Error adding {helper_name} to {target_file}: {e}")
        return False


def process_tool_file(tool_file: Path) -> int:
    """Process a single tool file and sync missing helpers. Returns number of helpers synced."""
    env_dir = tool_file.parent.parent
    env_name = env_dir.name
    
    domain, variation = parse_domain_and_variation(env_name)
    if not domain or variation is None:
        return 0
    
    # Find source in domains_warrior
    source_file = DOMAINS_WARRIOR / domain / "variations" / f"variation_{variation}" / "tools.py"
    if not source_file.exists():
        return 0
    
    # Find undefined helpers
    undefined = find_undefined_names(tool_file)
    if not undefined:
        return 0
    
    print(f"\n{env_name}/{tool_file.relative_to(env_dir)}")
    print(f"  Undefined: {sorted(undefined)}")
    
    synced = 0
    for helper_name in sorted(undefined):
        # Extract from source
        helper_code = extract_definition(source_file, helper_name)
        
        if helper_code:
            print(f"  Syncing: {helper_name}")
            if add_helper_to_file(tool_file, helper_name, helper_code):
                synced += 1
                print(f"    ✓ Added {helper_name}")
            else:
                print(f"    ✗ Failed to add {helper_name}")
        else:
            print(f"  ✗ {helper_name} not found in {source_file.name}")
    
    return synced


def main():
    print("Syncing missing helpers from domains_warrior to tau/tau_bench/envs")
    print("="*60)
    
    # Find all tool files
    tool_files = list(TAU_ENVS.glob("*/tools/*.py"))
    tool_files = [f for f in tool_files if f.name != '__init__.py']
    
    print(f"Found {len(tool_files)} tool files to check\n")
    
    total_synced = 0
    files_with_missing = 0
    
    for tool_file in tool_files:
        synced = process_tool_file(tool_file)
        if synced > 0:
            total_synced += synced
            files_with_missing += 1
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Files checked: {len(tool_files)}")
    print(f"Files with missing helpers: {files_with_missing}")
    print(f"Total helpers synced: {total_synced}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()

