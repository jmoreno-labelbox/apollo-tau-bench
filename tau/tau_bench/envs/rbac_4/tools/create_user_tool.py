from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateUserTool(Tool):
    """Establish a new user account with validation and logging for audit purposes."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        username: str = None, 
        email: str = None, 
        department: str = None, 
        mfa_enabled: bool = False, 
        created_by: str = None,
    user_id: Any = None,
    actor_id: Any = None,
    created_at: str = None
    ) -> str:
        users = data.get("users", {}).values()
        audit_logs = data.get("audit_logs", {}).values()

        # Validation: confirm that username/email are distinct
        for u in users.values():
            if u["username"] == username:
                payload = {"error": f"Username {username} already exists"}
                out = json.dumps(payload, indent=2)
                return out
            if u["email"] == email:
                payload = {"error": f"Email {email} already exists"}
                out = json.dumps(payload, indent=2)
                return out

        # Predictable new user_id
        new_id = f"U-{len(users) + 1:03d}"
        users.append(
            {
                "user_id": new_id,
                "username": username,
                "email": email,
                "department": department,
                "status": "PENDING_ACCESS",
                "mfa_enabled": mfa_enabled,
            }
        )

        # Entry for audit log
        new_log_id = f"L-{len(audit_logs) + 1:03d}"
        audit_logs.append(
            {
                "log_id": new_log_id,
                "actor_id": created_by,
                "action_type": "USER_CREATED",
                "target_id": new_id,
                "timestamp": "2025-08-11 10:00:00+00:00",
                "details": "User account created during onboarding process.",
            }
        )
        payload = {"success": f"User {new_id} created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateUser",
                "description": "Create a new user in the system with PENDING_ACCESS status and log the event.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string"},
                        "department": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                        "created_by": {"type": "string"},
                    },
                    "required": ["username", "email", "department", "created_by"],
                },
            },
        }
