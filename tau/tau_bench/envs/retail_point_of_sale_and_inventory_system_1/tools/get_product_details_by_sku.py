from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProductDetailsBySKU(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        products = data.get("products", {}).values()
        for product in products.values():
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
