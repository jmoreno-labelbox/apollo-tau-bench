from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListRolesTool(Tool):
    """Display roles, with an optional filter for temporary ones."""

    @staticmethod
    def invoke(data: dict[str, Any], is_temporary: bool = None) -> str:
        roles = data.get("roles", {}).values()
        if is_temporary is None:
            payload = roles
            out = json.dumps(payload, indent=2)
            return out
        payload = [r for r in roles.values() if r["is_temporary"] == is_temporary]
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRoles",
                "description": "List all roles optionally filtering by temporary flag",
                "parameters": {
                    "type": "object",
                    "properties": {"is_temporary": {"type": "boolean"}},
                },
            },
        }
