from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RevokeUserRoleTool(Tool):
    """
    Revoke a user's role (compliant with specifications).
    - Parameters: user_id, role_id, revoked_by
    - Functionality: delete the corresponding user_roles entry if it exists; if you prefer a soft-revoke for consistency,
      set expires_on to the assignment's assigned_on.
    - Result: {"removed": true/false}
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None, revoked_by: str = None) -> str:
        assignments = data.get("user_roles", {}).values()
        removed = False

        kept: list[dict[str, Any]] = []
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

        # Set up information for the audit log
        action_details = "REMOVED" if removed else "NOOP"
        log_info = {
            "log_id": f"LOG-{user_id}-{role_id}-revoke",
            "actor_id": revoked_by,
            "action_type": "RevokeRole",
            "target_id": f"{user_id}:{role_id}",
            "timestamp": _HARD_TS,
            "details": action_details,
        }
        payload = {
            "removed": bool(removed),
            "user_id": user_id,
            "role_id": role_id,
            "log_info": log_info,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revokeUserRole",
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
