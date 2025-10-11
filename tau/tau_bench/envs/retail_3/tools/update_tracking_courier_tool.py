# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _now_iso() -> str:
    """Return current UTC timestamp in ISO format (seconds precision)."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

class UpdateTrackingCourierTool(Tool):
    """
    Update the courier_name of an existing tracking record in tracking.json.

    Behavior:
    - Validates tracking_id exists in tracking.json (present inside each record's tracking_id list).
    - Overwrites 'courier_name' with the provided value.
    - Appends a status_history note 'courier_updated'.

    Input (kwargs):
        tracking_id (str, required)
        courier_name (str, required)

    Output:
        JSON string with {"tracking_id","courier_name"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], courier_name, tracking_id) -> str:

        if not tracking_id or not courier_name:
            return json.dumps({"error": "tracking_id and courier_name are required"}, indent=2)

        tracking = data.get("tracking", [])
        rec = next((t for t in tracking if tracking_id in (t.get("tracking_id") or [])), None)
        if not rec:
            return json.dumps(
                {"error": f"tracking_id '{tracking_id}' not found in tracking records"},
                indent=2,
            )

        rec["courier_name"] = courier_name
        rec.setdefault("status_history", []).append(
            {"status": "courier_updated", "timestamp": _now_iso()}
        )

        return json.dumps(
            {"tracking_id": tracking_id, "courier_name": courier_name},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_tracking_courier",
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