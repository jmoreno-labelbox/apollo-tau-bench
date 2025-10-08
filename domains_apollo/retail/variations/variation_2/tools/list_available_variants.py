from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListAvailableVariants(Tool):
    """Enumerate the variants available for a product."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                available = [v for v in variants.values() if v.get("available") is True]
                payload = {"product_id": product_id, "available_variants": available}
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAvailableVariants",
                "description": "List variants with available=true for a given product_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"product_id": {"type": "string"}},
                    "required": ["product_id"],
                },
            },
        }
