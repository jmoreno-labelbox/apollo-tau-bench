# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignCourierToOrder(Tool):
    """
    Add a courier tracking ID into an order's fulfillments.
    Deterministic: requires explicit tracking_ids and item_ids.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, courier_id: str, tracking_ids: List[str], item_ids: List[str]) -> str:
        # Confirm the courier's existence and ownership of all tracking_ids.
        couriers = data.get("couriers", [])
        courier = None
        for c in couriers:
            if c.get("courier_id") == courier_id:
                courier = c
                break
        if courier is None:
            return json.dumps({"error": "Courier not found", "courier_id": courier_id})

        for t in tracking_ids:
            if t not in courier.get("tracking_ids", []):
                return json.dumps({"error": "Tracking ID not owned by courier", "courier_id": courier_id, "tracking_id": t})

        # Revise order fulfillments.
        orders = list(data.get("orders", {}).values())
        for order in orders:
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({
                    "tracking_id": tracking_ids,
                    "item_ids": item_ids
                })
                order["fulfillments"] = fulfillments
                return json.dumps({
                    "status": "success",
                    "order_id": order_id,
                    "courier_id": courier_id,
                    "fulfillments": fulfillments
                })

        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_courier_to_order",
                "description": "Assign courier tracking to an order by adding a fulfillment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "courier_id": {"type": "string"},
                        "tracking_ids": {"type": "array", "items": {"type": "string"}},
                        "item_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["order_id", "courier_id", "tracking_ids", "item_ids"]
                }
            }
        }
