#!/usr/bin/env python3
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WARRIOR_BASE = ROOT / "tau_bench_warrior"
DOMAINS_DIR = WARRIOR_BASE / "domains"
ENVS_DIR = WARRIOR_BASE / "envs"


def to_class_name(domain_name: str) -> str:
    parts = re.split(r"[_-]", domain_name)
    return "".join(p.capitalize() for p in parts if p)


def ensure_env_py(target_env_dir: Path, domain_name: str) -> None:
    env_py = target_env_dir / "env.py"
    if env_py.exists():
        return
    class_name = f"Mock{to_class_name(domain_name)}DomainEnv"
    content = f"""
from tau_bench.envs.base import Env
from typing import Optional, Union
from tau_bench.envs.user import UserStrategy

try:
    from .tools import TOOLS  # tools.py
except Exception:  # pragma: no cover
    try:
        from .tools import TOOLS  # tools package
    except Exception:
        TOOLS = []

try:
    from .rules import RULES
except Exception:
    RULES = []

try:
    from .tasks_test import TASKS
except Exception:
    TASKS = []

def _load_data() -> dict:
    try:
        from .data import load_data
        return load_data()
    except Exception:
        return {{}}


class {class_name}(Env):
    def __init__(
        self,
        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,
        user_model: str = "gpt-4o",
        user_provider: Optional[str] = None,
        task_split: str = "test",
        task_index: Optional[int] = None,
    ):
        if task_split != "test":
            raise ValueError(f"Unknown task split: {{task_split}}")
        super().__init__(
            data_load_func=_load_data,
            tools=TOOLS,
            tasks=TASKS,
            wiki="",
            rules=RULES,
            user_strategy=user_strategy,
            user_model=user_model,
            user_provider=user_provider,
            task_index=task_index,
        )
"""
    env_py.write_text(content.strip() + "\n", encoding="utf-8")


def ensure_init_py(target_env_dir: Path, domain_name: str) -> None:
    init_py = target_env_dir / "__init__.py"
    if init_py.exists():
        return
    class_name = f"Mock{to_class_name(domain_name)}DomainEnv"
    init_py.write_text(f"from .env import {class_name} as Mock{to_class_name(domain_name)}DomainEnv\n", encoding="utf-8")


def copy_if_exists(src: Path, dst: Path) -> None:
    if src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    elif src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)


def main() -> None:
    ENVS_DIR.mkdir(parents=True, exist_ok=True)
    # Clear existing envs
    for child in ENVS_DIR.iterdir():
        if child.name.startswith("__"):
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

    for domain_dir in sorted(DOMAINS_DIR.glob("*")):
        if not domain_dir.is_dir() or domain_dir.name.startswith("__"):
            continue
        variations = domain_dir / "variations"
        if not variations.exists():
            continue
        for var_dir in sorted(variations.glob("*")):
            if not var_dir.is_dir():
                continue
            m = re.match(r"variation_(\d+)$", var_dir.name)
            idx = m.group(1) if m else var_dir.name
            env_name = f"{domain_dir.name}_{idx}"
            target = ENVS_DIR / env_name
            target.mkdir(parents=True, exist_ok=True)

            # Copy essential files
            copy_if_exists(var_dir / "rules.py", target / "rules.py")
            copy_if_exists(var_dir / "tasks_test.py", target / "tasks_test.py")
            copy_if_exists(var_dir / "tools.py", target / "tools.py")
            copy_if_exists(var_dir / "tools", target / "tools")

            # Copy shared domain data if present
            copy_if_exists(domain_dir / "data", target / "data")

            # Ensure env.py and __init__.py exist
            ensure_env_py(target, domain_dir.name)
            ensure_init_py(target, domain_dir.name)

    print("✓ Re-packaged warrior domains into tau_bench_warrior/envs")


if __name__ == "__main__":
    main()


