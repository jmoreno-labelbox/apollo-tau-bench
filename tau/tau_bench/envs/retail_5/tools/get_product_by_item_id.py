from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetProductByItemId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None) -> str:
        if not item_id:
            payload = {"error": "item_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]

        # Examine all products to identify which one includes this item_id
        for product in products.values():
            if item_id in product["variants"]:
                product["variants"][item_id]
                payload = {
                    "product_id": product["product_id"],
                    "product_name": product["name"],
                    "supplier_id": product["supplier_id"],
                    "item_id": item_id,
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"Item ID {item_id} not found in any product"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProductByItemId",
                "description": "Find the product ID and details given a specific item ID (variant ID).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "Item ID (variant ID) to search for",
                        }
                    },
                    "required": ["item_id"],
                },
            },
        }
