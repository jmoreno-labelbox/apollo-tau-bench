#!/usr/bin/env python3
"""
Automated fixing of tool errors found by direct_tool_test_all.py

This script can:
1. Fix syntax errors (mismatched parentheses/braces)
2. Fix data structure iteration errors (dict keys vs values)
3. Fix missing required arguments
4. Run in a loop to fix multiple domains deterministically
"""
import sys
import json
import re
import ast
from pathlib import Path
from typing import Dict, List, Tuple, Optional

sys.path.insert(0, str(Path(__file__).parent / "tau"))


class AutoFixer:
    """Automatically fix common error patterns"""
    
    def __init__(self, base_path: Path, results: Dict):
        self.base_path = base_path
        self.results = results
        self.fixes_applied = []
    
    def fix_syntax_error_missing_paren(self, env_name: str, line_num: int) -> bool:
        """Fix missing closing parenthesis on a specific line"""
        tools_path = self.base_path / env_name / "tools.py"
        
        if not tools_path.exists():
            return False
        
        with open(tools_path) as f:
            lines = f.readlines()
        
        if line_num > len(lines):
            return False
        
        # Check the specific line and previous lines for context
        target_line = lines[line_num - 1]
        
        # Common pattern: if any(...for x in dict.values():
        # Missing closing paren on the any()
        if 'if any(' in target_line and target_line.rstrip().endswith(':'):
            # Missing paren before the colon
            lines[line_num - 1] = target_line.rstrip()[:-1] + '):\n'
            
            # Write and verify
            new_content = ''.join(lines)
            try:
                ast.parse(new_content)
                with open(tools_path, 'w') as f:
                    f.write(new_content)
                self.fixes_applied.append({
                    'env': env_name,
                    'type': 'SYNTAX_MISSING_PAREN',
                    'line': line_num,
                    'description': 'Added missing closing parenthesis'
                })
                return True
            except SyntaxError:
                pass
        
        # Try generic approach: count opening and closing parens on line
        opens = target_line.count('(') - target_line.count(')')
        if opens > 0 and target_line.rstrip().endswith(':'):
            # Add missing closing parens
            lines[line_num - 1] = target_line.rstrip()[:-1] + ')' * opens + ':\n'
            
            new_content = ''.join(lines)
            try:
                ast.parse(new_content)
                with open(tools_path, 'w') as f:
                    f.write(new_content)
                self.fixes_applied.append({
                    'env': env_name,
                    'type': 'SYNTAX_MISSING_PAREN',
                    'line': line_num,
                    'description': f'Added {opens} missing closing parenthesis'
                })
                return True
            except SyntaxError:
                pass
        
        return False
    
    def fix_syntax_error_mismatched_brace(self, env_name: str, line_num: int, error_msg: str) -> bool:
        """Fix mismatched braces (like } when it should be ))"""
        tools_path = self.base_path / env_name / "tools.py"
        
        if not tools_path.exists():
            return False
        
        with open(tools_path) as f:
            lines = f.readlines()
        
        if line_num > len(lines):
            return False
        
        target_line = lines[line_num - 1]
        
        # Pattern 1: } should be )
        if "'}' does not match" in error_msg and '}' in target_line:
            # Replace trailing } with )
            if target_line.rstrip().endswith('}'):
                lines[line_num - 1] = target_line.rstrip()[:-1] + ')\n'
            elif '},' in target_line:
                lines[line_num - 1] = target_line.replace('},', '),', 1)
            
            new_content = ''.join(lines)
            try:
                ast.parse(new_content)
                with open(tools_path, 'w') as f:
                    f.write(new_content)
                self.fixes_applied.append({
                    'env': env_name,
                    'type': 'SYNTAX_MISMATCHED_BRACE',
                    'line': line_num,
                    'description': 'Changed } to )'
                })
                return True
            except SyntaxError:
                pass
        
        # Pattern 2: ] should be )
        if "']' does not match" in error_msg and ']' in target_line:
            if target_line.rstrip().endswith(']'):
                lines[line_num - 1] = target_line.rstrip()[:-1] + ')\n'
            elif '],' in target_line:
                lines[line_num - 1] = target_line.replace('],', '),', 1)
            
            new_content = ''.join(lines)
            try:
                ast.parse(new_content)
                with open(tools_path, 'w') as f:
                    f.write(new_content)
                self.fixes_applied.append({
                    'env': env_name,
                    'type': 'SYNTAX_MISMATCHED_BRACKET',
                    'line': line_num,
                    'description': 'Changed ] to )'
                })
                return True
            except SyntaxError:
                pass
        
        return False
    
    def fix_syntax_error_fstring(self, env_name: str, line_num: int) -> bool:
        """Fix f-string with unmatched parentheses"""
        tools_path = self.base_path / env_name / "tools.py"
        
        if not tools_path.exists():
            return False
        
        with open(tools_path) as f:
            lines = f.readlines()
        
        if line_num > len(lines):
            return False
        
        target_line = lines[line_num - 1]
        
        # Look for f-strings with unmatched parens
        if 'f"' in target_line or "f'" in target_line:
            # Find the f-string and count parens
            fixed_line = target_line
            
            # Simple heuristic: if there's an opening { with a ( inside but no )
            # Add ) before the }
            matches = re.finditer(r'\{([^}]*)\}', fixed_line)
            for match in matches:
                content = match.group(1)
                if '(' in content and ')' not in content:
                    # Add missing )
                    new_content = content + ')'
                    fixed_line = fixed_line.replace(match.group(0), '{' + new_content + '}')
            
            if fixed_line != target_line:
                lines[line_num - 1] = fixed_line
                
                new_content = ''.join(lines)
                try:
                    ast.parse(new_content)
                    with open(tools_path, 'w') as f:
                        f.write(new_content)
                    self.fixes_applied.append({
                        'env': env_name,
                        'type': 'SYNTAX_FSTRING',
                        'line': line_num,
                        'description': 'Fixed f-string with unmatched parentheses'
                    })
                    return True
                except SyntaxError:
                    pass
        
        return False
    
    def fix_dict_iteration_to_values(self, env_name: str, tool_names: List[str]) -> bool:
        """
        Fix tools that iterate over dict keys instead of values.
        
        Pattern: for item in data['table']: item['field']
        Should be: for item in data['table'].values(): item['field']
        """
        tools_path = self.base_path / env_name / "tools.py"
        
        if not tools_path.exists():
            return False
        
        with open(tools_path) as f:
            content = f.read()
        
        original_content = content
        lines = content.split('\n')
        
        # For each problematic tool
        for tool_name in tool_names:
            # Find the tool class
            tool_start_line = None
            for i, line in enumerate(lines):
                if f"class {tool_name}" in line:
                    tool_start_line = i
                    break
            
            if tool_start_line is None:
                continue
            
            # Look in the next 200 lines for iteration patterns
            tool_end_line = min(tool_start_line + 200, len(lines))
            
            for i in range(tool_start_line, tool_end_line):
                line = lines[i]
                
                # Pattern 1: for x in data['table']:
                # Should be: for x in data['table'].values():
                match = re.search(r"for (\w+) in data\['([^']+)'\]:", line)
                if match:
                    var_name = match.group(1)
                    table_name = match.group(2)
                    
                    # Check if next few lines access var_name as a dict
                    accesses_as_dict = False
                    for j in range(i + 1, min(i + 10, len(lines))):
                        if f"{var_name}[" in lines[j] or f"{var_name}.get(" in lines[j]:
                            accesses_as_dict = True
                            break
                    
                    if accesses_as_dict:
                        lines[i] = line.replace(
                            f"for {var_name} in data['{table_name}']:",
                            f"for {var_name} in data['{table_name}'].values():"
                        )
                
                # Pattern 2: for x in data.get('table', []):
                # Should be: for x in data.get('table', {}).values():
                match = re.search(r"for (\w+) in data\.get\('([^']+)', \[\]\):", line)
                if match:
                    var_name = match.group(1)
                    table_name = match.group(2)
                    
                    # Check if accessed as dict
                    accesses_as_dict = False
                    for j in range(i + 1, min(i + 10, len(lines))):
                        if f"{var_name}[" in lines[j] or f"{var_name}.get(" in lines[j]:
                            accesses_as_dict = True
                            break
                    
                    if accesses_as_dict:
                        lines[i] = line.replace(
                            f"for {var_name} in data.get('{table_name}', []):",
                            f"for {var_name} in data.get('{table_name}', {{}}).values():"
                        )
                
                # Pattern 3: list comprehension [x for x in data['table']]
                match = re.search(r"\[([^]]+) for (\w+) in data\['([^']+)'\]", line)
                if match:
                    expr = match.group(1)
                    var_name = match.group(2)
                    table_name = match.group(3)
                    
                    # Check if var_name is accessed as dict in expression
                    if f"{var_name}[" in expr or f"{var_name}.get(" in expr:
                        lines[i] = line.replace(
                            f"for {var_name} in data['{table_name}']",
                            f"for {var_name} in data['{table_name}'].values()"
                        )
        
        new_content = '\n'.join(lines)
        
        if new_content != original_content:
            # Verify it's valid Python
            try:
                ast.parse(new_content)
                with open(tools_path, 'w') as f:
                    f.write(new_content)
                self.fixes_applied.append({
                    'env': env_name,
                    'type': 'DICT_ITERATION',
                    'tools': tool_names,
                    'description': f'Changed dict iteration to .values() for {len(tool_names)} tools'
                })
                return True
            except SyntaxError as e:
                print(f"  ⚠️  Fix created invalid Python: {e}")
                return False
        
        return False
    
    def fix_dict_append_error(self, env_name: str, tool_names: List[str]) -> bool:
        """
        Fix tools that call .append() on a dict.
        
        Pattern: data['table'].append(item)
        Should be: data['table'][item_id] = item  OR  data['table'] = list(data['table'].values()); data['table'].append(item)
        """
        tools_path = self.base_path / env_name / "tools.py"
        
        if not tools_path.exists():
            return False
        
        with open(tools_path) as f:
            content = f.read()
        
        original_content = content
        lines = content.split('\n')
        
        # For each problematic tool
        for tool_name in tool_names:
            # Find the tool class
            tool_start_line = None
            for i, line in enumerate(lines):
                if f"class {tool_name}" in line:
                    tool_start_line = i
                    break
            
            if tool_start_line is None:
                continue
            
            # Look for .append() calls
            tool_end_line = min(tool_start_line + 200, len(lines))
            
            for i in range(tool_start_line, tool_end_line):
                line = lines[i]
                
                # Pattern: data['table'].append(item)
                match = re.search(r"data\['([^']+)'\]\.append\((.+)\)", line)
                if match:
                    table_name = match.group(1)
                    item_expr = match.group(2)
                    
                    # Look for item_id or similar in the item expression
                    # Common pattern: append({"id": new_id, ...})
                    # Change to: data['table'][new_id] = {...}
                    
                    # Try to find an id field in the item
                    id_match = re.search(r'"(\w*[Ii][Dd]\w*)"\s*:\s*(\w+)', item_expr)
                    if id_match:
                        id_field = id_match.group(1)
                        id_var = id_match.group(2)
                        
                        # Change append to dict assignment
                        indent = len(line) - len(line.lstrip())
                        lines[i] = ' ' * indent + f"data['{table_name}'][{id_var}] = {item_expr}\n"
                    else:
                        # No clear ID field, just convert to dict assignment with generated ID
                        # This is tricky, let's skip for now
                        pass
        
        new_content = '\n'.join(lines)
        
        if new_content != original_content:
            try:
                ast.parse(new_content)
                with open(tools_path, 'w') as f:
                    f.write(new_content)
                self.fixes_applied.append({
                    'env': env_name,
                    'type': 'DICT_APPEND',
                    'tools': tool_names,
                    'description': f'Changed .append() to dict assignment for {len(tool_names)} tools'
                })
                return True
            except SyntaxError as e:
                print(f"  ⚠️  Fix created invalid Python: {e}")
                return False
        
        return False
    
    def analyze_and_fix_all(self):
        """Analyze all errors and fix them"""
        
        print("=" * 70)
        print("AUTOMATED FIXING - PHASE 1: SYNTAX ERRORS")
        print("=" * 70)
        print()
        
        syntax_errors = []
        for env_name, errors in self.results.items():
            if not errors:
                continue
            
            for error in errors:
                if error.get('tool') == 'LOAD_ERROR':
                    error_msg = error['error']
                    line_match = re.search(r'line (\d+)', error_msg)
                    if line_match:
                        line_num = int(line_match.group(1))
                        syntax_errors.append((env_name, line_num, error_msg))
        
        print(f"Found {len(syntax_errors)} syntax errors")
        fixed = 0
        
        for env_name, line_num, error_msg in syntax_errors:
            print(f"  Fixing {env_name}:{line_num}...", end=" ")
            
            success = False
            
            # Try different fix strategies
            if "'}'" in error_msg and "does not match" in error_msg:
                success = self.fix_syntax_error_mismatched_brace(env_name, line_num, error_msg)
            elif "']'" in error_msg and "does not match" in error_msg:
                success = self.fix_syntax_error_mismatched_brace(env_name, line_num, error_msg)
            elif "f-string" in error_msg:
                success = self.fix_syntax_error_fstring(env_name, line_num)
            else:
                success = self.fix_syntax_error_missing_paren(env_name, line_num)
            
            if success:
                print("✅ FIXED")
                fixed += 1
            else:
                print("❌ Could not fix")
        
        print(f"\n✅ Fixed {fixed}/{len(syntax_errors)} syntax errors\n")
        
        print("=" * 70)
        print("AUTOMATED FIXING - PHASE 2: DICT ITERATION ERRORS")
        print("=" * 70)
        print()
        
        # Group by environment
        dict_iteration_errors = {}
        for env_name, errors in self.results.items():
            if not errors:
                continue
            
            tools_with_issue = []
            for error in errors:
                if error.get('tool') != 'LOAD_ERROR':
                    error_msg = error['error']
                    if ("string indices must be integers" in error_msg or
                        "'str' object has no attribute 'get'" in error_msg):
                        tools_with_issue.append(error['tool'])
            
            if tools_with_issue:
                dict_iteration_errors[env_name] = tools_with_issue
        
        print(f"Found {len(dict_iteration_errors)} environments with dict iteration errors")
        fixed = 0
        
        for env_name, tool_names in list(dict_iteration_errors.items())[:20]:  # First 20
            print(f"  Fixing {env_name} ({len(tool_names)} tools)...", end=" ")
            
            if self.fix_dict_iteration_to_values(env_name, tool_names):
                print("✅ FIXED")
                fixed += 1
            else:
                print("❌ Could not fix")
        
        print(f"\n✅ Fixed {fixed}/{min(20, len(dict_iteration_errors))} dict iteration errors\n")
        
        print("=" * 70)
        print("AUTOMATED FIXING - PHASE 3: DICT APPEND ERRORS")
        print("=" * 70)
        print()
        
        dict_append_errors = {}
        for env_name, errors in self.results.items():
            if not errors:
                continue
            
            tools_with_issue = []
            for error in errors:
                if error.get('tool') != 'LOAD_ERROR':
                    error_msg = error['error']
                    if "'dict' object has no attribute 'append'" in error_msg:
                        tools_with_issue.append(error['tool'])
            
            if tools_with_issue:
                dict_append_errors[env_name] = tools_with_issue
        
        print(f"Found {len(dict_append_errors)} environments with dict append errors")
        fixed = 0
        
        for env_name, tool_names in list(dict_append_errors.items())[:10]:  # First 10
            print(f"  Fixing {env_name} ({len(tool_names)} tools)...", end=" ")
            
            if self.fix_dict_append_error(env_name, tool_names):
                print("✅ FIXED")
                fixed += 1
            else:
                print("❌ Could not fix")
        
        print(f"\n✅ Fixed {fixed}/{min(10, len(dict_append_errors))} dict append errors\n")
        
        return len(self.fixes_applied)


def main():
    """Main entry point"""
    
    # Load test results
    results_file = Path('direct_tool_test_results.json')
    if not results_file.exists():
        print("❌ direct_tool_test_results.json not found")
        print("   Run direct_tool_test_all.py first!")
        return
    
    with open(results_file) as f:
        results = json.load(f)
    
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    fixer = AutoFixer(base_path, results)
    total_fixed = fixer.analyze_and_fix_all()
    
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total fixes applied: {total_fixed}")
    print()
    
    # Save fixes log
    with open('auto_fixes_applied.json', 'w') as f:
        json.dump(fixer.fixes_applied, f, indent=2)
    
    print("✅ Fixes log saved to auto_fixes_applied.json")
    print()
    print("=" * 70)
    print("NEXT STEPS:")
    print("  1. Run: python direct_tool_test_all.py")
    print("  2. Compare results to see how many errors were fixed")
    print("  3. Run this script again to fix remaining errors")
    print("=" * 70)


if __name__ == "__main__":
    main()

