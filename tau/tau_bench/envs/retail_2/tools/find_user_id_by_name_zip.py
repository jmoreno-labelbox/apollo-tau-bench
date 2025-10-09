from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindUserIdByNameZip(Tool):
    """Locate a user_id using first name, last name, and ZIP code."""

    @staticmethod
    def invoke(data: dict[str, Any], first_name: str, last_name: str, zip: str) -> str:
        users = data.get("users", {}).values()
        for user in users.values():
            if (
                user.get("name", {}).values().get("first_name") == first_name
                and user.get("name", {}).values().get("last_name") == last_name
                and user.get("address", {}).values().get("zip") == zip
            ):
                payload = {"user_id": user.get("user_id")}
                out = json.dumps(payload)
                return out
        payload = {
                "error": "User not found",
                "first_name": first_name,
                "last_name": last_name,
                "zip": zip,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUserIdByNameZip",
                "description": "Find user_id from users.json by first name, last name, and ZIP code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "zip": {"type": "string"},
                    },
                    "required": ["first_name", "last_name", "zip"],
                },
            },
        }
