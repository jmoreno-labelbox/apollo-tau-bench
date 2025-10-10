# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindProducts(Tool):
    """Tool to find products based on criteria."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
        brand: Optional[str] = None,
    ) -> str:
        """Execute the tool with given parameters."""
        products = data.get("product_master", [])
        results = []
        for product in products:
            if (not category or product.get("category") == category) and \
               (not subcategory or product.get("subcategory") == subcategory) and \
               (not brand or product.get("brand") == brand):
                results.append(product)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "find_products",
                "description": "Finds products based on category, subcategory, or brand.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string", "description": "The product category."},
                        "subcategory": {"type": "string", "description": "The product subcategory."},
                        "brand": {"type": "string", "description": "The product brand."},
                    },
                },
            },
        }
