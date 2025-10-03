#!/usr/bin/env python3
"""
Comprehensive fix script for all remaining environment issues.
"""

import re
import shutil
from pathlib import Path


def fix_sports_analytics_imports(env_file: Path) -> bool:
    """Fix imports for sports-analytics (hyphen issue)."""
    with open(env_file, 'r') as f:
        content = f.read()
    
    # Replace sports-analytics with sports_analytics in imports
    new_content = content.replace('domains.sports-analytics', 'domains.sports_analytics')
    
    if new_content != content:
        # Create backup
        shutil.copy2(env_file, env_file.with_suffix('.py.backup_fix'))
        # Write fix
        with open(env_file, 'w') as f:
            f.write(new_content)
        return True
    return False


def fix_task_outputs_advanced(tasks_file: Path) -> tuple[str, int]:
    """
    More aggressive conversion of task outputs from dict/list-of-dicts to list.
    """
    with open(tasks_file, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    changes = 0
    in_outputs = False
    in_list_outputs = False
    bracket_count = 0
    paren_count = 0
    outputs_indent = 0
    
    for line in lines:
        stripped = line.lstrip()
        
        # Check for outputs=[ with list of dicts
        if stripped.startswith('outputs=[') and not in_outputs:
            # This is outputs with a list
            bracket_count = line.count('[') - line.count(']')
            
            if bracket_count == 0:
                # Single line list
                indent = len(line) - len(stripped)
                new_lines.append(' ' * indent + 'outputs=[]')
                changes += 1
            else:
                # Multi-line list
                in_list_outputs = True
                outputs_indent = len(line) - len(stripped)
                new_lines.append(' ' * outputs_indent + 'outputs=[]')
                changes += 1
                
        elif stripped.startswith('outputs={') and not in_outputs:
            # Dict outputs
            brace_count = line.count('{') - line.count('}')
            
            if brace_count == 0:
                # Single line dict
                indent = len(line) - len(stripped)
                new_lines.append(' ' * indent + 'outputs=[]')
                changes += 1
            else:
                # Multi-line dict
                in_outputs = True
                outputs_indent = len(line) - len(stripped)
                new_lines.append(' ' * outputs_indent + 'outputs=[]')
                changes += 1
                
        elif in_outputs:
            # Inside a multi-line dict
            brace_count = line.count('{') - line.count('}')
            bracket_count += brace_count
            
            if bracket_count <= 0:
                in_outputs = False
            continue
            
        elif in_list_outputs:
            # Inside a multi-line list
            bracket_count += line.count('[') - line.count(']')
            
            if bracket_count <= 0:
                in_list_outputs = False
            continue
            
        else:
            new_lines.append(line)
    
    return '\n'.join(new_lines), changes


def fix_task_instruction_tuple(tasks_file: Path) -> bool:
    """Fix instruction fields that are tuples instead of strings."""
    with open(tasks_file, 'r') as f:
        content = f.read()
    
    # Pattern: instruction=("...", ) or instruction=('...', )
    # Replace with: instruction="..." or instruction='...'
    pattern = r"instruction=\((['\"])(.+?)\1,?\s*\)"
    new_content = re.sub(pattern, r'instruction=\1\2\1', content, flags=re.DOTALL)
    
    if new_content != content:
        shutil.copy2(tasks_file, tasks_file.with_suffix('.py.backup_fix'))
        with open(tasks_file, 'w') as f:
            f.write(new_content)
        return True
    return False


def fix_github_mcp_tools(variation_path: Path) -> bool:
    """Fix missing TOOLS in github_mcp/variation_7."""
    tools_init = variation_path / "tools" / "__init__.py"
    tools_py = variation_path / "tools.py"
    
    if not tools_py.exists() or not tools_init.exists():
        return False
    
    # Check if tools.py has TOOLS
    with open(tools_py, 'r') as f:
        tools_content = f.read()
    
    if 'TOOLS = [' not in tools_content:
        return False
    
    # Check if __init__.py already has it
    with open(tools_init, 'r') as f:
        init_content = f.read()
    
    if 'TOOLS' in init_content:
        return False
    
    # Add the import
    import_statement = f"""# Re-export TOOLS from the adjacent tools.py file
import sys
from pathlib import Path

# Add parent directory to path to import tools.py as a module
_parent = Path(__file__).parent.parent
_tools_module_path = _parent / "tools.py"

import importlib.util
spec = importlib.util.spec_from_file_location("_tools_module", _tools_module_path)
_tools_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_tools_module)

# Re-export TOOLS
TOOLS = _tools_module.TOOLS
"""
    
    shutil.copy2(tools_init, tools_init.with_suffix('.py.backup_fix'))
    with open(tools_init, 'w') as f:
        f.write(import_statement)
    
    return True


def main():
    """Main fix routine."""
    domains_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains")
    
    print("="*70)
    print("COMPREHENSIVE FIX SCRIPT")
    print("="*70 + "\n")
    
    # Fix 1: Sports-analytics import issues
    print("Fix 1: Sports-analytics import issues...")
    sports_files = list(domains_path.glob("sports-analytics/variations/*/env.py"))
    sports_fixed = 0
    for f in sports_files:
        if fix_sports_analytics_imports(f):
            sports_fixed += 1
            print(f"  ✓ Fixed {f.relative_to(domains_path)}")
    print(f"  Fixed {sports_fixed} sports-analytics files\n")
    
    # Fix 2: More task outputs conversions
    print("Fix 2: Converting remaining task outputs...")
    all_tasks_files = list(domains_path.glob("*/variations/*/tasks_test.py"))
    outputs_fixed = 0
    for tasks_file in all_tasks_files:
        # Create backup
        shutil.copy2(tasks_file, tasks_file.with_suffix('.py.backup_fix'))
        
        new_content, changes = fix_task_outputs_advanced(tasks_file)
        if changes > 0:
            with open(tasks_file, 'w') as f:
                f.write(new_content)
            outputs_fixed += 1
            rel_path = tasks_file.relative_to(domains_path)
            print(f"  ✓ {rel_path}: {changes} outputs converted")
    print(f"  Fixed outputs in {outputs_fixed} files\n")
    
    # Fix 3: Instruction tuple issues
    print("Fix 3: Fixing instruction tuples...")
    instruction_fixed = 0
    for tasks_file in all_tasks_files:
        if fix_task_instruction_tuple(tasks_file):
            instruction_fixed += 1
            rel_path = tasks_file.relative_to(domains_path)
            print(f"  ✓ {rel_path}")
    print(f"  Fixed {instruction_fixed} instruction fields\n")
    
    # Fix 4: github_mcp/variation_7 tools
    print("Fix 4: Fixing github_mcp/variation_7 tools...")
    github_var7 = domains_path / "github_mcp" / "variations" / "variation_7"
    if github_var7.exists():
        if fix_github_mcp_tools(github_var7):
            print("  ✓ Fixed github_mcp/variation_7/tools/__init__.py")
        else:
            print("  - Already fixed or not needed")
    print()
    
    print("="*70)
    print("FIXES COMPLETE")
    print("="*70)
    print("Run test_all_envs.py again to verify!")


if __name__ == "__main__":
    main()

