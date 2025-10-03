#!/usr/bin/env python3
"""
Comprehensive test script for ALL domain environments.
Tests that all 122 env.py files can be loaded.
"""

from pathlib import Path
from tau_bench.envs.user import UserStrategy
import importlib


def get_env_class_name(domain_name: str) -> str:
    """Convert domain folder name to environment class name."""
    parts = domain_name.replace('-', '_').split('_')
    return 'Mock' + ''.join(word.capitalize() for word in parts) + 'DomainEnv'


def test_environment(domain: str, variation: str) -> dict:
    """Test loading a single environment. Returns result dict."""
    module_path = f"domains.{domain}.variations.{variation}.env"
    class_name = get_env_class_name(domain)
    
    try:
        # Import the module
        module = importlib.import_module(module_path)
        env_class = getattr(module, class_name)
        
        # Create environment instance
        env = env_class(user_strategy=UserStrategy.HUMAN)
        
        # Validate
        num_tasks = len(env.tasks)
        num_rules = len(env.rules)
        has_data = len(env.data) > 0
        
        # Check first task if exists
        outputs_valid = True
        if num_tasks > 0:
            outputs_valid = isinstance(env.tasks[0].outputs, list)
        
        return {
            'status': 'PASS',
            'tasks': num_tasks,
            'rules': num_rules,
            'has_data': has_data,
            'outputs_valid': outputs_valid,
        }
        
    except Exception as e:
        return {
            'status': 'FAIL',
            'error': str(e),
        }


def main():
    """Test all environments."""
    domains_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains")
    
    # Find all env.py files
    env_files = list(domains_path.glob("*/variations/*/env.py"))
    
    print(f"\n{'='*70}")
    print(f"TESTING ALL {len(env_files)} ENVIRONMENTS")
    print('='*70 + '\n')
    
    results = {}
    passed = 0
    failed = 0
    
    for env_file in sorted(env_files):
        # Extract domain and variation from path
        parts = env_file.parts
        domain = parts[-4]  # domains/[domain]/variations/[variation]/env.py
        variation = parts[-2]
        
        env_name = f"{domain}/{variation}"
        result = test_environment(domain, variation)
        results[env_name] = result
        
        if result['status'] == 'PASS':
            passed += 1
            print(f"✅ {env_name:60s} Tasks:{result['tasks']:3d} Rules:{result['rules']:3d}")
        else:
            failed += 1
            print(f"❌ {env_name:60s} Error: {result['error'][:40]}")
    
    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print('='*70)
    print(f"Total environments: {len(env_files)}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    
    if failed > 0:
        print(f"\n{'='*70}")
        print("FAILED ENVIRONMENTS:")
        print('='*70)
        for env_name, result in results.items():
            if result['status'] == 'FAIL':
                print(f"❌ {env_name}")
                print(f"   Error: {result['error']}\n")
    
    if passed == len(env_files):
        print("\n🎉🎉🎉 ALL ENVIRONMENTS PASSED! 🎉🎉🎉")
    else:
        print(f"\n⚠️  {failed} environment(s) need attention")


if __name__ == "__main__":
    main()

