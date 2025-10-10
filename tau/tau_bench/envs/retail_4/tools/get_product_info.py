# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_id: str) -> str:
        """
        Get basic product information by item ID
        Data Sources: products.json
        """
        products = list(data.get("products", {}).values())
        for product in products:
            variants = product.get("variants", {})
            if item_id in variants:
                variant = variants[item_id]
                return json.dumps({
                    "status": "success",
                    "item_id": item_id,
                    "product_id": product.get("product_id"),
                    "product_name": product.get("name"),
                    "price": variant.get("price"),
                    "available": variant.get("available"),
                    "options": variant.get("options", {})
                })

        return json.dumps({"error": f"Item {item_id} not found", "status": "failed"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_info",
                "description": "Get basic product information by item ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string", "description": "Product item identifier (e.g., 'ITEM12345')"}
                    },
                    "required": ["item_id"]
                }
            }
        }
