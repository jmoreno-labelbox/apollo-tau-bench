# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignUserRoleTool(Tool):
    """assign_user_role"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_role_id = kwargs["user_role_id"]
        user_id = kwargs["user_id"]
        role_id = kwargs["role_id"]
        assigned_by = kwargs["assigned_by"]
        expires_on = kwargs.get("expires_on")
        roles = data.setdefault("user_roles", [])
        existing_active = next(
            (
                r
                for r in roles
                if r.get("user_id") == user_id
                and r.get("role_id") == role_id
                and not r.get("expires_on")
            ),
            None,
        )
        if existing_active:
            record = existing_active
        else:
            existing_by_id = next(
                (r for r in roles if r.get("user_role_id") == user_role_id), None
            )
            if existing_by_id:
                record = existing_by_id
            else:
                record = {
                    "user_role_id": user_role_id,
                    "user_id": user_id,
                    "role_id": role_id,
                    "assigned_by": assigned_by,
                    "assigned_on": _HARD_TS,
                    "expires_on": expires_on,
                }
                roles.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_user_role",
                "description": "Create a user_role assignment if not already active.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "assigned_by": {"type": "string"},
                        "assigned_on": {"type": "string"},
                        "expires_on": {"type": ["string", "null"]},
                    },
                    "required": [
                        "user_role_id",
                        "user_id",
                        "role_id",
                        "assigned_by",
                        "assigned_on",
                    ],
                },
            },
        }
