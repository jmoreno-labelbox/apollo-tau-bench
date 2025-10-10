# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteProduct(Tool):
    """Deletes a product."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id = kwargs.get("product_id")
        if not product_id:
            return json.dumps({"error": "product_id is a required parameter."})

        products = list(data.get("dim_product", {}).values())
        for product in products:
            if product.get("product_id") == product_id:
                data['dim_product'] = [d for d in data['dim_product'] if d['product_id'] != product_id]
                return json.dumps(
                    {
                        "status": "success",
                        "message": f"Product with id {product_id} deleted successfully",
                    }
                )

        return json.dumps({"error": f"Product with ID '{product_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_product",
                "description": "Deletes a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the product to delete.",
                        },
                    },
                    "required": ["product_id"],
                },
            },
        }
