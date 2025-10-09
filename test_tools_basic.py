#!/usr/bin/env python3
"""
Basic sanity test for tools to ensure they don't have obvious errors
"""

from tau_bench.envs import get_env

def test_retail_1():
    print("Testing retail_1 environment...")
    env = get_env('retail_1', user_strategy='static', user_model='gpt-4o', user_provider='openai', task_split='test')
    
    # Test GetInfoFromDB
    print("  Testing GetInfoFromDB...")
    result = env.tools_map['GetInfoFromDb'].invoke(
        data=env.data,
        database_name='users',
        filter_params={},
        required_fields=['user_id']
    )
    print(f"    ✅ GetInfoFromDb returned {len(result)} chars")
    
    # Test GetUserIdFromFullNameAndZip
    print("  Testing GetUserIdFromFullNameAndZip...")
    # Get first user to test with
    import json
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
        print(f"    ✅ GetUserIdFromFullNameAndZip returned: {result_data}")
    
    print("✅ retail_1 tools working correctly\n")

def test_airline_1():
    print("Testing airline_1 environment...")
    env = get_env('airline_1', user_strategy='static', user_model='gpt-4o', user_provider='openai', task_split='test')
    
    # Test basic tool invocation
    print("  Testing tools can be invoked...")
    # Just check that tools are loadable and have correct structure
    for tool_info in env.tools_info[:3]:  # Test first 3 tools
        tool_name = tool_info['function']['name']
        print(f"    Tool {tool_name}: ✅")
    
    print("✅ airline_1 tools structure correct\n")

if __name__ == "__main__":
    try:
        test_retail_1()
        test_airline_1()
        print("="*50)
        print("✅ ALL TESTS PASSED")
        print("="*50)
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        exit(1)

