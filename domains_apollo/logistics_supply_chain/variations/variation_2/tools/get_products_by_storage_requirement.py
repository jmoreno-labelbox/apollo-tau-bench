from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetProductsByStorageRequirement(Tool):
    """Utility for compiling a list of products that have particular storage needs."""

    @staticmethod
    def invoke(data: dict[str, Any], keyword: str = "", list_of_ids: list = None) -> str:
        keyword = keyword.lower()
        list_of_products = list_of_ids
        products = data.get("product_master", [])
        result = [
            p["sku"]
            for p in products
            if keyword in p.get("storage_requirements", "").lower()
        ]
        if list_of_products:
            result = [r for r in result if r in list_of_products]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductsByStorageRequirement",
                "description": "Filter products that have specific storage requirement keywords.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "Keyword for storage requirement (e.g., 'refrigerated')",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of products to choose from.",
                        },
                    },
                    "required": ["keyword"],
                },
            },
        }
