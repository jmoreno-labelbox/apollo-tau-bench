#!/usr/bin/env python3
"""
Fix Pattern 3: Data Validation / Missing Data (4 environments)

Environments:
- recipes_5
- smart_home_3
- smart_home_5
- social_media_advertising_1
"""

import json
import sys
from pathlib import Path

TAU_BASE = Path("tau/tau_bench/envs")

PATTERN3_ENVS = [
    "recipes_5",
    "smart_home_3",
    "smart_home_5",
    "social_media_advertising_1"
]


def investigate_environment(env_name: str):
    """Investigate what's wrong with an environment."""
    print(f"\n{'='*80}")
    print(f"🔍 Investigating: {env_name}")
    print(f"{'='*80}")
    
    # Check error analysis
    error_file = Path(f"tau/error_analyses/{env_name}_error_analysis.json")
    if error_file.exists():
        with open(error_file, 'r') as f:
            data = json.load(f)
        
        if 'fault_assignment_analysis' in data and data['fault_assignment_analysis']:
            fault = data['fault_assignment_analysis'][0]
            print(f"Error Description:")
            print(f"  {fault.get('description', 'No description')[:300]}")
            print()
    
    # Check data.json structure
    data_file = TAU_BASE / env_name / "data" / "data.json"
    if not data_file.exists():
        data_file = TAU_BASE / env_name / "data.json"
    
    if data_file.exists():
        print(f"✅ data.json exists: {data_file}")
        try:
            with open(data_file, 'r') as f:
                data = json.load(f)
            print(f"   Top-level keys: {list(data.keys())[:10]}")
            print(f"   Total keys: {len(data.keys())}")
        except Exception as e:
            print(f"   ⚠️  Error reading data.json: {e}")
    else:
        print(f"⚠️  data.json not found")
    
    # Check tasks
    tasks_file = TAU_BASE / env_name / "tasks_test.py"
    if tasks_file.exists():
        print(f"✅ tasks_test.py exists")
    else:
        print(f"⚠️  tasks_test.py not found")
    
    return True


def main():
    print("=" * 80)
    print("🔧 FIX PATTERN 3: Data Validation / Missing Data")
    print("=" * 80)
    print()
    print("Investigating 4 environments to understand data validation issues...")
    print()
    
    for env_name in PATTERN3_ENVS:
        investigate_environment(env_name)
    
    print("\n" + "=" * 80)
    print("📊 INVESTIGATION COMPLETE")
    print("=" * 80)
    print()
    print("Next steps:")
    print("1. Review error descriptions above")
    print("2. Check data.json for missing fields")
    print("3. Run environments individually to see actual errors:")
    print(f"   cd tau && PYTHONPATH=. python3 run.py --env {PATTERN3_ENVS[0]} --end-index 1")
    print()
    print("4. Re-run error analysis after fixes:")
    print(f"   python3 run_error_analysis_all_envs.py --run-tests --envs {' '.join(PATTERN3_ENVS)}")
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()

