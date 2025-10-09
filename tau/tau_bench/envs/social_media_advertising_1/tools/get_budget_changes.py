from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetBudgetChanges(Tool):
    """Fetches all IDs of budget changes."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        changes = data.get("budget_changes", [])
        ids_ = []
        for i in changes:
            ids_ += [i.get("change_id")]
        payload = {"budget_change_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getBudgetChanges",
                "description": "Retrieves all budget change IDs.",
                "parameters": {},
            },
        }
