from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReassignCourierForTracking(Tool):
    """Modify the delivery_carrier for a current tracking record."""

    @staticmethod
    def invoke(data, tracking_id: str = None, courier_id: str = None) -> str:
        if not tracking_id or not courier_id:
            payload = {"error": "tracking_id and courier_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        tr = _find_tracking(data, tracking_id)
        if not tr:
            payload = {"error": f"tracking_id {tracking_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        tr["delivery_carrier"] = courier_id
        payload = {"success": True, "tracking_id": tracking_id, "courier_id": courier_id}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "reassignCourierForTracking",
                "description": "Update delivery_carrier for a tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "courier_id": {"type": "string"},
                    },
                    "required": ["tracking_id", "courier_id"],
                },
            },
        }
