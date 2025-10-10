# Copyright held by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPolicyException(Tool):
    """
    Retrieve policy exceptions by ID, user, permission, reviewer, or status.

    kwargs:
      exception_id: str (optional) - Specific exception ID to retrieve
      user_id: str (optional) - Filter by requesting user
      permission_id: str (optional) - Filter by permission involved in exceptions
      reviewed_by: str (optional) - Filter by reviewer
      status: str (optional) - Filter by status (PENDING_REVIEW, ACTIVE, EXPIRED, DENIED)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], exception_id, permission_id, reviewed_by, status, user_id) -> str:

        exceptions = data.get("policy_exceptions", [])

        # Return a single exception if exception_id is supplied.
        if exception_id:
            exception = _find_by_id(exceptions, "exception_id", exception_id)
            if not exception:
                return json.dumps({"error": f"exception_id {exception_id} not found"})
            return json.dumps({"ok": True, "policy_exception": exception})

        # Filter exceptions according to specified criteria.
        filtered_exceptions = []
        for exception in exceptions:
            if user_id and exception.get("user_id") != user_id:
                continue
            if permission_id and exception.get("permission_id") != permission_id:
                continue
            if reviewed_by and exception.get("reviewed_by") != reviewed_by:
                continue
            if status and exception.get("status") != status:
                continue
            filtered_exceptions.append(exception)

        return json.dumps({"ok": True, "policy_exceptions": filtered_exceptions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_exception",
                "description": "Retrieve policy exceptions by ID, user, permission, reviewer, or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string", "description": "Specific policy exception ID to retrieve."},
                        "user_id": {"type": "string", "description": "Filter by requesting user ID."},
                        "permission_id": {"type": "string", "description": "Filter by permission involved in exceptions."},
                        "reviewed_by": {"type": "string", "description": "Filter by reviewer user ID."},
                        "status": {"type": "string", "description": "Filter by status (PENDING_REVIEW, ACTIVE, EXPIRED, DENIED)."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
