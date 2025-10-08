from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class UpdateProductPrice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None, item_id: str = None, new_price: float = None) -> str:
        if not product_id or not item_id or new_price is None:
            payload = {"error": "product_id, item_id, and new_price are required"}
            out = json.dumps(
                payload)
            return out

        products = data["products"]
        product = next((p for p in products if p["product_id"] == product_id), None)

        if not product:
            payload = {"error": f"Product {product_id} not found"}
            out = json.dumps(payload)
            return out

        if item_id not in product["variants"]:
            payload = {"error": f"Item {item_id} not found in product {product_id}"}
            out = json.dumps(
                payload)
            return out

        old_price = product["variants"][item_id]["price"]
        product["variants"][item_id]["price"] = new_price
        payload = {
                "success": True,
                "product_id": product_id,
                "item_id": item_id,
                "old_price": old_price,
                "new_price": new_price,
                "updated_at": get_current_timestamp(),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateProductPrice",
                "description": "Update the price of a specific product variant.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string", "description": "Product ID"},
                        "item_id": {
                            "type": "string",
                            "description": "Variant ID to update price for",
                        },
                        "new_price": {
                            "type": "number",
                            "description": "New price for the variant",
                        },
                    },
                    "required": ["product_id", "item_id", "new_price"],
                },
            },
        }
