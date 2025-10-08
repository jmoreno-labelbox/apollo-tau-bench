from tau_bench.envs.tool import Tool
import json
from typing import Any

class AttachSymbolicatedStackToRun(Tool):
    """Link a symbolicated stack trace URI to a build run by selecting a corresponding symbol record."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, build_id: str = None, module_name: str = None, platform: str = None) -> str:
        symbols = data.get("symbols", [])
        chosen = None
        for s in symbols:
            if (
                s.get("build_id") == build_id
                and s.get("module_name") == module_name
                and s.get("platform") == platform
            ):
                chosen = s
                break

        runs = data.get("build_runs", [])
        idx = _idx_by_id(runs, run_id)
        updated_run = None
        if idx is not None and chosen is not None:
            run = runs[idx]
            run["symbolicated_stack_uri"] = chosen.get("sym_uri")
            runs[idx] = run
            updated_run = run
        payload = {"chosen_symbol": chosen, "updated_run": updated_run}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AttachSymbolicatedStackToRun",
                "description": "Attach symbolicated stack URI on a run by matching symbol metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "build_id": {"type": "string"},
                        "module_name": {"type": "string"},
                        "platform": {"type": "string"},
                    },
                    "required": ["run_id", "build_id", "module_name", "platform"],
                },
            },
        }
