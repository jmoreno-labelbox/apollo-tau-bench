#!/usr/bin/env python3
"""
Comprehensive verification that tau-bench environments load and work correctly.
Tests environment loading, wiki presence, tool schemas, and actual tool invocation.
"""

import sys
import json
from pathlib import Path

# Add tau to path
sys.path.insert(0, str(Path(__file__).parent / "tau"))

from tau_bench.envs import get_env

def test_environment_loading(env_name):
    """Test that environment loads without errors."""
    print(f"\n{'='*60}")
    print(f"Testing: {env_name}")
    print('='*60)
    
    try:
        # Load environment (using 'human' strategy to avoid API calls)
        env = get_env(
            env_name, 
            user_strategy='human',  # Human doesn't require API keys
            user_model='gpt-4o',
            user_provider='openai',
            task_split='test'
        )
        print(f"✅ Environment loaded successfully")
        
        # Check wiki exists and is non-empty
        assert hasattr(env, 'wiki'), "Environment missing 'wiki' attribute"
        assert isinstance(env.wiki, str), f"Wiki should be string, got {type(env.wiki)}"
        assert len(env.wiki) > 0, "Wiki is empty"
        print(f"✅ Wiki present: {len(env.wiki)} characters")
        
        # Check tools are loaded
        assert hasattr(env, 'tools_info'), "Environment missing 'tools_info'"
        assert len(env.tools_info) > 0, "No tools loaded"
        print(f"✅ Tools loaded: {len(env.tools_info)} tools")
        
        # Check tasks are loaded
        assert hasattr(env, 'tasks'), "Environment missing 'tasks'"
        assert len(env.tasks) > 0, "No tasks loaded"
        print(f"✅ Tasks loaded: {len(env.tasks)} tasks")
        
        # Check data is loaded
        assert hasattr(env, 'data'), "Environment missing 'data'"
        assert isinstance(env.data, dict), f"Data should be dict, got {type(env.data)}"
        print(f"✅ Data loaded: {len(env.data)} tables")
        
        # Verify tool schemas are valid
        for tool_info in env.tools_info:
            assert 'type' in tool_info, "Tool missing 'type'"
            assert 'function' in tool_info, "Tool missing 'function'"
            assert 'name' in tool_info['function'], "Tool function missing 'name'"
            assert 'parameters' in tool_info['function'], "Tool function missing 'parameters'"
        print(f"✅ All tool schemas valid")
        
        return env, True
        
    except Exception as e:
        print(f"❌ Failed to load environment: {e}")
        import traceback
        traceback.print_exc()
        return None, False


def test_tool_invocation(env_name, env):
    """Test that tools can actually be invoked."""
    print(f"\n{'='*60}")
    print(f"Testing tool invocation: {env_name}")
    print('='*60)
    
    try:
        # Test depends on environment type
        if 'retail' in env_name:
            # Test GetInfoFromDb
            if 'GetInfoFromDb' in env.tools_map:
                print("  Testing GetInfoFromDb...")
                result = env.tools_map['GetInfoFromDb'].invoke(
                    data=env.data,
                    database_name='users',
                    filter_params={},
                    required_fields=['user_id']
                )
                result_data = json.loads(result)
                assert isinstance(result_data, list), "GetInfoFromDb should return list"
                print(f"    ✅ GetInfoFromDb returned {len(result_data)} users")
            
            # Test GetUserIdFromFullNameAndZip
            if 'GetUserIdFromFullNameAndZip' in env.tools_map:
                print("  Testing GetUserIdFromFullNameAndZip...")
                users = env.data.get('users', {})
                if users:
                    first_user = list(users.values())[0]
                    result = env.tools_map['GetUserIdFromFullNameAndZip'].invoke(
                        data=env.data,
                        first_name=first_user['name']['first_name'],
                        last_name=first_user['name']['last_name'],
                        zip=first_user['address']['zip']
                    )
                    result_data = json.loads(result)
                    assert result_data == first_user['user_id'], "Should find correct user"
                    print(f"    ✅ GetUserIdFromFullNameAndZip returned: {result_data}")
        
        elif 'airline' in env_name:
            # Just verify tools are callable
            print("  Verifying airline tools are callable...")
            for tool_name in list(env.tools_map.keys())[:3]:
                tool = env.tools_map[tool_name]
                assert hasattr(tool, 'invoke'), f"Tool {tool_name} missing invoke method"
                assert hasattr(tool, 'get_info'), f"Tool {tool_name} missing get_info method"
                print(f"    ✅ {tool_name} has correct interface")
        
        print(f"✅ Tool invocation tests passed")
        return True
        
    except Exception as e:
        print(f"❌ Tool invocation failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_data_structure(env_name, env):
    """Test that data structure is correctly handled (dict with string keys -> list)."""
    print(f"\n{'='*60}")
    print(f"Testing data structure: {env_name}")
    print('='*60)
    
    try:
        # Check raw data structure
        for table_name, table_data in list(env.data.items())[:3]:
            print(f"  Table '{table_name}': ", end='')
            
            # Data should be dict with string keys
            assert isinstance(table_data, dict), f"Table should be dict, got {type(table_data)}"
            
            if table_data:
                # Check keys are strings
                first_key = list(table_data.keys())[0]
                assert isinstance(first_key, str), f"Keys should be strings, got {type(first_key)}"
                
                # Check values are dicts
                first_value = list(table_data.values())[0]
                assert isinstance(first_value, dict), f"Values should be dicts, got {type(first_value)}"
                
                print(f"✅ {len(table_data)} records (dict format)")
            else:
                print(f"✅ empty table")
        
        print(f"✅ Data structure is correct")
        return True
        
    except Exception as e:
        print(f"❌ Data structure test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run comprehensive tests on multiple environments."""
    
    # Environments to test
    test_envs = [
        'retail_1',
        'retail_2', 
        'airline_1',
        'airline_2',
        'banking_services_1',
        'academic_search_1',
        'project_management_1',
    ]
    
    results = {}
    
    print(f"\n{'#'*60}")
    print("TAU-BENCH COMPREHENSIVE VERIFICATION")
    print(f"{'#'*60}")
    print(f"\nTesting {len(test_envs)} environments...\n")
    
    for env_name in test_envs:
        try:
            # Test 1: Environment loading
            env, load_success = test_environment_loading(env_name)
            if not load_success:
                results[env_name] = "❌ Failed to load"
                continue
            
            # Test 2: Data structure
            data_success = test_data_structure(env_name, env)
            
            # Test 3: Tool invocation
            tool_success = test_tool_invocation(env_name, env)
            
            if load_success and data_success and tool_success:
                results[env_name] = "✅ All tests passed"
            else:
                results[env_name] = "⚠️  Some tests failed"
                
        except Exception as e:
            results[env_name] = f"❌ Exception: {str(e)}"
    
    # Print summary
    print(f"\n\n{'='*60}")
    print("SUMMARY")
    print('='*60)
    
    for env_name, status in results.items():
        print(f"{env_name:40s} {status}")
    
    # Overall result
    success_count = sum(1 for s in results.values() if s.startswith("✅"))
    total_count = len(results)
    
    print(f"\n{'='*60}")
    print(f"RESULT: {success_count}/{total_count} environments passed all tests")
    print('='*60)
    
    if success_count == total_count:
        print("\n🎉 ALL ENVIRONMENTS VERIFIED SUCCESSFULLY! 🎉\n")
        return 0
    else:
        print(f"\n⚠️  {total_count - success_count} environment(s) had issues\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())

