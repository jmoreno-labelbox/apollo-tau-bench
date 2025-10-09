#!/usr/bin/env python3
"""
Run tests on multiple environments/tasks and collect ALL unique tool errors
"""
import json
import sys
import os
from pathlib import Path
from collections import defaultdict

# Add tau to path
sys.path.insert(0, str(Path(__file__).parent / "tau"))

from tau_bench.envs import get_env
from tau_bench.agents.tool_calling_agent import ToolCallingAgent

def collect_errors_from_env(env_name, task_indices, api_key):
    """Run tasks and collect errors"""
    errors = []
    
    os.environ['OPENAI_API_KEY'] = api_key
    
    try:
        env = get_env(
            env_name,
            user_strategy='human',  # Avoid API costs for user
            user_model='gpt-4o',
            user_provider='openai',
            task_split='test'
        )
        
        agent = ToolCallingAgent(
            tools_info=env.tools_info,
            wiki=env.wiki,
            model='gpt-4o-mini',
            provider='openai'
        )
        
        for task_idx in task_indices:
            try:
                # Reset env for this task
                test_env = get_env(
                    env_name,
                    user_strategy='human',
                    user_model='gpt-4o',
                    user_provider='openai',
                    task_split='test',
                    task_index=task_idx
                )
                
                result = agent.solve(env=test_env, task_index=task_idx, max_num_steps=30)
                messages = result.messages
                
                # Extract tool errors
                for i, msg in enumerate(messages):
                    if msg.get('role') == 'tool':
                        content = msg.get('content', '')
                        
                        # Check for REAL errors (not "not found" messages)
                        error_keywords = [
                            'Error:', 'Exception', 'Traceback', 'TypeError', 
                            'KeyError', 'AttributeError', 'string indices must be integers',
                            'unexpected keyword argument', 'missing 1 required',
                            'object has no attribute', 'cannot be interpreted'
                        ]
                        
                        if any(kw in content for kw in error_keywords):
                            errors.append({
                                'env': env_name,
                                'task_id': task_idx,
                                'tool': msg.get('name'),
                                'error': content
                            })
                
            except Exception as e:
                print(f"  Error running {env_name} task {task_idx}: {e}")
                
    except Exception as e:
        print(f"  Error loading {env_name}: {e}")
    
    return errors


def categorize_errors(all_errors):
    """Categorize errors by pattern for systematic fixing"""
    patterns = defaultdict(list)
    
    for error_info in all_errors:
        error = error_info['error']
        
        # Categorize by error type
        if 'missing 1 required positional argument' in error and 'filter_params' in error:
            patterns['missing_filter_params'].append(error_info)
        elif 'string indices must be integers' in error:
            patterns['string_indices_error'].append(error_info)
        elif 'object has no attribute' in error and 'append' in error:
            patterns['dict_append_error'].append(error_info)
        elif 'unexpected keyword argument' in error:
            patterns['schema_mismatch'].append(error_info)
        else:
            patterns['other'].append(error_info)
    
    return patterns


def main():
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY not set")
        return
    
    # Test environments to scan
    test_envs = [
        ('retail_1', [1, 2, 3, 9, 11, 12, 13]),
        ('retail_2', [1, 2, 3]),
        ('retail_3', [1, 2]),
        ('airline_2', [1, 2, 3]),
        ('banking_services_1', [1, 2]),
    ]
    
    print("=" * 70)
    print("COLLECTING ALL TOOL ERRORS")
    print("=" * 70)
    print()
    
    all_errors = []
    
    for env_name, task_indices in test_envs:
        print(f"Testing {env_name} (tasks: {task_indices})...")
        env_errors = collect_errors_from_env(env_name, task_indices, api_key)
        all_errors.extend(env_errors)
        print(f"  Found {len(env_errors)} errors")
    
    print()
    print("=" * 70)
    print(f"TOTAL ERRORS COLLECTED: {len(all_errors)}")
    print("=" * 70)
    print()
    
    # Categorize
    patterns = categorize_errors(all_errors)
    
    print("ERROR PATTERNS:")
    for pattern_name, errors in patterns.items():
        print(f"\n{pattern_name}: {len(errors)} occurrences")
        if errors:
            # Show unique tools affected
            tools = set(e['tool'] for e in errors)
            envs = set(e['env'] for e in errors)
            print(f"  Affected tools: {', '.join(tools)}")
            print(f"  Affected envs: {', '.join(envs)}")
            print(f"  Example: {errors[0]['error'][:150]}")
    
    # Save to file
    with open('error_analysis.json', 'w') as f:
        json.dump({
            'total_errors': len(all_errors),
            'patterns': {k: [{'env': e['env'], 'task': e['task_id'], 'tool': e['tool'], 'error': e['error'][:200]} 
                          for e in v] 
                        for k, v in patterns.items()}
        }, f, indent=2)
    
    print()
    print("=" * 70)
    print(f"✅ Error analysis saved to error_analysis.json")
    print("=" * 70)


if __name__ == "__main__":
    main()

