# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _idx_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[int]:
    for i, r in enumerate(rows):
        if r.get("id") == _id:
            return i
    return None

class RecordReproCommandForRun(Tool):
    """Record a reproduction command on a run."""
    @staticmethod
    def invoke(data: Dict[str, Any], command, run_id) -> str:
        runs = list(data.get("build_runs", {}).values())
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["repro_command"] = command
            runs[idx] = run
            updated = run
        return json.dumps({"run": updated}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_repro_command_for_run",
                "description": "Persist a deterministic repro command for a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "command": {"type": "string"}
                    },
                    "required": ["run_id", "command"]
                }
            }
        }