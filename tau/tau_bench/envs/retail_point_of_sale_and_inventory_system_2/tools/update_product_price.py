# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProductPrice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, new_price: float) -> str:
        products = list(data.get("products", {}).values())
        for i, product in enumerate(products):
            if product.get("sku") == sku:
                products[i]["price"] = new_price
                return json.dumps(products[i], indent=2)
                return json.dumps({"error": f"Product with SKU {sku} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_product_price",
                "description": "Update the price for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU to update."},
                        "new_price": {"type": "number", "description": "New product price."}
                    },
                    "required": ["sku", "new_price"]
                }
            }
        }
