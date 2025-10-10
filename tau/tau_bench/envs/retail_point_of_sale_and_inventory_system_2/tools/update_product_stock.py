# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProductStock(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, new_stock_quantity: int) -> str:
        products = list(data.get("products", {}).values())

        for i, product in enumerate(products):
            if product.get("sku") == sku:
                products[i]["stock_quantity"] = new_stock_quantity
                return json.dumps(products[i], indent=2)
                return json.dumps({"error": f"Product with SKU {sku} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_product_stock",
                "description": "Update the stock quantity of an existing product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU to update."},
                        "new_stock_quantity": {"type": "integer", "description": "New stock quantity for the product."}
                    },
                    "required": ["sku", "new_stock_quantity"]
                }
            }
        }
