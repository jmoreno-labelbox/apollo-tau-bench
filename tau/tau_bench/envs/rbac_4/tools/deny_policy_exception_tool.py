# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DenyPolicyExceptionTool(Tool):
    """Deny a policy exception request."""

    @staticmethod
    def invoke(data: Dict[str, Any], exception_id, reviewed_by, reviewed_on) -> str:
        eid = exception_id
        reviewer = reviewed_by
        for e in data.get("policy_exceptions", []):
            if e["exception_id"] == eid:
                e["status"] = "DENIED"
                e["reviewed_by"] = reviewer
                e["reviewed_on"] = reviewed_on
                return json.dumps({"success": f"Exception {eid} denied"}, indent=2)
        return json.dumps({"error": f"Exception {eid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deny_policy_exception",
                "description": "Deny a pending policy exception request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                        "reviewed_on": {"type": "string"}
                    },
                    "required": ["exception_id", "reviewed_by", "reviewed_on"]
                }
            }
        }
