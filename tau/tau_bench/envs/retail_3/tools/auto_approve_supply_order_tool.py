# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _now_iso() -> str:
    """Return current UTC timestamp in ISO format (seconds precision)."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

class AutoApproveSupplyOrderTool(Tool):
    """
    Automatically approve a pending supply order and register an approval event.

    Behavior:
    - Validates that the supply order exists and is in 'pending' status.
    - Sets status to 'approved'.
    - Appends an event {type: "approved", message: <optional reason>, timestamp: UTC ISO}.

    Input (kwargs):
        supply_order_id (str, required)
        reason (str, optional)

    Output:
        JSON string with {"supply_order_id","status","events_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], reason, supply_order_id) -> str:
        so_id = supply_order_id

        if not so_id:
            return json.dumps({"error": "supply_order_id is required"}, indent=2)

        supply_orders = data.get("supply_orders", [])
        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            return json.dumps({"error": f"supply_order_id '{so_id}' not found"}, indent=2)

        if so.get("status") != "pending":
            return json.dumps(
                {"error": f"status must be 'pending' to auto-approve (found '{so.get('status')}')"},
                indent=2,
            )

        so["status"] = "approved"
        event = {
            "type": "approved",
            "message": reason or "auto-approved",
            "timestamp": _now_iso(),
        }
        (so.setdefault("events", [])).append(event)

        return json.dumps(
            {
                "supply_order_id": so_id,
                "status": "approved",
                "events_len": len(so.get("events", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "auto_approve_supply_order",
                "description": "Approve a pending supply order and append an 'approved' event to its events array.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["supply_order_id"],
                },
            },
        }