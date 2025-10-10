#!/usr/bin/env python3
"""Analyze environment error patterns from error analysis JSON files."""

import json
import re
from collections import defaultdict

# Read all environment errors
errors = []
with open('/tmp/env_errors.txt', 'r') as f:
    for line in f:
        parts = line.strip().split('|', 2)
        if len(parts) == 3:
            errors.append({
                'file': parts[0].replace('_error_analysis.json', ''),
                'task_id': parts[1],
                'description': parts[2]
            })

print("=" * 80)
print("🔍 DETAILED ENVIRONMENT ERROR PATTERN ANALYSIS")
print("=" * 80)
print()

# Detailed pattern detection with specific error messages
patterns = {
    "str_no_get": [],
    "fixed_now_iso": [],
    "get_next_account_id": [],
    "table_not_defined": [],
    "empty_trajectory": [],
    "data_validation": [],
    "logic_bug": [],
    "other_undefined": []
}

undefined_vars = defaultdict(list)

for error in errors:
    desc = error['description']
    env = error['file']
    
    # Check for specific error messages
    if "'str' object has no attribute 'get'" in desc:
        patterns["str_no_get"].append(env)
    elif "_fixed_now_iso" in desc and "not defined" in desc:
        patterns["fixed_now_iso"].append(env)
    elif "get_next_account_id" in desc:
        patterns["get_next_account_id"].append(env)
    elif "_table" in desc and "not defined" in desc:
        patterns["table_not_defined"].append(env)
    elif "empty" in desc.lower() and "trajectory" in desc.lower():
        patterns["empty_trajectory"].append(env)
    elif any(word in desc.lower() for word in ["missing", "validation", "incorrect data", "expected data"]):
        patterns["data_validation"].append(env)
    elif "incorrectly enforced" in desc.lower() or "incorrect total" in desc.lower():
        patterns["logic_bug"].append(env)
    else:
        # Try to extract undefined variable names
        match = re.search(r"name '([^']+)' is not defined", desc)
        if match:
            var_name = match.group(1)
            if var_name not in ["_fixed_now_iso", "get_next_account_id", "_table"]:
                patterns["other_undefined"].append(env)
                undefined_vars[var_name].append(env)

# Print detailed breakdown
total = len(errors)

print("🔴 'str' object has no attribute 'get'")
envs = patterns["str_no_get"]
count = len(envs)
pct = (count / total) * 100
print(f"   Count: {count} ({pct:.1f}%)")
if envs:
    for i in range(0, len(envs), 6):
        print(f"   Affected: {', '.join(envs[i:i+6])}")
print()

print("🔴 Empty Trajectory (Initialization Failure)")
envs = patterns["empty_trajectory"]
count = len(envs)
pct = (count / total) * 100
print(f"   Count: {count} ({pct:.1f}%)")
if envs:
    for i in range(0, len(envs), 6):
        print(f"   Affected: {', '.join(envs[i:i+6])}")
print()

print("🔴 name '_fixed_now_iso' is not defined")
envs = patterns["fixed_now_iso"]
count = len(envs)
pct = (count / total) * 100
print(f"   Count: {count} ({pct:.1f}%)")
if envs:
    print(f"   Affected: {', '.join(envs)}")
print()

print("🔴 name 'get_next_account_id' is not defined")
envs = patterns["get_next_account_id"]
count = len(envs)
pct = (count / total) * 100
print(f"   Count: {count} ({pct:.1f}%)")
if envs:
    print(f"   Affected: {', '.join(envs)}")
print()

print("🔴 name '_table' is not defined")
envs = patterns["table_not_defined"]
count = len(envs)
pct = (count / total) * 100
print(f"   Count: {count} ({pct:.1f}%)")
if envs:
    print(f"   Affected: {', '.join(envs)}")
print()

print("🔴 Other Undefined Variables/Functions")
envs = patterns["other_undefined"]
count = len(envs)
pct = (count / total) * 100
print(f"   Count: {count} ({pct:.1f}%)")
if undefined_vars:
    for var, env_list in sorted(undefined_vars.items()):
        print(f"   • {var}: {', '.join(env_list)}")
print()

print("🔴 Data Validation/Missing Data")
envs = patterns["data_validation"]
count = len(envs)
pct = (count / total) * 100
print(f"   Count: {count} ({pct:.1f}%)")
if envs:
    print(f"   Affected: {', '.join(envs)}")
print()

print("🔴 Logic Bugs (Incorrect Enforcement)")
envs = patterns["logic_bug"]
count = len(envs)
pct = (count / total) * 100
print(f"   Count: {count} ({pct:.1f}%)")
if envs:
    print(f"   Affected: {', '.join(envs)}")
print()

print("=" * 80)
print()

# Summary stats
print("📊 PATTERN SUMMARY")
print("=" * 80)
print()

pattern_names = {
    "str_no_get": "'str' object has no attribute 'get'",
    "empty_trajectory": "Empty Trajectory",
    "fixed_now_iso": "_fixed_now_iso not defined",
    "get_next_account_id": "get_next_account_id not defined",
    "table_not_defined": "_table not defined",
    "other_undefined": "Other undefined variables",
    "data_validation": "Data validation",
    "logic_bug": "Logic bugs"
}

sorted_patterns = sorted(patterns.items(), key=lambda x: len(x[1]), reverse=True)
for key, envs in sorted_patterns:
    if envs:
        count = len(envs)
        pct = (count / total) * 100
        print(f"{pattern_names[key]:40} {count:3} envs ({pct:5.1f}%)")

print()
print("=" * 80)
print()

# Group by error type for fixing
print("📋 RECOMMENDED FIX STRATEGY")
print("=" * 80)
print()

print("🔧 PRIORITY 1: 'str' object has no attribute 'get' (MOST COMMON)")
count = len(patterns["str_no_get"])
if count > 0:
    print(f"   Affected: {count} environments ({(count/total)*100:.1f}%)")
    print("   Root Cause: Tools expect dict/object but receive string/key")
    print("   Fix: Review data access patterns in tools.py")
    print("   Look for: Iterating over dict.keys() instead of dict.values()")
    print("   Example: for item in data['items']: item.get('name')")
    print("            Should be: for item in data['items'].values(): item.get('name')")
    print()

print("🔧 PRIORITY 2: Empty Trajectories (INITIALIZATION FAILURES)")
count = len(patterns["empty_trajectory"])
if count > 0:
    print(f"   Affected: {count} environments ({(count/total)*100:.1f}%)")
    print("   Root Cause: Environment fails to start/initialize task")
    print("   Fix: Check env.py, __init__.py, and task loading")
    print("   Look for:")
    print("     • Missing imports")
    print("     • Data loading errors")
    print("     • Tool registration issues")
    print("     • Syntax errors preventing module load")
    print()

print("🔧 PRIORITY 3: Undefined Variables/Functions")
undefined_total = (len(patterns["fixed_now_iso"]) + 
                  len(patterns["get_next_account_id"]) + 
                  len(patterns["table_not_defined"]) + 
                  len(patterns["other_undefined"]))
if undefined_total > 0:
    print(f"   Affected: {undefined_total} environments ({(undefined_total/total)*100:.1f}%)")
    print("   Root Cause: Missing helper functions or incorrect imports")
    print("   Fix: Add missing function definitions or import statements")
    print("   Common missing:")
    if patterns["fixed_now_iso"]:
        print(f"     • _fixed_now_iso: {len(patterns['fixed_now_iso'])} envs")
        print("       Fix: Add datetime helper function")
    if patterns["get_next_account_id"]:
        print(f"     • get_next_account_id: {len(patterns['get_next_account_id'])} envs")
        print("       Fix: Add ID generation helper")
    if patterns["table_not_defined"]:
        print(f"     • _table: {len(patterns['table_not_defined'])} envs")
        print("       Fix: Initialize _table variable or import")
    if undefined_vars:
        print(f"     • Other: {len(patterns['other_undefined'])} envs")
        for var in list(undefined_vars.keys())[:5]:
            print(f"       - {var}")
    print()

print("🔧 PRIORITY 4: Data Validation/Logic Bugs")
count = len(patterns["data_validation"]) + len(patterns["logic_bug"])
if count > 0:
    print(f"   Affected: {count} environments ({(count/total)*100:.1f}%)")
    print("   Root Cause: Missing data or incorrect business logic")
    print("   Fix: Verify data.json and tool validation logic")
    print()

print("=" * 80)
print()

print("🎯 ACTION ITEMS")
print("=" * 80)
print()
print("1. Fix 'str' object errors:")
print("   • Search for: .keys() or dict iteration without .values()")
print(f"   • Environments to fix: {len(patterns['str_no_get'])}")
print()
print("2. Fix empty trajectories:")
print("   • Check each env for import/syntax errors")
print(f"   • Environments to fix: {len(patterns['empty_trajectory'])}")
print()
print("3. Fix undefined variables:")
print("   • Add missing helper functions")
print(f"   • Environments to fix: {undefined_total}")
print()
print("4. Fix data/logic issues:")
print("   • Review data.json and validation logic")
print(f"   • Environments to fix: {len(patterns['data_validation']) + len(patterns['logic_bug'])}")
print()
print("=" * 80)

