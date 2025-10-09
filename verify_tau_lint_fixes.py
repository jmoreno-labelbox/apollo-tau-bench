#!/usr/bin/env python3
"""
Verification script for tau/ directory lint fixes
Run this after applying fixes to verify all issues are resolved
"""

import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text: str):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text.center(70)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}\n")

def print_success(text: str):
    print(f"{Colors.GREEN}✓{Colors.END} {text}")

def print_error(text: str):
    print(f"{Colors.RED}✗{Colors.END} {text}")

def print_warning(text: str):
    print(f"{Colors.YELLOW}⚠{Colors.END} {text}")

def check_syntax_errors() -> Tuple[int, List[str]]:
    """Check for Python syntax errors using compileall"""
    print_header("1. Checking Python Syntax Errors")
    
    result = subprocess.run(
        ["python3", "-m", "compileall", "tau/", "-q"],
        capture_output=True,
        text=True
    )
    
    error_lines = [line for line in result.stdout.split('\n') if 'Error compiling' in line]
    error_count = len(error_lines)
    
    if error_count == 0:
        print_success("No syntax errors found!")
        return 0, []
    else:
        print_error(f"Found {error_count} files with syntax errors:")
        for line in error_lines[:10]:  # Show first 10
            print(f"  - {line}")
        if error_count > 10:
            print(f"  ... and {error_count - 10} more")
        return error_count, error_lines

def check_import_errors() -> Tuple[int, List[str]]:
    """Check for import errors using pylint"""
    print_header("2. Checking Import Errors")
    
    result = subprocess.run(
        ["pylint", "tau/tau_bench/", "--disable=all", 
         "--enable=import-error,no-name-in-module,relative-beyond-top-level",
         "--output-format=text"],
        capture_output=True,
        text=True,
        cwd="/Users/josemoreno/Desktop/repos/apollo-tau-bench/tau"
    )
    
    error_lines = [line for line in result.stdout.split('\n') if 'E0401' in line or 'import-error' in line]
    error_count = len(error_lines)
    
    if error_count == 0:
        print_success("No import errors found!")
        return 0, []
    else:
        print_error(f"Found {error_count} import errors:")
        for line in error_lines[:10]:
            print(f"  - {line}")
        if error_count > 10:
            print(f"  ... and {error_count - 10} more")
        return error_count, error_lines

def check_module_imports() -> Tuple[int, List[str]]:
    """Test if core modules can be imported"""
    print_header("3. Testing Core Module Imports")
    
    test_modules = [
        'tau_bench',
        'tau_bench.envs',
        'tau_bench.agents',
        'tau_bench.model_utils',
    ]
    
    sys.path.insert(0, 'tau')
    failed = []
    
    for module in test_modules:
        try:
            __import__(module)
            print_success(f"Successfully imported: {module}")
        except Exception as e:
            print_error(f"Failed to import {module}: {str(e)[:80]}")
            failed.append(module)
    
    return len(failed), failed

def check_init_files() -> Tuple[int, List[str]]:
    """Check for missing __init__.py files"""
    print_header("4. Checking __init__.py Coverage")
    
    tau_path = Path("tau/tau_bench")
    missing = []
    
    # Check all directories with Python files
    for py_file in tau_path.rglob("*.py"):
        parent = py_file.parent
        if parent.name == "__pycache__":
            continue
        init_file = parent / "__init__.py"
        if not init_file.exists() and parent not in [m.parent for m in missing]:
            missing.append(parent)
    
    if not missing:
        print_success("All package directories have __init__.py files")
        return 0, []
    else:
        print_error(f"Found {len(missing)} directories missing __init__.py:")
        for dir_path in missing[:10]:
            print(f"  - {dir_path}")
        if len(missing) > 10:
            print(f"  ... and {len(missing) - 10} more")
        return len(missing), [str(d) for d in missing]

def count_pyflakes_issues() -> Tuple[Dict[str, int], int]:
    """Count code quality issues using pyflakes"""
    print_header("5. Checking Code Quality (pyflakes)")
    
    result = subprocess.run(
        ["pyflakes", "tau/tau_bench/"],
        capture_output=True,
        text=True
    )
    
    lines = result.stdout.split('\n')
    
    categories = {
        'undefined name': 0,
        'imported but unused': 0,
        'redefinition': 0,
        'other': 0
    }
    
    for line in lines:
        if 'undefined name' in line:
            categories['undefined name'] += 1
        elif 'imported but unused' in line:
            categories['imported but unused'] += 1
        elif 'redefinition' in line:
            categories['redefinition'] += 1
        elif line.strip():
            categories['other'] += 1
    
    total = sum(categories.values())
    
    print(f"Total issues: {total}")
    for category, count in categories.items():
        if count > 0:
            if count > 1000:
                print_warning(f"  {category}: {count}")
            else:
                print(f"  {category}: {count}")
    
    return categories, total

def check_specific_issues() -> Dict[str, bool]:
    """Check for specific known issues"""
    print_header("6. Checking Specific Known Issues")
    
    issues = {}
    
    # Check for duplicate dictionary keys in openai.py
    openai_file = Path("tau/tau_bench/model_utils/model/openai.py")
    if openai_file.exists():
        content = openai_file.read_text()
        if content.count('"gpt-4o-2024-08-06"') > 1:
            print_error("Duplicate dictionary key 'gpt-4o-2024-08-06' in openai.py")
            issues['duplicate_dict_key'] = False
        else:
            print_success("No duplicate dictionary keys in openai.py")
            issues['duplicate_dict_key'] = True
    
    # Check for JavaScript-style literals (sample check)
    result = subprocess.run(
        ["grep", "-r", "\\bnull\\b", "tau/tau_bench/envs/", 
         "--include=*.py", "-l"],
        capture_output=True,
        text=True
    )
    null_files = [f for f in result.stdout.split('\n') if f]
    
    if null_files:
        print_warning(f"Found {len(null_files)} files using 'null' (should be 'None')")
        issues['javascript_literals'] = False
    else:
        print_success("No JavaScript-style 'null' literals found")
        issues['javascript_literals'] = True
    
    return issues

def main():
    print(f"\n{Colors.BOLD}TAU Directory Lint Verification{Colors.END}")
    print(f"{'='*70}\n")
    
    results = {}
    
    # Run all checks
    results['syntax_errors'], _ = check_syntax_errors()
    results['import_errors'], _ = check_import_errors()
    results['module_import_failures'], _ = check_module_imports()
    results['missing_init_files'], _ = check_init_files()
    results['code_quality'], total_quality_issues = count_pyflakes_issues()
    results['specific_issues'] = check_specific_issues()
    
    # Final summary
    print_header("FINAL SUMMARY")
    
    critical_issues = (
        results['syntax_errors'] + 
        results['import_errors'] + 
        results['module_import_failures'] +
        results['missing_init_files']
    )
    
    if critical_issues == 0:
        print_success(f"{Colors.BOLD}All critical issues resolved!{Colors.END}")
        print(f"\n{Colors.GREEN}✓ 0 syntax errors{Colors.END}")
        print(f"{Colors.GREEN}✓ 0 import errors{Colors.END}")
        print(f"{Colors.GREEN}✓ 0 module import failures{Colors.END}")
        print(f"{Colors.GREEN}✓ 0 missing __init__.py files{Colors.END}")
    else:
        print_error(f"{Colors.BOLD}{critical_issues} critical issues remain{Colors.END}")
        print(f"\n{Colors.RED}✗ {results['syntax_errors']} syntax errors{Colors.END}")
        print(f"{Colors.RED}✗ {results['import_errors']} import errors{Colors.END}")
        print(f"{Colors.RED}✗ {results['module_import_failures']} module import failures{Colors.END}")
        print(f"{Colors.RED}✗ {results['missing_init_files']} missing __init__.py files{Colors.END}")
    
    print(f"\n{Colors.YELLOW}Code Quality Issues:{Colors.END}")
    print(f"  - Undefined names: {results['code_quality']['undefined name']}")
    print(f"  - Unused imports: {results['code_quality']['imported but unused']}")
    print(f"  - Redefinitions: {results['code_quality']['redefinition']}")
    print(f"  - Other: {results['code_quality']['other']}")
    print(f"  {Colors.YELLOW}Total: {total_quality_issues}{Colors.END}")
    
    print("\n" + "="*70)
    
    # Save results to JSON
    results_json = {
        'critical_issues': critical_issues,
        'syntax_errors': results['syntax_errors'],
        'import_errors': results['import_errors'],
        'module_import_failures': results['module_import_failures'],
        'missing_init_files': results['missing_init_files'],
        'code_quality_issues': total_quality_issues,
        'code_quality_breakdown': results['code_quality'],
        'specific_issues': results['specific_issues']
    }
    
    with open('tau_verification_results.json', 'w') as f:
        json.dump(results_json, f, indent=2)
    
    print(f"\nDetailed results saved to: {Colors.BLUE}tau_verification_results.json{Colors.END}")
    
    return 0 if critical_issues == 0 else 1

if __name__ == "__main__":
    sys.exit(main())

