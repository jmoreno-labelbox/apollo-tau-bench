# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AttachCourierByNameTool(Tool):
    """
    Attach a specific courier (by name) to an order and create a tracking entry.

    Behavior:
    - Validates order exists (orders.json).
    - Validates courier exists (couriers.json).
    - Picks first unused tracking_id from the courier.
    - Writes a new record to tracking.json and appends a fulfillment entry to the order.

    Input (kwargs):
        order_id (str, required)
        courier_name (str, required)

    Output:
        JSON string with {"order_id","tracking_id","courier_name"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        courier_name = kwargs.get("courier_name")

        if not order_id or not courier_name:
            return json.dumps({"error": "order_id and courier_name are required"}, indent=2)

        orders = list(data.get("orders", {}).values())
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"order_id '{order_id}' not found"}, indent=2)

        couriers = data.get("couriers", [])
        courier = next((c for c in couriers if c.get("name") == courier_name), None)
        if not courier:
            return json.dumps({"error": f"courier '{courier_name}' not found"}, indent=2)

        used_ids = {tid for t in data.get("tracking", []) for tid in t.get("tracking_id", [])}
        candidate_ids = courier.get("tracking_ids", [])
        tid = next((tid for tid in candidate_ids if tid not in used_ids), None)

        if not tid:
            return json.dumps(
                {"error": f"No available tracking_id for courier '{courier_name}'"},
                indent=2,
            )

        tracking = data.setdefault("tracking", [])
        tracking.append(
            {
                "tracking_id": [tid],
                "order_id": order_id,
                "courier_name": courier_name,
                "status_history": [{"status": "label_created", "timestamp": _now_iso()}],
            }
        )

        order.setdefault("fulfillments", []).append(
            {
                "status": "label_created",
                "tracking_id": tid,
                "courier": courier_name,
                "timestamp": _now_iso(),
            }
        )

        return json.dumps(
            {"order_id": order_id, "tracking_id": tid, "courier_name": courier_name},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "attach_courier_by_name",
                "description": "Attach a specific courier by name to an order and create a new tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "courier_name": {"type": "string"},
                        "tracking_id": {"type": "string"},
                    },
                    "required": ["order_id", "courier_name", "tracking_id"],
                },
            },
        }
