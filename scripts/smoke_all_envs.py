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


def discover_env_names(envs_root: Path) -> List[str]:
    envs_dir = envs_root
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


def read_envs_file(path: Path) -> List[str]:
    envs: List[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        envs.append(s)
    return envs


def is_success(reward: float) -> bool:
    return (1 - 1e-6) <= reward <= (1 + 1e-6)


def run_single_env(env_name: str, provider: str, user_provider: str, model: str, user_model: str) -> Tuple[str, bool, str]:
    """Run one task for the env; return (env_name, passed, note). Note includes short error summary if present."""
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
        # Collect error messages if present
        err_msgs = []
        errs = 0
        for r in results:
            info = r.info if isinstance(r.info, dict) else None
            if info and "error" in info:
                errs += 1
                msg = str(info.get("error", "")).strip()
                if msg and msg not in err_msgs:
                    err_msgs.append(msg)
        passed = succ > 0
        note = f"tasks={total}, success={succ}, errors={errs}"
        if err_msgs:
            # Keep the note short: include up to 2 unique error messages
            preview = "; ".join(err_msgs[:2])
            if len(err_msgs) > 2:
                preview += f" (+{len(err_msgs)-2} more)"
            note = f"{note}; {preview}"
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
    parser.add_argument("--envs", default=None, help="Comma-separated env names to run; default is discover all in envs root")
    parser.add_argument("--envs-file", default=None, help="Path to a text file with env names (one per line) to run")
    parser.add_argument("--envs-root", default=str(REPO_ROOT / "tau_bench" / "envs"), help="Path to envs root to discover from (affects --envs discovery)")
    parser.add_argument("--envs-package", default=None, help="Python package path for envs (sets TAU_BENCH_ENVS_PACKAGE)")
    parser.add_argument("--write-failures", default=None, help="Path to write failed env names (one per line)")
    parser.add_argument("--write-failure-notes", default=None, help="Path to write failed env notes: 'env_name: note' per line")
    parser.add_argument("--max-workers", type=int, default=4, help="Run up to N envs concurrently (default: 4)")
    args = parser.parse_args()

    if args.envs_package:
        os.environ["TAU_BENCH_ENVS_PACKAGE"] = args.envs_package

    if args.envs_file:
        env_names = read_envs_file(Path(args.envs_file))
    elif args.envs:
        env_names = [e.strip() for e in args.envs.split(",") if e.strip()]
    else:
        env_names = discover_env_names(Path(args.envs_root))

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
        if args.write_failures:
            out_path = Path(args.write_failures)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                for name, _, _ in sorted(failed, key=lambda x: x[0]):
                    f.write(name + "\n")
            print(f"\nWritten failed envs to: {out_path}")
        if args.write_failure_notes:
            notes_path = Path(args.write_failure_notes)
            notes_path.parent.mkdir(parents=True, exist_ok=True)
            with open(notes_path, "w", encoding="utf-8") as f:
                for name, _, note in sorted(failed, key=lambda x: x[0]):
                    f.write(f"{name}: {note}\n")
            print(f"Written failed env notes to: {notes_path}")


if __name__ == "__main__":
    main()


