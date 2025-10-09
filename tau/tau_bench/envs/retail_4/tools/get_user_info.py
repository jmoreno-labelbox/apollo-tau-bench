from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetUserInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        """
        Get basic user information
        Data Sources: users.json (user_id, name, email, address)
        """
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        payload = {
            "status": "success",
            "user_id": user_id,
            "name": user.get("name", {}),
            "email": user.get("email", ""),
            "address": user.get("address", {}),
            "total_orders": len(user.get("orders", [])),
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserInfo",
                "description": "Get basic user information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User identifier (e.g., 'liam_wilson_6720')",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
