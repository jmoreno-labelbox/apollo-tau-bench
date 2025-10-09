from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindProductByName(Tool):
    """Locates a product's SKU and additional details using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], product_name: str = None) -> str:
        products = data.get("product_master", [])
        for product in products:
            if product.get("product_name") == product_name:
                payload = {
                    "sku": product.get("sku"),
                    "unit_price": product.get("unit_price"),
                    "weight_kg": product.get("weight_kg"),
                    "hazmat_information": product.get("hazmat_information"),
                    "country_of_origin": product.get("country_of_origin"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindProductByName",
                "description": "Finds a product's SKU, price, weight, and hazmat information by its full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {
                            "type": "string",
                            "description": "The full name of the product.",
                        }
                    },
                    "required": ["product_name"],
                },
            },
        }
