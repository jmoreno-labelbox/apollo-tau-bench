# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPolicyExceptionDetailsTool(Tool):
    """Return the full stored record for a given policy exception (no error payloads)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        eid = kwargs.get("exception_id")
        for e in data.get("policy_exceptions", []) or []:
            if e.get("exception_id") == eid:
                # Return the exact object as pretty JSON so you can grab reviewed_on, etc.
                return json.dumps(e, indent=2)
        # Not found → return empty object to avoid '"error":' keys tripping validators
        return "{}"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_exception_details",
                "description": "Return the full stored policy-exception record for the given ID.",
                "parameters": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "exception_id": {"type": "string", "description": "e.g., PE-007"}
                    },
                    "required": ["exception_id"]
                }
            }
        }
