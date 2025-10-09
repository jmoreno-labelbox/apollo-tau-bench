#!/usr/bin/env python3
"""
Replace all direct data["table"] accesses with _get_table(data, "table") calls
"""

from pathlib import Path
import re

def fix_direct_accesses(content):
    """
    Replace data["table"] with _get_table(data, "table")
    This needs to be careful not to replace things inside strings or comments
    """
    
    # Replace data["table_name"] with _get_table(data, "table_name")
    # Use a more sophisticated pattern that handles the context
    content = re.sub(
        r'\bdata\["(\w+)"\]',
        r'_get_table(data, "\1")',
        content
    )
    
    return content

def fix_environment(env_name):
    """Fix one environment"""
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    tools_file = base_path / env_name / "tools.py"
    
    if not tools_file.exists():
        return f"❌ {env_name}: tools.py not found"
    
    content = tools_file.read_text()
    
    # Count direct accesses before
    before_count = len(re.findall(r'\bdata\["(\w+)"\]', content))
    
    if before_count == 0:
        return f"⚠️  {env_name}: No direct accesses found"
    
    # Fix
    new_content = fix_direct_accesses(content)
    
    # Count after
    after_count = len(re.findall(r'\bdata\["(\w+)"\]', new_content))
    
    # Write back
    tools_file.write_text(new_content)
    
    fixed = before_count - after_count
    return f"✅ {env_name}: Fixed {fixed} direct accesses (had {before_count})"

def main():
    envs_to_fix = ['it_help_desk_2', 'it_help_desk_4', 'it_help_desk_6', 'rbac_3']
    
    print("=" * 70)
    print("FIXING ALL DIRECT data[\"table\"] ACCESSES")
    print("=" * 70)
    print()
    
    results = []
    for env_name in envs_to_fix:
        result = fix_environment(env_name)
        results.append(result)
        print(result)
    
    print()
    print("=" * 70)
    fixed_count = sum(1 for r in results if r.startswith("✅"))
    print(f"FIXED {fixed_count} / {len(envs_to_fix)} ENVIRONMENTS")
    print("=" * 70)

if __name__ == "__main__":
    main()

