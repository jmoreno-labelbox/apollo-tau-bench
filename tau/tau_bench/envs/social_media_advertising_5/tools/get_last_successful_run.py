from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetLastSuccessfulRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None) -> str:
        runs = [
            r
            for r in data.get("automation_runs", {}).values()
            if r.get("run_type") == run_type and r.get("status") == "completed"
        ]
        if not runs:
            payload = {"error": f"no successful run for {run_type}"}
            out = json.dumps(payload)
            return out
        last = max(runs, key=lambda x: x.get("ended_at", ""))
        payload = last
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLastSuccessfulRun",
                "description": "Gets most recent successful run of a type.",
                "parameters": {
                    "type": "object",
                    "properties": {"run_type": {"type": "string"}},
                    "required": ["run_type"],
                },
            },
        }
