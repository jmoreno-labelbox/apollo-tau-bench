# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPermissionByResourceId(Tool):
    """Finds all permissions associated with a specific resource ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id_to_find = kwargs.get("resource_id")
        try:
            all_permissions = list(data.get('permissions', {}).values())
        except (KeyError, json.JSONDecodeError):
            return json.dumps([])

        matching_permissions = [
            perm for perm in all_permissions
            if perm.get("resource_id") == resource_id_to_find
        ]

        return json.dumps(matching_permissions)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permission_by_resource_id",
                "description": "Retrieves a list of all permissions that are directly associated with a specific resource ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource to find permissions for (e.g., 'RES-032')."
                        }
                    },
                    "required": ["resource_id"]
                }
            }
        }
