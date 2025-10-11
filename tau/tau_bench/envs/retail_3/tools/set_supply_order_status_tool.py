# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _now_iso() -> str:
    """Return current UTC timestamp in ISO format (seconds precision)."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

class SetSupplyOrderStatusTool(Tool):
    """
    Set or override the status of a supply order in supply_orders.json.

    Behavior:
    - Validates that the supply_order_id exists.
    - Sets entry['status'] = provided value.
    - If status == "received", sets 'received_at' timestamp (UTC ISO) when not present.

    Input (kwargs):
        supply_order_id (str, required)
        status (str, required)  # for example, "pending", "approved", "in_transit", "received", "cancelled"

    Output:
        JSON string with {"supply_order_id","status"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], status, supply_order_id) -> str:
        so_id = supply_order_id

        if not so_id or not isinstance(status, str) or not status:
            return json.dumps(
                {"error": "supply_order_id and non-empty status are required"}, indent=2
            )

        supply_orders = data.get("supply_orders", [])
        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            return json.dumps({"error": f"supply_order_id '{so_id}' not found"}, indent=2)

        so["status"] = status
        if status == "received" and not so.get("received_at"):
            so["received_at"] = _now_iso()

        return json.dumps({"supply_order_id": so_id, "status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_supply_order_status",
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