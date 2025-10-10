# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPermissionByActionAndResource(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], action, resource_name) -> str:
        resource_id = None
        for res in data.get('resources', []):
            if res.get('name') == resource_name:
                resource_id = res.get('resource_id')
                break
        if not resource_id:
            return json.dumps({"error": "Resource not found"})

        for perm in list(data.get('permissions', {}).values()):
            if perm.get('action') == action and perm.get('resource_id') == resource_id:
                return json.dumps(perm)
        return json.dumps({"error": "Permission not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_permission_by_action_and_resource",
                        "description": "Retrieves a permission based on its action and resource.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "action": {"type": "string"},
                                        "resource_name": {"type": "string"}
                                },
                                "required": ["action", "resource_name"]
                        }
                }
        }
