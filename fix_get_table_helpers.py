#!/usr/bin/env python3
"""
Fix helper functions that return tables but don't convert dict to list properly
"""
import sys
import json
import re
import ast
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "tau"))


def fix_get_table_helper(env_name: str, base_path: Path) -> bool:
    """Fix _get_table or similar helper functions that return dict instead of values()"""
    
    tools_path = base_path / env_name / "tools.py"
    
    if not tools_path.exists():
        return False
    
    with open(tools_path) as f:
        content = f.read()
    
    original_content = content
    lines = content.split('\n')
    fixed = False
    
    # Look for _get_table or similar functions
    for i, line in enumerate(lines):
        # Pattern: def _get_table(...) or def _issues(...) or similar
        if re.match(r'\s*def (_get_table|_issues|_get_\w+|_load_\w+)\s*\(', line):
            # Look at the next few lines for the return statement
            for j in range(i + 1, min(i + 10, len(lines))):
                return_line = lines[j]
                
                # Pattern 1: return data.setdefault("table_name", [])
                # Should be: return list(data.get("table_name", {}).values()) if isinstance(data.get("table_name", {}), dict) else data.get("table_name", [])
                match = re.search(r'return data\.setdefault\((["\'])([^"\']+)\1, \[\]\)', return_line)
                if match:
                    quote = match.group(1)
                    table_name = match.group(2)
                    indent = len(return_line) - len(return_line.lstrip())
                    lines[j] = ' ' * indent + f'table = data.get({quote}{table_name}{quote}, {{}})\n'
                    lines.insert(j + 1, ' ' * indent + 'if isinstance(table, dict):\n')
                    lines.insert(j + 2, ' ' * (indent + 4) + 'return list(table.values())\n')
                    lines.insert(j + 3, ' ' * indent + 'return table if isinstance(table, list) else []\n')
                    fixed = True
                    break
                
                # Pattern 2: return data.get(name, [])
                if 'return data.get(name, [])' in return_line:
                    indent = len(return_line) - len(return_line.lstrip())
                    lines[j] = ' ' * indent + 'table = data.get(name, {})\n'
                    lines.insert(j + 1, ' ' * indent + 'if isinstance(table, dict):\n')
                    lines.insert(j + 2, ' ' * (indent + 4) + 'return list(table.values())\n')
                    lines.insert(j + 3, ' ' * indent + 'return table if isinstance(table, list) else []\n')
                    fixed = True
                    break
                
                # Stop if we hit another def/class
                if re.match(r'\s*(def|class)\s', return_line) and j != i:
                    break
            
            if fixed:
                break
        
        # Also look for similar patterns with different names
        match = re.match(r'\s*def (get_\w+|_load_\w+)\s*\([^)]*data[^)]*\)\s*->\s*list\[', line)
        if match:
            # Look for return statements
            for j in range(i + 1, min(i + 15, len(lines))):
                return_line = lines[j]
                
                if 'return data.get(' in return_line or 'return data[' in return_line:
                    # Check if it's returning a table without .values()
                    if '.values()' not in return_line and '.items()' not in return_line:
                        # Try to add .values()
                        # Pattern: return data.get('table', [])
                        # Change to: return list(data.get('table', {}).values()) if isinstance(data.get('table', {}), dict) else data.get('table', [])
                        
                        # For simplicity, let's add a helper wrapper
                        # Actually, this is getting complex. Let's just add .values() if the return is a simple get
                        if re.search(r'return data\.get\(["\'](\w+)["\'], \[\]\)', return_line):
                            table_match = re.search(r'return data\.get\(["\'](\w+)["\'], \[\]\)', return_line)
                            if table_match:
                                table_name = table_match.group(1)
                                indent = len(return_line) - len(return_line.lstrip())
                                
                                lines[j] = ' ' * indent + f'table = data.get("{table_name}", {{}})\n'
                                lines.insert(j + 1, ' ' * indent + 'if isinstance(table, dict):\n')
                                lines.insert(j + 2, ' ' * (indent + 4) + 'return list(table.values())\n')
                                lines.insert(j + 3, ' ' * indent + 'return table if isinstance(table, list) else []\n')
                                fixed = True
                                break
                
                if re.match(r'\s*(def|class)\s', return_line) and j != i:
                    break
            
            if fixed:
                break
    
    if not fixed:
        return False
    
    new_content = '\n'.join(lines)
    
    # Verify it's valid Python
    try:
        ast.parse(new_content)
        with open(tools_path, 'w') as f:
            f.write(new_content)
        return True
    except SyntaxError as e:
        print(f"  ⚠️  Fix created invalid Python: {e}")
        # Restore original
        with open(tools_path, 'w') as f:
            f.write(original_content)
        return False


def main():
    """Main entry point"""
    
    # Load test results
    results_file = Path('direct_tool_test_results.json')
    if not results_file.exists():
        print("❌ direct_tool_test_results.json not found")
        return
    
    with open(results_file) as f:
        results = json.load(f)
    
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    # Find environments with STR_USED_AS_DICT errors (likely _get_table issues)
    get_table_errors = {}
    for env_name, errors in results.items():
        if not errors:
            continue
        
        tools_with_issue = []
        for error in errors:
            if error.get('tool') != 'LOAD_ERROR':
                error_msg = error['error']
                if "'str' object has no attribute 'get'" in error_msg or \
                   "string indices must be integers" in error_msg:
                    tools_with_issue.append(error['tool'])
        
        if len(tools_with_issue) > 5:  # Likely a systemic _get_table issue
            get_table_errors[env_name] = tools_with_issue
    
    print("=" * 70)
    print("_GET_TABLE HELPER FIXER")
    print("=" * 70)
    print(f"Found {len(get_table_errors)} environments with potential _get_table issues")
    print("(Environments with >5 similar STR_USED_AS_DICT errors)")
    print()
    
    fixed_count = 0
    for env_name, tool_names in get_table_errors.items():
        print(f"  Fixing {env_name} ({len(tool_names)} tools)...", end=" ")
        
        if fix_get_table_helper(env_name, base_path):
            print("✅ FIXED")
            fixed_count += 1
        else:
            print("❌ Could not fix")
    
    print()
    print("=" * 70)
    print(f"✅ Fixed {fixed_count}/{len(get_table_errors)} environments")
    print("=" * 70)
    print()
    print("Run: python direct_tool_test_all.py to verify")


if __name__ == "__main__":
    main()

