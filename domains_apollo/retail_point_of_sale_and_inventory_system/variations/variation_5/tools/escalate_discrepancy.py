from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class EscalateDiscrepancy(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], escalation_level: str = "regional", adjustment_id: Any = None,
    store_id: Any = None,
    sku: str = None,
    amount: float = None,
    ) -> str:
        payload = {"escalated": True, "level": escalation_level}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EscalateDiscrepancy",
                "parameters": {
                    "store_id": {"type": "string"},
                    "sku": {"type": "string"},
                    "amount": {"type": "number"},
                    "escalation_level": {"type": "string"},
                },
                "required": ["store_id", "sku", "amount", "escalation_level"],
            },
        }
