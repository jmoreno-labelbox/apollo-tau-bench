#!/usr/bin/env python3
"""
Smoke test script for tau-bench that tests all environment variations
with different agent strategies and models.

This script runs quick smoke tests (1 trial each) across all environments
to ensure they are properly configured and can execute without errors.
"""

import subprocess
import sys
import os
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any
import argparse


def get_all_envs(envs_dir: str = None) -> List[str]:
    """Discover all available environment directories."""
    # Auto-detect the envs directory
    if envs_dir is None:
        # Try different possible locations
        possible_paths = [
            Path("tau/tau_bench/envs"),      # From root, tau/ subdirectory
            Path("tau_bench/envs"),          # From tau/ directory
            Path("../tau_bench/envs"),       # From subdirectory
        ]
        
        envs_path = None
        for path in possible_paths:
            if path.exists():
                envs_path = path
                break
    else:
        envs_path = Path(envs_dir)
    
    if envs_path is None or not envs_path.exists():
        print(f"Error: Could not find envs directory in any of: {[str(p) for p in possible_paths]}")
        return []
    
    envs = []
    for item in envs_path.iterdir():
        if item.is_dir() and not item.name.startswith("_") and item.name not in ["__pycache__"]:
            # Check if it has an env.py file (valid environment)
            if (item / "env.py").exists():
                envs.append(item.name)
    
    return sorted(envs)


def run_smoke_test(
    env: str,
    agent_strategy: str,
    model: str,
    user_model: str,
    task_split: str = "test",
    num_trials: int = 1,
    max_concurrency: int = 8,
    timeout: int = 300,
) -> Dict[str, Any]:
    """
    Run a single smoke test configuration.
    
    Returns:
        Dict with 'success', 'env', 'strategy', 'stdout', 'stderr', 'returncode', 'duration'
    """
    start_time = datetime.now()
    
    # Determine the working directory (use tau/ if it exists, otherwise current)
    tau_dir = Path("tau")
    if tau_dir.exists() and (tau_dir / "run.py").exists():
        work_dir = str(tau_dir.absolute())
    else:
        work_dir = os.getcwd()
    
    cmd = [
        "python", "run.py",
        "--env", env,
        "--agent-strategy", agent_strategy,
        "--model", model,
        "--user-model", user_model,
        "--model-provider", "openai",
        "--user-model-provider", "openai",
        "--num-trials", str(num_trials),
        "--task-split", task_split,
        "--max-concurrency", str(max_concurrency),
    ]
    
    print(f"\n{'='*80}")
    print(f"Testing: {env} | Strategy: {agent_strategy} | Model: {model}")
    print(f"Command: {' '.join(cmd)}")
    print(f"Working dir: {work_dir}")
    print(f"{'='*80}")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=work_dir,
        )
        
        duration = (datetime.now() - start_time).total_seconds()
        success = result.returncode == 0
        
        if success:
            print(f"✅ PASSED in {duration:.2f}s")
        else:
            print(f"❌ FAILED in {duration:.2f}s (exit code: {result.returncode})")
            if result.stderr:
                print(f"Error output: {result.stderr[:500]}")
        
        return {
            "success": success,
            "env": env,
            "agent_strategy": agent_strategy,
            "model": model,
            "user_model": user_model,
            "task_split": task_split,
            "returncode": result.returncode,
            "duration": duration,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "timestamp": start_time.isoformat(),
        }
        
    except subprocess.TimeoutExpired:
        duration = (datetime.now() - start_time).total_seconds()
        print(f"⏱️  TIMEOUT after {duration:.2f}s")
        return {
            "success": False,
            "env": env,
            "agent_strategy": agent_strategy,
            "model": model,
            "user_model": user_model,
            "task_split": task_split,
            "returncode": -1,
            "duration": duration,
            "stdout": "",
            "stderr": f"Timeout after {timeout}s",
            "timestamp": start_time.isoformat(),
        }
    
    except Exception as e:
        duration = (datetime.now() - start_time).total_seconds()
        print(f"💥 EXCEPTION: {e}")
        return {
            "success": False,
            "env": env,
            "agent_strategy": agent_strategy,
            "model": model,
            "user_model": user_model,
            "task_split": task_split,
            "returncode": -2,
            "duration": duration,
            "stdout": "",
            "stderr": str(e),
            "timestamp": start_time.isoformat(),
        }


def main():
    parser = argparse.ArgumentParser(
        description="Smoke test all tau-bench environment variations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Test all environments with default settings
  python smoke_test_all_variations.py
  
  # Test specific environments only
  python smoke_test_all_variations.py --envs retail_1 retail_2 airline_1
  
  # Test all environments with all strategies
  python smoke_test_all_variations.py --all-strategies
  
  # Quick test of first 5 environments
  python smoke_test_all_variations.py --limit 5
  
  # Test with custom model
  python smoke_test_all_variations.py --model gpt-4o --user-model gpt-4o
        """
    )
    
    parser.add_argument(
        "--envs",
        nargs="+",
        help="Specific environments to test (default: all discovered environments)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of environments to test (useful for quick smoke test)",
    )
    parser.add_argument(
        "--agent-strategies",
        nargs="+",
        default=["tool-calling"],
        choices=["tool-calling", "act", "react", "few-shot"],
        help="Agent strategies to test (default: tool-calling only)",
    )
    parser.add_argument(
        "--all-strategies",
        action="store_true",
        help="Test all agent strategies (shortcut for --agent-strategies tool-calling act react few-shot)",
    )
    parser.add_argument(
        "--model",
        default="gpt-4o-mini",
        help="Model to use for agent (default: gpt-4o-mini)",
    )
    parser.add_argument(
        "--user-model",
        default="gpt-4o",
        help="Model to use for user simulator (default: gpt-4o)",
    )
    parser.add_argument(
        "--task-split",
        default="test",
        choices=["train", "test", "dev"],
        help="Task split to use (default: test)",
    )
    parser.add_argument(
        "--num-trials",
        type=int,
        default=1,
        help="Number of trials per test (default: 1)",
    )
    parser.add_argument(
        "--max-concurrency",
        type=int,
        default=8,
        help="Max concurrency for each test (default: 8)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="Timeout in seconds for each test (default: 300)",
    )
    parser.add_argument(
        "--output",
        default="smoke_test_results.json",
        help="Output file for results (default: smoke_test_results.json)",
    )
    parser.add_argument(
        "--continue-on-failure",
        action="store_true",
        help="Continue testing even if some tests fail",
    )
    parser.add_argument(
        "--filter-pattern",
        help="Only test environments matching this pattern (e.g., 'retail', 'airline_')",
    )
    
    args = parser.parse_args()
    
    # Determine strategies to test
    if args.all_strategies:
        strategies = ["tool-calling", "act", "react", "few-shot"]
    else:
        strategies = args.agent_strategies
    
    # Discover or use specified environments
    if args.envs:
        envs = args.envs
    else:
        envs = get_all_envs()
        if not envs:
            print("Error: No environments found!")
            sys.exit(1)
    
    # Apply filter pattern
    if args.filter_pattern:
        envs = [e for e in envs if args.filter_pattern in e]
        print(f"Filtered to {len(envs)} environments matching '{args.filter_pattern}'")
    
    # Apply limit
    if args.limit:
        envs = envs[:args.limit]
        print(f"Limited to first {args.limit} environments")
    
    print(f"\n{'='*80}")
    print(f"SMOKE TEST CONFIGURATION")
    print(f"{'='*80}")
    print(f"Environments: {len(envs)}")
    print(f"Strategies: {strategies}")
    print(f"Model: {args.model}")
    print(f"User Model: {args.user_model}")
    print(f"Task Split: {args.task_split}")
    print(f"Total Tests: {len(envs) * len(strategies)}")
    print(f"{'='*80}\n")
    
    # Run all tests
    results = []
    total_tests = len(envs) * len(strategies)
    test_num = 0
    
    for env in envs:
        for strategy in strategies:
            test_num += 1
            print(f"\n[{test_num}/{total_tests}] Testing {env} with {strategy}...")
            
            result = run_smoke_test(
                env=env,
                agent_strategy=strategy,
                model=args.model,
                user_model=args.user_model,
                task_split=args.task_split,
                num_trials=args.num_trials,
                max_concurrency=args.max_concurrency,
                timeout=args.timeout,
            )
            
            results.append(result)
            
            # Stop on failure if requested
            if not result["success"] and not args.continue_on_failure:
                print(f"\n❌ Test failed and --continue-on-failure not set. Stopping.")
                break
        
        # Break outer loop too if we stopped
        if not args.continue_on_failure and results and not results[-1]["success"]:
            break
    
    # Summary
    print(f"\n\n{'='*80}")
    print(f"SMOKE TEST SUMMARY")
    print(f"{'='*80}")
    
    passed = sum(1 for r in results if r["success"])
    failed = sum(1 for r in results if not r["success"])
    total = len(results)
    
    print(f"Total Tests: {total}")
    print(f"✅ Passed: {passed} ({passed/total*100:.1f}%)")
    print(f"❌ Failed: {failed} ({failed/total*100:.1f}%)")
    
    if failed > 0:
        print(f"\n{'='*80}")
        print(f"FAILED TESTS:")
        print(f"{'='*80}")
        for result in results:
            if not result["success"]:
                print(f"  - {result['env']} | {result['agent_strategy']} | Exit: {result['returncode']}")
                if result['stderr']:
                    # Print first line of error
                    first_error_line = result['stderr'].split('\n')[0]
                    print(f"    Error: {first_error_line[:100]}")
    
    # Save results
    output_file = args.output
    with open(output_file, 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "config": {
                "model": args.model,
                "user_model": args.user_model,
                "strategies": strategies,
                "task_split": args.task_split,
                "num_envs": len(envs),
                "total_tests": total,
            },
            "summary": {
                "total": total,
                "passed": passed,
                "failed": failed,
                "success_rate": passed/total if total > 0 else 0,
            },
            "results": results,
        }, f, indent=2)
    
    print(f"\n📄 Detailed results saved to: {output_file}")
    print(f"{'='*80}\n")
    
    # Exit with appropriate code
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()

