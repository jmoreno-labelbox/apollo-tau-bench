# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductSkuByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_name = kwargs.get('product_name')
        products = list(data.get("products", {}).values())
        for product in products:
            if product.get("name") == product_name:
                return json.dumps({"sku": product.get("sku")})
        return json.dumps({"sku": None})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_sku_by_name",
                "description": "Retrieves the SKU (Stock Keeping Unit) for a given product name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {
                            "type": "string",
                            "description": "The full name of the product.",
                        },
                    },
                    "required": ["product_name"],
                },
            },
        }
