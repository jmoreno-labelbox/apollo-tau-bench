# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRolePermissions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], role_id) -> str:
        permission_ids = [
                rp['permission_id'] for rp in data.get('role_permissions', [])
                if rp.get('role_id') == role_id
        ]
        return json.dumps({"role_id": role_id, "permissions": permission_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_role_permissions",
                        "description": "Retrieves all permissions associated with a role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {"type": "string"}
                                },
                                "required": ["role_id"]
                        }
                }
        }
