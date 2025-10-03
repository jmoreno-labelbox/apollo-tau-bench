from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SearchProducts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], query: str, category: str | None = None) -> str:
        _queryL = query or ''.lower()
        _categoryL = category or ''.lower()
        pass
        products = data.get("products", [])
        results = []

        for product in products:
            if query.lower() in product.get("name", "").lower():
                if category and product.get("category", "").lower() != category.lower():
                    continue
                results.append(product)
        payload = {"products": results, "count": len(results)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchProducts",
                "description": "Search for products by name and optional category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query for product name.",
                        },
                        "category": {
                            "type": "string",
                            "description": "Optional: Filter by product category.",
                        },
                    },
                    "required": ["query"],
                },
            },
        }
