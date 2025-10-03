from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class RevokePolicyException(Tool):
    """Cancels an active policy exception, changing its status to 'REVOKED'."""

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None) -> str:
        try:
            policy_exceptions = data.get("policy_exceptions", [])
        except:
            policy_exceptions = []

        exception_found = False
        for exc in policy_exceptions:
            if exc.get("exception_id") == exception_id:
                exc["status"] = "REVOKED"
                exception_found = True
                break

        if not exception_found:
            payload = {"error": f"Policy exception with ID '{exception_id}' not found."}
            out = json.dumps(payload)
            return out

        data["policy_exceptions"] = policy_exceptions
        payload = {
            "message": "Policy exception revoked successfully.",
            "exception_id": exception_id,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokePolicyException",
                "description": "Revokes an active policy exception as a remediation action.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "The ID of the policy exception to revoke.",
                        }
                    },
                    "required": ["exception_id"],
                },
            },
        }
