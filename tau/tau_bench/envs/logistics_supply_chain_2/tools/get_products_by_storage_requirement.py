# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductsByStorageRequirement(Tool):
    """Tool to list products with specific storage requirements."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        keyword = kwargs.get("keyword", "").lower()
        list_of_products = kwargs.get("list_of_ids", None)
        products = list(data.get("product_master", {}).values())
        result = [p['sku'] for p in products if keyword in p.get("storage_requirements", "").lower()]
        if list_of_products:
            result = [r for r in result if r in list_of_products]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_products_by_storage_requirement",
                "description": "Filter products that have specific storage requirement keywords.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "Keyword for storage requirement (e.g., 'refrigerated')"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of products to choose from."
                        }
                    },
                    "required": ["keyword"]
                }
            }
        }
