# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateRoleDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_description, new_name, role_id) -> str:
        for role in list(data.get('roles', {}).values()):
            if role.get('role_id') == role_id:
                if new_name:
                    role['role_name'] = new_name
                if new_description:
                    role['description'] = new_description
                return json.dumps(role)
        return json.dumps({"error": "Role not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_role_details",
                        "description": "Updates the name and/or description of an existing role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {"type": "string"},
                                        "new_name": {"type": "string", "description": "The new name for the role."},
                                        "new_description": {"type": "string", "description": "The new description for the role."}
                                },
                                "required": ["role_id"]
                        }
                }
        }
