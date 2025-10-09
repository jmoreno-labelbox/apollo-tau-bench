from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetProductStock(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str) -> str:
        product_id = _sid(product_id)
        products = data.get("products", [])
        p = next((x for x in products if x.get("product_id") == product_id), None)
        if not p:
            payload = {"error": f"product {product_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"product_id": product_id, "stock_quantity": p.get("stock_quantity")}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductStock",
                "description": "Get current stock quantity for a product.",
                "parameters": {
                    "type": "object",
                    "properties": {"product_id": {"type": "string"}},
                    "required": ["product_id"],
                },
            },
        }
