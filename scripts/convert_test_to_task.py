#!/usr/bin/env python3
# Copyright Sierra

"""
python3 scripts/convert_test_to_task.py --out tau_bench/envs/airline/tasks.py
"""

import argparse
import importlib.util
import sys
from types import ModuleType
from pathlib import Path
from typing import Any, Dict, List

# We'll avoid importing the full tau_bench package (to not pull optional deps like litellm)
# by loading specific files directly via importlib and injecting a lightweight package stub.

REPO_ROOT = Path(__file__).resolve().parent.parent
TAU_BENCH_DIR = REPO_ROOT / "tau_bench"
TYPES_PATH = TAU_BENCH_DIR / "types.py"
AIRLINE_TASKS_TEST_PATH = TAU_BENCH_DIR / "envs" / "airline" / "tasks_test.py"


def _load_module_from_path(module_name: str, file_path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {module_name} from {file_path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    return mod


def task_to_dict(task_obj: Any) -> Dict[str, Any]:
    # Pydantic v2 supports model_dump; fall back to dict if a plain dict
    if hasattr(task_obj, "model_dump"):
        data = task_obj.model_dump()
    elif isinstance(task_obj, dict):
        data = task_obj
    else:
        # Last resort, try __dict__
        data = getattr(task_obj, "__dict__", {})

    # Convert actions: kwargs -> arguments
    actions = []
    for act in data.get("actions", []):
        if hasattr(act, "model_dump"):
            act_d = act.model_dump()
        elif isinstance(act, dict):
            act_d = act
        else:
            act_d = getattr(act, "__dict__", {})

        name = act_d.get("name")
        kwargs = act_d.get("kwargs", {})
        actions.append({"name": name, "arguments": kwargs})

    out: Dict[str, Any] = {
        # keep annotator as int if present, else omit
        **({"annotator": int(data["annotator"])} if "annotator" in data else {}),
        "user_id": data["user_id"],
        "instruction": data.get("instruction", ""),
        "actions": actions,
    }
    if "outputs" in data and data["outputs"] is not None:
        out["outputs"] = data["outputs"]
    return out


def render_tasks_py(tasks: List[Dict[str, Any]]) -> str:
    # Produce a Python file similar to existing tasks.py format
    # Use consistent 4-space indentation as in repo
    import json

    def dumps(obj: Any, indent: int = 8) -> str:
        return json.dumps(obj, indent=4, ensure_ascii=False)

    lines: List[str] = []
    lines.append("# Copyright Sierra")
    lines.append("")
    lines.append("tasks = [")
    for i, t in enumerate(tasks):
        if i > 0:
            lines.append("    ,")
        # Build the dict manually to match key ordering: annotator, user_id, instruction, actions, outputs
        item: Dict[str, Any] = {}
        if "annotator" in t:
            item["annotator"] = t["annotator"]
        item["user_id"] = t["user_id"]
        item["instruction"] = t.get("instruction", "")
        # transform actions to desired format already done, but ensure ordering "name", "arguments"
        item["actions"] = [
            {"name": a["name"], "arguments": a.get("arguments", {})} for a in t.get("actions", [])
        ]
        if "outputs" in t:
            item["outputs"] = t["outputs"]

        # Pretty print the dict with custom formatting:
        # We'll leverage json dumps for substructures and craft outer with quotes
        lines.append("    {")
        if "annotator" in item:
            lines.append(f"        \"annotator\": {item['annotator']},")
        lines.append(f"        \"user_id\": \"{item['user_id']}\",")
        # Escape instruction safely
        import json as _json
        instr = _json.dumps(item["instruction"])  # includes quotes
        lines.append(f"        \"instruction\": {instr},")
        lines.append("        \"actions\": [")
        for j, a in enumerate(item["actions"]):
            comma = "," if j < len(item["actions"]) - 1 else ""
            arg_str = dumps(a["arguments"])  # properly indented JSON
            # We want a stable pretty layout with name then arguments block
            lines.append("            {")
            lines.append(f"                \"name\": \"{a['name']}\",")
            # Indent the arguments block further, but keep as a single JSON block after the key
            # We'll indent every line of arg_str by 16 spaces
            arg_lines = arg_str.splitlines()
            if arg_lines:
                lines.append("                \"arguments\": {"
                             + ("" if len(arg_lines) == 1 else ""))
                # Re-render with manual control for consistent spacing
                # Re-parse to dict to then emit with custom indenting
                import json as _json2
                arg_obj = _json2.loads(arg_str)
                # Re-dumps with indent=4 then indent lines by 16 spaces, trimming outer braces to add ours
                arg_block = _json2.dumps(arg_obj, indent=4, ensure_ascii=False)
                arg_block_lines = arg_block.splitlines()
                # Remove first and last braces
                if arg_block_lines and arg_block_lines[0].strip() == "{":
                    arg_block_lines = arg_block_lines[1:]
                if arg_block_lines and arg_block_lines[-1].strip() == "}":
                    arg_block_lines = arg_block_lines[:-1]
                for k, l in enumerate(arg_block_lines):
                    lines.append("                " + l)
                lines.append("                }" + comma)
            else:
                lines.append("                \"arguments\": {}" + comma)
            lines.append("            }" + comma)
        lines.append("        ],")
        if "outputs" in item:
            # outputs is a simple list of strings or numbers
            outputs_str = dumps(item["outputs"])  # pretty
            # re-indent outputs block to match style
            outputs_lines = outputs_str.splitlines()
            if len(outputs_lines) == 1:
                lines.append(f"        \"outputs\": {outputs_lines[0]}")
            else:
                lines.append("        \"outputs\": [")
                for k, l in enumerate(outputs_lines[1:-1]):
                    lines.append("            " + l)
                lines.append("        ]")
        lines.append("    }")
    lines.append("]")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert airline tasks_test (Pydantic) to tasks dict format")
    parser.add_argument(
        "--out",
        type=str,
        default=str(Path(__file__).resolve().parent.parent / "tau_bench" / "envs" / "airline" / "tasks.py"),
        help="Output path for generated tasks.py",
    )
    args = parser.parse_args()

    # Prepare a lightweight package stub so that `from tau_bench.types import ...` resolves
    if "tau_bench" not in sys.modules:
        pkg = ModuleType("tau_bench")
        # Mark as a namespace/package-like module
        setattr(pkg, "__path__", [str(TAU_BENCH_DIR)])
        sys.modules["tau_bench"] = pkg

    # Load tau_bench.types directly so tasks_test can import it without triggering package __init__
    _load_module_from_path("tau_bench.types", TYPES_PATH)

    # Load tasks_test directly from file
    tasks_test_mod = _load_module_from_path("airline_tasks_test", AIRLINE_TASKS_TEST_PATH)
    if not hasattr(tasks_test_mod, "TASKS"):
        raise RuntimeError("Expected TASKS in airline tasks_test module")

    converted: List[Dict[str, Any]] = [task_to_dict(t) for t in getattr(tasks_test_mod, "TASKS")]
    content = render_tasks_py(converted)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")
    print(f"Wrote {len(converted)} tasks to {out_path}")


if __name__ == "__main__":
    main()


