# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], role_id) -> str:
        role_id_to_remove = role_id

        if not role_id_to_remove:
            return json.dumps({"error": "role_id must be provided."})

        roles = list(data.get('roles', {}).values())
        initial_roles_len = len(roles)
        updated_roles = [role for role in roles if role.get('role_id') != role_id_to_remove]

        if len(updated_roles) == initial_roles_len:
            return json.dumps({"error": "Role not found."})

        data['roles'] = updated_roles

        role_permissions = data.get('role_permissions', [])
        updated_role_permissions = [rp for rp in role_permissions if rp.get('role_id') != role_id_to_remove]
        data['role_permissions'] = updated_role_permissions

        user_roles = data.get('user_roles', [])
        updated_user_roles = [ur for ur in user_roles if ur.get('role_id') != role_id_to_remove]
        data['user_roles'] = updated_user_roles

        return json.dumps({"role_id": role_id_to_remove, "status": "removed"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "remove_role",
                        "description": "Deletes a role from the system, including all associated user and permission assignments.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {
                                                "type": "string",
                                                "description": "The ID of the role to be removed."
                                        }
                                },
                                "required": ["role_id"]
                        }
                }
        }
