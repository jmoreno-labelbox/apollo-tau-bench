# How to Run Tau-Bench Environments

This guide shows you how to run the tau-bench environments you've just synced from `domains_warrior`.

---

## 🔧 Setup

### 1. Set up your API keys

Edit the `.env` file in the `tau/` directory:

```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau
nano .env  # or use your preferred editor
```

Add your API keys:
```bash
OPENAI_API_KEY=sk-your-actual-key-here
ANTHROPIC_API_KEY=your-key-here  # if using Claude
GOOGLE_API_KEY=your-key-here     # if using Gemini
MISTRAL_API_KEY=your-key-here    # if using Mistral
```

### 2. Install dependencies (if not already done)

```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau
pip install -e .
```

---

## 🚀 Running Environments

### Basic Usage

```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau

# Run a single environment with just 1 task
python3 run.py --env academic_search_1 --start-index 0 --end-index 1

# Run with specific model
python3 run.py --env banking_services_1 --model gpt-4o --start-index 0 --end-index 2
```

### Available Environments

All 121 synced environments from `domains_warrior`:
- `academic_search_1` through `academic_search_5`
- `airline_1` through `airline_4`
- `banking_services_1`, `banking_services_2`, `banking_services_4`, `banking_services_5`, `banking_services_6`
- `career_planner_1` through `career_planner_5`
- `consulting_accounting_1`, `consulting_accounting_2`, `consulting_accounting_4`, `consulting_accounting_5`, `consulting_accounting_6`
- `data_science_1` through `data_science_6`
- `dev_ops_1` through `dev_ops_6`
- `digital_commerce_1` through `digital_commerce_5`
- `figma_gmail_mcp_pipeline_1` through `figma_gmail_mcp_pipeline_6`
- `file_system_1`, `file_system_7`, `file_system_8`, `file_system_9`
- `github_mcp_1`, `github_mcp_2`, `github_mcp_5`, `github_mcp_6`, `github_mcp_7`
- `it_help_desk_2`, `it_help_desk_4`, `it_help_desk_5`, `it_help_desk_6`
- `logistics_supply_chain_1`, `logistics_supply_chain_2`, `logistics_supply_chain_3`, `logistics_supply_chain_5`, `logistics_supply_chain_6`
- `new_hire_mcp_1` through `new_hire_mcp_5`
- `org_chart_1` through `org_chart_5`
- `project_management_1` through `project_management_5`
- `rbac_1` through `rbac_5`
- `real_estate_sales_1`, `real_estate_sales_2`, `real_estate_sales_3`, `real_estate_sales_4`, `real_estate_sales_7`
- `recipes_1` through `recipes_5`
- `retail_1` through `retail_6`
- `retail_point_of_sale_and_inventory_system_1`, `retail_point_of_sale_and_inventory_system_2`, `retail_point_of_sale_and_inventory_system_4`, `retail_point_of_sale_and_inventory_system_5`, `retail_point_of_sale_and_inventory_system_6`
- `smart_home_1` through `smart_home_5`
- `social_media_advertising_1` through `social_media_advertising_6`
- `sports_analytics_2`, `sports_analytics_3`, `sports_analytics_4`, `sports_analytics_5`

---

## 📝 Command Line Options

### Core Options

```bash
--env ENV_NAME              # Required: which environment to run
--model MODEL_NAME          # Agent model (default: gpt-4o-mini)
--user-model MODEL_NAME     # User simulator model (default: gpt-4o)
--agent-strategy STRATEGY   # tool-calling, act, react, or few-shot
--temperature TEMP          # Sampling temperature (default: 0.0)
```

### Task Selection

```bash
--start-index N            # Start from task N (default: 0)
--end-index N              # End at task N (default: -1 for all)
--task-ids 0 5 10          # Run specific task IDs only
```

### Performance Options

```bash
--max-concurrency N        # Parallel tasks (default: 2)
--num-trials N             # Repeat each task N times (default: 1)
```

### Output Options

```bash
--log-dir PATH             # Where to save results (default: results/)
```

---

## 💡 Example Commands

### 1. Quick Test (1 task, fast model)
```bash
python3 run.py \
  --env academic_search_1 \
  --model gpt-4o-mini \
  --start-index 0 \
  --end-index 1
```

### 2. Run First 5 Tasks with GPT-4o
```bash
python3 run.py \
  --env banking_services_1 \
  --model gpt-4o \
  --start-index 0 \
  --end-index 5 \
  --max-concurrency 3
```

### 3. Run Specific Tasks by ID
```bash
python3 run.py \
  --env retail_1 \
  --task-ids 0 2 5 8 \
  --model gpt-4o
```

### 4. Full Environment Run (All Tasks)
```bash
python3 run.py \
  --env consulting_accounting_1 \
  --model gpt-4o \
  --end-index -1 \
  --max-concurrency 5
```

### 5. Using Different Agent Strategies
```bash
# Tool calling (default, best for most cases)
python3 run.py --env data_science_1 --agent-strategy tool-calling

# ReAct agent (reasoning + acting)
python3 run.py --env data_science_1 --agent-strategy react

# Few-shot agent (with examples)
python3 run.py --env data_science_1 --agent-strategy few-shot
```

---

## 📊 Results

Results are saved to the `results/` directory with filenames like:
```
tool-calling-gpt-4o-mini-0.0_range_0-5_user-gpt-4o-llm_TIMESTAMP.json
```

Each result includes:
- Task execution traces
- Tool calls made
- Outputs generated
- Success/failure status
- Reward calculations

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'tau_bench'"
**Solution:** Make sure you're running from the `tau/` directory and have set `PYTHONPATH`:
```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau
export PYTHONPATH=.
python3 run.py --env academic_search_1 --start-index 0 --end-index 1
```

### Error: "Invalid API key"
**Solution:** Check your `.env` file has the correct API key:
```bash
cat .env  # verify keys are set
```

### Error: "Environment not found"
**Solution:** Make sure the environment name is correct and exists:
```bash
ls tau_bench/envs/ | grep -i "your_env_name"
```

### Tasks taking too long
**Solution:** 
- Use faster model: `--model gpt-4o-mini` instead of `gpt-4o`
- Reduce task count: `--end-index 1` for testing
- Use smaller concurrency: `--max-concurrency 1`

---

## 🔍 Analyzing Results

After running tasks, analyze errors:

```bash
cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau
export PYTHONPATH=.

python3 tau_bench/auto_error_identification.py \
  --platform openai \
  --model gpt-4o \
  --env academic_search_1 \
  --results-path results/YOUR_RESULTS_FILE.json \
  --output-path results/error_analysis.json \
  --max-concurrency 3
```

---

## 📚 What Just Got Synced?

✅ **121 `tools.py` files** copied from `domains_warrior` to `tau/tau_bench/envs/`
✅ **All syntax errors fixed** (3 files had f-string issues + BOM)
✅ **Backups created** (`.backup` files for all original tools)
✅ **airline_4 added** (was missing before)

Each environment now has:
- `tools.py` - Tool definitions (synced from warrior)
- `tasks_test.py` - Test task definitions
- `data.py` - Mock database
- `wiki.py` - Environment documentation
- `env.py` - Environment class

---

## ✅ Next Steps

1. **Test a single environment:**
   ```bash
   cd /Users/josemoreno/Desktop/repos/apollo-tau-bench/tau
   python3 run.py --env academic_search_1 --start-index 0 --end-index 1
   ```

2. **If it works, run more tasks:**
   ```bash
   python3 run.py --env academic_search_1 --end-index 5
   ```

3. **Try different environments:**
   ```bash
   python3 run.py --env banking_services_1 --end-index 3
   python3 run.py --env retail_1 --end-index 3
   ```

4. **Analyze failures:**
   ```bash
   export PYTHONPATH=.
   python3 tau_bench/auto_error_identification.py \
     --env academic_search_1 \
     --results-path results/<your-results-file>.json
   ```

---

## 📖 More Info

- See `README.md` for general tau-bench documentation
- See `AUTO_ERROR_IDENTIFICATION_USAGE.md` for error analysis details
- See `SYNC_WARRIOR_TOOLS_README.md` for sync script documentation

