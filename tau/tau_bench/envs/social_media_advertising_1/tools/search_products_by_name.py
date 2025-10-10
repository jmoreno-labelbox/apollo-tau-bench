# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchProductsByName(Tool):
    """Searches for products with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], name_query) -> str:
        products = list(data.get("dim_product", {}).values())
        matching_products = []
        
        for product in products:
            if name_query.lower() in product.get("name", "").lower():
                matching_products.append(product.get("product_id"))
        
        return json.dumps({"product_ids": matching_products})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_products_by_name",
                "description": "Searches for products with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in product names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
