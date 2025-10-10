# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddProduct(Tool):
    """Adds a new product."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id = kwargs.get("product_id")
        sku = kwargs.get("sku")
        name = kwargs.get("name")
        category = kwargs.get("category")

        if not product_id:
            return json.dumps({"error": "product_id is a required parameter."})
        if not sku:
            return json.dumps({"error": "sku is a required parameter."})
        if not name:
            return json.dumps({"error": "name is a required parameter."})
        if not category:
            return json.dumps({"error": "category is a required parameter."})

        new_product = {
            "product_id": product_id,
            "sku": sku,
            "name": name,
            "category": category
        }
        data['dim_product'] += [new_product]

        return json.dumps(
            {
                "status": "success",
                "message": f"New product was added: {new_product}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_product",
                "description": "Adds a new product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the new product.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the product.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the product (e.g., Electronics, Apparel).",
                        }
                    },
                    "required": ["product_id", "sku", "name", "category"],
                },
            },
        }
