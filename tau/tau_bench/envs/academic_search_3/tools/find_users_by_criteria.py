from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FindUsersByCriteria(Tool):
    """Utility for locating users based on different criteria."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, name: Any = None, research_field: Any = None, availability: Any = None, institution: Any = None) -> str:
        users = data.get("users", [])
        results = []
        for user in users:
            match = True
            if user_id and user_id != user.get("person_id"):
                match = False
            if name and name.lower() not in user.get("name", "").lower():
                match = False
            if research_field and research_field.lower() not in user.get("research_field", "").lower():
                match = False
            if availability and availability != user.get("availability"):
                match = False
            if institution and institution == user.get("institution"):
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
                "name": "FindUsersByCriteria",
                "description": "Finds researchers by ID, name, research field, availability, or to exclude an institution.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the user.",
                        },
                        "research_field": {
                            "type": "string",
                            "description": "A research field to filter by.",
                        },
                        "availability": {
                            "type": "string",
                            "description": "The availability status (e.g., 'available').",
                        },
                        "institution": {
                            "type": "string",
                            "description": "Excludes users who belong to this institution.",
                        },
                    },
                    "required": [],
                },
            },
        }
