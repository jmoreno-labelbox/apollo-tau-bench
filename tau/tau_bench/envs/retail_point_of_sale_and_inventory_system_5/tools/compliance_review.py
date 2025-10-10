# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComplianceReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"compliance_reviewed": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "compliance_review",
                "description": "Tool function: compliance_review",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
