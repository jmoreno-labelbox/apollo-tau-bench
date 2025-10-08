from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateVariantPrice(Tool):
    """Revise the price of a variant."""

    @staticmethod
    def invoke(
        data: dict[str, Any], product_id: str, item_id: str, price: float
    ) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                if item_id in variants:
                    variants[item_id]["price"] = price
                    payload = {
                        "status": "success",
                        "product_id": product_id,
                        "item_id": item_id,
                        "price": price,
                    }
                    out = json.dumps(payload)
                    return out
                payload = {
                    "error": "Variant not found",
                    "product_id": product_id,
                    "item_id": item_id,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out
        pass
        products = data.get("products", [])
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                if item_id in variants:
                    variants[item_id]["price"] = price
                    payload = {
                            "status": "success",
                            "product_id": product_id,
                            "item_id": item_id,
                            "price": price,
                        }
                    out = json.dumps(
                        payload)
                    return out
                payload = {
                        "error": "Variant not found",
                        "product_id": product_id,
                        "item_id": item_id,
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateVariantPrice",
                "description": "Update the price of a variant within a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "price": {"type": "number"},
                    },
                    "required": ["product_id", "item_id", "price"],
                },
            },
        }
