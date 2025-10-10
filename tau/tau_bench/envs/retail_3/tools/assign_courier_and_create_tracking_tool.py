# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignCourierAndCreateTrackingTool(Tool):
    """
    Assign a courier to an order and create a tracking entry in tracking.json.

    Behavior:
    - Reads the order (orders.json) and user's country (users.json) to choose a courier from couriers.json.
    - Picks the first unused tracking_id from the chosen courier's tracking_ids.
    - Writes a new entry to tracking.json:
        {
          "tracking_id": [ "<id>" ],
          "order_id": "...",
          "courier_name": "...",
          "status_history": [{ "status": "label_created", "timestamp": "UTC ISO" }]
        }
    - Also appends a fulfillment snippet to the order in orders.json:
        {
          "status": "label_created",
          "tracking_id": "<id>",
          "courier": "<courier_name>",
          "timestamp": "UTC ISO"
        }

    Input (kwargs):
        order_id (str, required)

    Output:
        JSON string with {"order_id","tracking_id","courier_name"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        if not order_id:
            return json.dumps({"error": "order_id is required"}, indent=2)

        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == order.get("user_id")), None)
        if not user:
            return json.dumps({"error": f"user '{order.get('user_id')}' not found"}, indent=2)

        country = ((user.get("address") or {}).get("country")) or "USA"
        couriers = data.get("couriers", [])
        courier = next(
            (c for c in couriers if country in (c.get("coverage_area") or [])),
            couriers[0] if couriers else None,
        )
        if not courier:
            return json.dumps({"error": f"No courier covers '{country}'"}, indent=2)

        used = {tid for t in data.get("tracking", []) for tid in t.get("tracking_id", [])}
        tid = next((tid for tid in courier.get("tracking_ids", []) if tid not in used), None)
        if not tid:
            return json.dumps(
                {"error": f"No available tracking_id for courier '{courier.get('name')}'"}, indent=2
            )

        data.setdefault("tracking", []).append(
            {
                "tracking_id": [tid],
                "order_id": order_id,
                "courier_name": courier.get("name"),
                "status_history": [{"status": "label_created", "timestamp": _now_iso()}],
            }
        )

        order.setdefault("fulfillments", []).append(
            {
                "status": "label_created",
                "tracking_id": tid,
                "courier": courier.get("name"),
                "timestamp": _now_iso(),
            }
        )

        return json.dumps(
            {
                "order_id": order_id,
                "tracking_id": tid,
                "courier_name": courier.get("name"),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_courier_and_create_tracking",
                "description": "Assign a courier based on user's country and create a new tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Target order_id in orders.json.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }
