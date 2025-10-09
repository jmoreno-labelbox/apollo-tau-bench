from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetLastSuccessfulRun(Tool):
    """Determines the last successful completion time of a job type."""

    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None) -> str:
        successful_runs = [
            r
            for r in data.get("automation_runs", {}).values()
            if r.get("run_type") == run_type and r.get("status") == "completed"
        ]
        if not successful_runs:
            payload = {"error": f"No successful run found for type '{run_type}'."}
            out = json.dumps(payload)
            return out
        last_run = max(successful_runs, key=lambda x: x["ended_at"])
        payload = last_run
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLastSuccessfulRun",
                "description": "Reads the automation log to find when a specific job type last completed successfully.",
                "parameters": {
                    "type": "object",
                    "properties": {"run_type": {"type": "string"}},
                    "required": ["run_type"],
                },
            },
        }
