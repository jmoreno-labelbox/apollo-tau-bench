# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRoleDetailsById(Tool):
    """ Find a specific role using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], role_id) -> str:
        try:
            roles = list(data.get('roles', {}).values())
        except:
            roles = []

        for role in roles:
            if role.get("role_id") == role_id:
                return json.dumps(role)

        return json.dumps({"error": f"Role with ID '{role_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_details_by_id",
                "description": "Retrieves the full details of a specific role by providing its unique role_id (e.g., 'ROL-013').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The unique identifier of the role to retrieve (e.g., 'ROL-011')."
                        }
                    },
                    "required": ["role_id"]
                }
            }
        }
