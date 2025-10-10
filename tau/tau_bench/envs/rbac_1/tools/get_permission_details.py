# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPermissionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], permission_id, permission_name) -> str:

        if not permission_id and not permission_name:
            return json.dumps({"error": "Either permission_id or permission_name must be provided."})

        for permission in list(data.get('permissions', {}).values()):
            if permission_id and permission.get('permission_id') == permission_id:
                return json.dumps(permission)
            if permission_name and permission.get('action') == permission_name:
                return json.dumps(permission)

        return json.dumps({"error": "Permission not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_permission_details",
                        "description": "Retrieves the full details of a permission by its ID or name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "permission_id": {
                                                "type": "string",
                                                "description": "The ID of the permission to retrieve."
                                        },
                                        "permission_name": {
                                                "type": "string",
                                                "description": "The name (action) of the permission to retrieve."
                                        }
                                }
                        }
                }
        }
