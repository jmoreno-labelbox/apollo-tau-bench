from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: int, status_enum: str) -> str:
        orders = _get_table(data, "orders")
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return _error("order not found")
        # basic valid transitions: placed -> delivered permitted, delivered unchangeable
        if order.get("status_enum") == "delivered" and status_enum != "delivered":
            return _error("illegal status transition")
        order["status_enum"] = status_enum
        payload = {"order_id": order_id, "status_enum": status_enum}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetOrderStatus",
                "description": "Sets the status_enum of an order with basic legal transition checks.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                    },
                    "required": ["order_id", "status_enum"],
                },
            },
        }
