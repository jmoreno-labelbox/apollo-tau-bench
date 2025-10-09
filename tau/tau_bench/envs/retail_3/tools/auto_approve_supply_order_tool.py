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

class AutoApproveSupplyOrderTool(Tool):
    """
    Automatically authorize a pending supply order and log an approval event.

    Behavior:
    - Confirms that the supply order exists and is in 'pending' status.
    - Changes status to 'approved'.
    - Adds an event {type: "approved", message: <optional reason>, timestamp: UTC ISO}.

    Input (kwargs):
        supply_order_id (str, required)
        reason (str, optional)

    Output:
        JSON string with {"supply_order_id","status","events_len"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, reason: str = None) -> str:
        so_id = supply_order_id

        if not so_id:
            payload = {"error": "supply_order_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        supply_orders = data.get("supply_orders", {}).values()
        so = next((s for s in supply_orders.values() if s.get("supply_order_id") == so_id), None)
        if not so:
            payload = {"error": f"supply_order_id '{so_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if so.get("status") != "pending":
            payload = {
                    "error": f"status must be 'pending' to auto-approve (found '{so.get('status')}')"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        so["status"] = "approved"
        event = {
            "type": "approved",
            "message": reason or "auto-approved",
            "timestamp": _now_iso(),
        }
        (so.setdefault("events", [])).append(event)
        payload = {
                "supply_order_id": so_id,
                "status": "approved",
                "events_len": len(so.get("events", [])),
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
                "name": "AutoApproveSupplyOrder",
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
