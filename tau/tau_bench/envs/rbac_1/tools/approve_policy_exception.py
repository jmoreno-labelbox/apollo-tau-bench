# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApprovePolicyException(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], exception_id, reviewed_by) -> str:
        for ex in data.get('policy_exceptions', []):
            if ex.get('exception_id') == exception_id:
                ex['status'] = 'ACTIVE'
                ex['reviewed_by'] = reviewed_by
                ex['reviewed_on'] = NOW.strftime(DT_STR_FORMAT)
                return json.dumps(ex)
        return json.dumps({"error": "Policy exception not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "approve_policy_exception",
                        "description": "Approves a pending policy exception.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "exception_id": {"type": "string"},
                                        "reviewed_by": {"type": "string"}
                                },
                                "required": ["exception_id", "reviewed_by"]
                        }
                }
        }
