from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAdsetBudget(Tool):
    """Modifies the daily budget for an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, new_budget: float = None) -> str:
        for adset in data.get("adsets", {}).values():
            if adset.get("adset_id") == adset_id:
                adset["daily_budget"] = new_budget
                payload = adset
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdsetBudget",
                "description": "Updates the daily budget for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"},
                    },
                    "required": ["adset_id", "new_budget"],
                },
            },
        }
