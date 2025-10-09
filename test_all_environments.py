#!/usr/bin/env python3
"""
Test ALL environments in tau/tau_bench/envs to verify they load correctly.
"""

import sys
import os
from pathlib import Path

# Add tau to path
sys.path.insert(0, str(Path(__file__).parent / "tau"))

from tau_bench.envs import get_env

def get_all_environment_names():
    """Get all environment names from tau/tau_bench/envs directory."""
    envs_dir = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    env_names = []
    for env_dir in envs_dir.iterdir():
        if env_dir.is_dir() and not env_dir.name.startswith('_') and env_dir.name != '__pycache__':
            env_names.append(env_dir.name)
    
    return sorted(env_names)


def test_environment(env_name):
    """Test that a single environment loads correctly."""
    try:
        # Load environment (using 'human' strategy to avoid API calls)
        env = get_env(
            env_name, 
            user_strategy='human',
            user_model='gpt-4o',
            user_provider='openai',
            task_split='test'
        )
        
        # Basic checks
        assert hasattr(env, 'wiki') and isinstance(env.wiki, str) and len(env.wiki) > 0, "Wiki missing or invalid"
        assert hasattr(env, 'tools_info') and len(env.tools_info) > 0, "Tools not loaded"
        assert hasattr(env, 'tasks') and len(env.tasks) > 0, "Tasks not loaded"
        assert hasattr(env, 'data') and isinstance(env.data, dict), "Data not loaded"
        
        # Verify tool schemas
        for tool_info in env.tools_info:
            assert 'type' in tool_info, "Tool missing 'type'"
            assert 'function' in tool_info, "Tool missing 'function'"
            assert 'name' in tool_info['function'], "Tool function missing 'name'"
        
        return {
            'status': 'PASS',
            'wiki_len': len(env.wiki),
            'num_tools': len(env.tools_info),
            'num_tasks': len(env.tasks),
            'num_tables': len(env.data),
            'error': None
        }
        
    except Exception as e:
        return {
            'status': 'FAIL',
            'wiki_len': 0,
            'num_tools': 0,
            'num_tasks': 0,
            'num_tables': 0,
            'error': str(e)
        }


def main():
    """Test all environments."""
    
    # Get all environment names
    env_names = get_all_environment_names()
    
    print(f"\n{'='*80}")
    print(f"TESTING ALL TAU-BENCH ENVIRONMENTS")
    print(f"{'='*80}")
    print(f"Found {len(env_names)} environments to test\n")
    
    results = {}
    passed = 0
    failed = 0
    
    # Test each environment
    for i, env_name in enumerate(env_names, 1):
        print(f"[{i:3d}/{len(env_names)}] Testing {env_name:50s} ", end='', flush=True)
        
        result = test_environment(env_name)
        results[env_name] = result
        
        if result['status'] == 'PASS':
            print(f"✅ PASS (wiki:{result['wiki_len']:5d} tools:{result['num_tools']:3d} tasks:{result['num_tasks']:3d})")
            passed += 1
        else:
            print(f"❌ FAIL - {result['error']}")
            failed += 1
    
    # Print summary
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Total Environments: {len(env_names)}")
    print(f"Passed: {passed} ({100*passed/len(env_names):.1f}%)")
    print(f"Failed: {failed} ({100*failed/len(env_names):.1f}%)")
    
    # Show failures if any
    if failed > 0:
        print(f"\n{'='*80}")
        print(f"FAILED ENVIRONMENTS")
        print(f"{'='*80}")
        for env_name, result in results.items():
            if result['status'] == 'FAIL':
                print(f"\n{env_name}:")
                print(f"  Error: {result['error']}")
    
    # Print result
    print(f"\n{'='*80}")
    if failed == 0:
        print(f"🎉 SUCCESS: ALL {passed} ENVIRONMENTS PASSED! 🎉")
        print(f"{'='*80}\n")
        return 0
    else:
        print(f"⚠️  {failed} ENVIRONMENT(S) FAILED")
        print(f"{'='*80}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())

