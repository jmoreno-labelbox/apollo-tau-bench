from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetVariantDetails(Tool):
    """Fetch a variant (using item_id) from products.json."""

    @staticmethod
    def invoke(data: dict[str, Any], item_id: str) -> str:
        products = data.get("products", [])
        for product in products:
            variants = product.get("variants", {})
            var = variants.get(item_id)
            if var:
                result = {"product_id": product.get("product_id"), "variant": var}
                payload = result
                out = json.dumps(payload)
                return out
        payload = {"error": "Variant not found", "item_id": item_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetVariantDetails",
                "description": "Get variant details by item_id from products.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"item_id": {"type": "string"}},
                    "required": ["item_id"],
                },
            },
        }
