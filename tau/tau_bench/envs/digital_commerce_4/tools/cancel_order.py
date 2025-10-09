from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CancelOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        order_id = _sid(order_id)
        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if order.get("status") == "Delivered":
            payload = {"error": "cannot cancel Delivered order"}
            out = json.dumps(payload, indent=2)
            return out
        order["status"] = "Cancelled"
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancelOrder",
                "description": "Cancel an order unless it is already Delivered.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
