from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateUserAddress(Tool):
    """Modify the user's address in users.json using user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, address: dict[str, Any]) -> str:
        users = data.get("users", [])
        for user in users:
            if user.get("user_id") == user_id:
                user["address"] = address
                payload = {"status": "success", "user_id": user_id, "address": address}
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
                "name": "UpdateUserAddress",
                "description": "Update a user's address in users.json by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "address": {
                            "type": "object",
                            "description": "Full address object with address1, address2, city, country, state, zip",
                        },
                    },
                    "required": ["user_id", "address"],
                },
            },
        }
