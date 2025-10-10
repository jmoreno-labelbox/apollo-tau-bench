# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchProductsByCategory(Tool):
    """Searches for products with a specific category."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        products = list(data.get("dim_product", {}).values())
        matching_products = []
        
        for product in products:
            if product.get("category") == category:
                matching_products.append(product.get("product_id"))
        
        return json.dumps({"product_ids": matching_products})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_products_by_category",
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
