# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHazmatProducts(Tool):
    """Tool to list all hazardous material products."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        products = list(data.get("product_master", {}).values())
        list_of_products = kwargs.get("list_of_ids", None)
        result = [p['sku'] for p in products if p.get("hazmat_information", {}).get("is_hazmat")]
        if list_of_products:
            result = [r for r in result if r in list_of_products]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hazmat_products",
                "description": "List all products classified as hazardous materials.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of products to choose from."
                        }
                    }
                }
            }
        }
