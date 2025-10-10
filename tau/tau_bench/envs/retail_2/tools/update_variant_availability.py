# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateVariantAvailability(Tool):
    """Change 'available' status for a variant."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_id: str, item_id: str, available: bool) -> str:
        products = list(data.get("products", {}).values())
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                if item_id in variants:
                    variants[item_id]["available"] = available
                    return json.dumps({"status": "success", "product_id": product_id, "item_id": item_id, "available": available})
                return json.dumps({"error": "Variant not found", "product_id": product_id, "item_id": item_id})
        return json.dumps({"error": "Product not found", "product_id": product_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_variant_availability",
                "description": "Update the 'available' flag for a variant within a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "available": {"type": "boolean"}
                    },
                    "required": ["product_id", "item_id", "available"]
                }
            }
        }
