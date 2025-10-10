# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputePaymentBehavior(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pub_id = kwargs.get("publisher_id")
        if not pub_id:
            return json.dumps({"error": "publisher_id is required"}, indent=2)
        pb = next((p for p in data.get("payment_behavior", []) if p.get("publisher_id") == pub_id), None)
        return json.dumps(pb or {"error": f"payment_behavior for {pub_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "compute_payment_behavior","description": "Return stored payment behavior stats for a publisher.","parameters": {"type": "object","properties": {"publisher_id": {"type": "string"}},"required": ["publisher_id"]}}}
