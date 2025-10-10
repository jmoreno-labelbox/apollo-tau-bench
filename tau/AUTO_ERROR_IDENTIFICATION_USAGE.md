# Auto Error Identification Script Usage

## What It Does

The `auto_error_identification.py` script analyzes failed agent trajectories using an LLM to:
1. **Fault Assignment**: Determine if failures are caused by the user, agent, or environment
2. **Fault Type Classification**: Categorize agent failures (wrong tool, wrong argument, partial completion, etc.)

## Fixes Applied

✅ **Updated from old environment names** (`airline`, `retail`) to support all current environments
✅ **Dynamic task loading** - now works with any environment in `tau/tau_bench/envs/`
✅ **Removed hardcoded imports** - uses `importlib` for flexibility

## How to Run

### Prerequisites

1. **Set up your `.env` file** with API keys:
   ```bash
   cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau
   
   # Copy the template if you haven't already
   cp env.template .env
   
   # Edit .env and add your API key
   # OPENAI_API_KEY=sk-...
   ```
   
   The script will automatically load API keys from `.env` - no need to set them manually!

2. **Set PYTHONPATH** (required when running from outside the package):
   ```bash
   export PYTHONPATH=.
   ```

3. **Have a results file** from a tau-bench run (contains trajectory data)

### Basic Usage

```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau

# Make sure your .env file has OPENAI_API_KEY set
export PYTHONPATH=.

python3 tau_bench/auto_error_identification.py \
  --platform openai \
  --model gpt-4 \
  --env airline_1 \
  --results-path results/my_results.json \
  --output-path results/error_analysis.json \
  --max-concurrency 5 \
  --max-num-failed-results 50
```

The script will automatically:
- ✅ Load API keys from `.env` file
- ✅ Display which `.env` file was loaded
- ⚠️ Warn if no `.env` file is found

### Required Arguments

- `--platform`: LLM platform (openai, anthropic, mistral, etc.)
- `--env`: Environment name (e.g., `airline_1`, `retail_2`, `banking_services_6`)
- `--results-path`: Path to the results JSON file from tau-bench run
- `--output-path`: Where to save the analysis results

### Optional Arguments

- `--model`: Specific model name (default depends on platform)
- `--base-url`: Custom API endpoint
- `--max-concurrency`: Number of parallel API calls (default: 1)
- `--max-num-failed-results` or `-n`: Limit analysis to first N failures

## Supported Environments

The script now works with **any environment** in `tau/tau_bench/envs/`, including:

- `airline_1`, `airline_2`, `airline_3`, `airline_4`, `airline_5`
- `retail_1`, `retail_2`, `retail_3`, `retail_4`, `retail_5`, `retail_6`
- `banking_services_1`, `banking_services_2`, `banking_services_4`, `banking_services_5`, `banking_services_6`
- All other environments in the envs directory

## Output Format

The script produces a JSON file with two analyses:

```json
{
  "fault_assignment_analysis": [
    {
      "task_id": 0,
      "author": "agent",
      "description": "The agent called GetCustomerDetails with wrong customer_id..."
    }
  ],
  "fault_type_analysis": [
    {
      "task_id": 0,
      "fault_type": "used_wrong_tool_argument",
      "description": "The agent used incorrect customer_id parameter..."
    }
  ]
}
```

### Fault Authors
- `user`: The simulated user caused the error
- `agent`: The AI agent made a mistake
- `environment`: System/data issue (neither user nor agent)

### Fault Types (for agent errors)
- `called_wrong_tool`: Agent used incorrect tool
- `used_wrong_tool_argument`: Correct tool, wrong parameters
- `goal_partially_completed`: Task not fully completed
- `other`: Other types of failures

## Example: Analyzing Airline Results

```bash
# Run tau-bench first to get results
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau
python3 -m tau_bench.run \
  --env airline_1 \
  --model gpt-4o-mini \
  --start-index 0 \
  --end-index 10

# Then analyze failures
PYTHONPATH=. python3 tau_bench/auto_error_identification.py \
  --platform openai \
  --model gpt-4 \
  --env airline_1 \
  --results-path results/tool-calling-gpt-4o-mini-*.json \
  --output-path results/airline_1_error_analysis.json \
  -n 20
```

## Troubleshooting

### ModuleNotFoundError: No module named 'tau_bench'
**Solution**: Set PYTHONPATH before running:
```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau
export PYTHONPATH=.
```

### Could not load tasks from environment 'X'
**Solution**: Verify the environment exists:
```bash
ls tau_bench/envs/ | grep "^X$"
```

### API authentication errors
**Solution**: Make sure your `.env` file has the correct API key:
```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau

# Check if .env exists
ls -la .env

# Edit it to add your API key
# For OpenAI: OPENAI_API_KEY=sk-...
# For Anthropic: ANTHROPIC_API_KEY=sk-ant-...
```

If the script shows "⚠️ No .env file found", create one:
```bash
cp env.template .env
# Then edit .env and add your keys
```

