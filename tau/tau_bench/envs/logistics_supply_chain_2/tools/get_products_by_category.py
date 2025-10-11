# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductsByCategory(Tool):
    """Tool to retrieve products by category name."""

    @staticmethod
    def invoke(data: Dict[str, Any], category = "", list_of_ids = None) -> str:
        category = category.lower()
        list_of_products = list_of_ids
        products = list(data.get("product_master", {}).values())
        result = [p['sku'] for p in products if p["category"].lower() == category]
        if list_of_products:
            result = [r for r in result if r in list_of_products]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_products_by_category",
                "description": "Get all products that belong to a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Category name (e.g., 'Pharmaceuticals')"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of products to choose from."
                        }
                    },
                    "required": ["category"]
                }
            }
        }
