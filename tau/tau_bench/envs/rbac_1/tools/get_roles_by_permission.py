from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetRolesByPermission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None) -> str:
        if not permission_id:
            payload = {"error": "permission_id must be provided."}
            out = json.dumps(payload)
            return out

        role_permissions = data.get("role_permissions", {}).values()
        roles = data.get("roles", {}).values()

        matching_role_ids = {
            rp["role_id"]
            for rp in role_permissions.values() if rp.get("permission_id") == permission_id
        }

        matching_roles = [
            role for role in roles.values() if role.get("role_id") in matching_role_ids
        ]
        payload = {"roles": matching_roles}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRolesByPermission",
                "description": "Retrieves a list of roles that have a specific permission assigned.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the permission to look up.",
                        }
                    },
                    "required": ["permission_id"],
                },
            },
        }
