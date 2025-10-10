# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        """
        Get basic user information
        Data Sources: users.json (user_id, name, email, address)
        """
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        return json.dumps({
            "status": "success",
            "user_id": user_id,
            "name": user.get("name", {}),
            "email": user.get("email", ""),
            "address": user.get("address", {}),
            "total_orders": len(user.get("orders", []))
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_info",
                "description": "Get basic user information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "User identifier (e.g., 'lucas_brown_6720')"}
                    },
                    "required": ["user_id"]
                }
            }
        }
