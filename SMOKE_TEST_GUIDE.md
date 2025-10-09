# Smoke Test Guide

A comprehensive smoke testing script for tau-bench that validates all environment variations.

## Quick Start

### Test all environments (default settings)
```bash
python smoke_test_all_variations.py
```

### Test first 5 environments (quick check)
```bash
python smoke_test_all_variations.py --limit 5
```

### Test specific environments
```bash
python smoke_test_all_variations.py --envs retail_1 retail_2 airline_1
```

### Test all environments with all strategies
```bash
python smoke_test_all_variations.py --all-strategies
```

### Test environments matching a pattern
```bash
python smoke_test_all_variations.py --filter-pattern "retail"
python smoke_test_all_variations.py --filter-pattern "airline_"
```

## Advanced Usage

### Custom models
```bash
python smoke_test_all_variations.py \
  --model gpt-4o \
  --user-model gpt-4o \
  --limit 10
```

### Specific strategies
```bash
python smoke_test_all_variations.py \
  --agent-strategies tool-calling react \
  --limit 20
```

### Continue on failures
```bash
python smoke_test_all_variations.py \
  --continue-on-failure \
  --output smoke_test_2024-10-09.json
```

### With timeout and concurrency
```bash
python smoke_test_all_variations.py \
  --timeout 600 \
  --max-concurrency 2 \
  --limit 10
```

## All Options

```
--envs ENVS [ENVS ...]
    Specific environments to test (default: all discovered environments)

--limit LIMIT
    Limit number of environments to test (useful for quick smoke test)

--agent-strategies {tool-calling,act,react,few-shot} [{tool-calling,act,react,few-shot} ...]
    Agent strategies to test (default: tool-calling only)

--all-strategies
    Test all agent strategies (shortcut for all 4 strategies)

--model MODEL
    Model to use for agent (default: gpt-4o-mini)

--user-model USER_MODEL
    Model to use for user simulator (default: gpt-4o)

--task-split {train,test,dev}
    Task split to use (default: test)

--num-trials NUM_TRIALS
    Number of trials per test (default: 1)

--max-concurrency MAX_CONCURRENCY
    Max concurrency for each test (default: 1)

--timeout TIMEOUT
    Timeout in seconds for each test (default: 300)

--output OUTPUT
    Output file for results (default: smoke_test_results.json)

--continue-on-failure
    Continue testing even if some tests fail

--filter-pattern FILTER_PATTERN
    Only test environments matching this pattern (e.g., 'retail', 'airline_')
```

## Output

The script generates:
1. **Console output**: Real-time progress and results
2. **JSON file**: Detailed results including stdout/stderr for each test

### Example Output Structure

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
  "results": [
    {
      "success": true,
      "env": "retail_1",
      "agent_strategy": "tool-calling",
      "model": "gpt-4o-mini",
      "user_model": "gpt-4o",
      "returncode": 0,
      "duration": 45.3,
      "timestamp": "2024-10-09T12:35:00"
    }
  ]
}
```

## Common Scenarios

### Pre-deployment validation
```bash
# Test a sample of each domain with all strategies
python smoke_test_all_variations.py \
  --envs retail_1 airline_1 banking_services_1 \
  --all-strategies \
  --continue-on-failure
```

### Regression testing after code changes
```bash
# Test all environments but continue on failure to see full impact
python smoke_test_all_variations.py \
  --continue-on-failure \
  --output regression_test_$(date +%Y%m%d).json
```

### Performance baseline
```bash
# Test with timing data
python smoke_test_all_variations.py \
  --limit 20 \
  --timeout 600 \
  --output performance_baseline.json
```

### Quick domain validation
```bash
# Test all variations of a specific domain
python smoke_test_all_variations.py \
  --filter-pattern "retail_" \
  --all-strategies
```

## Exit Codes

- `0`: All tests passed
- `1`: One or more tests failed

## Tips

1. **Start small**: Use `--limit 5` for initial validation
2. **Use patterns**: `--filter-pattern` is great for domain-specific testing
3. **Continue on failure**: Use `--continue-on-failure` to see all failures at once
4. **Save results**: Always use `--output` with timestamps for historical tracking
5. **Parallel testing**: Increase `--max-concurrency` for faster execution (but watch resource usage)

## Troubleshooting

### "No environments found"
- Check that you're running from the project root
- Verify tau_bench/envs/ directory exists

### Timeout errors
- Increase `--timeout` (default is 300 seconds)
- Check if specific environments are consistently timing out

### Memory issues
- Reduce `--max-concurrency` to 1
- Test fewer environments at once with `--limit`

### Model errors
- Ensure your API keys are set in environment or .env file
- Verify model names are correct for your provider

