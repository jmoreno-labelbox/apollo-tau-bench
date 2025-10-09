from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RecordReproCommandForRun(Tool):
    """Log a reproduction command for a run."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, command: str = None) -> str:
        runs = data.get("build_runs", {}).values()
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["repro_command"] = command
            runs[idx] = run
            updated = run
        payload = {"run": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordReproCommandForRun",
                "description": "Persist a deterministic repro command for a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "command": {"type": "string"},
                    },
                    "required": ["run_id", "command"],
                },
            },
        }
