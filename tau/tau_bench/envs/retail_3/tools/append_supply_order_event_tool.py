# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppendSupplyOrderEventTool(Tool):
    """
    Append an event note to a supply order's 'events' list in supply_orders.json.

    Behavior:
    - Validates that the supply_order_id exists.
    - Appends an event object:
        {
          "type": "<string>",
          "message": "<string>",
          "timestamp": "UTC ISO"
        }
    - Creates the 'events' list if it does not exist.

    Input (kwargs):
        supply_order_id (str, required)
        event_type (str, required)
        message (str, required)

    Output:
        JSON string with {"supply_order_id","events_len"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        so_id = kwargs.get("supply_order_id")
        event_type = kwargs.get("event_type")
        message = kwargs.get("message")

        if not so_id or not event_type or not message:
            return json.dumps(
                {"error": "supply_order_id, event_type, and message are required"},
                indent=2,
            )

        supply_orders = data.get("supply_orders", [])
        so = next((s for s in supply_orders if s.get("supply_order_id") == so_id), None)
        if not so:
            return json.dumps({"error": f"supply_order_id '{so_id}' not found"}, indent=2)

        event = {
            "type": str(event_type),
            "message": str(message),
            "timestamp": _now_iso(),
        }
        so.setdefault("events", []).append(event)

        return json.dumps(
            {"supply_order_id": so_id, "events_len": len(so.get("events", []))},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_supply_order_event",
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
