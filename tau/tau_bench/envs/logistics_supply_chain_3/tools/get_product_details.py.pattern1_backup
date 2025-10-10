# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductDetails(Tool):
    """Finds a product's details by its sku."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        products = data.get("product_master", [])
        for product in products:
            if product.get("sku") == sku:
                return json.dumps(product)
        return json.dumps({"error": "Product not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Finds all product details from product_master by its sku",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The sku of the product.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
