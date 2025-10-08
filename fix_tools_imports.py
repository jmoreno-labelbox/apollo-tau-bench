#!/usr/bin/env python3
"""
Script to fix tools/__init__.py files to re-export TOOLS from the adjacent tools.py file.

This solves the Python import precedence issue where tools/ directory shadows tools.py module.
"""

import os
from pathlib import Path
import argparse


def fix_tools_init(variation_path: Path, domain_name: str, variation_name: str):
    """Add TOOLS import to tools/__init__.py if needed."""
    tools_py = variation_path / "tools.py"
    tools_init = variation_path / "tools" / "__init__.py"
    
    # Only process if both files exist
    if not tools_py.exists() or not tools_init.exists():
        return False
    
    # Check if tools.py has TOOLS
    with open(tools_py, 'r') as f:
        tools_content = f.read()
    
    if 'TOOLS = [' not in tools_content:
        return False
    
    # Read current __init__.py content
    with open(tools_init, 'r') as f:
        init_content = f.read()
    
    # Check if it already has the import
    if 'TOOLS' in init_content and 'import' in init_content:
        print(f"   ✓ {domain_name}/{variation_name}/tools/__init__.py already has TOOLS export")
        return False
    
    # Create the import statement
    # We need to import from the parent's tools module
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
    
    # Write the new content
    with open(tools_init, 'w') as f:
        f.write(import_statement)
    
    print(f"   ✓ Updated {domain_name}/{variation_name}/tools/__init__.py")
    return True


def main():
    """Main function to process all variations."""
    ap = argparse.ArgumentParser()
    ap.add_argument("--domains-root", type=str, required=True, help="Path to domains root (e.g., tau_bench_warrior/domains)")
    args = ap.parse_args()
    domains_path = Path(args.domains_root)
    
    total_updated = 0
    
    # Iterate through all domain directories
    for domain_dir in sorted(domains_path.iterdir()):
        if not domain_dir.is_dir() or domain_dir.name in ['__pycache__', '.git']:
            continue
        
        domain_name = domain_dir.name
        variations_path = domain_dir / "variations"
        
        if not variations_path.exists():
            continue
        
        # Process each variation
        for variation_dir in sorted(variations_path.iterdir()):
            if not variation_dir.is_dir():
                continue
            
            variation_name = variation_dir.name
            
            if fix_tools_init(variation_dir, domain_name, variation_name):
                total_updated += 1
    
    print(f"\n{'='*60}")
    print(f"Total tools/__init__.py files updated: {total_updated}")


if __name__ == "__main__":
    main()

