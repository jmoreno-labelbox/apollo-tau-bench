from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ListAllProducts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], limit: int | None = None) -> str:
        products = data.get("products", [])
        if limit:
            products = products[:limit]
        payload = {"products": products, "count": len(products)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAllProducts",
                "description": "List all products with optional limit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "limit": {
                            "type": "integer",
                            "description": "Optional: Maximum number of products to return.",
                        }
                    },
                    "required": [],
                },
            },
        }
