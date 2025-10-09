from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetRoleNameTool(Tool):
    """get_role_name
    Find a role using role_id and return its role_name and metadata.
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        if not role_id:
            payload = {"error": "role_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        roles: list[dict[str, Any]] = data.get("roles", {}).values()
        rec = next((r for r in roles if r.get("role_id") == role_id), None)
        if not rec:
            payload = {"error": f"Role {role_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        out = {
            "role_id": rec.get("role_id"),
            "role_name": rec.get("role_name"),
            "description": rec.get("description"),
            "is_temporary": rec.get("is_temporary"),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRoleName",
                "description": "Return role_name and metadata for a given role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Unique role identifier (e.g., ROL-001)",
                        }
                    },
                    "required": ["role_id"],
                },
            },
        }
