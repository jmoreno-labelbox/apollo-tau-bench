# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryForHousehold(Tool):
    """Retrieves all inventory items for a given household ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        inventory = data.get("inventory_items", [])
        household_inventory = [item for item in inventory if item.get("household_id") == household_id]
        return json.dumps(household_inventory)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_for_household",
                "description": "Retrieves all inventory items for a given household ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer", "description": "The unique ID of the household."}},
                    "required": ["household_id"],
                },
            },
        }
