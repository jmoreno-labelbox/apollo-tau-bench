# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPolicyExceptionById(Tool):
    """ Get the full details of a specific policy exception using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id")
        try:
            policy_exceptions = data.get('policy_exceptions', [])
        except:
            policy_exceptions = []

        for exc in policy_exceptions:
            if exc.get("exception_id") == exception_id:
                return json.dumps(exc)

        return json.dumps({"error": f"Policy exception with ID '{exception_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_exception_by_id",
                "description": "Retrieves the full details of a specific policy exception using its unique ID (e.g., 'PE-010').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "The unique ID of the policy exception to retrieve."
                        }
                    },
                    "required": ["exception_id"]
                }
            }
        }
