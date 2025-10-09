from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProductsByCategory(Tool):
    """Utility for fetching products based on their category name."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = "", list_of_ids: list = None) -> str:
        category = category.lower()
        list_of_products = list_of_ids
        products = data.get("product_master", {}).values()
        result = [p["sku"] for p in products.values() if p["category"].lower() == category]
        if list_of_products:
            result = [r for r in result.values() if r in list_of_products]
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
