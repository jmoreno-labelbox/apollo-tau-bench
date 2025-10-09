from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindUsers(Tool):
    """
    Utility for finding users by name or research area, or retrieving details of a specific user by their ID.
    This utility supersedes GetUserDetails.
    """

    @staticmethod
    def invoke(data: dict[str, Any], *, user_id: Any = None, name: Any = None, research_field: Any = None, availability: Any = None, institution: Any = None) -> str:
        user_id = user_id
        name = name
        research_field = research_field

        users = data.get("users", [])

        if user_id:
            for user in users:
                if user.get("person_id") == user_id:
                    payload = user
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"User with ID '{user_id}' not found."}
            out = json.dumps(payload)
            return out

        if not name and not research_field:
            payload = {
                    "error": "For a general search, 'name' or 'research_field' is required."
                }
            out = json.dumps(
                payload)
            return out

        results = [
            user
            for user in users
            if (not name or name.lower() in user.get("name", "").lower())
            and (
                not research_field
                or research_field.lower() in user.get("research_field", "").lower()
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUsers",
                "description": "Searches for users by name or research field, or retrieves a single user by their specific ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The specific ID of the user to retrieve.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the user to search for.",
                        },
                        "research_field": {
                            "type": "string",
                            "description": "The research field of the user.",
                        },
                    },
                },
            },
        }
