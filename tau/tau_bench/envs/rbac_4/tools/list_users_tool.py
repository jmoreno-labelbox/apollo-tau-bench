# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListUsersTool(Tool):
    """List users with optional filters."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        dept = kwargs.get("department")
        status = kwargs.get("status")
        mfa_enabled = kwargs.get("mfa_enabled")
        users = list(data.get("users", {}).values())

        results = []
        for u in users:
            if dept and u["department"] != dept:
                continue
            if status and u["status"] != status:
                continue
            if mfa_enabled is not None and u["mfa_enabled"] != mfa_enabled:
                continue
            results.append(u)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_users",
                "description": "List users with optional filters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string"},
                        "status": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"}
                    }
                }
            }
        }
