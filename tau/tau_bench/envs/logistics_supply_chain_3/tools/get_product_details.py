from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetProductDetails(Tool):
    """Locates a product's information using its SKU."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        products = data.get("product_master", [])
        for product in products:
            if product.get("sku") == sku:
                payload = product
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductDetails",
                "description": "Finds all product details from product_master by its sku",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The sku of the product.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
