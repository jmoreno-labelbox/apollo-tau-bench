from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class ExecuteInventoryTransfer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, quantity: int = None, from_store_id: int = None, to_store_id: int = None) -> str:
        inventory = data.get("inventory", [])
        from_item = None
        to_item = None

        for item in inventory:
            if item["store_id"] == from_store_id and item["sku"] == sku:
                from_item = item
            if item["store_id"] == to_store_id and item["sku"] == sku:
                to_item = item

        if from_item and to_item:
            from_item["quantity"] -= quantity
            to_item["quantity"] += quantity
            payload = {
                "status": "success",
                "sku": sku,
                "quantity": quantity,
                "from_store": from_store_id,
                "to_store": to_store_id,
            }
            out = json.dumps(payload)
            return out
        payload = {
            "status": "failed",
            "reason": "Inventory item not found in one or both stores.",
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExecuteInventoryTransfer",
                "description": "Executes a stock transfer of a specific SKU from one store to another.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to transfer.",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "The quantity of stock to transfer.",
                        },
                        "from_store_id": {
                            "type": "string",
                            "description": "The ID of the origin store.",
                        },
                        "to_store_id": {
                            "type": "string",
                            "description": "The ID of the destination store.",
                        },
                    },
                    "required": ["sku", "quantity", "from_store_id", "to_store_id"],
                },
            },
        }
