# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProduct(Tool):
    """Tool to update product details."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        updates = kwargs.get("updates")
        products = data.get("product_master", [])

        for product in products:
            if product["sku"] == sku:
                product.update(updates)
                return json.dumps({"success": f"product {sku} updated"}, indent=2)
        return json.dumps({"error": f"sku {sku} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_product",
                "description": "Update product by SKU",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "The SKU to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["sku", "updates"]
                }
            }
        }
