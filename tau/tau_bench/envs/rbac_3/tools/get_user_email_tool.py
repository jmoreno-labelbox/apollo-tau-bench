# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserEmailTool(Tool):
    """get_user_email"""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        if not user_id:
            return json.dumps({"error": "user_id is required"}, indent=2)

        users: List[Dict[str, Any]] = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found"}, indent=2)

        out = {
            "user_id": user.get("user_id"),
            "username": user.get("username"),
            "email": user.get("email"),
            "status": user.get("status"),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_email",
                "description": (
                    "Return the email address and username for a given user_id."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Unique user identifier (e.g., U-007)",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
