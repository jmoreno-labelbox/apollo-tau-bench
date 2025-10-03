#!/usr/bin/env python3
"""
Convert all domains/* variations into tau_bench/envs/<domain>_<n> envs.

What it does per domain variation:
- Create tau_bench/envs/<domain>_<n>/
- Copy rules.py, tasks.py, tasks_test.py, tools.py, tools/*, and data/*.json
- Generate data/__init__.py with load_data() for that env
- Build a new env.py with ABSOLUTE imports (like tau_bench.envs.airline.env)
- Fix tools imports to use tau_bench.envs.tool.Tool and local data path
- Remove the header line from tasks.py if it equals exactly "# Copyright Sierra"
- Register the env in tau_bench/envs/__init__.py and allow it in tau_bench/run.py

Usage:
  python scripts/convert_domains_to_envs.py [--domains banking_services,retail,...]
  python scripts/convert_domains_to_envs.py --dry-run
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOMAINS_ROOT = REPO_ROOT / "domains"
ENVS_ROOT = REPO_ROOT / "tau_bench" / "envs"
ENV_REGISTRY_FILE = ENVS_ROOT / "__init__.py"
RUN_FILE = REPO_ROOT / "tau_bench" / "run.py"


@dataclass
class VariationTarget:
    domain_name: str           # e.g. banking_services
    variation_num: int         # e.g. 1
    source_dir: Path           # domains/<domain>/variations/variation_<n>
    dest_env_dir: Path         # tau_bench/envs/<domain>_<n>


def snake_to_camel(s: str) -> str:
    return "".join(p.capitalize() for p in s.split("_"))


def find_variations(target_domains: list[str] | None) -> list[VariationTarget]:
    targets: list[VariationTarget] = []
    for domain_dir in sorted(DOMAINS_ROOT.iterdir()):
        if not domain_dir.is_dir():
            continue
        domain_name = domain_dir.name
        if target_domains and domain_name not in target_domains:
            continue
        variations_root = domain_dir / "variations"
        if not variations_root.is_dir():
            continue
        for var_dir in sorted(variations_root.iterdir()):
            if not var_dir.is_dir():
                continue
            m = re.match(r"variation_(\d+)$", var_dir.name)
            if not m:
                continue
            n = int(m.group(1))
            dest = ENVS_ROOT / f"{domain_name}_{n}"
            targets.append(VariationTarget(domain_name, n, var_dir, dest))
    return targets


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def write_file(p: Path, content: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def copy_tree(src: Path, dst: Path, exclude_patterns: list[str] | None = None) -> None:
    exclude_patterns = exclude_patterns or []
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(
        src,
        dst,
        ignore=shutil.ignore_patterns(*exclude_patterns),
        dirs_exist_ok=False,
    )


def generate_env_py(domain: str, n: int) -> str:
    env_pkg = f"tau_bench.envs.{domain}_{n}"
    class_name = f"Mock{snake_to_camel(domain)}DomainEnv"
    return (
        "# Copyright Sierra\n\n"
        f"from tau_bench.envs.base import Env\n"
        f"from {env_pkg}.data import load_data\n"
        f"from {env_pkg}.rules import RULES\n"
        f"from {env_pkg}.tools import TOOLS\n"
        "from typing import Optional, Union\n"
        "from tau_bench.envs.user import UserStrategy\n\n\n"
        f"class {class_name}(Env):\n"
        "    def __init__(\n"
        "        self,\n"
        "        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,\n"
        "        user_model: str = \"gpt-4o\",\n"
        "        user_provider: Optional[str] = None,\n"
        "        task_split: str = \"test\",\n"
        "        task_index: Optional[int] = None,\n"
        "    ):\n"
        "        match task_split:\n"
        "            case \"test\":\n"
        f"                from {env_pkg}.tasks_test import TASKS as tasks\n"
        "            case _:\n"
        "                raise ValueError(f\"Unknown task split: {task_split}\")\n"
        "        super().__init__(\n"
        "            data_load_func=load_data,\n"
        "            tools=TOOLS,\n"
        "            tasks=tasks,\n"
        "            wiki=\"\",\n"
        "            rules=RULES,\n"
        "            user_strategy=user_strategy,\n"
        "            user_model=user_model,\n"
        "            user_provider=user_provider,\n"
        "            task_index=task_index,\n"
        "        )\n"
        "        self.terminate_tools = [\"transfer_to_human_agents\"]\n"
    )


def generate_data_init(json_files: list[Path]) -> str:
    tables = [p.stem for p in json_files]
    body = [
        "import json",
        "import os",
        "from typing import Any",
        "",
        "FOLDER_PATH = os.path.dirname(__file__)",
        "",
        "def load_data() -> dict[str, Any]:",
        "    db: dict[str, Any] = {}",
        "    # auto-generated from files present in data/",
        f"    tables = {tables}",
        "    for name in tables:",
        "        path = os.path.join(FOLDER_PATH, f\"{name}.json\")",
        "        try:",
        "            with open(path, 'r', encoding='utf-8') as f:",
        "                content = f.read()",
        "                db[name] = json.loads(content) if content else []",
        "        except FileNotFoundError:",
        "            db[name] = []",
        "    return db",
        "",
    ]
    return "\n".join(body) + "\n"


def transform_tools_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"from\s+domains\.dto\s+import\s+Tool", "from tau_bench.envs.tool import Tool", text)
    # Common DATA_DIR patterns -> point to local env data/
    text = re.sub(
        r"os\.path\.join\(os\.path\.dirname\(__file__\),\s*['\"]\.{0,2}/\.{0,2}/data['\"]\)",
        "os.path.join(os.path.dirname(__file__), 'data')",
        text,
    )
    # Some tools use timezone-aware NOW etc.; leave as-is
    path.write_text(text, encoding="utf-8")


def strip_header_copyright(path: Path) -> None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except Exception:
        return
    if lines and lines[0].strip() == "# Copyright Sierra":
        new_text = "\n".join(lines[1:]) + ("\n" if lines[1:] else "")
        path.write_text(new_text, encoding="utf-8")


def upsert_env_registry(env_name: str, domain_class: str) -> None:
    text = ENV_REGISTRY_FILE.read_text(encoding="utf-8")
    if f"elif env_name == \"{env_name}\"" in text or f"env_name == \"{env_name}\"" in text:
        return
    block = (
        f"    elif env_name == \"{env_name}\":\n"
        f"        from tau_bench.envs.{env_name} import {domain_class}\n\n"
        f"        return {domain_class}(\n"
        "            user_strategy=user_strategy,\n"
        "            user_model=user_model,\n"
        "            task_split=task_split,\n"
        "            user_provider=user_provider,\n"
        "            task_index=task_index,\n"
        "        )\n"
    )
    # insert before the final else:
    text = re.sub(r"\n\s*else:\n\s*raise ValueError\([\s\S]*\)$", lambda m: "\n" + block + m.group(0), text, count=1, flags=re.MULTILINE)
    ENV_REGISTRY_FILE.write_text(text, encoding="utf-8")


def upsert_run_assert(env_name: str) -> None:
    text = RUN_FILE.read_text(encoding="utf-8")
    m = re.search(r"assert config\.env in \[(.*?)\]", text, flags=re.DOTALL)
    if not m:
        return
    inside = m.group(1)
    items = [i.strip().strip("'\"") for i in inside.split(",") if i.strip()]
    if env_name in items:
        return
    items.append(env_name)
    items_sorted = sorted(set(items))
    new_inside = ",\n        ".join(f"\"{i}\"" for i in items_sorted)
    new_text = text[: m.start(1)] + new_inside + text[m.end(1) :]
    RUN_FILE.write_text(new_text, encoding="utf-8")


def process_target(t: VariationTarget, dry_run: bool) -> None:
    env_name = f"{t.domain_name}_{t.variation_num}"
    class_name = f"Mock{snake_to_camel(t.domain_name)}DomainEnv"

    print(f"Processing {t.source_dir} -> {t.dest_env_dir}")
    if dry_run:
        return

    ensure_dir(t.dest_env_dir)

    # Copy simple top-level files if present
    for fname in ["rules.py", "tasks.py", "tasks_test.py", "tools.py"]:
        src = t.source_dir / fname
        if src.exists():
            shutil.copy2(src, t.dest_env_dir / fname)

    # Copy tools folder if present
    tools_src = t.source_dir / "tools"
    tools_dst = t.dest_env_dir / "tools"
    if tools_src.is_dir():
        copy_tree(tools_src, tools_dst, exclude_patterns=["__pycache__", "*.backup*", "*.bak*"])

    # Copy data from domain root data/
    domain_data = (t.source_dir.parent.parent) / "data"
    data_dst = t.dest_env_dir / "data"
    ensure_dir(data_dst)
    if domain_data.is_dir():
        for jf in sorted(domain_data.glob("*.json")):
            if ".backup" in jf.name or jf.name.endswith(".backup_rekey"):
                continue
            shutil.copy2(jf, data_dst / jf.name)

    # Generate data/__init__.py from files present
    json_files = sorted(data_dst.glob("*.json"))
    write_file(data_dst / "__init__.py", generate_data_init(json_files))

    # Build env.py (absolute imports)
    write_file(t.dest_env_dir / "env.py", generate_env_py(t.domain_name, t.variation_num))

    # __init__.py re-export
    write_file(t.dest_env_dir / "__init__.py", f"from .env import {class_name} as {class_name}\n")

    # Transform tools imports to use tau_bench.envs.tool.Tool and local DATA_DIR
    for p in [t.dest_env_dir / "tools.py"] + list((t.dest_env_dir / "tools").glob("*.py")):
        if p and p.exists():
            transform_tools_file(p)

    # Strip header from tasks.py only (not tasks_test)
    tasks_py = t.dest_env_dir / "tasks.py"
    if tasks_py.exists():
        strip_header_copyright(tasks_py)

    # Register env and allow in run assertions
    upsert_env_registry(env_name, class_name)
    upsert_run_assert(env_name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--domains", type=str, default=None, help="Comma-separated list of domain names to convert (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="List what would be converted without changing files")
    args = parser.parse_args()

    domains = [d.strip() for d in args.domains.split(",")] if args.domains else None
    targets = find_variations(domains)
    if not targets:
        print("No domain variations found.")
        return
    for t in targets:
        process_target(t, args.dry_run)
    print("Done.")


if __name__ == "__main__":
    main()


