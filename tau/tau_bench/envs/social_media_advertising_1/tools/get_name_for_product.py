from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetNameForProduct(Tool):
    """Fetches the name of a specific product."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None) -> str:
        products = data.get("dim_product", {}).values()

        for product in products.values():
            if product.get("product_id") == product_id:
                payload = {"name": product.get("name")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Product with ID '{product_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getNameForProduct",
                "description": "Retrieves the name for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the product.",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }
