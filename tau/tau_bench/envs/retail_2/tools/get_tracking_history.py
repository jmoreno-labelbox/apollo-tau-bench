# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTrackingHistory(Tool):
    """Retrieve tracking history for a given order_id from tracking.json records."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        tracking_records = data.get("tracking", [])
        # Entries in tracking.json are expected to contain: order_id, tracking_history, tracking_id[], address, among others.
        for rec in tracking_records:
            if rec.get("order_id") == order_id:
                return json.dumps({
                    "order_id": order_id,
                    "tracking_id": rec.get("tracking_id"),
                    "delivery_carrier": rec.get("delivery_carrier"),
                    "tracking_history": rec.get("tracking_history", {})
                })
        return json.dumps({"error": "Tracking record not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_tracking_history",
                "description": "Get tracking history for an order from tracking.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"}
                    },
                    "required": ["order_id"]
                }
            }
        }
