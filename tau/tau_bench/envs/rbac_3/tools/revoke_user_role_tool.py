# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RevokeUserRoleTool(Tool):
    """
    Revoke a user's role (spec-compliant).
    - Params: user_id, role_id, revoked_by
    - Behavior: remove matching user_roles entry if present; if you prefer soft-revoke for determinism,
      mark expires_on to the assignment's assigned_on.
    - Output: {"removed": true/false}
    """

    @staticmethod
    def invoke(data: Dict[str, Any], revoked_by, role_id, user_id) -> str:

        assignments = data.get("user_roles", [])
        removed = False

        kept: List[Dict[str, Any]] = []
        for assignment in assignments:
            if (
                assignment.get("user_id") == user_id
                and assignment.get("role_id") == role_id
                and not removed
            ):
                removed = True
            else:
                kept.append(assignment)

        if removed:
            data["user_roles"] = kept

        # Gather audit log details.
        action_details = "REMOVED" if removed else "NOOP"
        log_info = {
            "log_id": f"LOG-{user_id}-{role_id}-revoke",
            "actor_id": revoked_by,
            "action_type": "revoke_role",
            "target_id": f"{user_id}:{role_id}",
            "timestamp": _HARD_TS,
            "details": action_details,
        }

        return json.dumps(
            {
                "removed": bool(removed),
                "user_id": user_id,
                "role_id": role_id,
                "log_info": log_info,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_user_role",
                "description": (
                    "Revoke a specific role from a user (remove the assignment). Returns info for follow-up audit logging."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "revoked_by": {
                            "type": "string",
                            "description": "Reviewer/admin who revokes (e.g., U-010)",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": (
                                "ISO 8601 timestamp for when the revoke occurred"
                            ),
                        },
                    },
                    "required": ["user_id", "role_id", "revoked_by"],
                },
            },
        }
