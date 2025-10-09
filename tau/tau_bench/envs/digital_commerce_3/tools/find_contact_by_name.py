from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindContactByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], first_name: Any, last_name: Any) -> str:
        matches = [
            c
            for c in data.get("contacts", [])
            if c.get("first_name") == first_name and c.get("last_name") == last_name
        ]
        payload = matches[0] if matches else {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findContactByName",
                "description": "Returns contact by exact first and last name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }
