from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchAutomationRunsByType(Tool):
    """Looks for automation runs that have a specific run type."""

    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None) -> str:
        runs = data.get("automation_runs", {}).values()
        matching_runs = []

        for run in runs:
            if run.get("run_type") == run_type:
                matching_runs.append(run.get("run_id"))
        payload = {"automation_run_ids": matching_runs}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAutomationRunsByType",
                "description": "Searches for automation runs with a specific run type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {
                            "type": "string",
                            "description": "The run type to search for (e.g., plan_freeze, budget_apply, creative_rotation).",
                        }
                    },
                    "required": ["run_type"],
                },
            },
        }
