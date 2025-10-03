from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class UpdateInventoryItemQuantity(Tool):
    """Modifies the amount of an item in the household stock."""

    @staticmethod
    def invoke(data: dict[str, Any], inv_item_id: str = None, new_quantity: int = None) -> str:
        inventory = data.get("inventory_items", [])
        for item in inventory:
            if item.get("inv_item_id") == inv_item_id:
                item["quantity"] = new_quantity
                payload = item
                out = json.dumps(payload)
                return out
        payload = {"error": f"Inventory item {inv_item_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryItemQuantity",
                "description": "Updates the quantity of an item in the household inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inv_item_id": {"type": "integer"},
                        "new_quantity": {"type": "number"},
                    },
                    "required": ["inv_item_id", "new_quantity"],
                },
            },
        }
