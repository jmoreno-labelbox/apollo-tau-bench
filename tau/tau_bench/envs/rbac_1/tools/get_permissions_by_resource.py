# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPermissionsByResource(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], resource_id) -> str:
        for res in data.get('resources', []):
            if res.get('resource_id') == resource_id:
                resource_id = res.get('resource_id')
                break
        if not resource_id:
            return json.dumps({"error": "Resource not found"})

        perms = []
        for perm in list(data.get('permissions', {}).values()):
            if perm.get('resource_id') == resource_id:
                perms.append(perm)
        return json.dumps(perms)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_permissions_by_resource",
                        "description": "Retrieves all permissions referencing a given resource.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "resource_id": {"type": "string"}
                                },
                                "required": ["resource_id"]
                        }
                }
        }
