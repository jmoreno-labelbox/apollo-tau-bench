from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetInventoryForHousehold(Tool):
    """Fetches all stock items for a specific household ID."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: str = None) -> str:
        inventory = data.get("inventory_items", [])
        household_inventory = [
            item for item in inventory if item.get("household_id") == household_id
        ]
        payload = household_inventory
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getInventoryForHousehold",
                "description": "Retrieves all inventory items for a given household ID.",
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
