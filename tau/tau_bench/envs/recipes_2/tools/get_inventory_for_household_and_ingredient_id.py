from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetInventoryForHouseholdAndIngredientId(Tool):
    """Fetches all stock items for a specific household ID and a particular ingredient ID."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None, ingredient_id: str = None) -> str:
        if household_id is None or ingredient_id is None:
            payload = {"error": "household_id and ingredient_id parameters are required."}
            out = json.dumps(payload)
            return out

        inventory = data.get("inventory_items", [])

        household_ingredient_inventory = [
            item
            for item in inventory
            if item.get("household_id") == household_id
            and item.get("ingredient_id") == ingredient_id
        ]
        payload = household_ingredient_inventory
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "description": "Retrieves inventory items for a specific household and ingredient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {
                            "type": "integer",
                            "description": "The unique ID of the household.",
                        },
                        "ingredient_id": {
                            "type": "integer",
                            "description": "The unique ID of the ingredient to find in the inventory.",
                        },
                    },
                    "required": ["household_id", "ingredient_id"],
                },
            },
        }
