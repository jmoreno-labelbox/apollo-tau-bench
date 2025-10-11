# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_id(data: Dict[str, Any], collection: str, prefix: str) -> str:
    n = len(data.get(collection, [])) + 1
    return f"{prefix}-{n:03d}"

def _find_by_id(items: List[Dict[str, Any]], key: str, value: str) -> Optional[Dict[str, Any]]:
    for it in items or []:
        if it.get(key) == value:
            return it
    return None

class CreatePolicyException(Tool):
    """
    Create a new policy exception request.

    kwargs:
      user_id: str (required) - User for whom exception is created
      permission_id: str (required) - Permission requiring exception
      reviewed_by: str (required) - User ID who will review the exception
      reason: str (required) - Business justification for the exception
      expires_on: str (optional) - ISO timestamp when exception expires
    """
    @staticmethod
    def invoke(data: Dict[str, Any], expires_on, permission_id = "", reason = "", reviewed_by = "", user_id = "") -> str:

        if not user_id or not permission_id or not reviewed_by or not reason:
            return json.dumps({"error": "user_id, permission_id, reviewed_by, and reason are required"})

        # Check if the user is present.
        if not _find_by_id(list(data.get("users", {}).values()), "user_id", user_id):
            return json.dumps({"error": f"user_id {user_id} not found"})

        # Check if permission is granted.
        if not _find_by_id(list(data.get("permissions", {}).values()), "permission_id", permission_id):
            return json.dumps({"error": f"permission_id {permission_id} not found"})

        # Check if the reviewer is present.
        if not _find_by_id(list(data.get("users", {}).values()), "user_id", reviewed_by):
            return json.dumps({"error": f"reviewed_by {reviewed_by} not found"})

        # Establish a new policy exemption.
        new_exception = {
            "exception_id": _next_id(data, "policy_exceptions", "PE"),
            "user_id": user_id,
            "permission_id": permission_id,
            "reviewed_by": reviewed_by,
            "requested_on": get_current_timestamp(),
            "reviewed_on": None,
            "expires_on": expires_on,
            "reason": reason,
            "status": "PENDING_REVIEW"
        }

        data.setdefault("policy_exceptions", []).append(new_exception)
        return json.dumps({"ok": True, "policy_exception": new_exception})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_policy_exception",
                "description": "Create a new policy exception request for emergency access.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "User ID for whom exception is created."},
                        "permission_id": {"type": "string", "description": "Permission ID requiring exception."},
                        "reviewed_by": {"type": "string", "description": "User ID who will review the exception."},
                        "reason": {"type": "string", "description": "Business justification for the exception."},
                        "expires_on": {"type": "string", "description": "ISO timestamp when exception expires (optional)."}
                    },
                    "required": ["user_id", "permission_id", "reviewed_by", "reason"],
                    "additionalProperties": False
                }
            }
        }