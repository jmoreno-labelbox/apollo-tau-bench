from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddTrackingCustomEventTool(Tool):
    """
    Add a custom event to the status_history of a tracking record.

    Behavior:
    - Confirms that tracking_id exists in tracking.json.
    - Adds {"status": <event_status>, "timestamp": UTC ISO, "note": <optional str>}.
    - Does not alter orders.json (pure tracking enhancement).

    Input (kwargs):
        tracking_id (str, required)
        event_status (str, required)   # e.g., "in_transit", "delayed", "checkpoint"
        note (str, optional)

    Output:
        JSON string with {"tracking_id","new_status","history_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, event_status: str = None, note: str = None) -> str:
        if not tracking_id or not event_status:
            payload = {"error": "tracking_id and event_status are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        tracking = data.get("tracking", {}).values()
        rec = next(
            (t for t in tracking.values() if tracking_id in (t.get("tracking_id") or [])), None
        )
        if not rec:
            payload = {"error": f"tracking_id '{tracking_id}' not found in tracking records"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        event = {"status": str(event_status), "timestamp": _now_iso()}
        if note:
            event["note"] = str(note)

        rec.setdefault("status_history", []).append(event)
        payload = {
                "tracking_id": tracking_id,
                "new_status": event_status,
                "history_len": len(rec.get("status_history", [])),
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
                "name": "AddTrackingCustomEvent",
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
