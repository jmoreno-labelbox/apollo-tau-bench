from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any

class UpdateStockQuantity(Tool):
    """Tool for adjusting the quantity of a specific product, useful after restocks or in cases of missing or damaged inventory"""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        store_id: str = None,
        sku: str = None,
        quantity: int = None,
        relative_quantity: int = None
    ) -> str:
        if (
            (store_id is None)
            or (sku is None)
            or ((quantity is None) and (relative_quantity is None))
        ):
            payload = {"error": "store_id, sku, and quantity are required"}
            out = json.dumps(payload)
            return out

        if (quantity is not None) and (quantity < 0):
            payload = {"error": "quantity must be 0 or greater"}
            out = json.dumps(payload)
            return out

        inventory = data.get("inventory", [])

        for item in inventory:
            # Item that matches
            if (item["store_id"] == store_id) and (item["sku"] == sku):
                item["quantity"]

                # Revise the quantity
                if quantity is not None:
                    item["quantity"] = quantity
                else:
                    item["quantity"] += int(relative_quantity)

                # Modify the status
                if item["quantity"] <= item["safety_stock"]:
                    item["status"] = "critical"
                elif item["quantity"] <= item["reorder_level"]:
                    item["status"] = "low_stock"
                else:
                    item["status"] = "in_stock"
                payload = {"success": True}
                out = json.dumps(payload)
                return out
        payload = {"error": "No matching product was found at the store"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateStockQuantity",
                "description": "Updates the quantity of a product and sets the status based on the quantity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "timestamp for database operations",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The specific ID of the store for the item",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The specific sku for the item",
                        },
                        "quantity": {
                            "type": "int",
                            "description": "The quantity to set for the item. Overrides relative_quantity",
                        },
                        "relative_quantity": {
                            "type": "int",
                            "description": "Will add or remove this much from the current quantity: 5 will add 5 and -2 will remove 2",
                        },
                    },
                },
            },
        }
