from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class FetchUsers(Tool):
    """Utility for locating users by their ID, name, or research area."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, name: Any = None, research_field: Any = None, availability: Any = None, institution: Any = None) -> str:
        user_id = user_id
        name = name
        research_field = research_field

        users = data.get("users", [])

        if user_id:
            for user in users:
                if user.get("person_id") == user_id:
                    payload = [user]
                    out = json.dumps(payload, indent=2)
                    return out
            payload = []
            out = json.dumps(payload)
            return out

        if not name and not research_field:
            payload = {"error": "Either user_id, name, or research_field is required."}
            out = json.dumps(
                payload)
            return out

        results = []
        for user in users:
            match = True
            if name and name.lower() not in user.get("name", "").lower():
                match = False
            if (
                research_field
                and research_field.lower() not in user.get("research_field", "").lower()
            ):
                match = False
            if match:
                results.append(user)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchUsers",
                "description": "Searches for users by their name or research field.",
                "parameters": {
                    "type": "object",
                    "properties": {
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
