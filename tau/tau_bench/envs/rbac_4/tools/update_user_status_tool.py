# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserStatusTool(Tool):
    """Update a user's status, department, or MFA settings with cascading effects."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        users = list(data.get("users", {}).values())
        audit_logs = data.get("audit_logs", [])
        sessions = data.get("sessions", [])

        user_id = kwargs.get("user_id")
        new_status = kwargs.get("status")
        department = kwargs.get("department")
        mfa_enabled = kwargs.get("mfa_enabled")

        # Locate user
        user = next((u for u in users if u["user_id"] == user_id), None)
        if not user:
            return json.dumps({"error": f"User {user_id} not found"}, indent=2)

        # Update details
        if new_status:
            user["status"] = new_status
            if new_status in ["SUSPENDED", "DISABLED"]:
                for s in sessions:
                    if s["user_id"] == user_id and s.get("end_time") is None:
                        s["end_time"] = "2025-08-11 13:00:00+00:00"
        if department:
            user["department"] = department
        if mfa_enabled is not None:
            user["mfa_enabled"] = mfa_enabled

        # Audit
        log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append({
            "log_id": log_id,
            "actor_id": kwargs.get("updated_by"),
            "action_type": "USER_UPDATED",
            "target_id": user_id,
            "timestamp": "2025-08-11 13:00:00+00:00",
            "details": "User status/attributes updated"
        })

        return json.dumps({"success": f"User {user_id} updated"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_status",
                "description": "Update a user's status/department/MFA. Terminates sessions if suspended/disabled.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "status": {"type": "string"},
                        "department": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                        "updated_by": {"type": "string"}
                    },
                    "required": ["user_id", "updated_by"]
                }
            }
        }
