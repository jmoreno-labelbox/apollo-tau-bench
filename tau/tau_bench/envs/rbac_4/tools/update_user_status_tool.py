from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateUserStatusTool(Tool):
    """Revise a user's status, department, or MFA settings with cascading impacts."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        status: str = None,
        department: str = None,
        mfa_enabled: bool = None,
        updated_by: str = None
    ) -> str:
        users = data.get("users", [])
        audit_logs = data.get("audit_logs", [])
        sessions = data.get("sessions", [])

        # Find user
        user = next((u for u in users if u["user_id"] == user_id), None)
        if not user:
            payload = {"error": f"User {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        # Revise details
        if status:
            user["status"] = status
            if status in ["SUSPENDED", "DISABLED"]:
                for s in sessions:
                    if s["user_id"] == user_id and s.get("end_time") is None:
                        s["end_time"] = "2025-08-11 13:00:00+00:00"
        if department:
            user["department"] = department
        if mfa_enabled is not None:
            user["mfa_enabled"] = mfa_enabled

        # Examine
        log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append(
            {
                "log_id": log_id,
                "actor_id": updated_by,
                "action_type": "USER_UPDATED",
                "target_id": user_id,
                "timestamp": "2025-08-11 13:00:00+00:00",
                "details": "User status/attributes updated",
            }
        )
        payload = {"success": f"User {user_id} updated"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserStatus",
                "description": "Update a user's status/department/MFA. Terminates sessions if suspended/disabled.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "status": {"type": "string"},
                        "department": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                        "updated_by": {"type": "string"},
                    },
                    "required": ["user_id", "updated_by"],
                },
            },
        }
