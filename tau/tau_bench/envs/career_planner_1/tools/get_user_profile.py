from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        """Fetch the complete profile for a specified user ID."""
        users = data.get("users", [])
        user_profile = next((u for u in users if u.get("user_id") == user_id), None)

        if user_profile:
            payload = user_profile
            out = json.dumps(payload, indent=2)
            return out
        else:
            payload = {"error": f"User with ID {user_id} not found."}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetUserProfile",
                "description": "Retrieve the full profile of a user by their user ID, including their team ID, role, and manager.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID to retrieve the profile for.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
