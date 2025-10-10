# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GrantRoleTool(Tool):
    """grant_role: assign a role either by request_id or direct user_id/role_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        assigned_by = kwargs.get("assigned_by")
        if request_id:
            return AssignRoleOnApprovalTool.invoke(
                data, request_id=request_id, assigned_by=assigned_by
            )
        # direct
        return AssignUserRoleTool.invoke(
            data,
            user_role_id=kwargs.get("user_role_id"),
            user_id=kwargs.get("user_id"),
            role_id=kwargs.get("role_id"),
            assigned_by=assigned_by,
            expires_on=kwargs.get("expires_on"),
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "grant_role",
                "description": "Assign a role by request_id or direct user/role pair.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "user_role_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "assigned_by": {"type": "string"},
                        "expires_on": {"type": ["string", "null"]},
                    },
                    "required": ["assigned_by"],
                },
            },
        }
