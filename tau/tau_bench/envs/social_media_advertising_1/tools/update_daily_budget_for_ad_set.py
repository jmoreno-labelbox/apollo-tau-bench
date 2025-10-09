from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateDailyBudgetForAdSet(Tool):
    """Modifies the daily budget of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, new_budget: float = None) -> str:
        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_budget = adset["daily_budget"]
                adset["daily_budget"] = new_budget
                payload = {
                    "status": "success",
                    "message": f"Ad set budget updated from {old_budget} to {new_budget}",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set {adset_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDailyBudgetForAdset",
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
