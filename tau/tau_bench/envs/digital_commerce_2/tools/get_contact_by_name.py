from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetContactByName(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], first_name: Any = None, last_name: Any = None) -> str:
        if not first_name or not last_name:
            payload = {"error": "Missing required field: first_name and/or last_name"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        contacts = data.get("contacts", {}).values()
        for contact in contacts.values():
            if (
                contact.get("first_name") == first_name
                and contact.get("last_name") == last_name
            ):
                payload = contact
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No contact found with name '{first_name} {last_name}'"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetContactByName",
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
