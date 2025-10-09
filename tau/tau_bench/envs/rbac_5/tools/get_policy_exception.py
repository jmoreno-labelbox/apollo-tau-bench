from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class GetPolicyException(Tool):
    """
    Retrieve policy exceptions based on ID, user, permission, reviewer, or status.

    kwargs:
      exception_id: str (optional) - Specific exception ID to retrieve
      user_id: str (optional) - Filter by the user making the request
      permission_id: str (optional) - Filter by the permission related to exceptions
      reviewed_by: str (optional) - Filter by the reviewer
      status: str (optional) - Filter by status (PENDING_REVIEW, ACTIVE, EXPIRED, DENIED)
    """

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, user_id: str = None, 
               permission_id: str = None, reviewed_by: str = None, status: str = None) -> str:
        exceptions = data.get("policy_exceptions", [])

        # If exception_id is supplied, return the specific exception
        if exception_id:
            exception = _find_by_id(exceptions, "exception_id", exception_id)
            if not exception:
                payload = {"error": f"exception_id {exception_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "policy_exception": exception}
            out = json.dumps(payload)
            return out

        # Narrow down exceptions according to the supplied criteria
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
        payload = {"ok": True, "policy_exceptions": filtered_exceptions}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyException",
                "description": "Retrieve policy exceptions by ID, user, permission, reviewer, or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "Specific policy exception ID to retrieve.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Filter by requesting user ID.",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "Filter by permission involved in exceptions.",
                        },
                        "reviewed_by": {
                            "type": "string",
                            "description": "Filter by reviewer user ID.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by status (PENDING_REVIEW, ACTIVE, EXPIRED, DENIED).",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
