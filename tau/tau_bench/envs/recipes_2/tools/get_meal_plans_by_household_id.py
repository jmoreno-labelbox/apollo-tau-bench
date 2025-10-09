from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetMealPlansByHouseholdId(Tool):
    """Fetches all meal plans associated with a particular household ID."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        if household_id is None:
            payload = {"error": "household_id parameter is required."}
            out = json.dumps(payload)
            return out
        meal_plans = data.get("meal_plans", [])
        matching_plans = [
            plan for plan in meal_plans if plan.get("household_id") == household_id
        ]
        payload = matching_plans
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMealPlansByHouseholdId",
                "description": "Retrieves all meal plans for a specific household ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        }
                    },
                    "required": ["household_id"],
                },
            },
        }
