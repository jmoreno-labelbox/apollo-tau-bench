from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserOrders(Tool):
    """Fetch the list of order IDs associated with a specific user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        users = data.get("users", [])
        for user in users:
            if user.get("user_id") == user_id:
                payload = {"orders": user.get("orders", [])}
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found", "user_id": user_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserOrders",
                "description": "Get order IDs linked to a given user_id from users.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
