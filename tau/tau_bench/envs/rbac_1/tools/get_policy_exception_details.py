# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPolicyExceptionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], exception_id) -> str:
        for ex in data.get('policy_exceptions', []):
            if ex.get('exception_id') == exception_id:
                return json.dumps(ex)
        return json.dumps({"error": "Policy exception not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_policy_exception_details",
                        "description": "Retrieves details for a specific policy exception.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "exception_id": {"type": "string"}
                                },
                                "required": ["exception_id"]
                        }
                }
        }
