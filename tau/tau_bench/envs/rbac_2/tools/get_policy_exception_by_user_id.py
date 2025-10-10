# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPolicyExceptionByUserId(Tool):
    """Finds all policy exceptions for a specific user, with an option to include inactive ones."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id, include_inactive = False) -> str:
        
        terminal_statuses = {"REVOKED", "REJECTED", "EXPIRED"}
        try:
            policy_exceptions = data.get('policy_exceptions', [])
        except:
            policy_exceptions = []

        user_exceptions = []
        for exc in policy_exceptions:
            if exc.get("user_id") == user_id:
                if include_inactive:
                    user_exceptions.append(exc)
                elif exc.get("status") not in terminal_statuses:
                    user_exceptions.append(exc)
        
        return json.dumps(user_exceptions)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_exception_by_user_id",
                "description": "Retrieves a list of policy exceptions for a given user ID. By default, it only returns active exceptions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user to find exceptions for."},
                        "include_inactive": {"type": "boolean", "description": "Set to true to include expired, revoked, or rejected exceptions. Defaults to false."}
                    },
                    "required": ["user_id"]
                }
            }
        }
