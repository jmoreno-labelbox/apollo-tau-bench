from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputePaymentBehavior(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None) -> str:
        if not publisher_id:
            payload = {"error": "publisher_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        pb = next(
            (
                p
                for p in data.get("payment_behavior", [])
                if p.get("publisher_id") == publisher_id
            ),
            None,
        )
        payload = pb or {"error": f"payment_behavior for {publisher_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputePaymentBehavior",
                "description": "Return stored payment behavior stats for a publisher.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }
