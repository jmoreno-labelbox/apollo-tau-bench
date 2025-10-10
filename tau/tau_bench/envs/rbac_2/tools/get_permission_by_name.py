# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPermissionByName(Tool):
    """
    Find a specific permission using its action name. Can be filtered by a resource ID.
    If resource_id is omitted, it will return the first permission matching the name.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permission_name = kwargs.get("permission_name")
        resource_id = kwargs.get("resource_id") 
        try:
            permissions = list(data.get('permissions', {}).values())
        except (KeyError, json.JSONDecodeError):
            permissions = []

        for perm in permissions:
            if perm.get("action") == permission_name:
                if resource_id and perm.get("resource_id") != resource_id:
                    continue
                return json.dumps(perm)

        error_message = f"Permission '{permission_name}' not found."
        if resource_id:
            error_message += f" on resource '{resource_id}'"
            
        return json.dumps({"error": error_message})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permission_by_name",
                "description": "Retrieves the details of a specific permission by its action name (e.g., 'admin-db-cluster'). Can be optionally filtered by the resource it applies to.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_name": {
                            "type": "string",
                            "description": "The name of the action the permission allows (e.g., 'read-repo', 'admin-db-cluster')."
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Optional. The ID of the resource to filter by (e.g., 'RES-025')." 
                        }
                    },
                    "required": ["permission_name"] 
                }
            }
        }
