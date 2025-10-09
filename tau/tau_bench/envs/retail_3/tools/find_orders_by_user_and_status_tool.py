from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindOrdersByUserAndStatusTool(Tool):
    """
    Locate orders filtered by user_id and optional status.

    Behavior:
    - If status is provided, filters orders for an exact match.
    - Returns a concise listing: order_id, status, items_len, timestamp.

    Input (kwargs):
        user_id (str, required)
        status (str, optional)

    Output:
        JSON string with {"user_id","count","orders":[...]} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, status: str = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", {}).values()
        filtered = []
        for o in orders.values():
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
        payload = {"user_id": user_id, "count": len(filtered), "orders": filtered}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindOrdersByUserAndStatus",
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
