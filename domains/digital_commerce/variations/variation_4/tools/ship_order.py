from tau_bench.envs.tool import Tool
import json
from typing import Any

class ShipOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        order_id = _sid(order_id)
        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if order.get("status") != "Processing":
            payload = {"error": "order not in Processing"}
            out = json.dumps(payload, indent=2)
            return out
        order["status"] = "Shipped"
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "shipOrder",
                "description": "Ship a Processing order: checks stock and decrements product inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
