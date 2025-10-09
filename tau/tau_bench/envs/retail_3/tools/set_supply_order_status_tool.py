from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class SetSupplyOrderStatusTool(Tool):
    """
    Set or change the status of a supply order in supply_orders.json.

    Behavior:
    - Confirms that the supply_order_id exists.
    - Updates entry['status'] to the provided value.
    - If status == "received", sets 'received_at' timestamp (UTC ISO) if not already present.

    Input (kwargs):
        supply_order_id (str, required)
        status (str, required)  # e.g., "pending","approved","in_transit","received","cancelled"

    Output:
        JSON string with {"supply_order_id","status"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, status: str = None) -> str:
        so_id = supply_order_id

        if not so_id or not isinstance(status, str) or not status:
            payload = {"error": "supply_order_id and non-empty status are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        supply_orders = data.get("supply_orders", [])
        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            payload = {"error": f"supply_order_id '{so_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        so["status"] = status
        if status == "received" and not so.get("received_at"):
            so["received_at"] = _now_iso()
        payload = {"supply_order_id": so_id, "status": status}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetSupplyOrderStatus",
                "description": "Set or override the 'status' of an existing supply order (supply_orders.json).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["supply_order_id", "status"],
                },
            },
        }
