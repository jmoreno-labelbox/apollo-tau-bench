# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductDetails(Tool):
    """Retrieve product details from products.json by product_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_id: str) -> str:
        products = list(data.get("products", {}).values())
        for product in products:
            if product.get("product_id") == product_id:
                return json.dumps(product)
        return json.dumps({"error": "Product not found", "product_id": product_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get product details by product_id from products.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"}
                    },
                    "required": ["product_id"]
                }
            }
        }
