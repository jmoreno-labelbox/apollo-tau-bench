# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_stock_quantity(Tool):
    """
    Tool to set the quantity of a certain product. This can be used after restocks or to handle cases where inventory is missing or damaged
    """

    @staticmethod
    def invoke(data: Dict[str, Any], quantity, relative_quantity, sku, store_id, timestamp) -> str:

        if (
            (store_id is None)
            or (sku is None)
            or ((quantity is None) and (relative_quantity is None))
        ):
            return json.dumps({"error": "store_id, sku, and quantity are required"})

        if (quantity is not None) and (quantity < 0):
            return json.dumps({"error": "quantity must be 0 or greater"})

        inventory = list(data.get("inventory", {}).values())

        for item in inventory:
            # Corresponding element
            if (item["store_id"] == store_id) and (item["sku"] == sku):
                former_quantity = item["quantity"]

                # Modify the amount.
                if quantity is not None:
                    item["quantity"] = quantity
                else:
                    item["quantity"] += int(relative_quantity)

                # Revise the status.
                if item["quantity"] <= item["safety_stock"]:
                    item["status"] = "critical"
                elif item["quantity"] <= item["reorder_level"]:
                    item["status"] = "low_stock"
                else:
                    item["status"] = "in_stock"

                return json.dumps({"success": True})

        return json.dumps({"error": "No matching product was found at the store"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_stock_quantity",
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
                            "type": "integer",
                            "description": "The quantity to set for the item. Overrides relative_quantity",
                        },
                        "relative_quantity": {
                            "type": "integer",
                            "description": "Will add or remove this much from the current quantity: 5 will add 5 and -2 will remove 2",
                        },
                    },
                },
            },
        }
