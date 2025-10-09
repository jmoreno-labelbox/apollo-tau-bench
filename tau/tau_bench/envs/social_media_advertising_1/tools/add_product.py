from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddProduct(Tool):
    """Creates a new product."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None, sku: str = None, name: str = None, category: str = None) -> str:
        if not product_id:
            payload = {"error": "product_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not sku:
            payload = {"error": "sku is a required parameter."}
            out = json.dumps(payload)
            return out
        if not name:
            payload = {"error": "name is a required parameter."}
            out = json.dumps(payload)
            return out
        if not category:
            payload = {"error": "category is a required parameter."}
            out = json.dumps(payload)
            return out

        new_product = {
            "product_id": product_id,
            "sku": sku,
            "name": name,
            "category": category,
        }
        data["dim_product"] += [new_product]
        payload = {
                "status": "success",
                "message": f"New product was added: {new_product}",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addProduct",
                "description": "Adds a new product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the new product.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the product.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the product (e.g., Electronics, Apparel).",
                        },
                    },
                    "required": ["product_id", "sku", "name", "category"],
                },
            },
        }
