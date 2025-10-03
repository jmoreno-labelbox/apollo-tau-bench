from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetProductDetailsBySKU(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("sku") == sku:
                payload = product
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
                "name": "GetProductDetailsBySku",
                "description": "Get detailed information about a product by its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Stock Keeping Unit (SKU) of the product.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
