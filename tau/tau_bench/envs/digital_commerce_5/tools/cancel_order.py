from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CancelOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, cancel_at: Any) -> str:
        order_id = _as_id(order_id)
        if not order_id or not cancel_at:
            return _err("order_id and cancel_at are required.")
        orders = data.get("orders", [])
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")
        order["status"] = "Cancelled"
        order["cancelled_at"] = cancel_at
        payload = {"order_id": order_id, "new_status": "Cancelled"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelOrder",
                "description": "Cancel an order at a deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "cancel_at": {"type": "string"},
                    },
                    "required": ["order_id", "cancel_at"],
                },
            },
        }
