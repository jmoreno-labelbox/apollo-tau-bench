## Tau standalone quickstart

### 1) Install

Option A: editable install from this `tau/` folder

```bash
pip install -e .
```

Option B: run without install (ensure imports work)

```bash
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"
```

### 2) Configure API keys

```bash
cp env.template .env
# edit .env to set OPENAI_API_KEY (and others if needed)
```

### 3) Run

Retail example:

```bash
python run.py \
  --agent-strategy tool-calling \
  --env retail_1 \
  --model gpt-4o-mini --model-provider openai \
  --user-model gpt-4o --user-model-provider openai \
  --user-strategy llm \
  --max-concurrency 5
```

Airline, specific task IDs:

```bash
python run.py \
  --agent-strategy tool-calling \
  --env airline_1 \
  --model gpt-4o --model-provider openai \
  --user-model gpt-4o --user-model-provider openai \
  --user-strategy llm \
  --task-ids 2 4 6
```

Notes:
- Results are saved under `results/` with a timestamped filename.
- Increase `--max-concurrency` to match your API rate limits.
- For the `few-shot` agent strategy, also pass `--few-shot-displays-path <path-to-jsonl>`.

