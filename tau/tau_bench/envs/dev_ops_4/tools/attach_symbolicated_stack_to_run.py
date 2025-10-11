# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _idx_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[int]:
    for i, r in enumerate(rows):
        if r.get("id") == _id:
            return i
    return None

class AttachSymbolicatedStackToRun(Tool):
    """Attach a symbolicated stack trace URI to a build run by choosing a matching symbol record."""
    @staticmethod
    def invoke(data: Dict[str, Any], build_id, module_name, platform, run_id) -> str:

        symbols = list(data.get("symbols", {}).values())
        chosen = None
        for s in symbols:
            if s.get("build_id") == build_id and s.get("module_name") == module_name and s.get("platform") == platform:
                chosen = s
                break

        runs = list(data.get("build_runs", {}).values())
        idx = _idx_by_id(runs, run_id)
        updated_run = None
        if idx is not None and chosen is not None:
            run = runs[idx]
            run["symbolicated_stack_uri"] = chosen.get("sym_uri")
            runs[idx] = run
            updated_run = run

        return json.dumps({"chosen_symbol": chosen, "updated_run": updated_run}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "attach_symbolicated_stack_to_run",
                "description": "Attach symbolicated stack URI on a run by matching symbol metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "build_id": {"type": "string"},
                        "module_name": {"type": "string"},
                        "platform": {"type": "string"}
                    },
                    "required": ["run_id", "build_id", "module_name", "platform"]
                }
            }
        }