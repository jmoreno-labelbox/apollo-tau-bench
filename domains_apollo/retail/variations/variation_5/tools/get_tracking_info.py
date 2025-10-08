from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetTrackingInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, order_id: str = None) -> str:
        if not tracking_id and not order_id:
            payload = {"error": "Either tracking_id or order_id is required"}
            out = json.dumps(payload)
            return out

        tracking_data = data["tracking"]

        if tracking_id:
            tracking_info = next(
                (t for t in tracking_data if tracking_id in t["tracking_id"]), None
            )
        else:
            tracking_info = next(
                (t for t in tracking_data if t["order_id"] == order_id), None
            )

        if not tracking_info:
            payload = {"error": "Tracking information not found"}
            out = json.dumps(payload)
            return out
        payload = tracking_info
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTrackingInfo",
                "description": "Get tracking information for an order by tracking ID or order ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {
                            "type": "string",
                            "description": "Tracking ID to look up",
                        },
                        "order_id": {
                            "type": "string",
                            "description": "Order ID to get tracking for",
                        },
                    },
                },
            },
        }
