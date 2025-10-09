from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetRoleByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_name: str = None) -> str:
        for role in data.get("roles", []):
            if role.get("role_name") == role_name:
                payload = role
                out = json.dumps(payload)
                return out
        payload = {"error": "Role not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleByName",
                "description": "Retrieves role details based on the role name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name of the role to search for.",
                        }
                    },
                    "required": ["role_name"],
                },
            },
        }
