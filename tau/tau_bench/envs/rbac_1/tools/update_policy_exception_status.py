from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class UpdatePolicyExceptionStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, status: str = None) -> str:
        for ex in data.get("policy_exceptions", []):
            if ex.get("exception_id") == exception_id:
                ex["status"] = status
                payload = ex
                out = json.dumps(payload)
                return out
        payload = {"error": "Policy exception not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePolicyExceptionStatus",
                "description": "Updates the status of a policy exception (e.g., ACTIVE, EXPIRED).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["exception_id", "status"],
                },
            },
        }
