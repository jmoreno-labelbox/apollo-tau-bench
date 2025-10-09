from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchBudgetChangesByAdSet(Tool):
    """Looks for budget changes related to a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        changes = data.get("budget_changes", {}).values()
        matching_changes = []

        for change in changes.values():
            if change.get("adset_id") == adset_id:
                matching_changes.append(change.get("change_id"))
        payload = {"budget_change_ids": matching_changes}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchBudgetChangesByAdset",
                "description": "Searches for budget changes for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID to search for.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }
