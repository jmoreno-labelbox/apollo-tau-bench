#!/usr/bin/env python3
"""
Fix 'str_no_get' errors: Convert dict.values() to lists in data loading.

The issue: JSON data files contain dicts like {"key1": {...}, "key2": {...}}
but tools expect lists of dicts [{...}, {...}].

Solution: Modify data/__init__.py to convert dicts to lists of values.
"""

import argparse
import re
import sys
from pathlib import Path


def fix_data_init(file_path: Path) -> bool:
    """
    Fix data/__init__.py to convert dict values to lists.
    
    Changes:
        db[name] = json.loads(content) if content else []
    To:
        loaded = json.loads(content) if content else []
        db[name] = list(loaded.values()) if isinstance(loaded, dict) else loaded
    """
    try:
        source = file_path.read_text(encoding='utf-8')
        original = source
        
        # Pattern to match: db[name] = json.loads(content) if content else []
        pattern = r'(\s+)(db\[name\]\s*=\s*json\.loads\(content\)\s*if\s*content\s*else\s*\[\])'
        
        # Replacement: convert dict to list of values
        replacement = r'''\1loaded = json.loads(content) if content else []
\1db[name] = list(loaded.values()) if isinstance(loaded, dict) else loaded'''
        
        source = re.sub(pattern, replacement, source)
        
        if source != original:
            file_path.write_text(source, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", nargs='+', help="Environment names to fix (e.g., dev_ops_1)")
    parser.add_argument("--all", action='store_true', help="Fix all 10 affected environments")
    args = parser.parse_args()
    
    # List of affected environments
    affected_envs = [
        "dev_ops_1", "dev_ops_2", "dev_ops_3",
        "digital_commerce_4",
        "real_estate_sales_2",
        "recipes_3", "recipes_5",
        "retail_2", "retail_6",
        "social_media_advertising_4"
    ]
    
    if args.all:
        envs = affected_envs
    elif args.env:
        envs = args.env
    else:
        print("Error: Specify --env ENV_NAME or --all")
        sys.exit(1)
    
    base_path = Path("tau/tau_bench/envs")
    modified_count = 0
    
    for env_name in envs:
        data_init = base_path / env_name / "data" / "__init__.py"
        
        if not data_init.exists():
            print(f"✗ {env_name}: data/__init__.py not found")
            continue
        
        if fix_data_init(data_init):
            print(f"✓ {env_name}")
            modified_count += 1
        else:
            print(f"- {env_name}: no changes needed")
    
    print(f"\nModified {modified_count}/{len(envs)} environments")


if __name__ == "__main__":
    main()

