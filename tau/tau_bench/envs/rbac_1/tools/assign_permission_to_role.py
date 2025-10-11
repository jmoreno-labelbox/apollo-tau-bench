# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignPermissionToRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], permission_id, role_id) -> str:
        role_permissions = data.get('role_permissions', [])
        assignment = {
                "role_id": role_id,
                "permission_id": permission_id
        }
        role_permissions.append(assignment)
        data['role_permissions'] = role_permissions
        return json.dumps(assignment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "assign_permission_to_role",
                        "description": "Assigns a permission to a role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {"type": "string"},
                                        "permission_id": {"type": "string"}
                                },
                                "required": ["role_id", "permission_id"]
                        }
                }
        }
