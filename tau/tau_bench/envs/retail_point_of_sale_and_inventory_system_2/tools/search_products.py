# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchProducts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], query: str, category: Optional[str] = None) -> str:
        products = list(data.get("products", {}).values())
        results = []

        for product in products:
            if query.lower() in product.get("name", "").lower():
                if category and product.get("category", "").lower() != category.lower():
                    continue
                results.append(product)
                return json.dumps({"products": results, "count": len(results)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_products",
                "description": "Search for products by name and optional category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query for product name."},
                        "category": {"type": "string", "description": "Optional: Filter by product category."}
                    },
                    "required": ["query"]
                }
            }
        }
