# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHouseholdByUserId(Tool):
    """Retrieves household information for a given user ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        households = list(data.get("households", {}).values())
        for household in households:
            if household.get("primary_user_id") == user_id:
                return json.dumps(household)
        return json.dumps({"error": f"Household for user ID '{user_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_household_by_user_id",
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
