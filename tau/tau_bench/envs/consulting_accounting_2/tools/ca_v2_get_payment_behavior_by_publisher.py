# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_one(lst: List[Dict[str, Any]], key: str, value: Any) -> Dict[str, Any] | None:
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class CaV2GetPaymentBehaviorByPublisher(Tool):
    """Get payment behavior data for a specific publisher."""

    @staticmethod
    def invoke(data: Dict[str, Any], publisher_id) -> str:
        if not publisher_id:
            return _error("publisher_id is required.")

        payment_behaviors = data.get("payment_behavior", [])
        behavior = _find_one(payment_behaviors, "publisher_id", publisher_id)
        return json.dumps(behavior) if behavior else _error(f"Payment behavior for publisher '{publisher_id}' not found.")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_payment_behavior_by_publisher",
                "description": "Get payment behavior patterns for a specific publisher.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }