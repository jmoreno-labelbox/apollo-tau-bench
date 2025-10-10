# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DualApproval(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"dual_approved": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "dual_approval",
                "description": "Tool function: dual_approval",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
