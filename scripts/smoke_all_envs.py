#!/usr/bin/env python3
import argparse
import os
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, List, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))


def discover_env_names() -> List[str]:
    envs_dir = REPO_ROOT / "tau_bench" / "envs"
    names: List[str] = []
    for p in sorted(envs_dir.iterdir()):
        if not p.is_dir():
            continue
        if p.name.startswith("__"):
            continue
        if not (p / "__init__.py").exists():
            continue
        names.append(p.name)
    return names


def is_success(reward: float) -> bool:
    return (1 - 1e-6) <= reward <= (1 + 1e-6)


def run_single_env(env_name: str, provider: str, user_provider: str, model: str, user_model: str) -> Tuple[str, bool, str]:
    """Run one task for the env; return (env_name, passed, note)."""
    try:
        from tau_bench.types import RunConfig
        from tau_bench.run import run
    except Exception as e:
        return env_name, False, f"import-error: {e}"

    try:
        config = RunConfig(
            model_provider=provider,
            user_model_provider=user_provider,
            model=model,
            user_model=user_model,
            env=env_name,
            agent_strategy="tool-calling",
            temperature=0.0,
            task_split="test",
            start_index=0,
            end_index=1,
            log_dir="results",
            max_concurrency=1,
            seed=10,
            shuffle=0,
            user_strategy="llm",
        )
        results = run(config)
        total = len(results)
        succ = sum(1 for r in results if is_success(r.reward))
        errs = sum(1 for r in results if isinstance(r.info, dict) and ("error" in r.info))
        passed = succ > 0
        note = f"tasks={total}, success={succ}, errors={errs}"
        return env_name, passed, note
    except Exception as e:
        # Collapse long traces into short note lines
        msg = str(e)
        if "AuthenticationError" in msg or "api_key" in msg:
            msg = "authentication-error (set provider API keys)"
        return env_name, False, msg


def main() -> None:
    parser = argparse.ArgumentParser(description="Smoke test all tau_bench envs with a minimal run().")
    parser.add_argument("--provider", default="openai", help="LLM provider for agent model (default: openai)")
    parser.add_argument("--user-provider", default="openai", help="Provider for simulated user model (default: openai)")
    parser.add_argument("--model", default="gpt-4o", help="Model name for agent (default: gpt-4o)")
    parser.add_argument("--user-model", default="gpt-4o", help="Model name for user (default: gpt-4o)")
    parser.add_argument("--envs", default=None, help="Comma-separated env names to run; default is discover all in tau_bench/envs")
    parser.add_argument("--max-workers", type=int, default=4, help="Run up to N envs concurrently (default: 4)")
    args = parser.parse_args()

    if args.envs:
        env_names = [e.strip() for e in args.envs.split(",") if e.strip()]
    else:
        env_names = discover_env_names()

    results: List[Tuple[str, bool, str]] = []

    def _do(env_name: str) -> Tuple[str, bool, str]:
        return run_single_env(env_name, args.provider, args.user_provider, args.model, args.user_model)

    with ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as ex:
        for res in ex.map(_do, env_names):
            results.append(res)

    passed = [r for r in results if r[1]]
    failed = [r for r in results if not r[1]]

    print("\n===== Smoke Test Summary =====")
    print(f"Total envs: {len(results)}  |  Passed: {len(passed)}  |  Failed: {len(failed)}")

    if passed:
        print("\n-- Passed --")
        for name, _, note in sorted(passed, key=lambda x: x[0]):
            print(f"  {name}: {note}")

    if failed:
        print("\n-- Failed --")
        for name, _, note in sorted(failed, key=lambda x: x[0]):
            print(f"  {name}: {note}")


if __name__ == "__main__":
    main()


