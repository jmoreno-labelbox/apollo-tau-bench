from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateOrderStatus(Tool):
    """Update the order status to the given value."""

    @staticmethod
    def invoke(data, order_id=None, status=None) -> str:
        if not order_id or status is None:
            payload = {"error": "order_id and status are required"}
            out = json.dumps(payload, indent=2)
            return out
        o = _find_order(data, order_id)
        if not o:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        o["status"] = status
        payload = {"success": True, "order_id": order_id, "status": status}
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
                "name": "updateOrderStatus",
                "description": "Update the status field on an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["order_id", "status"],
                },
            },
        }
