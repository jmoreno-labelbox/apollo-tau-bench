from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class ListProductsBySupplier(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None) -> str:
        if not supplier_id:
            payload = {"error": "supplier_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        supplier_products = [p for p in products.values() if p["supplier_id"] == supplier_id]
        payload = supplier_products
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listProductsBySupplier",
                "description": "Get all products supplied by a specific supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to get products for",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }
