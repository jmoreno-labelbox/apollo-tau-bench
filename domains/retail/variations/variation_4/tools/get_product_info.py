from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetProductInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str) -> str:
        """
        Get basic product information by item ID
        Data Sources: products.json
        """
        products = data.get("products", [])
        for product in products:
            variants = product.get("variants", {})
            if item_id in variants:
                variant = variants[item_id]
                payload = {
                    "status": "success",
                    "item_id": item_id,
                    "product_id": product.get("product_id"),
                    "product_name": product.get("name"),
                    "price": variant.get("price"),
                    "available": variant.get("available"),
                    "options": variant.get("options", {}),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Item {item_id} not found", "status": "failed"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductInfo",
                "description": "Get basic product information by item ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "Product item identifier (e.g., 'ITEM12345')",
                        }
                    },
                    "required": ["item_id"],
                },
            },
        }
