#!/usr/bin/env python3
"""
Lint all tools.py files in tau/tau_bench/envs/
"""
import ast
import sys
from pathlib import Path
from collections import defaultdict
import json


def lint_file(filepath: Path) -> dict:
    """
    Lint a single Python file.
    Returns dict with:
      - syntax_valid: bool
      - errors: list of error messages
      - warnings: list of warning messages
    """
    result = {
        "syntax_valid": True,
        "errors": [],
        "warnings": []
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Check for syntax errors
        try:
            ast.parse(source)
        except SyntaxError as e:
            result["syntax_valid"] = False
            result["errors"].append(f"SyntaxError at line {e.lineno}: {e.msg}")
            return result
        
        # Check for common issues
        lines = source.split('\n')
        
        # Check for .values().values() pattern (dict_values bug)
        for i, line in enumerate(lines, 1):
            if '.values()' in line and line.count('.values()') > 1:
                # Check if it's actually chaining .values() twice
                if '.values().values()' in line or '.values() .values()' in line:
                    result["errors"].append(
                        f"Line {i}: Calling .values() twice on dict (dict_values has no .values() method)"
                    )
            
            # Check for common dict iteration issues
            if 'for ' in line and ' in ' in line and '.values()' in line:
                # Look for patterns like: for x in dict.values().something()
                if '.values().' in line and not '.values().get(' in line:
                    parts_after_values = line.split('.values().')[1] if '.values().' in line else ""
                    if parts_after_values and not parts_after_values.startswith('get('):
                        result["warnings"].append(
                            f"Line {i}: Potential dict_values method call - verify this is correct"
                        )
        
        # Check for undefined variables in common patterns
        if 'from tau_bench.types import' not in source:
            result["warnings"].append("No import from tau_bench.types (may be intentional)")
        
    except Exception as e:
        result["syntax_valid"] = False
        result["errors"].append(f"Failed to read/parse file: {str(e)}")
    
    return result


def main():
    tau_dir = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    if not tau_dir.exists():
        print(f"❌ Directory not found: {tau_dir}")
        sys.exit(1)
    
    # Find all tools.py files
    tools_files = []
    
    # Direct tools.py files
    tools_files.extend(tau_dir.glob("*/tools.py"))
    
    # tools.py inside tools/ directories
    tools_files.extend(tau_dir.glob("*/tools/tools.py"))
    
    tools_files = sorted(tools_files)
    
    print(f"🔍 Found {len(tools_files)} tools.py files to lint\n")
    print("=" * 80)
    
    stats = {
        "total": len(tools_files),
        "syntax_valid": 0,
        "syntax_errors": 0,
        "has_warnings": 0,
        "clean": 0
    }
    
    results_by_file = {}
    files_with_issues = []
    
    for filepath in tools_files:
        env_name = filepath.parent.name
        if filepath.parent.name == "tools":
            env_name = filepath.parent.parent.name + "/tools"
        
        result = lint_file(filepath)
        results_by_file[str(filepath.relative_to(tau_dir.parent.parent))] = result
        
        # Update stats
        if result["syntax_valid"]:
            stats["syntax_valid"] += 1
            if result["errors"]:
                stats["syntax_errors"] += 1
                files_with_issues.append((env_name, filepath, result))
            elif result["warnings"]:
                stats["has_warnings"] += 1
                files_with_issues.append((env_name, filepath, result))
            else:
                stats["clean"] += 1
        else:
            stats["syntax_errors"] += 1
            files_with_issues.append((env_name, filepath, result))
    
    # Print detailed results for files with issues
    if files_with_issues:
        print("\n📋 FILES WITH ISSUES:\n")
        for env_name, filepath, result in files_with_issues:
            rel_path = filepath.relative_to(tau_dir.parent.parent)
            
            if not result["syntax_valid"] or result["errors"]:
                print(f"❌ {env_name}")
                print(f"   {rel_path}")
                for error in result["errors"]:
                    print(f"   ERROR: {error}")
            elif result["warnings"]:
                print(f"⚠️  {env_name}")
                print(f"   {rel_path}")
                for warning in result["warnings"]:
                    print(f"   WARNING: {warning}")
            print()
    
    # Print summary
    print("=" * 80)
    print("\n📊 SUMMARY:\n")
    print(f"Total files:          {stats['total']}")
    print(f"✅ Clean:             {stats['clean']}")
    print(f"⚠️  With warnings:     {stats['has_warnings']}")
    print(f"❌ With errors:       {stats['syntax_errors']}")
    print(f"✅ Syntax valid:      {stats['syntax_valid']}")
    print(f"❌ Syntax invalid:    {stats['total'] - stats['syntax_valid']}")
    
    # Save detailed results
    output_file = Path(__file__).parent / "tau_tools_lint_results.json"
    with open(output_file, 'w') as f:
        json.dump({
            "stats": stats,
            "results": results_by_file,
            "files_with_issues": [
                {
                    "env": env_name,
                    "path": str(filepath.relative_to(tau_dir.parent.parent)),
                    "result": result
                }
                for env_name, filepath, result in files_with_issues
            ]
        }, f, indent=2)
    
    print(f"\n💾 Detailed results saved to: {output_file.name}")
    
    # Exit code
    if stats['syntax_errors'] > 0:
        print("\n⚠️  Some files have errors that should be fixed!")
        sys.exit(1)
    else:
        print("\n✅ All files passed basic linting!")
        sys.exit(0)


if __name__ == "__main__":
    main()

