# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductDetailsBySKU(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str) -> str:
        products = list(data.get("products", {}).values())
        for product in products:
            if product.get("sku") == sku:
                return json.dumps(product, indent=2)
                return json.dumps({"error": f"Product with SKU {sku} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_details_by_sku",
                "description": "Get detailed information about a product by its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Stock Keeping Unit (SKU) of the product."}
                    },
                    "required": ["sku"]
                }
            }
        }
