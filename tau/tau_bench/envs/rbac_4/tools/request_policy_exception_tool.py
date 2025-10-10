# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RequestPolicyExceptionTool(Tool):
    """Create a new policy exception request."""

    @staticmethod
    def invoke(data: Dict[str, Any], permission_id, reason, requested_on, user_id) -> str:
        uid = user_id
        pid = permission_id
        exceptions = data.get("policy_exceptions", [])

        new_id = f"PE-{len(exceptions) + 1:03d}"
        record = {
            "exception_id": new_id,
            "user_id": uid,
            "permission_id": pid,
            "reviewed_by": None,
            "requested_on": requested_on,
            "reviewed_on": None,
            "expires_on": None,
            "reason": reason,
            "status": "PENDING_REVIEW"
        }
        exceptions.append(record)
        return json.dumps({"success": f"Policy exception {new_id} requested"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "request_policy_exception",
                "description": "Create a new policy exception request for a specific permission",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "permission_id": {"type": "string"},
                        "reason": {"type": "string"},
                        "requested_on": {"type": "string"}
                    },
                    "required": ["user_id", "permission_id", "reason", "requested_on"]
                }
            }
        }
