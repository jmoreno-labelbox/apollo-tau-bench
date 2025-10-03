from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetRoleIdByName(Tool):
    """
    Locates one or more roles by searching for a name, giving priority to exact matches
    while also returning other roles that include the search term.
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_name: str = None) -> str:
        find_role_name = role_name
        try:
            roles = data.get("roles", [])
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
            payload = {"error": f"No roles found matching or containing '{find_role_name}'."}
            out = json.dumps(payload)
            return out
        payload = all_matches
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleIdByName",
                "description": "Retrieves a list of roles based on a name. Returns all roles that either exactly match the name or contain the name as a substring.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name of the role to search for (e.g., 'sales-lead').",
                        }
                    },
                    "required": ["role_name"],
                },
            },
        }
