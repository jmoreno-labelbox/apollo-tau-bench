from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetHouseholdByUserId(Tool):
    """Obtains household details for a specified user ID."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        households = data.get("households", [])
        for household in households:
            if household.get("primary_user_id") == user_id:
                payload = household
                out = json.dumps(payload)
                return out
        payload = {"error": f"Household for user ID '{user_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHouseholdByUserId",
                "description": "Retrieves household information for a given user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "integer",
                            "description": "The unique ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
