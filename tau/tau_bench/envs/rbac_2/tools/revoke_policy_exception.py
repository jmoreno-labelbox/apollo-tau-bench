# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RevokePolicyException(Tool):
    """ Revokes an active policy exception, setting its status to 'REVOKED'. """
    @staticmethod
    def invoke(data: Dict[str, Any], exception_id) -> str:
        try:
            policy_exceptions = data.get('policy_exceptions', [])
        except:
            policy_exceptions = []

        exception_found = False
        for exc in policy_exceptions:
            if exc.get("exception_id") == exception_id:
                exc["status"] = "REVOKED"
                exception_found = True
                break
        
        if not exception_found:
            return json.dumps({"error": f"Policy exception with ID '{exception_id}' not found."})

        data['policy_exceptions'] = policy_exceptions
        return json.dumps({"message": "Policy exception revoked successfully.", "exception_id": exception_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_policy_exception",
                "description": "Revokes an active policy exception as a remediation action.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string", "description": "The ID of the policy exception to revoke."}
                    },
                    "required": ["exception_id"]
                }
            }
        }
