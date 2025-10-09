from tau_bench.envs.tool import Tool
import json
from typing import Any
from tau_bench.envs.retail_1.tools import _match




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserIdFromFullNameAndZip(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], first_name: str, last_name: str, zip: str) -> str:
        pass
        db = _convert_db_to_list(data.get("users", {}).values())
        filter_params = {
            "name": {"first_name": first_name, "last_name": last_name},
            "address": {"zip": zip},
        }
        user = [row for row in db.values() if _match(row, filter_params)]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        return (
            json.dumps(user[0]["user_id"])
            if user
            else json.dumps({"error": "User not found"})
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserIdFromFullNameAndZip",
                "description": "Retrieve user information by user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The user's first name.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The user's last name.",
                        },
                        "zip": {
                            "type": "string",
                            "description": "The user's zip code.",
                        },
                    },
                    "required": ["first_name", "last_name", "zip"],
                },
            },
        }
