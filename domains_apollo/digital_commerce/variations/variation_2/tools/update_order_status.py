from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class UpdateOrderStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, new_status: Any) -> str:
        order_id = _idstr(order_id)
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                order["status"] = new_status
                payload = order
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No order found with ID '{order_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOrderStatus",
                "description": "Update the status of an existing order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Exact order ID to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status to set for the order (e.g., Processing, Shipped, Delivered).",
                        },
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }
