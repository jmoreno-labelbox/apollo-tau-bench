from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class DualApproval(Tool):
    @staticmethod
    def invoke(data: dict[str, Any],
        adjustment_id: Any = None,
        approver_id: Any = None
    ) -> str:
        payload = {"dual_approved": True}
        out = json.dumps(payload, indent=2)
        return out
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DualApproval",
                "parameters": {"adjustment_id": {"type": "string"}},
                "required": ["adjustment_id"],
            },
        }
