# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserRolesTool(Tool):
    """Retrieve all roles assigned to a given user (echo user_id for chaining)."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        roles: List[str] = []
        assignments = data.get("user_roles", [])
        for assignment in assignments:
            if assignment.get("user_id") == user_id and not assignment.get(
                "expires_on"
            ):
                roles.append(assignment.get("role_id"))
        return json.dumps({"user_id": user_id, "roles": roles}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_roles",
                "description": "Get all active role IDs assigned to a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Unique user identifier (e.g., U-007)",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
