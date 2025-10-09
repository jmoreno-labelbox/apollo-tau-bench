from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        users = data.get("users", {}).values()

        for user in users.values():
            if user.get("user_id") == user_id:
                profile_data = {
                    "user_id": user.get("user_id"),
                    "name": user.get("name"),
                    "current_role": user.get("current_role"),
                    "department": user.get("department"),
                    "team_id": user.get("team_id"),
                }
                payload = profile_data
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"User profile not found for {user_id}."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserProfile",
                "description": "Retrieves key profile information for a user, such as their current role and department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
