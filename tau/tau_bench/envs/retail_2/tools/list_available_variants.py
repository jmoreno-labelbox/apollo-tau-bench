# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAvailableVariants(Tool):
    """List available variants for a product."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_id: str) -> str:
        products = list(data.get("products", {}).values())
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                available = [v for v in variants.values() if v.get("available") is True]
                return json.dumps({"product_id": product_id, "available_variants": available})
        return json.dumps({"error": "Product not found", "product_id": product_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_available_variants",
                "description": "List variants with available=true for a given product_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"}
                    },
                    "required": ["product_id"]
                }
            }
        }
