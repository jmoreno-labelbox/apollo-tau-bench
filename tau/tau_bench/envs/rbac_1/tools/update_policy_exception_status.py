# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdatePolicyExceptionStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id")
        new_status = kwargs.get("status")
        for ex in data.get('policy_exceptions', []):
            if ex.get('exception_id') == exception_id:
                ex['status'] = new_status
                return json.dumps(ex)
        return json.dumps({"error": "Policy exception not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_policy_exception_status",
                        "description": "Updates the status of a policy exception (e.g., ACTIVE, EXPIRED).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "exception_id": {"type": "string"},
                                        "status": {"type": "string"}
                                },
                                "required": ["exception_id", "status"]
                        }
                }
        }
