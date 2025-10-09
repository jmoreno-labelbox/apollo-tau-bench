#!/usr/bin/env python3
"""
Analyze ALL tool files across ALL environments to find every possible error pattern
WITHOUT running them (static code analysis)
"""
import re
import ast
import json
from pathlib import Path
from collections import defaultdict

def analyze_tool_file(file_path):
    """Analyze a single tool file for error patterns"""
    errors = []
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Error Pattern 1: Iterating over dict without .values()
    for i, line in enumerate(lines):
        # Pattern: for row in variable where variable = data["name"]
        if 'for row in ' in line or '[row for row in ' in line:
            # Check if it's iterating over a dict
            var_match = re.search(r'for row in (\w+)', line)
            if var_match:
                var_name = var_match.group(1)
                
                # Look backwards to see if this var is assigned from data["..."]
                for j in range(max(0, i-10), i):
                    if f'{var_name} = data[' in lines[j] and '.values()' not in line:
                        errors.append({
                            'type': 'dict_iteration_without_values',
                            'line': i + 1,
                            'code': line.strip(),
                            'variable': var_name
                        })
                        break
    
    # Error Pattern 2: data["name"].append() on dicts
    for i, line in enumerate(lines):
        if 'data[' in line and '.append(' in line:
            match = re.search(r'data\["(\w+)"\]\.append\(', line)
            if match:
                db_name = match.group(1)
                errors.append({
                    'type': 'dict_append',
                    'line': i + 1,
                    'code': line.strip(),
                    'database': db_name
                })
    
    # Error Pattern 3: data.get with [] default
    for i, line in enumerate(lines):
        if 'data.get(' in line and ', [])' in line:
            errors.append({
                'type': 'wrong_default_value',
                'line': i + 1,
                'code': line.strip()
            })
    
    # Error Pattern 4: Schema mismatches (required params)
    # Look for get_info() methods with database_name param but not in required
    in_get_info = False
    has_database_name = False
    
    for i, line in enumerate(lines):
        if 'def get_info(' in line:
            in_get_info = True
            has_database_name = False
        
        if in_get_info and '"database_name"' in line:
            has_database_name = True
        
        if in_get_info and '"required":' in line and has_database_name:
            if 'database_name' not in line and 'filter_params' in line:
                errors.append({
                    'type': 'missing_database_name_in_required',
                    'line': i + 1,
                    'code': line.strip()
                })
        
        if in_get_info and 'return {' in line and i > 0 and '}' in lines[i-1]:
            in_get_info = False
    
    # Error Pattern 5: Parameter name mismatches (delivery_options vs delivery_option)
    for i, line in enumerate(lines):
        if 'def invoke(' in line:
            # Look for function parameters
            func_start = i
            func_end = i
            
            # Find end of function signature
            for j in range(i, min(i + 20, len(lines))):
                if ') -> str:' in lines[j]:
                    func_end = j
                    break
            
            func_signature = '\n'.join(lines[func_start:func_end+1])
            
            # Look for the schema later
            for k in range(func_end, min(func_end + 100, len(lines))):
                if 'def get_info(' in lines[k]:
                    schema_start = k
                    
                    # Find end of schema
                    for m in range(schema_start, min(schema_start + 50, len(lines))):
                        if m > schema_start and 'def ' in lines[m]:
                            schema_end = m
                            break
                    else:
                        schema_end = min(schema_start + 50, len(lines))
                    
                    schema = '\n'.join(lines[schema_start:schema_end])
                    
                    # Check for mismatches
                    if 'delivery_option:' in func_signature and '"delivery_options"' in schema:
                        errors.append({
                            'type': 'param_name_mismatch',
                            'line': i + 1,
                            'code': f'delivery_option vs delivery_options mismatch'
                        })
                    
                    break
    
    return errors


def main():
    base_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench-1/tau/tau_bench/envs")
    
    # Find ALL tool files (both tools.py and individual tool files)
    all_tool_files = list(base_path.rglob("tools.py"))
    all_tool_files.extend(base_path.rglob("tools/*.py"))
    
    print(f"=" * 70)
    print(f"ANALYZING {len(all_tool_files)} TOOL FILES")
    print(f"=" * 70)
    print()
    
    all_errors = []
    files_with_errors = 0
    
    for tool_file in all_tool_files:
        errors = analyze_tool_file(tool_file)
        
        if errors:
            rel_path = tool_file.relative_to(base_path)
            files_with_errors += 1
            all_errors.extend([{**e, 'file': str(rel_path)} for e in errors])
    
    print(f"Files analyzed: {len(all_tool_files)}")
    print(f"Files with errors: {files_with_errors}")
    print(f"Total errors found: {len(all_errors)}")
    print()
    
    # Categorize
    by_type = defaultdict(list)
    for error in all_errors:
        by_type[error['type']].append(error)
    
    print("=" * 70)
    print("ERROR BREAKDOWN BY TYPE:")
    print("=" * 70)
    
    for error_type, errors in sorted(by_type.items(), key=lambda x: -len(x[1])):
        print(f"\n{error_type}: {len(errors)} occurrences")
        
        # Show affected files
        files = set(e['file'] for e in errors)
        print(f"  Affected files: {len(files)}")
        
        if len(files) <= 5:
            for f in list(files)[:5]:
                print(f"    - {f}")
        
        # Show example
        print(f"  Example: {errors[0]['code'][:100]}")
    
    # Save detailed report
    with open('error_analysis.json', 'w') as f:
        json.dump({
            'total_errors': len(all_errors),
            'files_analyzed': len(all_tool_files),
            'files_with_errors': files_with_errors,
            'by_type': {k: len(v) for k, v in by_type.items()},
            'details': all_errors
        }, f, indent=2)
    
    print()
    print("=" * 70)
    print("✅ Full error analysis saved to error_analysis.json")
    print("=" * 70)


if __name__ == "__main__":
    main()

