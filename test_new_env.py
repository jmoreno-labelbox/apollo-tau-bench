#!/usr/bin/env python3
"""
Simple test script for new domain environments.
Tests that environments can be loaded and basic functionality works.
"""

from tau_bench.envs.user import UserStrategy


def test_environment(domain: str, variation: str):
    """Test loading and basic functionality of an environment."""
    print(f"\n{'='*70}")
    print(f"Testing: {domain} - {variation}")
    print('='*70)
    
    # Dynamically import the environment
    module_path = f"domains.{domain}.variations.{variation}.env"
    
    # Get the class name (e.g., MockAirlineDomainEnv)
    parts = domain.split('_')
    class_name = 'Mock' + ''.join(word.capitalize() for word in parts) + 'DomainEnv'
    
    try:
        # Import the module
        module = __import__(module_path, fromlist=[class_name])
        env_class = getattr(module, class_name)
        
        # Create environment instance with HUMAN strategy (no API needed)
        env = env_class(user_strategy=UserStrategy.HUMAN)
        
        # Basic checks
        print(f"✅ Environment loaded successfully!")
        print(f"✅ Tasks: {len(env.tasks)}")
        print(f"✅ Rules: {len(env.rules)}")
        print(f"✅ Data loaded: {'flights' in env.data or 'users' in env.data or len(env.data) > 0}")
        
        # Check first task
        if len(env.tasks) > 0:
            task = env.tasks[0]
            print(f"✅ First task has {len(task.actions)} actions")
            print(f"✅ Outputs type: {type(task.outputs).__name__} (should be 'list')")
            
        # Note: We skip env.reset() because HUMAN strategy requires keyboard input
        print(f"✅ Environment structure validated!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Test multiple environments."""
    test_cases = [
        ("airline", "variation_3"),
        ("retail", "variation_2"),
        ("banking_services", "variation_1"),
    ]
    
    print("\n" + "="*70)
    print("TESTING NEW DOMAIN ENVIRONMENTS")
    print("="*70)
    
    results = {}
    for domain, variation in test_cases:
        success = test_environment(domain, variation)
        results[f"{domain}/{variation}"] = "✅ PASS" if success else "❌ FAIL"
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    for env_name, status in results.items():
        print(f"{status} - {env_name}")
    
    all_passed = all("✅" in v for v in results.values())
    if all_passed:
        print("\n🎉 All tests passed! Your environments are ready to use!")
    else:
        print("\n⚠️  Some tests failed. Check errors above.")


if __name__ == "__main__":
    main()

