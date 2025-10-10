# Copyright Sierra Inc.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserOrders(Tool):
    """Get list of order IDs for a given user_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        users = list(data.get("users", {}).values())
        for user in users:
            if user.get("user_id") == user_id:
                return json.dumps({"orders": user.get("orders", [])})
        return json.dumps({"error": "User not found", "user_id": user_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_orders",
                "description": "Get order IDs linked to a given user_id from users.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                    "required": ["user_id"]
                }
            }
        }
