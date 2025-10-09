from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetProductSkuByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_name: str = None) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("name") == product_name:
                payload = {"sku": product.get("sku")}
                out = json.dumps(payload)
                return out
        payload = {"sku": None}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductSkuByName",
                "description": "Retrieves the SKU (Stock Keeping Unit) for a given product name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {
                            "type": "string",
                            "description": "The full name of the product.",
                        },
                    },
                    "required": ["product_name"],
                },
            },
        }
