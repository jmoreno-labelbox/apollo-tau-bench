from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetProductsByCategory(Tool):
    """Utility for fetching products based on their category name."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = "", list_of_ids: list = None) -> str:
        category = category.lower()
        list_of_products = list_of_ids
        products = data.get("product_master", [])
        result = [p["sku"] for p in products if p["category"].lower() == category]
        if list_of_products:
            result = [r for r in result if r in list_of_products]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductsByCategory",
                "description": "Get all products that belong to a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Category name (e.g., 'Pharmaceuticals')",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of products to choose from.",
                        },
                    },
                    "required": ["category"],
                },
            },
        }
