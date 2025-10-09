from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetProductById(Tool):
    """Fetch a product using product_id."""

    @staticmethod
    def invoke(data, product_id: str = None) -> str:
        if not product_id:
            payload = {"error": "product_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        prod = next(
            (p for p in data.get("products", []) if p.get("product_id") == product_id),
            None,
        )
        payload = prod or {"error": f"product_id {product_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getProductById",
                "description": "Get a product by product_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"product_id": {"type": "string"}},
                    "required": ["product_id"],
                },
            },
        }
