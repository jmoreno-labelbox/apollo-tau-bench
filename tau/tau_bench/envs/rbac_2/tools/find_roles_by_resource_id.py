# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindRolesByResourceId(Tool):
    """ Finds all roles that grant permissions to a specific resource ID. """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id = kwargs.get("resource_id")
        try:
            role_permissions = data.get('role_permissions', [])
            permissions = list(data.get('permissions', {}).values())
        except:
            return json.dumps({"error": "Data files not found."})

        perm_ids_for_resource = {p["permission_id"] for p in permissions if p.get("resource_id") == resource_id}

        if not perm_ids_for_resource:
            return json.dumps([])

        role_ids_for_resource = {rp["role_id"] for rp in role_permissions if rp.get("permission_id") in perm_ids_for_resource}
        
        return json.dumps(list(role_ids_for_resource))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_roles_by_resource_id",
                "description": "Returns a list of role IDs that are associated with a given resource ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string", "description": "The ID of the resource to find associated roles for."}
                    },
                    "required": ["resource_id"]
                }
            }
        }
