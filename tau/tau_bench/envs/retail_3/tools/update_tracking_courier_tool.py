from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateTrackingCourierTool(Tool):
    """
    Modify the courier_name of an existing tracking record in tracking.json.

    Behavior:
    - Confirms that tracking_id exists in tracking.json (found within each record's tracking_id list).
    - Replaces 'courier_name' with the provided value.
    - Adds a status_history note 'courier_updated'.

    Input (kwargs):
        tracking_id (str, required)
        courier_name (str, required)

    Output:
        JSON string with {"tracking_id","courier_name"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, courier_name: str = None) -> str:
        if not tracking_id or not courier_name:
            payload = {"error": "tracking_id and courier_name are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        tracking = data.get("tracking", [])
        rec = next(
            (t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None
        )
        if not rec:
            payload = {"error": f"tracking_id '{tracking_id}' not found in tracking records"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        rec["courier_name"] = courier_name
        rec.setdefault("status_history", []).append(
            {"status": "courier_updated", "timestamp": _now_iso()}
        )
        payload = {"tracking_id": tracking_id, "courier_name": courier_name}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTrackingCourier",
                "description": "Update the courier_name field for an existing tracking record (tracking.json).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "courier_name": {"type": "string"},
                    },
                    "required": ["tracking_id", "courier_name"],
                },
            },
        }
