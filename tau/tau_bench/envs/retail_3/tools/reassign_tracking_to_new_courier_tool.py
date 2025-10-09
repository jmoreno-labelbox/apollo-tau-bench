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

class ReassignTrackingToNewCourierTool(Tool):
    """
    Reassign an existing tracking record to a different courier, creating a new tracking id.

    Behavior:
    - Confirms the tracking record exists.
    - Confirms the new courier exists and provides an unused tracking id.
    - Updates tracking.courier_name, adds the new id to tracking.tracking_id (maintains history),
      and records 'reassigned_to_<courier>'.
    - Adds a fulfillment update to the corresponding order indicating the reassignment and new tracking id.

    Input (kwargs):
        tracking_id (str, required)     # any id currently on the record
        new_courier_name (str, required)

    Output:
        JSON string with {"order_id","old_courier","new_courier","new_tracking_id"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, new_courier_name: str = None) -> str:
        if not tracking_id or not new_courier_name:
            payload = {"error": "tracking_id and new_courier_name are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        tracking_db = _convert_db_to_list(data.get("tracking", {}))
        rec = next(
            (t for t in tracking_db if tracking_id in (t.get("tracking_id") or [])), None
        )
        if not rec:
            payload = {"error": f"tracking_id '{tracking_id}' not found in tracking"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        old_courier = rec.get("courier_name")

        couriers = data.get("couriers", [])
        new_courier = next(
            (c for c in couriers if c.get("name") == new_courier_name), None
        )
        if not new_courier:
            payload = {"error": f"courier '{new_courier_name}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        used_tids = {tid for t in tracking_db for tid in (t.get("tracking_id") or [])}
        new_tid = next(
            (t for t in new_courier.get("tracking_ids", []) if t not in used_tids), None
        )
        if not new_tid:
            payload = {"error": f"No available tracking_id for courier '{new_courier_name}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        rec["courier_name"] = new_courier_name
        rec.setdefault("tracking_id", []).append(new_tid)
        rec.setdefault("status_history", []).append(
            {"status": f"reassigned_to_{new_courier_name}", "timestamp": _now_iso()}
        )

        order_id = rec.get("order_id")
        if order_id:
            orders = data.get("orders", [])
            order = next((o for o in orders if o.get("order_id") == order_id), None)
            if order:
                order.setdefault("fulfillments", []).append(
                    {
                        "status": "carrier_reassigned",
                        "tracking_id": new_tid,
                        "courier": new_courier_name,
                        "timestamp": _now_iso(),
                    }
                )
        payload = {
                "order_id": order_id,
                "old_courier": old_courier,
                "new_courier": new_courier_name,
                "new_tracking_id": new_tid,
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
                "name": "reassignTrackingToNewCourier",
                "description": "Reassign a tracking record to a different courier and append the new tracking id; mirror change to order fulfillments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "new_courier_name": {"type": "string"},
                    },
                    "required": ["tracking_id", "new_courier_name"],
                },
            },
        }
