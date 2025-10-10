#!/usr/bin/env python3
"""
Convert a monolithic tools.py file to a modular tools/ directory structure
(like airline has)

Usage:
    python3 convert_to_modular_tools.py <env_name>
    
Example:
    python3 convert_to_modular_tools.py academic_search_1
"""

import ast
import sys
import re
from pathlib import Path
from typing import List, Tuple


def extract_tool_classes(tools_py_path: Path) -> List[Tuple[str, str]]:
    """
    Extract tool classes from tools.py
    Returns list of (class_name, class_code) tuples
    """
    with open(tools_py_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse AST
    tree = ast.parse(content)
    
    # Find all class definitions
    tool_classes = []
    imports = []
    
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            # Check if it's a Tool subclass
            for base in node.bases:
                if isinstance(base, ast.Name) and base.id == "Tool":
                    # Extract the class definition from source
                    class_start = node.lineno - 1
                    class_end = node.end_lineno
                    class_lines = content.split('\n')[class_start:class_end]
                    class_code = '\n'.join(class_lines)
                    tool_classes.append((node.name, class_code))
                    break
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            # Capture imports
            import_line = content.split('\n')[node.lineno - 1]
            imports.append(import_line)
    
    return tool_classes, imports


def snake_to_filename(class_name: str) -> str:
    """
    Convert ClassName to class_name.py
    SearchUsers -> search_users.py
    """
    # Insert underscore before uppercase letters
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', class_name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
    return f"{name}.py"


def create_modular_structure(env_path: Path, dry_run: bool = True):
    """
    Convert tools.py to tools/ directory structure
    """
    tools_py = env_path / "tools.py"
    
    if not tools_py.exists():
        print(f"❌ {tools_py} does not exist")
        return
    
    print(f"🔍 Analyzing {env_path.name}/tools.py...")
    
    # Extract classes
    tool_classes, imports = extract_tool_classes(tools_py)
    
    if not tool_classes:
        print(f"❌ No Tool classes found in {tools_py}")
        return
    
    print(f"✅ Found {len(tool_classes)} tool classes")
    print()
    
    # Create tools/ directory
    tools_dir = env_path / "tools"
    
    if dry_run:
        print("📋 DRY RUN - No files will be modified")
        print()
        print(f"Would create directory: {tools_dir.relative_to(env_path.parent.parent)}")
        print()
    else:
        tools_dir.mkdir(exist_ok=True)
        print(f"✅ Created directory: {tools_dir}")
    
    # Create individual tool files
    init_imports = []
    all_tools_list = []
    
    for class_name, class_code in tool_classes:
        filename = snake_to_filename(class_name)
        file_path = tools_dir / filename
        
        # Build file content
        file_content = "# Copyright Sierra\n\n"
        
        # Add necessary imports
        file_content += "import json\n"
        file_content += "from typing import Any, Dict, List, Optional\n"
        file_content += "from tau_bench.envs.tool import Tool\n\n\n"
        
        # Add class code
        file_content += class_code + "\n"
        
        if dry_run:
            print(f"  Would create: {filename} ({len(file_content)} bytes)")
        else:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)
            print(f"  ✅ Created: {filename}")
        
        # Track for __init__.py
        init_imports.append(f"from .{filename[:-3]} import {class_name}")
        all_tools_list.append(class_name)
    
    print()
    
    # Create __init__.py
    init_path = tools_dir / "__init__.py"
    init_content = "# Copyright Sierra\n\n"
    init_content += "\n".join(init_imports)
    init_content += "\n\n"
    init_content += "ALL_TOOLS = [\n"
    for tool_name in all_tools_list:
        init_content += f"    {tool_name},\n"
    init_content += "]\n"
    
    if dry_run:
        print(f"  Would create: __init__.py ({len(init_content)} bytes)")
        print()
        print("  Content preview:")
        lines = init_content.split('\n')
        print("  " + "\n  ".join(lines[:10]))
        if len(lines) > 10:
            remaining = len(lines) - 10
            print(f"  ... ({remaining} more lines)")
    else:
        with open(init_path, 'w', encoding='utf-8') as f:
            f.write(init_content)
        print(f"  ✅ Created: __init__.py")
    
    print()
    
    # Update env.py import
    env_py = env_path / "env.py"
    if env_py.exists():
        with open(env_py, 'r') as f:
            env_content = f.read()
        
        # Check current import
        old_import = f"from tau_bench.envs.{env_path.name}.tools import TOOLS"
        new_import = f"from tau_bench.envs.{env_path.name}.tools import ALL_TOOLS"
        
        if old_import in env_content:
            new_env_content = env_content.replace(old_import, new_import)
            new_env_content = new_env_content.replace("tools=TOOLS", "tools=ALL_TOOLS")
            
            if dry_run:
                print(f"Would update env.py imports:")
                print(f"  - {old_import}")
                print(f"  + {new_import}")
            else:
                with open(env_py, 'w') as f:
                    f.write(new_env_content)
                print(f"✅ Updated env.py imports")
    
    print()
    
    # Backup/rename original tools.py
    backup_path = env_path / "tools.py.monolithic"
    if dry_run:
        print(f"Would rename: tools.py → tools.py.monolithic (backup)")
    else:
        tools_py.rename(backup_path)
        print(f"✅ Renamed: tools.py → tools.py.monolithic")
    
    print()
    print("=" * 60)
    if dry_run:
        print("DRY RUN COMPLETE")
        print()
        print("To actually perform the conversion, run:")
        print(f"  python3 {sys.argv[0]} {env_path.name} --execute")
    else:
        print("✅ CONVERSION COMPLETE!")
        print()
        print(f"Created {len(tool_classes)} tool files in {tools_dir.relative_to(env_path.parent.parent)}")
        print()
        print("Next steps:")
        print(f"  1. Test the environment: cd tau && python3 run.py --env {env_path.name} --end-index 1")
        print(f"  2. If it works, delete backup: rm {backup_path}")
    print("=" * 60)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 convert_to_modular_tools.py <env_name> [--execute]")
        print()
        print("Example:")
        print("  python3 convert_to_modular_tools.py academic_search_1")
        print("  python3 convert_to_modular_tools.py academic_search_1 --execute")
        sys.exit(1)
    
    env_name = sys.argv[1]
    execute = "--execute" in sys.argv
    
    tau_envs = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    env_path = tau_envs / env_name
    
    if not env_path.exists():
        print(f"❌ Environment not found: {env_path}")
        sys.exit(1)
    
    create_modular_structure(env_path, dry_run=not execute)


if __name__ == "__main__":
    main()

