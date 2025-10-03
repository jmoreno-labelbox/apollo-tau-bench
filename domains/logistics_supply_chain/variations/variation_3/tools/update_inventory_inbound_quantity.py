from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class UpdateInventoryInboundQuantity(Tool):
    """Revises the inbound quantity for a particular product within a warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, warehouse_id: str = None, quantity_to_add: int = None) -> str:
        inventory_items = data.get("inventory", [])
        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                original_inbound = item.get("quantity_inbound", 0)
                item["quantity_inbound"] = original_inbound + quantity_to_add
                payload = {
                    "status": "success",
                    "inventory_id": item.get("inventory_id"),
                    "new_inbound_quantity": item["quantity_inbound"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Inventory record not found to update"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryInboundQuantity",
                "description": "Updates the inbound quantity for a specific product in a warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse.",
                        },
                        "quantity_to_add": {
                            "type": "integer",
                            "description": "The quantity to add to the inbound total.",
                        },
                    },
                    "required": ["sku", "warehouse_id", "quantity_to_add"],
                },
            },
        }
