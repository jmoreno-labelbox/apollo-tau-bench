# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePolicyException(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exceptions = data.get('policy_exceptions', [])
        new_id_num = max((int(e['exception_id'][3:]) for e in exceptions), default=0) + 1
        new_exception_id = f"PE-{new_id_num:03d}"
        new_exception = {
                "exception_id": new_exception_id,
                "user_id": kwargs.get("user_id"),
                "permission_id": kwargs.get("permission_id"),
                "reviewed_by": kwargs.get("reviewed_by"),
                "reason": kwargs.get("reason"),
                "expires_on": kwargs.get("expires_on"),
                "status": "PENDING_REVIEW"
        }
        exceptions.append(new_exception)
        data['policy_exceptions'] = exceptions
        return json.dumps(new_exception)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_policy_exception",
                        "description": "Creates a policy exception for a user and permission.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "permission_id": {"type": "string"},
                                        "reviewed_by": {"type": "string"},
                                        "reason": {"type": "string"},
                                        "expires_on": {"type": "string", "format": "date-time"}
                                },
                                "required": ["user_id", "permission_id", "reason"]
                        }
                }
        }
