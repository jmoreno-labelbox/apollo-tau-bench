from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class AssignPermissionToRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, permission_id: str = None) -> str:
        role_permissions = data.get("role_permissions", [])
        assignment = {
            "role_id": role_id,
            "permission_id": permission_id,
        }
        role_permissions.append(assignment)
        data["role_permissions"] = role_permissions
        payload = assignment
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignPermissionToRole",
                "description": "Assigns a permission to a role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string"},
                        "permission_id": {"type": "string"},
                    },
                    "required": ["role_id", "permission_id"],
                },
            },
        }
