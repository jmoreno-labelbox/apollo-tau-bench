from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class AttachCourierByNameTool(Tool):
    """
    Assign a specific courier (by name) to an order and generate a tracking entry.

    Behavior:
    - Confirms the order exists (orders.json).
    - Confirms the courier exists (couriers.json).
    - Selects the first available tracking_id from the courier.
    - Creates a new record in tracking.json and adds a fulfillment entry to the order.

    Input (kwargs):
        order_id (str, required)
        courier_name (str, required)

    Output:
        JSON string with {"order_id","tracking_id","courier_name"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, courier_name: str = None) -> str:
        if not order_id or not courier_name:
            payload = {"error": "order_id and courier_name are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order_id '{order_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        couriers = data.get("couriers", [])
        courier = next((c for c in couriers if c.get("name") == courier_name), None)
        if not courier:
            payload = {"error": f"courier '{courier_name}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        used_ids = {
            tid for t in data.get("tracking", []) for tid in t.get("tracking_id", [])
        }
        candidate_ids = courier.get("tracking_ids", [])
        tid = next((tid for tid in candidate_ids if tid not in used_ids), None)

        if not tid:
            payload = {"error": f"No available tracking_id for courier '{courier_name}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        tracking = data.setdefault("tracking", [])
        tracking.append(
            {
                "tracking_id": [tid],
                "order_id": order_id,
                "courier_name": courier_name,
                "status_history": [
                    {"status": "label_created", "timestamp": _now_iso()}
                ],
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
        payload = {"order_id": order_id, "tracking_id": tid, "courier_name": courier_name}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "attachCourierByName",
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
