# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRoleNameTool(Tool):
    """get_role_name
    Lookup a role by role_id and return its role_name and metadata.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        if not role_id:
            return json.dumps({"error": "role_id is required"}, indent=2)

        roles: List[Dict[str, Any]] = list(data.get("roles", {}).values())
        rec = next((r for r in roles if r.get("role_id") == role_id), None)
        if not rec:
            return json.dumps({"error": f"Role {role_id} not found"}, indent=2)

        out = {
            "role_id": rec.get("role_id"),
            "role_name": rec.get("role_name"),
            "description": rec.get("description"),
            "is_temporary": rec.get("is_temporary"),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_name",
                "description": "Return role_name and metadata for a given role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "Unique role identifier (e.g., ROL-001)",
                        }
                    },
                    "required": ["role_id"],
                },
            },
        }
