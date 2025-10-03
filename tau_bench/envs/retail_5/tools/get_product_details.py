from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetProductDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None) -> str:
        if not product_id:
            payload = {"error": "product_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        product = next((p for p in products if p["product_id"] == product_id), None)

        if not product:
            payload = {"error": f"Product {product_id} not found"}
            out = json.dumps(payload)
            return out
        payload = product
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProductDetails",
                "description": "Get detailed information about a specific product including all variants.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "Product ID to get details for",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }
