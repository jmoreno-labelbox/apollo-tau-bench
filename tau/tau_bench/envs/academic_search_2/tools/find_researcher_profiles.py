from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindResearcherProfiles(Tool):
    """Looks for users based on their name, research area, user_id, or institution."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, research_field: str = None, user_id: str = None, institution: str = None) -> str:
        if not any([name, research_field, user_id, institution]):
            payload = data.get("users", {}).values()
            out = json.dumps(payload, indent=2)
            return out

        users = data.get("users", {}).values()
        results = [
            user
            for user in users.values() if (not name or name.lower() in user.get("name", "").lower())
            and (
                not research_field
                or research_field.lower() in user.get("research_field", "").lower()
            )
            and (not user_id or user.get("person_id") == user_id)
            and (not institution or institution.lower() in user.get("organization", "").lower())
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindResearcherProfiles",
                "description": "Searches for users by their name, research field, user_id, or institution.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "research_field": {"type": "string"},
                        "user_id": {"type": "string"},
                        "institution": {"type": "string"},
                    },
                },
            },
        }
