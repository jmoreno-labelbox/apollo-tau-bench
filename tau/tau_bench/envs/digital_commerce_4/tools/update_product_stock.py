from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateProductStock(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str, delta: int) -> str:
        products = data.get("products", {}).values()
        ok = _adjust_stock(products, product_id, delta)
        if not ok:
            payload = {"error": "stock adjustment failed"}
            out = json.dumps(payload, indent=2)
            return out
        p = next((x for x in products.values() if x.get("product_id") == product_id), None)
        _append_audit(data, "UPDATE_STOCK", product_id, {"delta": delta})
        _ws_append(data, product_id, "UPDATE_STOCK", {"delta": delta})
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
                "name": "UpdateProductStock",
                "description": "Adjust product stock by delta (must not go negative). Appends deterministic audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "delta": {"type": "integer"},
                    },
                    "required": ["product_id", "delta"],
                },
            },
        }
