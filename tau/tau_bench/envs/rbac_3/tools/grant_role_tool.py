from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class GrantRoleTool(Tool):
    """grant_role: allocate a role either via request_id or directly using user_id/role_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str = None,
        assigned_by: str = None,
        user_role_id: str = None,
        user_id: str = None,
        role_id: str = None,
        expires_on: str = None
    ) -> str:
        if request_id:
            return AssignRoleOnApprovalTool.invoke(
                data, request_id=request_id, assigned_by=assigned_by
            )
        #straightforward
        return AssignUserRoleTool.invoke(
            data,
            user_role_id=user_role_id,
            user_id=user_id,
            role_id=role_id,
            assigned_by=assigned_by,
            expires_on=expires_on,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GrantRole",
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
