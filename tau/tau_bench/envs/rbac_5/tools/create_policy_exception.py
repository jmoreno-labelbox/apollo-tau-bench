from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreatePolicyException(Tool):
    """
    Establish a new policy exception request.

    kwargs:
      user_id: str (mandatory) - User for whom the exception is created
      permission_id: str (mandatory) - Permission that requires an exception
      reviewed_by: str (mandatory) - User ID responsible for reviewing the exception
      reason: str (mandatory) - Business justification for the exception
      expires_on: str (optional) - ISO timestamp indicating when the exception expires
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = "", permission_id: str = "", reviewed_by: str = "", reason: str = "", expires_on: Any = None) -> str:
        if not user_id or not permission_id or not reviewed_by or not reason:
            payload = {
                    "error": "user_id, permission_id, reviewed_by, and reason are required"
                }
            out = json.dumps(
                payload)
            return out

        #Confirm the user is present
        if not _find_by_id(data.get("users", []), "user_id", user_id):
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload)
            return out

        #Confirm the permission is present
        if not _find_by_id(data.get("permissions", []), "permission_id", permission_id):
            payload = {"error": f"permission_id {permission_id} not found"}
            out = json.dumps(payload)
            return out

        #Confirm the reviewer is present
        if not _find_by_id(data.get("users", []), "user_id", reviewed_by):
            payload = {"error": f"reviewed_by {reviewed_by} not found"}
            out = json.dumps(payload)
            return out

        #Establish a new policy exception
        new_exception = {
            "exception_id": _next_id(data, "policy_exceptions", "PE"),
            "user_id": user_id,
            "permission_id": permission_id,
            "reviewed_by": reviewed_by,
            "requested_on": get_current_timestamp(),
            "reviewed_on": None,
            "expires_on": expires_on,
            "reason": reason,
            "status": "PENDING_REVIEW",
        }

        data.setdefault("policy_exceptions", []).append(new_exception)
        payload = {"ok": True, "policy_exception": new_exception}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePolicyException",
                "description": "Create a new policy exception request for emergency access.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User ID for whom exception is created.",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "Permission ID requiring exception.",
                        },
                        "reviewed_by": {
                            "type": "string",
                            "description": "User ID who will review the exception.",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Business justification for the exception.",
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "ISO timestamp when exception expires (optional).",
                        },
                    },
                    "required": ["user_id", "permission_id", "reviewed_by", "reason"],
                    "additionalProperties": False,
                },
            },
        }
