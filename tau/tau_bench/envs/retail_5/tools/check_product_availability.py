from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class CheckProductAvailability(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None, product_id: str = None) -> str:
        if not item_id and not product_id:
            payload = {"error": "Either item_id or product_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]

        if item_id:
            for product in products.values():
                for variant_id, variant in product["variants"].items():
                    if variant["item_id"] == item_id:
                        payload = {
                                "item_id": item_id,
                                "product_name": product["name"],
                                "available": variant["available"],
                                "price": variant["price"],
                                "options": variant["options"],
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
            payload = {"error": "Item not found"}
            out = json.dumps(payload)
            return out

        if product_id:
            product = next((p for p in products.values() if p["product_id"] == product_id), None)
            if not product:
                payload = {"error": "Product not found"}
                out = json.dumps(payload)
                return out

            available_variants = []
            for variant_id, variant in product["variants"].items():
                if variant["available"]:
                    available_variants.append(
                        {
                            "item_id": variant["item_id"],
                            "price": variant["price"],
                            "options": variant["options"],
                        }
                    )
            payload = {
                    "product_id": product_id,
                    "product_name": product["name"],
                    "available_variants": available_variants,
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
                "name": "checkProductAvailability",
                "description": "Check availability of a specific product variant or all variants of a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "Specific item ID to check",
                        },
                        "product_id": {
                            "type": "string",
                            "description": "Product ID to check all variants",
                        },
                    },
                },
            },
        }
