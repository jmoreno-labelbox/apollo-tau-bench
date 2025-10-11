# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApprovePolicyExceptionTool(Tool):
    """Approve a policy exception."""

    @staticmethod
    def invoke(data: Dict[str, Any], exception_id, expires_on, reviewed_by, reviewed_on) -> str:
        eid = exception_id
        reviewer = reviewed_by
        expires = expires_on
        for e in data.get("policy_exceptions", []):
            if e["exception_id"] == eid:
                e["status"] = "ACTIVE"
                e["reviewed_by"] = reviewer
                e["reviewed_on"] = reviewed_on
                e["expires_on"] = expires
                return json.dumps({"success": f"Exception {eid} approved"}, indent=2)
        return json.dumps({"error": f"Exception {eid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_policy_exception",
                "description": "Approve a pending policy exception request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                        "expires_on": {"type": "string"},
                        "reviewed_on": {"type": "string"}
                    },
                    "required": ["exception_id", "reviewed_by", "expires_on", "reviewed_on"]
                }
            }
        }
