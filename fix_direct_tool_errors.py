#!/usr/bin/env python3
"""
Tool to inspect and fix errors found by direct_tool_test_all.py

Main error patterns:
1. 'str' object has no attribute 'get' (70 errors)
2. 'dict' object has no attribute 'append' (42 errors)  
3. string indices must be integers (36 errors)
4. Syntax errors (mismatched parentheses/braces) (14 errors)
5. Missing required arguments (~10 errors)
"""
import sys
import json
import re
import ast
from pathlib import Path
from typing import Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).parent / "tau"))

class DomainInspector:
    """Inspect failing domains to understand the root cause"""
    
    def __init__(self, base_path: Path):
        self.base_path = base_path
    
    def inspect_domain(self, env_name: str, errors: List[Dict]) -> Dict:
        """Deep inspection of a domain's errors"""
        env_path = self.base_path / env_name
        tools_path = env_path / "tools.py"
        data_path = env_path / "data.py"
        
        inspection = {
            'env_name': env_name,
            'errors': errors,
            'tools_exists': tools_path.exists(),
            'data_exists': data_path.exists(),
            'issues_found': []
        }
        
        # Check for LOAD_ERROR (syntax errors)
        if errors and errors[0].get('tool') == 'LOAD_ERROR':
            inspection['issues_found'].append({
                'type': 'SYNTAX_ERROR',
                'message': errors[0]['error'],
                'file': 'tools.py'
            })
            
            # Try to extract line number from error
            line_match = re.search(r'line (\d+)', errors[0]['error'])
            if line_match and tools_path.exists():
                line_num = int(line_match.group(1))
                inspection['issues_found'][-1]['line'] = line_num
                
                # Read surrounding lines
                try:
                    with open(tools_path) as f:
                        lines = f.readlines()
                        start = max(0, line_num - 5)
                        end = min(len(lines), line_num + 5)
                        inspection['issues_found'][-1]['context'] = {
                            'lines': lines[start:end],
                            'start_line': start + 1,
                            'error_line': line_num
                        }
                except Exception as e:
                    inspection['issues_found'][-1]['read_error'] = str(e)
        
        # Check for runtime errors
        else:
            for error in errors:
                tool_name = error['tool']
                error_msg = error['error']
                
                if "'str' object has no attribute 'get'" in error_msg:
                    inspection['issues_found'].append({
                        'type': 'STR_USED_AS_DICT',
                        'tool': tool_name,
                        'message': 'Tool is treating a string as a dict'
                    })
                    
                elif "'dict' object has no attribute 'append'" in error_msg:
                    inspection['issues_found'].append({
                        'type': 'DICT_USED_AS_LIST',
                        'tool': tool_name,
                        'message': 'Tool is treating a dict as a list'
                    })
                    
                elif "string indices must be integers" in error_msg:
                    inspection['issues_found'].append({
                        'type': 'STRING_INDEXED',
                        'tool': tool_name,
                        'message': 'Tool is indexing a string as if it were a dict'
                    })
                    
                elif "missing 1 required" in error_msg:
                    inspection['issues_found'].append({
                        'type': 'MISSING_ARGUMENT',
                        'tool': tool_name,
                        'message': error_msg
                    })
        
        return inspection


class DomainFixer:
    """Fix common error patterns in domains"""
    
    def __init__(self, base_path: Path):
        self.base_path = base_path
    
    def fix_syntax_errors(self, env_name: str, inspection: Dict) -> bool:
        """Fix common syntax errors like mismatched parentheses"""
        tools_path = self.base_path / env_name / "tools.py"
        
        if not tools_path.exists():
            return False
        
        with open(tools_path) as f:
            content = f.read()
        
        original_content = content
        fixed = False
        
        # Fix 1: Mismatched } when should be )
        if "closing parenthesis '}' does not match opening parenthesis '('" in str(inspection):
            # Find lines with mismatched braces
            lines = content.split('\n')
            for i, line in enumerate(lines):
                # Look for common pattern: f"...{var}" where it should be f"...(var)"
                # or return statements with wrong closing brace
                if '}' in line:
                    # Check if this is a likely mismatch
                    # Count opening ( and closing )
                    open_parens = line.count('(') - line.count(')')
                    close_braces = line.count('}') - line.count('{')
                    
                    if open_parens > 0 and '}' in line:
                        # Likely mismatch - try replacing trailing } with )
                        if line.rstrip().endswith('}'):
                            lines[i] = line.rstrip()[:-1] + ')'
                            fixed = True
                        elif '},' in line:
                            lines[i] = line.replace('},', '),')
                            fixed = True
            
            if fixed:
                content = '\n'.join(lines)
        
        # Fix 2: Mismatched ] when should be )
        if "closing parenthesis ']' does not match opening parenthesis '('" in str(inspection):
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if ']' in line:
                    open_parens = line.count('(') - line.count(')')
                    close_brackets = line.count(']') - line.count('[')
                    
                    if open_parens > 0 and ']' in line:
                        if line.rstrip().endswith(']'):
                            lines[i] = line.rstrip()[:-1] + ')'
                            fixed = True
                        elif '],' in line:
                            lines[i] = line.replace('],', '),')
                            fixed = True
            
            if fixed:
                content = '\n'.join(lines)
        
        # Fix 3: Unmatched f-string parentheses
        if "f-string: unmatched '('" in str(inspection):
            # Find f-strings with unmatched parens
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if 'f"' in line or "f'" in line:
                    # Count parens in f-string
                    in_fstring = False
                    paren_count = 0
                    new_line = ""
                    
                    j = 0
                    while j < len(line):
                        char = line[j]
                        
                        if (line[j:j+2] == 'f"' or line[j:j+2] == "f'"):
                            in_fstring = True
                            new_line += line[j:j+2]
                            j += 2
                            continue
                        
                        if in_fstring and char in '"\'':
                            if paren_count > 0:
                                # Unclosed parens, add closing ones
                                new_line += ')' * paren_count
                                paren_count = 0
                            in_fstring = False
                        
                        if in_fstring and char == '(':
                            paren_count += 1
                        elif in_fstring and char == ')':
                            paren_count -= 1
                        
                        new_line += char
                        j += 1
                    
                    if new_line != line:
                        lines[i] = new_line
                        fixed = True
            
            if fixed:
                content = '\n'.join(lines)
        
        if fixed and content != original_content:
            # Verify it's valid Python
            try:
                ast.parse(content)
                with open(tools_path, 'w') as f:
                    f.write(content)
                return True
            except SyntaxError as e:
                print(f"  ⚠️  Fix created invalid Python: {e}")
                return False
        
        return False
    
    def fix_data_structure_errors(self, env_name: str, inspection: Dict) -> bool:
        """Fix data structure type errors (str used as dict, dict used as list, etc)"""
        tools_path = self.base_path / env_name / "tools.py"
        
        if not tools_path.exists():
            return False
        
        with open(tools_path) as f:
            content = f.read()
        
        original_content = content
        fixed = False
        
        # Get list of problematic tools
        str_as_dict_tools = [issue['tool'] for issue in inspection['issues_found'] 
                            if issue.get('type') == 'STR_USED_AS_DICT']
        dict_as_list_tools = [issue['tool'] for issue in inspection['issues_found']
                             if issue.get('type') == 'DICT_USED_AS_LIST']
        string_indexed_tools = [issue['tool'] for issue in inspection['issues_found']
                               if issue.get('type') == 'STRING_INDEXED']
        
        # Parse the file to find these tool classes
        try:
            tree = ast.parse(content)
        except SyntaxError:
            return False
        
        # For each problematic tool, we need to find and fix the issue
        # This is complex because we need to understand the data flow
        # For now, let's focus on common patterns
        
        lines = content.split('\n')
        
        # Fix 1: dict.append() -> list.append()
        # This usually means data[table] should be data[table].values() or similar
        for tool_name in dict_as_list_tools:
            # Find the tool class
            for i, line in enumerate(lines):
                if f"class {tool_name}" in line:
                    # Look in the next 100 lines for .append( calls on data structures
                    for j in range(i, min(i + 100, len(lines))):
                        if '.append(' in lines[j]:
                            # Check if it's accessing data[something]
                            # Common pattern: data['table_name'].append(...)
                            # Should be: data['table_name'] = data['table_name'] + [...]
                            # OR: data['table_name'].setdefault('key', []).append(...)
                            
                            # Try to detect the pattern
                            match = re.search(r"data\['([^']+)'\]\.append\(", lines[j])
                            if match:
                                table_name = match.group(1)
                                # Change to list concatenation
                                lines[j] = lines[j].replace(
                                    f"data['{table_name}'].append(",
                                    f"data['{table_name}'] = list(data['{table_name}'].values()) if isinstance(data['{table_name}'], dict) else data['{table_name}']; data['{table_name}'].append("
                                )
                                fixed = True
                                break
                    break
        
        # Fix 2: string['key'] -> dict['key']
        # This usually means we're iterating over dict.keys() instead of dict.values() or dict.items()
        for tool_name in string_indexed_tools + str_as_dict_tools:
            # Find the tool class
            for i, line in enumerate(lines):
                if f"class {tool_name}" in line:
                    # Look for patterns like: for x in data[table]:
                    # Should be: for x in data[table].values():
                    for j in range(i, min(i + 100, len(lines))):
                        # Pattern: for item in data['table']:
                        match = re.search(r"for (\w+) in data\['([^']+)'\]:", lines[j])
                        if match:
                            var_name = match.group(1)
                            table_name = match.group(2)
                            lines[j] = lines[j].replace(
                                f"for {var_name} in data['{table_name}']:",
                                f"for {var_name} in data['{table_name}'].values():"
                            )
                            fixed = True
                            break
                        
                        # Pattern: for item_id in data['table']:
                        # followed by: item = data['table'][item_id]
                        match = re.search(r"for (\w+) in data\['([^']+)'\]:", lines[j])
                        if match:
                            var_name = match.group(1)
                            table_name = match.group(2)
                            # Check next line for: item = data['table'][var_name]
                            if j + 1 < len(lines):
                                if f"data['{table_name}'][{var_name}]" in lines[j + 1]:
                                    # This is actually correct - iterating over keys
                                    # The error must be elsewhere
                                    continue
                    break
        
        if fixed and content != original_content:
            new_content = '\n'.join(lines)
            # Verify it's valid Python
            try:
                ast.parse(new_content)
                with open(tools_path, 'w') as f:
                    f.write(new_content)
                return True
            except SyntaxError as e:
                print(f"  ⚠️  Fix created invalid Python: {e}")
                return False
        
        return False


def main():
    """Main inspection and fixing loop"""
    base_path = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    # Load test results
    with open('direct_tool_test_results.json') as f:
        results = json.load(f)
    
    # Filter to only failing environments
    failing = {env: errs for env, errs in results.items() if errs}
    
    print("=" * 70)
    print(f"DOMAIN INSPECTION & FIXING TOOL")
    print("=" * 70)
    print(f"Found {len(failing)} failing environments with {sum(len(e) for e in failing.values())} total errors")
    print("=" * 70)
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] == 'inspect':
        # Inspection mode - show details of specific domain
        if len(sys.argv) < 3:
            print("Usage: python fix_direct_tool_errors.py inspect <env_name>")
            print("\nAvailable failing environments:")
            for env in sorted(failing.keys())[:20]:
                print(f"  - {env}")
            if len(failing) > 20:
                print(f"  ... and {len(failing) - 20} more")
            return
        
        env_name = sys.argv[2]
        if env_name not in failing:
            print(f"❌ Environment '{env_name}' not found or has no errors")
            return
        
        inspector = DomainInspector(base_path)
        inspection = inspector.inspect_domain(env_name, failing[env_name])
        
        print(f"🔍 INSPECTION: {env_name}")
        print("=" * 70)
        print(f"Errors: {len(inspection['errors'])}")
        print(f"Tools file exists: {inspection['tools_exists']}")
        print(f"Data file exists: {inspection['data_exists']}")
        print()
        print("Issues found:")
        for issue in inspection['issues_found']:
            print(f"  • Type: {issue['type']}")
            if 'tool' in issue:
                print(f"    Tool: {issue['tool']}")
            print(f"    Message: {issue['message']}")
            if 'context' in issue:
                print(f"    Error at line {issue['context']['error_line']}:")
                for line in issue['context']['lines']:
                    print(f"      {line.rstrip()}")
            print()
        
        # Save detailed inspection
        inspection_file = f'inspection_{env_name}.json'
        with open(inspection_file, 'w') as f:
            json.dump(inspection, f, indent=2, default=str)
        print(f"✅ Detailed inspection saved to {inspection_file}")
    
    elif len(sys.argv) > 1 and sys.argv[1] == 'fix':
        # Fix mode - try to automatically fix errors
        print("🔧 FIX MODE - Attempting to fix common error patterns")
        print()
        
        # Categorize errors by type
        syntax_errors = []
        data_structure_errors = []
        
        inspector = DomainInspector(base_path)
        fixer = DomainFixer(base_path)
        
        for env_name, errors in failing.items():
            inspection = inspector.inspect_domain(env_name, errors)
            
            has_syntax = any(i['type'] == 'SYNTAX_ERROR' for i in inspection['issues_found'])
            has_data_struct = any(i['type'] in ['STR_USED_AS_DICT', 'DICT_USED_AS_LIST', 'STRING_INDEXED'] 
                                  for i in inspection['issues_found'])
            
            if has_syntax:
                syntax_errors.append((env_name, inspection))
            elif has_data_struct:
                data_structure_errors.append((env_name, inspection))
        
        print(f"Syntax errors: {len(syntax_errors)}")
        print(f"Data structure errors: {len(data_structure_errors)}")
        print()
        
        # Fix syntax errors first
        print("Fixing syntax errors...")
        fixed_count = 0
        for env_name, inspection in syntax_errors:
            print(f"  Attempting to fix {env_name}...", end=" ")
            if fixer.fix_syntax_errors(env_name, inspection):
                print("✅ FIXED")
                fixed_count += 1
            else:
                print("❌ Could not fix")
        
        print(f"Fixed {fixed_count}/{len(syntax_errors)} syntax errors")
        print()
        
        # Fix data structure errors
        print("Fixing data structure errors...")
        fixed_count = 0
        for env_name, inspection in data_structure_errors[:10]:  # Try first 10
            print(f"  Attempting to fix {env_name}...", end=" ")
            if fixer.fix_data_structure_errors(env_name, inspection):
                print("✅ FIXED")
                fixed_count += 1
            else:
                print("❌ Could not fix")
        
        print(f"Fixed {fixed_count}/10 data structure errors (tried first 10)")
        print()
        
        print("=" * 70)
        print("✅ Fixes applied - run direct_tool_test_all.py again to verify")
        print("=" * 70)
    
    else:
        # Default: show summary
        print("Available commands:")
        print(f"  python fix_direct_tool_errors.py inspect <env_name>")
        print(f"    - Deep inspection of a specific failing environment")
        print()
        print(f"  python fix_direct_tool_errors.py fix")
        print(f"    - Attempt to automatically fix common error patterns")
        print()
        print("\nError type summary:")
        
        error_types = {}
        for env, errs in failing.items():
            for err in errs:
                error_msg = err['error']
                if 'LOAD_ERROR' in err['tool']:
                    key = 'SYNTAX_ERROR'
                elif "'str' object has no attribute 'get'" in error_msg:
                    key = 'STR_USED_AS_DICT'
                elif "'dict' object has no attribute 'append'" in error_msg:
                    key = 'DICT_USED_AS_LIST'
                elif "string indices must be integers" in error_msg:
                    key = 'STRING_INDEXED'
                elif "missing 1 required" in error_msg:
                    key = 'MISSING_ARGUMENT'
                else:
                    key = 'OTHER'
                
                if key not in error_types:
                    error_types[key] = []
                error_types[key].append(env)
        
        for error_type, envs in sorted(error_types.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"  {error_type}: {len(envs)} environments")
        
        print()
        print("Top 10 failing environments:")
        sorted_failing = sorted(failing.items(), key=lambda x: len(x[1]), reverse=True)[:10]
        for env, errs in sorted_failing:
            print(f"  {env}: {len(errs)} errors")


if __name__ == "__main__":
    main()

