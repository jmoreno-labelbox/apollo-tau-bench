from tau_bench.envs.tool import Tool
import json
from typing import Any

class ScheduleDelivery(Tool):
    """Establish a 'scheduled' timestamp in tracking_history."""

    @staticmethod
    def invoke(data, tracking_id: str = None, scheduled: str = None) -> str:
        if not tracking_id or not scheduled:
            payload = {"error": "tracking_id and scheduled (ISO string) are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        tr = _find_tracking(data, tracking_id)
        if not tr:
            payload = {"error": f"tracking_id {tracking_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        hist = tr.setdefault("tracking_history", {})
        hist["scheduled"] = scheduled
        payload = {"success": True, "tracking_id": tracking_id, "scheduled": scheduled}
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
                "name": "scheduleDelivery",
                "description": "Set scheduled timestamp for a tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "scheduled": {"type": "string"},
                    },
                    "required": ["tracking_id", "scheduled"],
                },
            },
        }
