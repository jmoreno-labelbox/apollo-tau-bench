# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListProductsByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], category: str) -> str:
        products = list(data.get("products", {}).values())
        category_products = [p for p in products if p.get("category", "").lower() == category.lower()]
                return json.dumps({"products": category_products, "count": len(category_products), "category": category}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_products_by_category",
                "description": "List all products in a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string", "description": "Product category to filter by."}
                    },
                    "required": ["category"]
                }
            }
        }
