# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CancelOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, cancel_at: Any) -> str:
        if not order_id or not cancel_at:
            return _err("order_id and cancel_at are required.")
        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if _as_id(o.get("order_id")) == order_id), None)
        if not order:
            return _err("Order not found.")
        order["status"] = "Cancelled"
        order["cancelled_at"] = cancel_at
        return json.dumps({"order_id": order_id, "new_status": "Cancelled"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_order",
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
