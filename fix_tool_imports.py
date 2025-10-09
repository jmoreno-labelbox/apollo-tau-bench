#!/usr/bin/env python3
"""
Fix imports in individual tool files to include _match and other helper functions from tools.py
"""

import os
import re
from pathlib import Path

def fix_tool_file_imports(tool_file: Path, env_name: str):
    """Add necessary imports to individual tool files."""
    content = tool_file.read_text()
    
    # Check if it uses _match or other helpers but doesn't import them
    needs_match = '_match(' in content
    needs_apply_update = '_apply_update(' in content
    needs_apply_delete = '_apply_delete(' in content
    
    # Check if imports are already there
    has_tools_import = f'from tau_bench.envs.{env_name}.tools import' in content
    
    if (needs_match or needs_apply_update or needs_apply_delete) and not has_tools_import:
        # Build import statement
        imports_needed = []
        if needs_match:
            imports_needed.append('_match')
        if needs_apply_update:
            imports_needed.append('_apply_update')
        if needs_apply_delete:
            imports_needed.append('_apply_delete')
        
        import_statement = f"from tau_bench.envs.{env_name}.tools import {', '.join(imports_needed)}\n"
        
        # Find where to insert (after other imports)
        lines = content.split('\n')
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('import ') or line.startswith('from '):
                insert_idx = i + 1
            elif line.strip() == '' and insert_idx > 0:
                continue
            elif (line.startswith('def ') or line.startswith('class ')) and insert_idx > 0:
                break
        
        lines.insert(insert_idx, import_statement)
        content = '\n'.join(lines)
        
        tool_file.write_text(content)
        return True
    
    return False

def main():
    tau_envs_dir = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    if not tau_envs_dir.exists():
        print(f"❌ tau/tau_bench/envs directory not found at {tau_envs_dir}")
        return
    
    print("🔧 Fixing tool file imports...\n")
    
    fixed_count = 0
    
    # Process each environment directory
    for env_dir in tau_envs_dir.iterdir():
        if not env_dir.is_dir() or env_dir.name.startswith('_') or env_dir.name == '__pycache__':
            continue
        
        tools_dir = env_dir / "tools"
        if not tools_dir.exists():
            continue
        
        env_name = env_dir.name
        
        for tool_file in tools_dir.glob("*.py"):
            if tool_file.name == "__init__.py":
                continue
            
            if fix_tool_file_imports(tool_file, env_name):
                fixed_count += 1
                print(f"  ✅ Fixed imports in {env_name}/{tool_file.name}")
    
    print(f"\n✅ Fixed imports in {fixed_count} tool files!")

if __name__ == "__main__":
    main()

