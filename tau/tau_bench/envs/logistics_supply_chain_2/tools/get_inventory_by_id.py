from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetInventoryById(Tool):
    """Utility for obtaining an inventory item using its inventory ID."""

    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None) -> str:
        inventories = data.get("inventory", {}).values()
        for item in inventories:
            if item["inventory_id"] == inventory_id:
                payload = item
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Inventory with ID {inventory_id} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryById",
                "description": "Retrieve inventory item details using inventory ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Inventory ID (e.g., 'INV-0008').",
                        }
                    },
                    "required": ["inventory_id"],
                },
            },
        }
