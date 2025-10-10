# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindProductByName(Tool):
    """Finds a product's SKU and other details by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_name = kwargs.get("product_name")
        products = list(data.get("product_master", {}).values())
        for product in products:
            if product.get("product_name") == product_name:
                return json.dumps(
                    {
                        "sku": product.get("sku"),
                        "unit_price": product.get("unit_price"),
                        "weight_kg": product.get("weight_kg"),
                        "hazmat_information": product.get("hazmat_information"),
                        "country_of_origin": product.get("country_of_origin"),
                    }
                )
        return json.dumps({"error": "Product not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_product_by_name",
                "description": "Finds a product's SKU, price, weight, and hazmat information by its full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {
                            "type": "string",
                            "description": "The full name of the product.",
                        }
                    },
                    "required": ["product_name"],
                },
            },
        }
