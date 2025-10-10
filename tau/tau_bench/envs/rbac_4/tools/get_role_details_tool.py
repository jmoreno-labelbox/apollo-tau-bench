# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRoleDetailsTool(Tool):
    """Get details about a specific role."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get("role_id")
        for r in list(data.get("roles", {}).values()):
            if r["role_id"] == rid:
                return json.dumps(r, indent=2)
        return json.dumps({"error": f"Role {rid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_details",
                "description": "Get role_name, description, and is_temporary flag for a given role_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string"}
                    },
                    "required": ["role_id"]
                }
            }
        }
