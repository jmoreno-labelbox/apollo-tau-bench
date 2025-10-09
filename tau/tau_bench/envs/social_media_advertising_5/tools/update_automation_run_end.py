from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateAutomationRunEnd(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, status: str = None, ended_at: str = None) -> str:
        for r in data.get("automation_runs", []):
            if r.get("run_id") == run_id:
                r["status"] = status
                r["ended_at"] = ended_at
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": f"run {run_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAutomationRunEnd",
                "description": "Sets final status and end time for a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "status": {"type": "string"},
                        "ended_at": {"type": "string"},
                    },
                    "required": ["run_id", "status", "ended_at"],
                },
            },
        }
