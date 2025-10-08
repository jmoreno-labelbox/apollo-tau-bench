from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class AssignUserRoleTool(Tool):
    """AssignUserRole"""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_role_id: str,
        user_id: str,
        role_id: str,
        assigned_by: str,
        expires_on: str = None,
        assigned_on: str = None
    ) -> str:
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
        payload = record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignUserRole",
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
