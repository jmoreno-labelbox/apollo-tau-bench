from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAutomationRuns(Tool):
    """Fetches all IDs of automation runs."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        runs = data.get("automation_runs", [])
        ids_ = []
        for i in runs:
            ids_ += [i.get("run_id")]
        payload = {"automation_run_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAutomationRuns",
                "description": "Retrieves all automation run IDs.",
                "parameters": {},
            },
        }
