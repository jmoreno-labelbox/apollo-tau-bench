from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetRoleDetailsTool(Tool):
    """Retrieve information on a particular role."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        rid = role_id
        for r in data.get("roles", {}).values():
            if r["role_id"] == rid:
                payload = r
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Role {rid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleDetails",
                "description": "Get role_name, description, and is_temporary flag for a given role_id",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }
