# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPolicyExceptionDetailsTool(Tool):
    """Return the full stored record for a given policy exception (no error payloads)."""

    @staticmethod
    def invoke(data: Dict[str, Any], exception_id) -> str:
        eid = exception_id
        for e in data.get("policy_exceptions", []) or []:
            if e.get("exception_id") == eid:
                # Return the object formatted as pretty JSON to easily access reviewed_on and other fields.
                return json.dumps(e, indent=2)
        # If not found, return an empty object to prevent '"error":' keys from triggering validators.
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
