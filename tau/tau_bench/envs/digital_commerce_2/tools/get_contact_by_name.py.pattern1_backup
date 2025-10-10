# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetContactByName(Tool):
    """Fetch a contact by exact first_name and last_name."""

    @staticmethod
    def invoke(data: Dict[str, Any], first_name: Any, last_name: Any) -> str:
        first_name = first_name
        last_name = last_name
        if not first_name or not last_name:
            return json.dumps(
                {"error": "Missing required field: first_name and/or last_name"}, indent=2
            )
        contacts = data.get("contacts", [])
        for contact in contacts:
            if contact.get("first_name") == first_name and contact.get("last_name") == last_name:
                return json.dumps(contact, indent=2)

        return json.dumps(
            {"error": f"No contact found with name '{first_name} {last_name}'"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_contact_by_name",
                "description": "Fetch a contact's full details by exact first_name and last_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "Exact first name of the contact.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Exact last name of the contact.",
                        },
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }
