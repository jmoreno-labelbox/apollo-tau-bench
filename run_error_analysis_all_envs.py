#!/usr/bin/env python3
"""
Run auto_error_identification.py across all tau-bench environments.

This script:
1. Finds all environments
2. Looks for existing results files or runs tests to generate them
3. Runs error analysis on each environment
4. Generates a comprehensive report
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import List, Dict, Optional
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading


def get_all_environments() -> List[str]:
    """Get list of all environment names."""
    tau_envs = Path(__file__).parent / "tau" / "tau_bench" / "envs"
    
    envs = []
    for env_dir in sorted(tau_envs.iterdir()):
        if env_dir.is_dir() and env_dir.name != "__pycache__":
            # Check if it has an env.py file (valid environment)
            if (env_dir / "env.py").exists():
                envs.append(env_dir.name)
    
    return envs


def find_results_file(env_name: str, results_dir: Path) -> Optional[Path]:
    """Find the most recent results file for an environment."""
    # First try the original pattern (in case results files do contain env name)
    pattern = f"*{env_name}*.json"
    matching_files = list(results_dir.glob(pattern))
    
    if not matching_files:
        # Try broader pattern
        matching_files = list(results_dir.glob("*.json"))
        matching_files = [f for f in matching_files if env_name in f.stem]
    
    if not matching_files:
        # Since results files don't contain environment names in their filename,
        # we cannot reliably determine which results file belongs to which environment.
        # Return None to indicate no results file found for this environment.
        return None
    
    if matching_files:
        # Return most recent
        return max(matching_files, key=lambda p: p.stat().st_mtime)
    
    return None


def run_test_for_env(env_name: str, num_tasks: int = 3) -> Optional[Path]:
    """Run a quick test for an environment to generate results."""
    tau_dir = Path(__file__).parent / "tau"
    
    print(f"  Running {num_tasks} tasks for {env_name}...")
    
    cmd = [
        "python3", "run.py",
        "--env", env_name,
        "--model", "gpt-4o-mini",
        "--start-index", "0",
        "--end-index", str(num_tasks),
    ]
    
    try:
        result = subprocess.run(
            cmd,
            cwd=tau_dir,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        # Extract results file from output
        for line in result.stdout.split('\n'):
            if 'Results saved to' in line:
                results_file = line.split('Results saved to')[-1].strip()
                return tau_dir / results_file
        
        return None
    
    except subprocess.TimeoutExpired:
        print(f"  ⚠️  Timeout running tests for {env_name}")
        return None
    except Exception as e:
        print(f"  ❌ Error running tests for {env_name}: {e}")
        return None


def run_error_analysis(env_name: str, results_path: Path, output_dir: Path) -> bool:
    """Run error analysis for an environment."""
    tau_dir = Path(__file__).parent / "tau"
    output_path = output_dir / f"{env_name}_error_analysis.json"
    
    cmd = [
        "python3", "tau_bench/auto_error_identification.py",
        "--platform", "openai",
        "--model", "gpt-4o",
        "--env", env_name,
        "--results-path", str(results_path),
        "--output-path", str(output_path),
        "--max-concurrency", "3",
        "--max-num-failed-results", "10"
    ]
    
    env = os.environ.copy()
    env['PYTHONPATH'] = str(tau_dir)
    
    try:
        result = subprocess.run(
            cmd,
            cwd=tau_dir,
            capture_output=True,
            text=True,
            env=env,
            timeout=180  # 3 minute timeout
        )
        
        if result.returncode == 0 and output_path.exists():
            return True
        else:
            print(f"  Error output: {result.stderr[:200]}")
            return False
    
    except subprocess.TimeoutExpired:
        print(f"  ⚠️  Timeout analyzing {env_name}")
        return False
    except Exception as e:
        print(f"  ❌ Error analyzing {env_name}: {e}")
        return False


def summarize_analysis(analysis_file: Path) -> Dict:
    """Summarize an error analysis file."""
    try:
        with open(analysis_file) as f:
            data = json.load(f)
        
        fault_assignment = data.get('fault_assignment_analysis', [])
        fault_types = data.get('fault_type_analysis', [])
        
        summary = {
            'total_failures': len(fault_assignment),
            'user_faults': sum(1 for f in fault_assignment if f.get('author') == 'user'),
            'agent_faults': sum(1 for f in fault_assignment if f.get('author') == 'agent'),
            'env_faults': sum(1 for f in fault_assignment if f.get('author') == 'environment'),
            'fault_types': {}
        }
        
        for ft in fault_types:
            fault_type = ft.get('fault_type', 'unknown')
            summary['fault_types'][fault_type] = summary['fault_types'].get(fault_type, 0) + 1
        
        return summary
    
    except Exception as e:
        return {'error': str(e)}


def main():
    parser = argparse.ArgumentParser(description="Run error analysis across all environments")
    parser.add_argument("--run-tests", action="store_true", help="Run tests to generate results files")
    parser.add_argument("--num-tasks", type=int, default=1, help="Number of tasks to run per environment (default: 1)")
    parser.add_argument("--envs", nargs="+", help="Specific environments to analyze (default: all)")
    parser.add_argument("--skip-analysis", action="store_true", help="Skip error analysis, just run tests")
    parser.add_argument("--test-concurrency", type=int, default=3, help="Number of environments to test concurrently (default: 3)")
    parser.add_argument("--analysis-concurrency", type=int, default=5, help="Number of environments to analyze concurrently (default: 5)")
    args = parser.parse_args()
    
    tau_dir = Path(__file__).parent / "tau"
    results_dir = tau_dir / "results"
    output_dir = tau_dir / "error_analyses"
    output_dir.mkdir(exist_ok=True)
    
    print("🔍 Auto Error Identification - All Environments")
    print("=" * 80)
    print()
    
    # Get environments
    if args.envs:
        envs = args.envs
        print(f"Analyzing {len(envs)} specified environments")
    else:
        envs = get_all_environments()
        print(f"Found {len(envs)} environments")
    
    print()
    
    stats = {
        'total': len(envs),
        'tested': 0,
        'analyzed': 0,
        'skipped': 0,
        'failed': 0
    }
    
    summaries = {}
    lock = threading.Lock()
    
    def process_environment(env_info):
        """Process a single environment (test + analyze)."""
        i, env_name = env_info
        
        with lock:
            print(f"[{i}/{len(envs)}] {env_name}")
        
        # Find or generate results file
        results_file = find_results_file(env_name, results_dir)
        
        if not results_file and args.run_tests:
            with lock:
                print(f"  Running {args.num_tasks} task(s) for {env_name}...")
            results_file = run_test_for_env(env_name, args.num_tasks)
            if results_file:
                with lock:
                    stats['tested'] += 1
        
        if not results_file:
            with lock:
                if args.run_tests:
                    print(f"  ⏭️  No results file found (tests may have failed)")
                else:
                    print(f"  ⏭️  No results file found (use --run-tests to generate results)")
                stats['skipped'] += 1
                print()
            return None
        
        with lock:
            print(f"  📄 Using: {results_file.name}")
        
        if args.skip_analysis:
            with lock:
                print()
            return None
        
        # Run error analysis
        success = run_error_analysis(env_name, results_file, output_dir)
        
        if success:
            with lock:
                print(f"  ✅ Analysis complete")
                stats['analyzed'] += 1
            
            # Summarize
            analysis_file = output_dir / f"{env_name}_error_analysis.json"
            summary = summarize_analysis(analysis_file)
            
            with lock:
                summaries[env_name] = summary
                
                if summary.get('total_failures', 0) > 0:
                    print(f"     Failures: {summary['total_failures']} " +
                          f"(User: {summary['user_faults']}, " +
                          f"Agent: {summary['agent_faults']}, " +
                          f"Env: {summary['env_faults']})")
                print()
            
            return summary
        else:
            with lock:
                print(f"  ❌ Analysis failed")
                stats['failed'] += 1
                print()
            return None
    
    # Process environments concurrently
    if args.run_tests:
        max_workers = args.test_concurrency
    else:
        max_workers = args.analysis_concurrency
    
    print(f"Using {max_workers} concurrent workers")
    print()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        futures = {
            executor.submit(process_environment, (i, env_name)): env_name
            for i, env_name in enumerate(envs, 1)
        }
        
        # Wait for completion
        for future in as_completed(futures):
            env_name = futures[future]
            try:
                future.result()
            except Exception as e:
                with lock:
                    print(f"❌ Error processing {env_name}: {e}")
                    stats['failed'] += 1
    
    # Print summary
    print("=" * 80)
    print("📊 SUMMARY")
    print("=" * 80)
    print()
    print(f"Total environments:        {stats['total']}")
    print(f"Tests run:                 {stats['tested']}")
    print(f"Analyses completed:        {stats['analyzed']}")
    print(f"Skipped (no results):      {stats['skipped']}")
    print(f"Failed:                    {stats['failed']}")
    print()
    
    if summaries:
        print("Environments with failures:")
        for env_name, summary in summaries.items():
            if summary.get('total_failures', 0) > 0:
                print(f"  • {env_name}: {summary['total_failures']} failures")
        print()
    
    print(f"📁 Analysis files saved to: {output_dir}")
    print()
    
    # Save comprehensive report
    report_file = output_dir / "comprehensive_report.json"
    with open(report_file, 'w') as f:
        json.dump({
            'stats': stats,
            'summaries': summaries,
            'timestamp': str(Path(__file__).parent)
        }, f, indent=2)
    
    print(f"📄 Comprehensive report: {report_file}")
    print("=" * 80)
    print()
    
    # Run detailed error analysis if we have results
    if summaries and not args.skip_analysis:
        print()
        print("=" * 80)
        print("Running detailed error analysis...")
        print("=" * 80)
        print()
        
        try:
            # Import the analyzer
            sys.path.insert(0, str(Path(__file__).parent))
            from analyze_error_results import ErrorAnalyzer
            
            # Run analysis
            analyzer = ErrorAnalyzer(output_dir, verbose=False)
            analysis_results = analyzer.analyze()
            
            # Save detailed results
            if analysis_results:
                detailed_report = output_dir / "detailed_error_analysis.json"
                with open(detailed_report, 'w') as f:
                    json.dump(analysis_results, f, indent=2)
                print()
                print(f"💾 Detailed analysis saved to: {detailed_report}")
        
        except Exception as e:
            print(f"⚠️  Warning: Could not run detailed analysis: {e}")
            print(f"   You can run it manually: python3 analyze_error_results.py")


if __name__ == "__main__":
    main()

