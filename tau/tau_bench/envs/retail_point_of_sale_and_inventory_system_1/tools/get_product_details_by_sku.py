# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductDetailsBySKU(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get('sku')
        products = list(data.get("products", {}).values())
        for product in products:
            if product.get("sku") == sku:
                return json.dumps(product)
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_details_by_sku",
                "description": "Retrieves all details for a product given its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                    },
                    "required": ["sku"],
                },
            },
        }
