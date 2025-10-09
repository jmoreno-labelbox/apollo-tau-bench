from tau_bench.envs.tool import Tool
import json
from typing import Any

class RequestPolicyExceptionTool(Tool):
    """Initiate a new policy exception request."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, permission_id: str = None, reason: str = None, requested_on: str = None) -> str:
        exceptions = data.get("policy_exceptions", [])

        new_id = f"PE-{len(exceptions) + 1:03d}"
        record = {
            "exception_id": new_id,
            "user_id": user_id,
            "permission_id": permission_id,
            "reviewed_by": None,
            "requested_on": requested_on,
            "reviewed_on": None,
            "expires_on": None,
            "reason": reason,
            "status": "PENDING_REVIEW",
        }
        exceptions.append(record)
        payload = {"success": f"Policy exception {new_id} requested"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RequestPolicyException",
                "description": "Create a new policy exception request for a specific permission",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "permission_id": {"type": "string"},
                        "reason": {"type": "string"},
                        "requested_on": {"type": "string"},
                    },
                    "required": ["user_id", "permission_id", "reason", "requested_on"],
                },
            },
        }
