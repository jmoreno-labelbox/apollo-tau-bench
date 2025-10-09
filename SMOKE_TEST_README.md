# Smoke Test Suite for Tau-Bench

A comprehensive smoke testing framework to validate all environment variations in tau-bench.

## 🎯 What's Included

### 1. **smoke_test_all_variations.py** (Main Script)
A full-featured Python script that:
- Auto-discovers all environments in `tau_bench/envs/`
- Tests multiple agent strategies (tool-calling, act, react, few-shot)
- Supports filtering, limiting, and custom models
- Generates detailed JSON reports
- Provides rich console output with progress tracking

### 2. **quick_smoke_test.sh** (Convenience Wrapper)
A bash wrapper for common testing scenarios:
- **quick**: Test 5 environments (< 5 minutes)
- **sample**: Test one env per domain with all strategies
- **domain**: Test all variations of a specific domain
- **full**: Test everything (takes hours!)

### 3. **SMOKE_TEST_GUIDE.md** (Documentation)
Comprehensive usage guide with examples and troubleshooting tips.

## 🚀 Quick Start

### Fastest Test (5 environments)
```bash
./quick_smoke_test.sh quick
```

### Test Specific Domain
```bash
./quick_smoke_test.sh domain retail
```

### Test with Python Script
```bash
# Quick test
python smoke_test_all_variations.py --limit 5

# Test specific environments
python smoke_test_all_variations.py --envs retail_1 airline_1 banking_services_1

# Test with all strategies
python smoke_test_all_variations.py --limit 10 --all-strategies
```

## 📊 What Gets Tested

For each environment, the script runs:
```bash
python run.py \
  --env <environment_name> \
  --agent-strategy <strategy> \
  --model <model> \
  --user-model <user_model> \
  --num-trials 1 \
  --task-split test \
  --max-concurrency 1
```

### Discovered Environments (122 total)
The script automatically discovers all valid environments:
- **academic_search**: 5 variations
- **airline**: 5 variations
- **banking_services**: 5 variations
- **career_planner**: 5 variations
- **consulting_accounting**: 5 variations
- **data_science**: 6 variations
- **dev_ops**: 6 variations
- **digital_commerce**: 5 variations
- **figma_gmail_mcp_pipeline**: 6 variations
- **file_system**: 4 variations
- **github_mcp**: 5 variations
- **it_help_desk**: 4 variations
- **logistics_supply_chain**: 5 variations
- **new_hire_mcp**: 5 variations
- **org_chart**: 5 variations
- **project_management**: 5 variations
- **rbac**: 5 variations
- **real_estate_sales**: 5 variations
- **recipes**: 5 variations
- **retail**: 6 variations
- **retail_point_of_sale_and_inventory_system**: 5 variations
- **smart_home**: 5 variations
- **social_media_advertising**: 6 variations
- **sports_analytics**: 4 variations

### Agent Strategies
- **tool-calling** (default)
- **act**
- **react**
- **few-shot**

## 📈 Output

### Console Output
```
==================================================
Testing: retail_1 | Strategy: tool-calling | Model: gpt-4o-mini
==================================================
✅ PASSED in 45.32s

[2/122] Testing airline_1 with tool-calling...
```

### JSON Report (smoke_test_results.json)
```json
{
  "timestamp": "2024-10-09T12:34:56",
  "config": {
    "model": "gpt-4o-mini",
    "user_model": "gpt-4o",
    "strategies": ["tool-calling"],
    "task_split": "test",
    "num_envs": 122,
    "total_tests": 122
  },
  "summary": {
    "total": 122,
    "passed": 120,
    "failed": 2,
    "success_rate": 0.984
  },
  "results": [...]
}
```

## 🎓 Common Use Cases

### 1. Pre-Deployment Validation
```bash
# Test a representative sample
python smoke_test_all_variations.py \
  --envs retail_1 airline_1 banking_services_1 \
  --all-strategies \
  --continue-on-failure
```

### 2. Regression Testing
```bash
# Test all environments, save results
python smoke_test_all_variations.py \
  --continue-on-failure \
  --output "regression_$(date +%Y%m%d).json"
```

### 3. Domain-Specific Testing
```bash
# Test all retail environments
./quick_smoke_test.sh domain retail

# Or with Python
python smoke_test_all_variations.py --filter-pattern "retail_"
```

### 4. Quick Sanity Check
```bash
# Test first 5 environments
./quick_smoke_test.sh quick
```

### 5. Performance Benchmarking
```bash
# Test with timing data
python smoke_test_all_variations.py \
  --limit 20 \
  --timeout 600 \
  --output performance_baseline.json
```

## ⚙️ Configuration Options

### Python Script Options
```bash
--envs                   # Specific environments to test
--limit                  # Limit number of environments
--agent-strategies       # Which strategies to test
--all-strategies         # Test all 4 strategies
--model                  # Agent model (default: gpt-4o-mini)
--user-model            # User model (default: gpt-4o)
--task-split            # train/test/dev (default: test)
--num-trials            # Trials per test (default: 1)
--max-concurrency       # Parallel tasks (default: 1)
--timeout               # Per-test timeout (default: 300s)
--output                # Results JSON file
--continue-on-failure   # Don't stop on first failure
--filter-pattern        # Pattern to match environments
```

### Bash Wrapper Modes
```bash
./quick_smoke_test.sh quick     # 5 envs, tool-calling
./quick_smoke_test.sh sample    # Sample per domain, all strategies
./quick_smoke_test.sh domain X  # All X environments
./quick_smoke_test.sh full      # Everything (long!)
./quick_smoke_test.sh help      # Show help
```

## 🔍 Interpreting Results

### Exit Codes
- `0`: All tests passed ✅
- `1`: One or more tests failed ❌

### Success Criteria
Each test is considered successful if:
1. Command exits with code 0
2. No timeout occurs
3. No exceptions are raised

### Failure Analysis
Failed tests include:
- Return code
- stdout/stderr output
- Duration before failure
- Timestamp for reproduction

## 💡 Tips & Best Practices

1. **Start Small**: Use `--limit 5` for initial validation
2. **Use Patterns**: Filter by domain with `--filter-pattern`
3. **Continue on Failure**: Use `--continue-on-failure` to see all issues
4. **Save Results**: Always use `--output` with timestamps
5. **Parallel Testing**: Increase `--max-concurrency` carefully (watch resources)
6. **Timeout Adjustment**: Increase `--timeout` for slow environments
7. **Model Selection**: Use cheaper models for smoke tests (gpt-4o-mini)

## 🐛 Troubleshooting

### No environments found
- Ensure you're running from project root
- Check `tau_bench/envs/` or `tau/tau_bench/envs/` exists

### Timeout errors
- Increase `--timeout` (default 300s)
- Check specific environments that timeout consistently

### Memory issues
- Reduce `--max-concurrency` to 1
- Test fewer environments with `--limit`

### Model/API errors
- Verify API keys in environment or `.env`
- Check model names are correct for provider

## 📚 Additional Resources

- See `SMOKE_TEST_GUIDE.md` for detailed examples
- Run `python smoke_test_all_variations.py --help` for all options
- Run `./quick_smoke_test.sh help` for wrapper usage

## 🏗️ Architecture

```
smoke_test_all_variations.py
├── get_all_envs()          # Auto-discover environments
├── run_smoke_test()        # Execute single test
└── main()                  # Orchestrate all tests
    ├── Parse arguments
    ├── Discover/filter envs
    ├── Run tests
    ├── Collect results
    ├── Generate summary
    └── Save JSON report

quick_smoke_test.sh
├── quick mode              # Fast validation
├── sample mode             # Representative testing
├── domain mode             # Focused testing
└── full mode               # Comprehensive testing
```

## 📝 Example Session

```bash
# Quick validation
$ ./quick_smoke_test.sh quick
🚀 Running QUICK smoke test (5 environments, tool-calling only)...

==================================================
Testing: academic_search_1 | Strategy: tool-calling | Model: gpt-4o-mini
==================================================
✅ PASSED in 42.5s

[2/5] Testing: airline_1 | Strategy: tool-calling
✅ PASSED in 38.2s

# ... more tests ...

==================================================
SMOKE TEST SUMMARY
==================================================
Total Tests: 5
✅ Passed: 5 (100.0%)
❌ Failed: 0 (0.0%)

📄 Detailed results saved to: smoke_test_quick_20241009_143022.json
```

## 🎉 Success!

You now have a complete smoke testing framework that can validate all tau-bench environment variations with flexible configuration options!

