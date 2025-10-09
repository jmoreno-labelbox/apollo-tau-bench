from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateProductPrice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str, new_price: float) -> str:
        products = data.get("products", [])
        for i, product in enumerate(products):
            if product.get("sku") == sku:
                products[i]["price"] = new_price
                data["products"] = products
                payload = products[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Product with SKU {sku} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProductPrice",
                "description": "Update the price for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU to update.",
                        },
                        "new_price": {
                            "type": "number",
                            "description": "New product price.",
                        },
                    },
                    "required": ["sku", "new_price"],
                },
            },
        }
