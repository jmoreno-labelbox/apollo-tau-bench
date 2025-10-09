#!/usr/bin/env python3
"""
Master script that runs all fixes in a loop until no more errors can be fixed
"""
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List

# Import our fixing modules
sys.path.insert(0, str(Path(__file__).parent))

def run_tests() -> Dict:
    """Run direct_tool_test_all.py and return results"""
    print("🧪 Running tests...")
    subprocess.run([sys.executable, "direct_tool_test_all.py"], 
                   capture_output=True, text=True)
    
    with open('direct_tool_test_results.json') as f:
        return json.load(f)


def count_errors(results: Dict) -> tuple:
    """Count environments and total errors"""
    env_errors = sum(1 for errs in results.values() if errs)
    total_errors = sum(len(errs) for errs in results.values())
    return env_errors, total_errors


def apply_all_fixes():
    """Apply all available fixes"""
    fixes_applied = 0
    
    # Fix 1: Syntax errors
    print("  → Applying syntax fixes...")
    result = subprocess.run([sys.executable, "auto_fix_tool_errors.py"], 
                          capture_output=True, text=True)
    if "Fixed" in result.stdout:
        # Parse output to count fixes
        for line in result.stdout.split('\n'):
            if line.startswith('✅ Fixed') and 'syntax' in line:
                parts = line.split('/')
                if parts:
                    try:
                        count = int(parts[0].split()[-1])
                        fixes_applied += count
                    except:
                        pass
    
    # Fix 2: Dict iteration errors (v3)
    print("  → Applying dict iteration fixes...")
    result = subprocess.run([sys.executable, "fix_dict_iteration_v3.py"], 
                          capture_output=True, text=True)
    if "Fixed" in result.stdout:
        for line in result.stdout.split('\n'):
            if line.startswith('✅ Fixed') and 'environments' in line:
                try:
                    count = int(line.split('/')[0].split()[-1])
                    fixes_applied += count
                except:
                    pass
    
    return fixes_applied


def main():
    """Main loop"""
    print("=" * 70)
    print("AUTOMATED ERROR FIXING LOOP")
    print("=" * 70)
    print()
    
    # Initial test
    results = run_tests()
    env_errors, total_errors = count_errors(results)
    
    print(f"Initial state: {env_errors} envs with {total_errors} total errors")
    print()
    
    iteration = 1
    max_iterations = 5
    
    while iteration <= max_iterations:
        print("=" * 70)
        print(f"ITERATION {iteration}")
        print("=" * 70)
        
        # Apply all fixes
        fixes = apply_all_fixes()
        
        if fixes == 0:
            print("\n❌ No fixes applied in this iteration")
            break
        
        print(f"\n✅ Applied {fixes} fixes in this iteration")
        
        # Re-run tests
        results = run_tests()
        new_env_errors, new_total_errors = count_errors(results)
        
        print(f"\nResults: {new_env_errors} envs with {new_total_errors} total errors")
        
        # Check if we made progress
        if new_env_errors >= env_errors and new_total_errors >= total_errors:
            print("\n⚠️  No progress made, stopping")
            break
        
        print(f"Progress: Fixed {env_errors - new_env_errors} envs, {total_errors - new_total_errors} errors")
        
        env_errors = new_env_errors
        total_errors = new_total_errors
        iteration += 1
        print()
    
    print()
    print("=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    print(f"Remaining: {env_errors} environments with {total_errors} total errors")
    print()
    
    # Show breakdown of remaining errors
    if total_errors > 0:
        error_types = {}
        for env, errs in results.items():
            for err in errs:
                if err.get('tool') == 'LOAD_ERROR':
                    key = 'SYNTAX_ERROR'
                elif "'str' object has no attribute 'get'" in err['error']:
                    key = 'STR_USED_AS_DICT'
                elif "'dict' object has no attribute 'append'" in err['error']:
                    key = 'DICT_USED_AS_LIST'
                elif "string indices must be integers" in err['error']:
                    key = 'STRING_INDEXED'
                else:
                    key = 'OTHER'
                
                error_types[key] = error_types.get(key, 0) + 1
        
        print("Remaining error types:")
        for error_type, count in sorted(error_types.items(), key=lambda x: -x[1]):
            print(f"  {error_type}: {count}")
        print()
        
        # Show top failing environments
        sorted_results = sorted(
            [(env, errs) for env, errs in results.items() if errs],
            key=lambda x: len(x[1]),
            reverse=True
        )[:10]
        
        print("Top 10 failing environments:")
        for env, errs in sorted_results:
            print(f"  {env}: {len(errs)} errors")


if __name__ == "__main__":
    main()

