from tau_bench.envs.tool import Tool
import json
from typing import Any

class ApprovePolicyExceptionTool(Tool):
    """Authorize a policy exception."""

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, reviewed_by: str = None, expires_on: str = None, reviewed_on: str = None, permission_id: Any = None) -> str:
        for e in data.get("policy_exceptions", []):
            if e["exception_id"] == exception_id:
                e["status"] = "ACTIVE"
                e["reviewed_by"] = reviewed_by
                e["reviewed_on"] = reviewed_on
                e["expires_on"] = expires_on
                payload = {"success": f"Exception {exception_id} approved"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Exception {exception_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApprovePolicyException",
                "description": "Approve a pending policy exception request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                        "expires_on": {"type": "string"},
                        "reviewed_on": {"type": "string"},
                    },
                    "required": [
                        "exception_id",
                        "reviewed_by",
                        "expires_on",
                        "reviewed_on",
                    ],
                },
            },
        }
