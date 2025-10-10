# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAllProducts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], limit: Optional[int] = None) -> str:
        products = list(data.get("products", {}).values())
        if limit:
            products = products[:limit]
        return json.dumps({"products": products, "count": len(products)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_all_products",
                "description": "List all products with optional limit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "limit": {"type": "integer", "description": "Optional: Maximum number of products to return."}
                    },
                    "required": []
                }
            }
        }
