from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchAutomationRunsByStatus(Tool):
    """Looks for automation runs that have a specific status."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        runs = data.get("automation_runs", {}).values()
        matching_runs = []

        for run in runs:
            if run.get("status") == status:
                matching_runs.append(run.get("run_id"))
        payload = {"automation_run_ids": matching_runs}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAutomationRunsByStatus",
                "description": "Searches for automation runs with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., completed, failed).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }
