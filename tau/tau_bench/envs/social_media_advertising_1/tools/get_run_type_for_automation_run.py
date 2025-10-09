from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetRunTypeForAutomationRun(Tool):
    """Fetches the type of run for a specific automation run."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None) -> str:
        runs = data.get("automation_runs", {}).values()

        for run in runs:
            if run.get("run_id") == run_id:
                payload = {"run_type": run.get("run_type")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Automation run with ID '{run_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRunTypeForAutomationRun",
                "description": "Retrieves the run type for a specific automation run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run.",
                        }
                    },
                    "required": ["run_id"],
                },
            },
        }
