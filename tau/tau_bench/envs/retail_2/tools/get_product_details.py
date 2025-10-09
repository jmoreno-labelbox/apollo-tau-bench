from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetProductDetails(Tool):
    """Obtain product information from products.json using product_id."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("product_id") == product_id:
                payload = product
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductDetails",
                "description": "Get product details by product_id from products.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"product_id": {"type": "string"}},
                    "required": ["product_id"],
                },
            },
        }
