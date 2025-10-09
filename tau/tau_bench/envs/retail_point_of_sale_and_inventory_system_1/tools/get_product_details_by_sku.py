from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class GetProductDetailsBySKU(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("sku") == sku:
                payload = product
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductDetailsBySku",
                "description": "Retrieves all details for a product given its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                    },
                    "required": ["sku"],
                },
            },
        }
