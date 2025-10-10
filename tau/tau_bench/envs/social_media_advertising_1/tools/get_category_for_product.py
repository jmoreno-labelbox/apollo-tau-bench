# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCategoryForProduct(Tool):
    """Retrieves the category for a specific product."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_id) -> str:
        products = list(data.get("dim_product", {}).values())
        
        for product in products:
            if product.get("product_id") == product_id:
                return json.dumps({"category": product.get('category')})
        
        return json.dumps({"error": f"Product with ID '{product_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_category_for_product",
                "description": "Retrieves the category for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the product.",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }
