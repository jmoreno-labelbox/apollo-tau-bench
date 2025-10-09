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

class AppendSupplyOrderEventTool(Tool):
    """
    Add an event note to a supply order's 'events' list in supply_orders.json.

    Behavior:
    - Confirms that the supply_order_id exists.
    - Adds an event object:
        {
          "type": "<string>",
          "message": "<string>",
          "timestamp": "UTC ISO"
        }
    - Creates the 'events' list if it is not already present.

    Input (kwargs):
        supply_order_id (str, required)
        event_type (str, required)
        message (str, required)

    Output:
        JSON string with {"supply_order_id","events_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, event_type: str = None, message: str = None) -> str:
        so_id = supply_order_id
        event_type = event_type
        message = message

        if not so_id or not event_type or not message:
            payload = {"error": "supply_order_id, event_type, and message are required"}
            out = json.dumps(
                payload, indent=2,
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

        event = {
            "type": str(event_type),
            "message": str(message),
            "timestamp": _now_iso(),
        }
        so.setdefault("events", []).append(event)
        payload = {"supply_order_id": so_id, "events_len": len(so.get("events", []))}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendSupplyOrderEvent",
                "description": "Append a typed event with message to a supply order's events array (supply_orders.json).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["supply_order_id", "event_type", "message"],
                },
            },
        }
