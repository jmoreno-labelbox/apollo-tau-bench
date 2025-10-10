# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddTrackingCustomEventTool(Tool):
    """
    Append a custom event to the status_history of a tracking record.

    Behavior:
    - Validates tracking_id exists in tracking.json.
    - Appends {"status": <event_status>, "timestamp": UTC ISO, "note": <optional str>}.
    - Does not modify orders.json (pure tracking enrichment).

    Input (kwargs):
        tracking_id (str, required)
        event_status (str, required)   # for example, "in_progress", "postponed", "waypoint"
        note (str, optional)

    Output:
        JSON string with {"tracking_id","new_status","history_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], event_status, note, tracking_id) -> str:

        if not tracking_id or not event_status:
            return json.dumps({"error": "tracking_id and event_status are required"}, indent=2)

        tracking = data.get("tracking", [])
        rec = next((t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None)
        if not rec:
            return json.dumps(
                {"error": f"tracking_id '{tracking_id}' not found in tracking records"},
                indent=2,
            )

        event = {"status": str(event_status), "timestamp": _now_iso()}
        if note:
            event["note"] = str(note)

        rec.setdefault("status_history", []).append(event)

        return json.dumps(
            {
                "tracking_id": tracking_id,
                "new_status": event_status,
                "history_len": len(rec.get("status_history", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_tracking_custom_event",
                "description": "Append a custom status event (with optional note) to a tracking record's status_history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "event_status": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["tracking_id", "event_status"],
                },
            },
        }
