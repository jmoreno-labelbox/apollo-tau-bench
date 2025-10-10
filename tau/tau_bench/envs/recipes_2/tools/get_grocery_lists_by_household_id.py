# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGroceryListsByHouseholdId(Tool):
    """Retrieves all grocery lists for a specific household ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            return json.dumps({"error": "household_id parameter is required."})

        grocery_lists = data.get("grocery_lists", [])
        
        matching_lists = [
            glist for glist in grocery_lists 
            if glist.get("household_id") == household_id
        ]
        
        return json.dumps(matching_lists)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grocery_lists_by_household_id",
                "description": "Retrieves all grocery lists for a specific household ID.",
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
