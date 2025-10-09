from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetRolePermissions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        permission_ids = [
            rp["permission_id"]
            for rp in data.get("role_permissions", [])
            if rp.get("role_id") == role_id
        ]
        payload = {"role_id": role_id, "permissions": permission_ids}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRolePermissions",
                "description": "Retrieves all permissions associated with a role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }
