# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateVariantPrice(Tool):
    """Update price for a variant."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_id: str, item_id: str, price: float) -> str:
        products = list(data.get("products", {}).values())
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                if item_id in variants:
                    variants[item_id]["price"] = price
                    return json.dumps({"status": "success", "product_id": product_id, "item_id": item_id, "price": price})
                return json.dumps({"error": "Variant not found", "product_id": product_id, "item_id": item_id})
        return json.dumps({"error": "Product not found", "product_id": product_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_variant_price",
                "description": "Update the price of a variant within a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "price": {"type": "number"}
                    },
                    "required": ["product_id", "item_id", "price"]
                }
            }
        }
