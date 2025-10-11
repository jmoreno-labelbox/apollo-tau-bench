# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _now_iso() -> str:
    """Return current UTC timestamp in ISO format (seconds precision)."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

class ReassignTrackingToNewCourierTool(Tool):
    """
    Reassign an existing tracking record to a different courier, generating a fresh tracking id.

    Behavior:
    - Validates the tracking record exists.
    - Validates the new courier exists and provides an unused tracking id.
    - Updates tracking.courier_name, appends the new id to tracking.tracking_id (keeps history),
      and logs 'reassigned_to_<courier>'.
    - Appends a fulfillment update into the corresponding order noting the reassignment and new tracking id.

    Input (kwargs):
        tracking_id (str, required)     # any identifier presently in the database
        new_courier_name (str, required)

    Output:
        JSON string with {"order_id","old_courier","new_courier","new_tracking_id"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], new_courier_name, tracking_id) -> str:
        tid = tracking_id

        if not tid or not new_courier_name:
            return json.dumps({"error": "tracking_id and new_courier_name are required"}, indent=2)

        tracking_db = data.get("tracking", [])
        rec = next((t for t in tracking_db if tid in (t.get("tracking_id") or [])), None)
        if not rec:
            return json.dumps({"error": f"tracking_id '{tid}' not found in tracking"}, indent=2)

        old_courier = rec.get("courier_name")

        couriers = data.get("couriers", [])
        new_courier = next((c for c in couriers if c.get("name") == new_courier_name), None)
        if not new_courier:
            return json.dumps({"error": f"courier '{new_courier_name}' not found"}, indent=2)

        used_tids = {tid for t in tracking_db for tid in (t.get("tracking_id") or [])}
        new_tid = next((t for t in new_courier.get("tracking_ids", []) if t not in used_tids), None)
        if not new_tid:
            return json.dumps(
                {"error": f"No available tracking_id for courier '{new_courier_name}'"},
                indent=2,
            )

        rec["courier_name"] = new_courier_name
        rec.setdefault("tracking_id", []).append(new_tid)
        rec.setdefault("status_history", []).append(
            {"status": f"reassigned_to_{new_courier_name}", "timestamp": _now_iso()}
        )

        order_id = rec.get("order_id")
        if order_id:
            orders = list(list(list(data.get("orders", {}).values())) if isinstance(data.get("orders"), dict) else data.get("orders", []))
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

        return json.dumps(
            {
                "order_id": order_id,
                "old_courier": old_courier,
                "new_courier": new_courier_name,
                "new_tracking_id": new_tid,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reassign_tracking_to_new_courier",
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