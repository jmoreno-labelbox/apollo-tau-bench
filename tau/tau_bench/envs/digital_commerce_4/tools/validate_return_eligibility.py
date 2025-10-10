# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateReturnEligibility(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any) -> str:
        if not order_id:
            return json.dumps({"error": "order_id is required."}, indent=2)
        order_id = _as_id(order_id)
        order = next(
            (o for o in list(data.get("orders", {}).values()) if _as_id(o.get("order_id")) == order_id), None
        )
        if not order:
            return json.dumps({}, indent=2)
        status = str(order.get("status", ""))
        eligible_statuses = {"Delivered", "Completed"}  # align with SOP
        eligible = status in eligible_statuses
        out = {"order_id": order_id, "status": status, "eligible": eligible}
        if not eligible:
            out["reason"] = "Order status is not eligible for return."
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_return_eligibility",
                "description": "Check if an order is eligible for return based on status (Delivered/Completed).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Order to check."}
                    },
                    "required": ["order_id"],
                },
            },
        }
