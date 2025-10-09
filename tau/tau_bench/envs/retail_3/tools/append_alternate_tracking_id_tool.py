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

class AppendAlternateTrackingIdTool(Tool):
    """
    Add an alternate tracking_id to an existing tracking record.

    Behavior:
    - Confirms that tracking_id exists in tracking data.
    - Retrieves courier_name from the record.
    - Obtains an unused tracking_id from the same courier.
    - Adds the new tracking_id and records 'alt_tracking_added' in status_history.
    """

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None) -> str:
        original_tid = tracking_id
        if not original_tid:
            payload = {"error": "tracking_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        tracking = data.get("tracking", [])
        rec = next(
            (t for t in tracking if original_tid in (t.get("tracking_id") or [])), None
        )
        if not rec:
            payload = {
                    "error": f"tracking_id '{original_tid}' not found in tracking records"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        courier_name = rec.get("courier_name")
        if not courier_name:
            payload = {"error": "courier_name is missing on the tracking record"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        couriers = data.get("couriers", [])
        courier = next((c for c in couriers if c.get("name") == courier_name), None)
        if not courier:
            payload = {"error": f"courier '{courier_name}' not found in couriers data"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        used_ids = {tid for t in tracking for tid in t.get("tracking_id", [])}
        candidate_ids = courier.get("tracking_ids", [])
        new_tid = next((tid for tid in candidate_ids if tid not in used_ids), None)

        if not new_tid:
            payload = {"error": f"No available tracking_id for courier '{courier_name}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        rec.setdefault("tracking_id", []).append(new_tid)
        rec.setdefault("status_history", []).append(
            {"status": "alt_tracking_added", "timestamp": _now_iso()}
        )
        payload = {
                "original_tracking_id": original_tid,
                "added_tracking_id": new_tid,
                "all_tracking_ids": rec.get("tracking_id", []),
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
                "name": "appendAlternateTrackingId",
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
