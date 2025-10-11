# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePermission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], action, description, resource_id) -> str:
        permissions = list(data.get('permissions', {}).values())
        new_id_num = max((int(p['permission_id'][2:]) for p in permissions), default=0) + 1
        new_permission_id = f"P-{new_id_num:03d}"
        new_permission = {
                "permission_id": new_permission_id,
                "action": action,
                "resource_id": resource_id,
                "description": description
        }
        permissions.append(new_permission)
        data['permissions'] = permissions
        return json.dumps(new_permission)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_permission",
                        "description": "Creates a new permission.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "action": {
                                                "type": "string",
                                                "description": "The action the permission grants (e.g., read, write)."
                                        },
                                        "resource_id": {
                                                "type": "string",
                                                "description": "The ID of the resource this permission applies to."
                                        },
                                        "description": {
                                                "type": "string",
                                                "description": "A description of the permission."
                                        }
                                },
                                "required": ["action", "resource_id"]
                        }
                }
        }
