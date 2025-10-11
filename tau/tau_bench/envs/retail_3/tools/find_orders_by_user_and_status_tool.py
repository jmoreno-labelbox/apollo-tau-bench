# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindOrdersByUserAndStatusTool(Tool):
    """
    Find orders filtered by user_id and optional status.

    Behavior:
    - If status is provided, filters orders with exact match.
    - Returns a compact listing: order_id, status, items_len, timestamp.

    Input (kwargs):
        user_id (str, required)
        status (str, optional)

    Output:
        JSON string with {"user_id","count","orders":[...]} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], status, user_id) -> str:

        if not user_id:
            return json.dumps({"error": "user_id is required"}, indent=2)

        orders = list(data.get("orders", {}).values())
        filtered = []
        for o in orders:
            if o.get("user_id") != user_id:
                continue
            if status and o.get("status") != status:
                continue
            filtered.append(
                {
                    "order_id": o.get("order_id"),
                    "status": o.get("status"),
                    "items_len": len(o.get("items", [])),
                    "timestamp": o.get("timestamp"),
                }
            )

        return json.dumps(
            {"user_id": user_id, "count": len(filtered), "orders": filtered}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_orders_by_user_and_status",
                "description": "Return orders for a given user_id, optionally filtered by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["user_id"],
                },
            },
        }
