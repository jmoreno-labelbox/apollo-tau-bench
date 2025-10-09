from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class ComplianceReview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transfer_id: str = None, adjustment_id: str = None) -> str:
        payload = {"compliance_reviewed": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComplianceReview",
                "parameters": {"transfer_id": {"type": "string"}},
                "required": ["transfer_id"],
            },
        }
