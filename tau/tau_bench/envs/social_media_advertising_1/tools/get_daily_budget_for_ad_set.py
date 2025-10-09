from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetDailyBudgetForAdSet(Tool):
    """Fetches the daily budget allocated for a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        adsets = data.get("adsets", {}).values()

        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                payload = {"daily_budget": adset.get("daily_budget")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDailyBudgetForAdset",
                "description": "Retrieves the daily budget for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }
