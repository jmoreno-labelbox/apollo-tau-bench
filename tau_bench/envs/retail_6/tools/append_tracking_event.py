from tau_bench.envs.tool import Tool
import json
from typing import Any

class AppendTrackingEvent(Tool):
    """Insert or replace an event timestamp in tracking_history for a tracking id (key -> timestamp)."""

    @staticmethod
    def invoke(data, tracking_id=None, event=None, timestamp=None) -> str:
        if not tracking_id or not event or not timestamp:
            payload = {"error": "tracking_id, event, timestamp are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        t = _find_tracking(data, tracking_id)
        if not t:
            payload = {"error": f"tracking_id {tracking_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        history = t.setdefault("tracking_history", {})
        history[event] = timestamp
        payload = {
                "success": True,
                "tracking_id": tracking_id,
                "event": event,
                "timestamp": timestamp,
            }
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
                "name": "appendTrackingEvent",
                "description": "Set an event timestamp in tracking.tracking_history for a given tracking_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "event": {"type": "string"},
                        "timestamp": {"type": "string"},
                    },
                    "required": ["tracking_id", "event", "timestamp"],
                },
            },
        }
