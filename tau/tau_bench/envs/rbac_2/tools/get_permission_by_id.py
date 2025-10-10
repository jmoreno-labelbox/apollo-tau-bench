# Copyright held by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPermissionById(Tool):
    """ Get the full details of a specific permission using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], permission_id) -> str:
        try:
            permissions = list(data.get('permissions', {}).values())
        except (KeyError, json.JSONDecodeError):
            permissions = []

        for perm in permissions:
            if perm.get("permission_id") == permission_id:
                return json.dumps(perm)

        return json.dumps({"error": f"Permission with ID '{permission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permission_by_id",
                "description": "Retrieves the full details of a specific permission (action, resource_id) using its unique permission_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The unique ID of the permission to retrieve (e.g., 'P-021')."
                        }
                    },
                    "required": ["permission_id"]
                }
            }
        }
