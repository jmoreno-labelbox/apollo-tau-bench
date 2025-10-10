# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindResourcesByRoleId(Tool):
    """Finds all resource IDs that a specific role grants permissions to."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        try:
            role_permissions = data.get('role_permissions', [])
            permissions = list(data.get('permissions', {}).values())
        except:
            return json.dumps({"error": "Data files not found."})

        perm_ids_for_role = {
            rp["permission_id"] for rp in role_permissions if rp.get("role_id") == role_id
        }

        if not perm_ids_for_role:
            return json.dumps([])

        resource_ids = {
            p["resource_id"] for p in permissions if p.get("permission_id") in perm_ids_for_role
        }
        
        return json.dumps(list(resource_ids))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_resources_by_role_id",
                "description": "Returns a list of all unique resource IDs that a specific role has permissions for.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "The ID of the role to find associated resources for."}
                    },
                    "required": ["role_id"]
                }
            }
        }
