#!/usr/bin/env python3
"""
Directly invoke EVERY tool in EVERY environment to find bugs - NO LLM needed
"""
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

sys.path.insert(0, str(Path(__file__).parent / "tau"))

def test_environment_tools(env_name):
    """Test all tools in one environment by direct invocation"""
    
    try:
        # Import environment
        env_module = __import__(f'tau_bench.envs.{env_name}.env', fromlist=[''])
        tools_module = __import__(f'tau_bench.envs.{env_name}.tools', fromlist=['TOOLS'])
        data_module = __import__(f'tau_bench.envs.{env_name}.data', fromlist=['load_data'])
        
        # Load data
        data = data_module.load_data()
        tools = tools_module.TOOLS
        
        errors = []
        
        # Test each tool with minimal params
        for tool in tools:
            tool_name = tool.get_info()['function']['name']
            
            try:
                # Get schema to understand required params
                schema = tool.get_info()['function']['parameters']
                required = schema.get('required', [])
                properties = schema.get('properties', {})
                
                # Build minimal test params
                test_params = {}
                for param in required:
                    if param in properties:
                        param_type = properties[param].get('type', 'string')
                        
                        if param_type == 'string':
                            test_params[param] = 'test_id'
                        elif param_type == 'integer':
                            test_params[param] = 1
                        elif param_type == 'number':
                            test_params[param] = 1.0
                        elif param_type == 'array':
                            test_params[param] = []
                        elif param_type == 'object':
                            test_params[param] = {}
                        elif param_type == 'boolean':
                            test_params[param] = False
                
                # Invoke tool
                result = tool.invoke(data, **test_params)
                
                # Check if result contains error
                if 'Error:' in result or 'Exception' in result:
                    # This is expected - normal "not found" type errors
                    pass
                    
            except Exception as e:
                # This is a REAL bug
                error_msg = str(e)
                if any(kw in error_msg for kw in [
                    'string indices must be integers',
                    "'dict' object has no attribute 'append'",
                    "'str' object has no attribute 'get'",
                    "'list' object has no attribute 'keys'",
                    'missing 1 required',
                    'unexpected keyword'
                ]):
                    errors.append({
                        'tool': tool_name,
                        'error': error_msg[:200]
                    })
        
        return env_name, errors
        
    except Exception as e:
        return env_name, [{'tool': 'LOAD_ERROR', 'error': str(e)[:200]}]


def main():
    base = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    env_names = sorted([d.name for d in base.iterdir() 
                       if d.is_dir() and not d.name.startswith('_') and d.name != '__pycache__'])
    
    print("=" * 70)
    print(f"DIRECT TOOL TESTING - ALL {len(env_names)} ENVIRONMENTS")
    print("=" * 70)
    print(f"No LLM calls - just direct Python invocation")
    print(f"Testing ALL tools in each environment")
    print("=" * 70)
    print()
    
    # Test all in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(test_environment_tools, env): env for env in env_names}
        
        results = {}
        for future in as_completed(futures):
            env_name, errors = future.result()
            results[env_name] = errors
            
            status = "✅" if len(errors) == 0 else f"❌ {len(errors)}"
            print(f"{status} {env_name}")
    
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    total_errors = sum(len(errs) for errs in results.values())
    envs_with_errors = sum(1 for errs in results.values() if errs)
    
    print(f"Environments: {len(env_names)}")
    print(f"With errors: {envs_with_errors}")
    print(f"Total errors: {total_errors}")
    
    if total_errors > 0:
        print()
        print("Top 10 environments with most errors:")
        sorted_results = sorted(results.items(), key=lambda x: len(x[1]), reverse=True)[:10]
        for env, errs in sorted_results:
            if errs:
                print(f"  {env}: {len(errs)} errors")
    
    # Save detailed report
    with open('direct_tool_test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print()
    print("=" * 70)
    print("✅ Saved to direct_tool_test_results.json")
    print("=" * 70)


if __name__ == "__main__":
    main()

