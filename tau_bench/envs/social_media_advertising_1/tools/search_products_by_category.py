from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SearchProductsByCategory(Tool):
    """Looks for products that belong to a certain category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None) -> str:
        products = data.get("dim_product", [])
        matching_products = []

        for product in products:
            if product.get("category") == category:
                matching_products.append(product.get("product_id"))
        payload = {"product_ids": matching_products}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchProductsByCategory",
                "description": "Searches for products with a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to search for (e.g., Electronics, Apparel, Home).",
                        }
                    },
                    "required": ["category"],
                },
            },
        }
