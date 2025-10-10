# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetVariantDetails(Tool):
    """Retrieve a variant (by item_id) from products.json."""

    @staticmethod
    def invoke(data: Dict[str, Any], item_id: str) -> str:
        products = list(data.get("products", {}).values())
        for product in products:
            variants = product.get("variants", {})
            var = variants.get(item_id)
            if var:
                result = {"product_id": product.get("product_id"), "variant": var}
                return json.dumps(result)
        return json.dumps({"error": "Variant not found", "item_id": item_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_variant_details",
                "description": "Get variant details by item_id from products.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"}
                    },
                    "required": ["item_id"]
                }
            }
        }
