from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserPaymentMethods(Tool):
    """Enumerate all payment options for a specified user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        users = data.get("users", [])
        for user in users:
            if user.get("user_id") == user_id:
                payload = {"payment_methods": user.get("payment_methods", {})}
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
                "name": "GetUserPaymentMethods",
                "description": "Retrieve payment methods for a given user_id from users.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
