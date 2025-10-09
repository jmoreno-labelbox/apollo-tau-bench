from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListRoles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        roles = data.get("roles", [])
        payload = {"roles": roles}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRoles",
                "description": "Lists all available roles in the system.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
