from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserEmailTool(Tool):
    """GetUserEmail"""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        users: list[dict[str, Any]] = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        out = {
            "user_id": user.get("user_id"),
            "username": user.get("username"),
            "email": user.get("email"),
            "status": user.get("status"),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserEmail",
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
