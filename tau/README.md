## Tau module quickstart

### Setup
- Install from the repository root:

```bash
pip install -e .
```

- Copy the env template and fill in your API keys (from the repository root):

```bash
cp env.template .env
# edit .env to set OPENAI_API_KEY (and others if needed)
```

### Run
Run the benchmark via the root entrypoint `run.py`.

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


