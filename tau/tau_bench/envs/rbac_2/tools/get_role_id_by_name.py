# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRoleIdByName(Tool):
    """
    Finds one or more roles by searching for a name. It prioritizes an exact match
    but will also return other roles that contain the search string.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], role_name) -> str:
        find_role_name = role_name
        try:
            roles = list(data.get('roles', {}).values())
        except (KeyError, json.JSONDecodeError):
            roles = []

        exact_matches = []
        partial_matches = []

        for role in roles:
            current_role_name = role.get("role_name", "")
            
            if current_role_name == find_role_name:
                exact_matches.append(role)
            elif find_role_name in current_role_name:
                partial_matches.append(role)
        
        all_matches = exact_matches + partial_matches

        if not all_matches:
            return json.dumps({"error": f"No roles found matching or containing '{find_role_name}'."})
        
        return json.dumps(all_matches)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_id_by_name",
                "description": "Retrieves a list of roles based on a name. Returns all roles that either exactly match the name or contain the name as a substring.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name of the role to search for (e.g., 'sales-lead')."
                        }
                    },
                    "required": ["role_name"]
                }
            }
        }
