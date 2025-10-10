# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRolesByPermission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], permission_id) -> str:

        if not permission_id:
            return json.dumps({"error": "permission_id must be provided."})

        role_permissions = data.get('role_permissions', [])
        roles = list(data.get('roles', {}).values())

        matching_role_ids = {
                rp['role_id'] for rp in role_permissions
                if rp.get('permission_id') == permission_id
        }

        matching_roles = [
                role for role in roles
                if role.get('role_id') in matching_role_ids
        ]

        return json.dumps({"roles": matching_roles})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_roles_by_permission",
                        "description": "Retrieves a list of roles that have a specific permission assigned.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "permission_id": {
                                                "type": "string",
                                                "description": "The ID of the permission to look up."
                                        }
                                },
                                "required": ["permission_id"]
                        }
                }
        }
