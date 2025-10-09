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

class SearchUsers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, user_id: Any = None, name: Any = None, research_field: Any = None, availability: Any = None, institution: Any = None) -> str:
        """
        Conducts a user search.
        - If 'user_id' is supplied, it returns the information for that particular user.
        - If not, it filters users based on 'name' and/or 'research_field'.
        - If no arguments are given, it returns all users.
        """
        users = data.get("users", [])

        # When a user_id is given, it takes precedence and retrieves a specific user.
        if user_id:
            for user in users:
                if user.get("person_id") == user_id:
                    payload = user
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"User with ID '{user_id}' not found."}
            out = json.dumps(payload)
            return out

        # In the absence of a user_id, it performs a search using other criteria and returns a collection.
        if not name and not research_field:
            payload = users
            out = json.dumps(payload, indent=2)
            return out

        results = [
            user
            for user in users
            if (not name or name.lower() in user.get("label", "").lower())
            and (
                not research_field
                or research_field.lower() in user.get("study_field", "").lower()
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Provides the function schema intended for use by the language model.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchUsers",
                "description": "Searches for users by ID, name, or research field. If a user_id is provided, returns the details of that user. Otherwise, returns a list of users that match the other criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to retrieve details for.",
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
