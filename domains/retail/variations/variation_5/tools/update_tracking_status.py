from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class UpdateTrackingStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, status: str = None) -> str:
        if not tracking_id or not status:
            payload = {"error": "tracking_id and status are required"}
            out = json.dumps(payload)
            return out

        tracking_data = data["tracking"]
        tracking_info = next(
            (t for t in tracking_data if tracking_id in t["tracking_id"]), None
        )

        if not tracking_info:
            payload = {"error": "Tracking information not found"}
            out = json.dumps(payload)
            return out

        if "tracking_history" not in tracking_info:
            tracking_info["tracking_history"] = {}

        tracking_info["tracking_history"][status] = get_current_timestamp()
        payload = {
                "success": True,
                "tracking_id": tracking_id,
                "new_status": status,
                "updated_at": get_current_timestamp(),
                "tracking_history": tracking_info["tracking_history"],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateTrackingStatus",
                "description": "Update the tracking status of a shipment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {
                            "type": "string",
                            "description": "Tracking ID to update",
                        },
                        "status": {
                            "type": "string",
                            "description": "New tracking status (e.g., in_transit, delivered)",
                        },
                    },
                    "required": ["tracking_id", "status"],
                },
            },
        }
