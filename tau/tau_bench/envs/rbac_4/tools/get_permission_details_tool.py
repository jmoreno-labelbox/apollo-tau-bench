# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPermissionDetailsTool(Tool):
    """Get full details of a permission by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("permission_id")
        for p in list(data.get("permissions", {}).values()):
            if p["permission_id"] == pid:
                return json.dumps(p, indent=2)
        return json.dumps({"error": f"Permission {pid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permission_details",
                "description": "Get full permission record from permission_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {"type": "string"}
                    },
                    "required": ["permission_id"]
                }
            }
        }
