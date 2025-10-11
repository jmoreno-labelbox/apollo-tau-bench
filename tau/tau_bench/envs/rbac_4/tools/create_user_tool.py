# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateUserTool(Tool):
    """Create a new user account with validation and audit logging."""
    @staticmethod
    def invoke(data: Dict[str, Any], created_by, department, email, username, mfa_enabled = False) -> str:
        users = list(data.get("users", {}).values())
        audit_logs = data.get("audit_logs", [])

        # Verification: confirm that username/email is distinct.
        for u in users:
            if u["username"] == username:
                return json.dumps({"error": f"Username {username} already exists"}, indent=2)
            if u["email"] == email:
                return json.dumps({"error": f"Email {email} already exists"}, indent=2)

        # Predictable new user_id
        new_id = f"U-{len(users) + 1:03d}"
        users.append({
            "user_id": new_id,
            "username": username,
            "email": email,
            "department": department,
            "status": "PENDING_ACCESS",
            "mfa_enabled": mfa_enabled
        })

        # Entry for audit log
        new_log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append({
            "log_id": new_log_id,
            "actor_id": created_by,
            "action_type": "USER_CREATED",
            "target_id": new_id,
            "timestamp": "2025-08-11 10:00:00+00:00",
            "details": "User account created during onboarding process."
        })

        return json.dumps({"success": f"User {new_id} created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_user",
                "description": "Create a new user in the system with PENDING_ACCESS status and log the event.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string"},
                        "department": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                        "created_by": {"type": "string"}
                    },
                    "required": ["username", "email", "department", "created_by"]
                }
            }
        }
