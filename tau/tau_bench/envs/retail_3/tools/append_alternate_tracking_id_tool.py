# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _now_iso() -> str:
    """Return current UTC timestamp in ISO format (seconds precision)."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

class AppendAlternateTrackingIdTool(Tool):
    """
    Append an alternate tracking_id to an existing tracking record.

    Behavior:
    - Validates tracking_id exists in tracking data.
    - Reads courier_name from record.
    - Pulls an unused tracking_id from the same courier.
    - Appends the new tracking_id and logs 'alt_tracking_added' in status_history.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], tracking_id) -> str:
        original_tid = tracking_id
        if not original_tid:
            return json.dumps({"error": "tracking_id is required"}, indent=2)

        tracking = data.get("tracking", [])
        rec = next((t for t in tracking if original_tid in (t.get("tracking_id") or [])), None)
        if not rec:
            return json.dumps(
                {"error": f"tracking_id '{original_tid}' not found in tracking records"},
                indent=2,
            )

        courier_name = rec.get("courier_name")
        if not courier_name:
            return json.dumps({"error": "courier_name is missing on the tracking record"}, indent=2)

        couriers = data.get("couriers", [])
        courier = next((c for c in couriers if c.get("name") == courier_name), None)
        if not courier:
            return json.dumps(
                {"error": f"courier '{courier_name}' not found in couriers data"},
                indent=2,
            )

        used_ids = {tid for t in tracking for tid in t.get("tracking_id", [])}
        candidate_ids = courier.get("tracking_ids", [])
        new_tid = next((tid for tid in candidate_ids if tid not in used_ids), None)

        if not new_tid:
            return json.dumps(
                {"error": f"No available tracking_id for courier '{courier_name}'"},
                indent=2,
            )

        rec.setdefault("tracking_id", []).append(new_tid)
        rec.setdefault("status_history", []).append(
            {"status": "alt_tracking_added", "timestamp": _now_iso()}
        )

        return json.dumps(
            {
                "original_tracking_id": original_tid,
                "added_tracking_id": new_tid,
                "all_tracking_ids": rec.get("tracking_id", []),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_alternate_tracking_id",
                "description": (
                    "Append an alternate tracking_id to an existing tracking record. "
                    "Selects an unused ID from the same courier and appends it to the tracking_id list."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {
                            "type": "string",
                            "description": "An existing tracking_id that identifies the tracking record to modify.",
                        }
                    },
                    "required": ["tracking_id"],
                },
            },
        }