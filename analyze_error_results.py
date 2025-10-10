#!/usr/bin/env python3
"""
Analyze error results from comprehensive_report.json and individual error analysis files.

This script:
1. Reads comprehensive_report.json to find environments with environment faults
2. Cross-correlates with individual error analysis files to extract error details
3. Summarizes error types, counts, and affected files
4. Provides actionable insights for fixing remaining issues

Usage:
    python3 analyze_error_results.py
    python3 analyze_error_results.py --error-analyses-dir tau/error_analyses
    python3 analyze_error_results.py --verbose
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Optional
import re
import argparse


class ErrorAnalyzer:
    def __init__(self, error_analyses_dir: Path, verbose: bool = False):
        self.error_analyses_dir = error_analyses_dir
        self.verbose = verbose
        self.comprehensive_report_path = error_analyses_dir / "comprehensive_report.json"
        
        # Error pattern classifications
        self.error_patterns = {
            "str_no_get": r"'str' object has no attribute 'get'",
            "dict_no_append": r"'dict' object has no attribute 'append'",
            "undefined_name": r"name '([^']+)' is not defined",
            "string_indices": r"string indices must be integers",
            "not_callable": r"'(\w+)' object is not callable",
            "missing_arg": r"missing \d+ required positional argument",
            "unexpected_arg": r"(?:got an unexpected keyword argument|takes \d+ positional arguments? but \d+ were? given)",
            "key_error": r"KeyError: '([^']+)'",
            "attribute_error": r"'(\w+)' object has no attribute '(\w+)'",
            "import_error": r"(?:ImportError|ModuleNotFoundError): (.+)",
            "type_error": r"TypeError: (.+)",
            "value_error": r"ValueError: (.+)",
            "empty_trajectory": r"empty|no conversation|initialization",
            "json_schema": r"Invalid schema|schema must|is not valid under",
        }
    
    def load_comprehensive_report(self) -> Dict[str, Any]:
        """Load the comprehensive report."""
        if not self.comprehensive_report_path.exists():
            print(f"❌ Error: {self.comprehensive_report_path} not found!")
            print(f"   Run tests first: python3 run_error_analysis_all_envs.py --run-tests")
            sys.exit(1)
        
        with open(self.comprehensive_report_path, 'r') as f:
            return json.load(f)
    
    def load_individual_analysis(self, env_name: str) -> Optional[Dict[str, Any]]:
        """Load individual error analysis file for an environment."""
        analysis_path = self.error_analyses_dir / f"{env_name}_error_analysis.json"
        
        if not analysis_path.exists():
            if self.verbose:
                print(f"⚠️  Warning: {analysis_path} not found")
            return None
        
        try:
            with open(analysis_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            if self.verbose:
                print(f"⚠️  Warning: Could not parse {analysis_path}")
            return None
    
    def classify_error(self, error_text: str) -> str:
        """Classify an error based on its text."""
        if not error_text:
            return "unknown"
        
        error_lower = error_text.lower()
        
        # Check each pattern
        for pattern_name, pattern_regex in self.error_patterns.items():
            if re.search(pattern_regex, error_text, re.IGNORECASE):
                return pattern_name
        
        # Fallback to generic classification
        if "error" in error_lower:
            return "other_error"
        
        return "unknown"
    
    def extract_error_details(self, analysis_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract error details from an environment's analysis data."""
        errors = []
        
        # Extract from fault_assignment_analysis
        for fault in analysis_data.get("fault_assignment_analysis", []):
            if fault.get("author") == "environment":
                errors.append({
                    "task_id": fault.get("task_id", "unknown"),
                    "description": fault.get("description", ""),
                    "type": "environment_fault"
                })
        
        return errors
    
    def analyze(self) -> Dict[str, Any]:
        """Run the full analysis."""
        print("╔════════════════════════════════════════════════════════════════════════════╗")
        print("║           ERROR ANALYSIS RESULTS                                           ║")
        print("╚════════════════════════════════════════════════════════════════════════════╝")
        print()
        
        # Load comprehensive report
        report = self.load_comprehensive_report()
        summaries = report.get("summaries", {})
        
        if not summaries:
            print("✅ No test results found in comprehensive_report.json")
            print("   Run tests first with: python3 run_error_analysis_all_envs.py --run-tests")
            return {}
        
        # Find environments with environment faults
        envs_with_env_faults = {}
        envs_passing = []
        envs_agent_faults = []
        envs_user_faults = []
        
        for env_name, summary in summaries.items():
            env_faults = summary.get("env_faults", 0)
            agent_faults = summary.get("agent_faults", 0)
            user_faults = summary.get("user_faults", 0)
            total_failures = summary.get("total_failures", 0)
            
            if total_failures == 0:
                envs_passing.append(env_name)
            elif env_faults > 0:
                envs_with_env_faults[env_name] = summary
            elif agent_faults > 0:
                envs_agent_faults.append(env_name)
            elif user_faults > 0:
                envs_user_faults.append(env_name)
        
        # Print overview
        total_tested = len(summaries)
        print(f"📊 OVERVIEW")
        print(f"   Total environments tested: {total_tested}")
        print(f"   ✅ Passing:                {len(envs_passing)} ({len(envs_passing)/total_tested*100:.1f}%)")
        print(f"   🤖 Agent faults only:      {len(envs_agent_faults)} ({len(envs_agent_faults)/total_tested*100:.1f}%)")
        print(f"   👤 User faults only:       {len(envs_user_faults)} ({len(envs_user_faults)/total_tested*100:.1f}%)")
        print(f"   ❌ Environment bugs:       {len(envs_with_env_faults)} ({len(envs_with_env_faults)/total_tested*100:.1f}%)")
        print()
        
        if not envs_with_env_faults:
            print("🎉 No environment bugs found! All failures are agent or user faults.")
            print()
            return {
                "total_tested": total_tested,
                "passing": len(envs_passing),
                "agent_faults": len(envs_agent_faults),
                "user_faults": len(envs_user_faults),
                "env_bugs": 0,
                "error_details": {}
            }
        
        # Analyze each environment with environment faults
        print("━" * 80)
        print(f"❌ ENVIRONMENTS WITH BUGS ({len(envs_with_env_faults)})")
        print("━" * 80)
        print()
        
        error_classifications = defaultdict(list)
        detailed_errors = {}
        
        for env_name, summary in sorted(envs_with_env_faults.items()):
            env_faults = summary.get("env_faults", 0)
            
            # Load individual analysis
            analysis = self.load_individual_analysis(env_name)
            
            if analysis:
                errors = self.extract_error_details(analysis)
                
                if errors:
                    detailed_errors[env_name] = errors
                    
                    # Classify each error
                    for error in errors:
                        error_class = self.classify_error(error["description"])
                        error_classifications[error_class].append({
                            "env": env_name,
                            "task": error["task_id"],
                            "description": error["description"]
                        })
                        
                        print(f"🔴 {env_name} ({env_faults} fault{'s' if env_faults > 1 else ''})")
                        print(f"   Task: {error['task_id']}")
                        print(f"   Type: {error_class}")
                        print(f"   Error: {error['description'][:200]}{'...' if len(error['description']) > 200 else ''}")
                        print()
                else:
                    print(f"🔴 {env_name} ({env_faults} fault{'s' if env_faults > 1 else ''})")
                    print(f"   ⚠️  No detailed error information available")
                    print()
            else:
                print(f"🔴 {env_name} ({env_faults} fault{'s' if env_faults > 1 else ''})")
                print(f"   ⚠️  Error analysis file not found")
                print()
        
        # Print error classification summary
        if error_classifications:
            print()
            print("━" * 80)
            print("📋 ERROR CLASSIFICATION SUMMARY")
            print("━" * 80)
            print()
            
            for error_type, occurrences in sorted(error_classifications.items(), key=lambda x: -len(x[1])):
                print(f"🔸 {error_type.upper().replace('_', ' ')}: {len(occurrences)} occurrence(s)")
                
                # Group by environment
                envs = defaultdict(list)
                for occ in occurrences:
                    envs[occ["env"]].append(occ)
                
                for env, errors in sorted(envs.items()):
                    print(f"   └─ {env} ({len(errors)} error{'s' if len(errors) > 1 else ''})")
                    if self.verbose:
                        for err in errors:
                            print(f"      Task {err['task']}: {err['description'][:100]}...")
                print()
        
        # Print actionable recommendations
        print("━" * 80)
        print("💡 RECOMMENDED ACTIONS")
        print("━" * 80)
        print()
        
        if error_classifications:
            # Prioritize by frequency
            sorted_errors = sorted(error_classifications.items(), key=lambda x: -len(x[1]))
            
            for i, (error_type, occurrences) in enumerate(sorted_errors[:5], 1):
                env_count = len(set(occ["env"] for occ in occurrences))
                print(f"{i}. Fix '{error_type}' errors ({len(occurrences)} occurrences in {env_count} environment{'s' if env_count > 1 else ''})")
                
                # Provide specific guidance based on error type
                if error_type == "str_no_get":
                    print(f"   → Pattern 1: Dict vs list bug - use list(data.get('key', {{}}).values())")
                elif error_type == "dict_no_append":
                    print(f"   → Pattern 5: Use dict assignment instead of append()")
                elif error_type == "undefined_name":
                    print(f"   → Pattern 4: Add missing helper functions to tools/__init__.py")
                elif error_type == "json_schema":
                    print(f"   → Pattern 2: Fix JSON schema validation errors")
                elif error_type == "empty_trajectory":
                    print(f"   → Check for initialization errors or JSON schema issues")
                else:
                    print(f"   → Investigate individual cases in error analysis files")
                
                # List affected environments
                affected_envs = sorted(set(occ["env"] for occ in occurrences))
                print(f"   Affected: {', '.join(affected_envs)}")
                print()
        
        print("━" * 80)
        
        return {
            "total_tested": total_tested,
            "passing": len(envs_passing),
            "agent_faults": len(envs_agent_faults),
            "user_faults": len(envs_user_faults),
            "env_bugs": len(envs_with_env_faults),
            "error_details": detailed_errors,
            "error_classifications": {k: len(v) for k, v in error_classifications.items()}
        }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze error results from tau-bench test runs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic analysis
  python3 analyze_error_results.py
  
  # Verbose output with detailed error messages
  python3 analyze_error_results.py --verbose
  
  # Custom error analyses directory
  python3 analyze_error_results.py --error-analyses-dir /path/to/error_analyses
        """
    )
    
    parser.add_argument(
        "--error-analyses-dir",
        type=Path,
        default=Path("tau/error_analyses"),
        help="Path to error analyses directory (default: tau/error_analyses)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed error messages for each occurrence"
    )
    
    parser.add_argument(
        "--json-output",
        type=Path,
        help="Save analysis results to JSON file"
    )
    
    args = parser.parse_args()
    
    # Ensure error analyses directory exists
    if not args.error_analyses_dir.exists():
        print(f"❌ Error: Directory not found: {args.error_analyses_dir}")
        print(f"   Run tests first: python3 run_error_analysis_all_envs.py --run-tests")
        sys.exit(1)
    
    # Run analysis
    analyzer = ErrorAnalyzer(args.error_analyses_dir, verbose=args.verbose)
    results = analyzer.analyze()
    
    # Save JSON output if requested
    if args.json_output and results:
        with open(args.json_output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n💾 Results saved to: {args.json_output}")
    
    # Exit with appropriate code
    if results and results.get("env_bugs", 0) > 0:
        sys.exit(1)  # Exit with error if environment bugs found
    else:
        sys.exit(0)  # Exit successfully


if __name__ == "__main__":
    main()

