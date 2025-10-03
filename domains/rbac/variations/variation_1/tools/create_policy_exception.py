from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class CreatePolicyException(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        permission_id: str = None,
        reviewed_by: str = None,
        reason: str = None,
        expires_on: str = None
    ) -> str:
        exceptions = data.get("policy_exceptions", [])
        new_id_num = (
            max((int(e["exception_id"][3:]) for e in exceptions), default=0) + 1
        )
        new_exception_id = f"PE-{new_id_num:03d}"
        new_exception = {
            "exception_id": new_exception_id,
            "user_id": user_id,
            "permission_id": permission_id,
            "reviewed_by": reviewed_by,
            "reason": reason,
            "expires_on": expires_on,
            "status": "PENDING_REVIEW",
        }
        exceptions.append(new_exception)
        data["policy_exceptions"] = exceptions
        payload = new_exception
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePolicyException",
                "description": "Creates a policy exception for a user and permission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "permission_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                        "reason": {"type": "string"},
                        "expires_on": {"type": "string", "format": "date-time"},
                    },
                    "required": ["user_id", "permission_id", "reason"],
                },
            },
        }
