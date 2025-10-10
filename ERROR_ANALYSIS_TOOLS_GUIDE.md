# Error Analysis Tools Guide

**Complete guide to analyzing and debugging tau-bench environment errors**

---

## Quick Start

### Run Full Test Suite with Analysis

```bash
# Test all 122 environments with automatic error analysis
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 1 --test-concurrency 20

# This will:
# 1. Run 1 task per environment (122 tests total)
# 2. Analyze all failures using LLM classification
# 3. Generate comprehensive_report.json
# 4. Automatically run detailed error analysis
# 5. Show actionable recommendations
```

### Run Analysis on Existing Results

```bash
# If you already have test results, just analyze them
python3 run_error_analysis_all_envs.py

# Or analyze specific environments
python3 run_error_analysis_all_envs.py --envs academic_search_1 banking_services_2
```

### Run Standalone Error Analysis

```bash
# After tests are complete, you can re-run analysis independently
python3 analyze_error_results.py

# Verbose mode (shows detailed error messages)
python3 analyze_error_results.py --verbose

# Save results to JSON
python3 analyze_error_results.py --json-output analysis_results.json
```

---

## Tools Overview

### 1. `run_error_analysis_all_envs.py`

**Purpose:** Orchestrates test execution and error analysis across all environments

**Key Features:**
- Concurrent test execution (configurable workers)
- Automatic result file discovery
- LLM-powered fault classification
- Comprehensive reporting
- Integrated detailed error analysis

**Arguments:**
```
--run-tests              Run tests to generate results files
--num-tasks N            Number of tasks per environment (default: 1)
--test-concurrency N     Concurrent test workers (default: 3)
--analysis-concurrency N Concurrent analysis workers (default: 5)
--envs ENV1 ENV2...      Specific environments to test
--skip-analysis          Only run tests, skip error analysis
```

**Outputs:**
- `tau/error_analyses/{env_name}_error_analysis.json` - Per-environment analysis
- `tau/error_analyses/comprehensive_report.json` - Overall summary
- `tau/error_analyses/detailed_error_analysis.json` - Classified errors with recommendations

---

### 2. `analyze_error_results.py`

**Purpose:** Deep-dive analysis of error patterns with actionable recommendations

**Key Features:**
- Cross-correlates comprehensive report with individual error files
- Classifies errors into known patterns
- Groups by error type and affected environments
- Provides specific fix recommendations
- Priority-based action items

**Arguments:**
```
--error-analyses-dir PATH  Path to error analyses (default: tau/error_analyses)
--verbose, -v              Show detailed error messages
--json-output PATH         Save analysis to JSON file
```

**Error Classifications:**
- `str_no_get` - Pattern 1: Dict vs list bug
- `dict_no_append` - Pattern 5: Append on dict
- `undefined_name` - Pattern 4: Missing helper functions
- `json_schema` - Pattern 2: Schema validation errors
- `empty_trajectory` - Pattern 2: Initialization failures
- `not_callable` - API mismatches
- `missing_arg` / `unexpected_arg` - Function signature issues
- `key_error` / `attribute_error` - Data structure issues
- `import_error` - Module loading problems
- And more...

**Outputs:**
- Console: Formatted analysis with recommendations
- JSON (optional): Machine-readable results

---

## Output Files

### comprehensive_report.json

**Structure:**
```json
{
  "stats": {
    "total": 122,
    "tested": 122,
    "analyzed": 122,
    "skipped": 0,
    "failed": 0
  },
  "summaries": {
    "environment_name": {
      "total_failures": 1,
      "user_faults": 0,
      "agent_faults": 0,
      "env_faults": 1,
      "fault_types": {
        "wrong_tool": 1
      }
    }
  }
}
```

### {env_name}_error_analysis.json

**Structure:**
```json
{
  "fault_assignment_analysis": [
    {
      "task_id": "task_1",
      "author": "environment",
      "description": "Error: 'str' object has no attribute 'get'"
    }
  ],
  "fault_type_analysis": [
    {
      "task_id": "task_1",
      "fault_type": "wrong_tool_argument",
      "description": "Agent used incorrect parameter"
    }
  ]
}
```

### detailed_error_analysis.json

**Structure:**
```json
{
  "total_tested": 122,
  "passing": 73,
  "agent_faults": 20,
  "user_faults": 5,
  "env_bugs": 24,
  "error_classifications": {
    "str_no_get": 8,
    "undefined_name": 6,
    "json_schema": 4
  },
  "error_details": {
    "env_name": [
      {
        "task_id": "task_1",
        "description": "Full error message",
        "type": "environment_fault"
      }
    ]
  }
}
```

---

## Usage Examples

### Example 1: Quick Test of Specific Environments

```bash
# Test only the environments we just fixed
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 1 \
  --envs retail_point_of_sale_5 smart_home_2 data_science_3 smart_home_5
```

### Example 2: Fast Full Test

```bash
# Test all environments with high concurrency
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 1 --test-concurrency 20
```

### Example 3: Re-analyze Without Re-testing

```bash
# If you already have results, just re-run analysis
python3 analyze_error_results.py --verbose
```

### Example 4: Custom Analysis Location

```bash
# Analyze results from a different directory
python3 analyze_error_results.py --error-analyses-dir /path/to/results --json-output report.json
```

### Example 5: CI/CD Integration

```bash
# Run tests and fail CI if environment bugs found
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 1 --test-concurrency 20
EXIT_CODE=$?

# analyze_error_results.py exits with code 1 if bugs found
python3 analyze_error_results.py
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo "❌ Environment bugs detected!"
    exit 1
fi
```

---

## Interpreting Results

### Fault Categories

**✅ Passing (env_faults = 0, total_failures = 0)**
- Environment is working correctly
- No action needed

**🤖 Agent Faults (agent_faults > 0, env_faults = 0)**
- Agent is making mistakes (wrong tool, wrong args, etc.)
- Environment is correct
- No environment fixes needed

**👤 User Faults (user_faults > 0, env_faults = 0)**
- Task definition issues
- Ambiguous requirements
- No environment fixes needed

**❌ Environment Bugs (env_faults > 0)**
- **THESE NEED FIXING**
- Environment has implementation bugs
- Use error classification to determine fix approach

---

### Error Pattern Quick Reference

| Error Type | Pattern | Fix Approach |
|------------|---------|--------------|
| `'str' object has no attribute 'get'` | Pattern 1 | `list(data.get('key', {}).values())` |
| `'dict' object has no attribute 'append'` | Pattern 5 | Use dict assignment instead |
| `name 'X' is not defined` | Pattern 4 | Add helper to `tools/__init__.py` |
| `Invalid schema` / `schema must` | Pattern 2 | Fix JSON schema structure |
| Empty trajectory | Pattern 2 | Check JSON schema / initialization |
| `'X' object is not callable` | API mismatch | Fix function signature |
| `missing N required positional argument` | API mismatch | Fix parameter definition |
| `unexpected keyword argument` | API mismatch | Align tool schema with implementation |

---

## Recommended Workflow

### 1. Run Full Test Suite

```bash
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 1 --test-concurrency 20
```

**Expected time:** ~30-60 minutes for 122 environments

### 2. Review Analysis Output

The script will automatically show:
- Pass rate
- Environments with bugs
- Error classifications
- Prioritized action items

### 3. Fix Issues by Priority

Follow the numbered recommendations:
1. Most common error types first
2. Batch fixes for similar issues
3. Verify fixes with targeted re-tests

### 4. Re-run Analysis

```bash
# Quick re-test of fixed environments
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 1 \
  --envs fixed_env_1 fixed_env_2 fixed_env_3

# Or re-analyze all existing results
python3 analyze_error_results.py --verbose
```

### 5. Iterate Until Clean

Repeat steps 3-4 until `env_bugs = 0`

---

## Troubleshooting

### "No results file found"

**Solution:** Run with `--run-tests` flag:
```bash
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 1
```

### "comprehensive_report.json not found"

**Solution:** Run the test suite first:
```bash
python3 run_error_analysis_all_envs.py --run-tests
```

### "Timeout running tests"

**Solution:** Increase timeout in script or reduce concurrency:
```bash
python3 run_error_analysis_all_envs.py --run-tests --test-concurrency 5
```

### Analysis hangs or is very slow

**Solution:** 
- Check API rate limits
- Reduce concurrency: `--analysis-concurrency 3`
- Check for network issues

---

## Advanced Usage

### Custom Error Pattern Detection

Edit `analyze_error_results.py` to add new patterns:

```python
self.error_patterns = {
    # ... existing patterns ...
    "my_custom_pattern": r"regex pattern here",
}
```

### Filtering Specific Error Types

```python
# In analyze_error_results.py, add custom filtering
def analyze(self):
    # ... existing code ...
    
    # Filter for specific error types
    critical_errors = {
        k: v for k, v in error_classifications.items()
        if k in ["str_no_get", "json_schema"]
    }
```

### Integration with CI/CD

```yaml
# .github/workflows/test.yml
name: Test Tau-Bench Environments

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Run tests
        run: |
          python3 run_error_analysis_all_envs.py \
            --run-tests \
            --num-tasks 1 \
            --test-concurrency 10
      
      - name: Analyze results
        run: python3 analyze_error_results.py --json-output results.json
      
      - name: Upload results
        uses: actions/upload-artifact@v2
        with:
          name: test-results
          path: tau/error_analyses/
```

---

## Tips & Best Practices

1. **Start with syntax check** - Run `python3 -m py_compile` on all files first
2. **Use high concurrency for tests** - `--test-concurrency 20` is safe for most systems
3. **Lower concurrency for analysis** - `--analysis-concurrency 5` to avoid API rate limits
4. **Test 1 task per env** - `--num-tasks 1` is sufficient for error detection
5. **Save JSON outputs** - Easier to track progress over time
6. **Use verbose mode** - When debugging specific environments
7. **Batch fixes** - Group similar errors and fix together
8. **Re-test frequently** - Catch regressions early

---

## Performance Tuning

### Optimal Settings for Different Scenarios

**Quick smoke test (5-10 mins):**
```bash
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 1 \
  --test-concurrency 30 --analysis-concurrency 10 \
  --envs $(head -20 envs.txt)
```

**Full test (30-60 mins):**
```bash
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 1 \
  --test-concurrency 20 --analysis-concurrency 5
```

**Deep analysis (multiple tasks, 2-3 hours):**
```bash
python3 run_error_analysis_all_envs.py --run-tests --num-tasks 5 \
  --test-concurrency 10 --analysis-concurrency 3
```

---

## Next Steps After Analysis

Once you have zero environment bugs:

1. **Document patterns** - Record common issues for future reference
2. **Create fix scripts** - Automate common fixes
3. **Update tests** - Add regression tests
4. **Review agent performance** - Focus on agent_faults if pass rate still low
5. **Optimize tasks** - Review user_faults for task clarity

---

## Files Generated

```
tau/
├── error_analyses/
│   ├── comprehensive_report.json          # Overall summary
│   ├── detailed_error_analysis.json       # Classified errors
│   ├── academic_search_1_error_analysis.json
│   ├── academic_search_2_error_analysis.json
│   └── ... (one per environment)
└── results/
    ├── tool-calling-gpt-4o-mini-0.0_range_0-1_user-gpt-4o-llm_*.json
    └── ... (test results)
```

---

## Support

For issues or questions:
1. Check this guide
2. Review error classifications
3. Run with `--verbose` for details
4. Check individual error analysis files
5. Review recent git history for similar fixes

---

**Last Updated:** October 10, 2025
**Version:** 2.0
**Status:** Production Ready ✅

