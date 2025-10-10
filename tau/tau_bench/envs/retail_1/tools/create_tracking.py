# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTracking(Tool): # WRITE
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, item_ids: List[str], courier_id: str, delivery_option: str) -> str:
        orders = data["orders"]
        order = [row for row in orders if row["order_id"] == order_id]

        couriers = data["couriers"]
        # Check if the delivery carrier exists
        courier_id_list = [row["courier_id"] for row in couriers]
        if courier_id not in courier_id_list:
            return json.dumps({"error": "Delivery carrier not found. It must be the id of a courier from the couriers database."})

        if len(order) > 1:
            return json.dumps({"error": "Multiple orders found"})
        if not order:
            return json.dumps({"error": "Order not found"})
        order = order[0]

        tracking_id = f"TRK{len(data['tracking']) + 1:07d}"

        # Add to the order db
        fulfillment = {
            "tracking_id": [tracking_id],
            "item_ids": item_ids
        }
        order.setdefault("fulfillments", []).append(fulfillment)

        # Add to the tracking db
        tracking_dict = {}
        tracking_dict["tracking_id"] = [tracking_id]
        tracking_dict["item_ids"] = item_ids
        tracking_dict["order_id"] = order_id
        tracking_dict["address"] = order.get("address", {})
        tracking_dict["delivery_carrier"] = courier_id
        tracking_dict["delivery_options"] = delivery_option
        tracking_dict["tracking_history"] = {"received": "2025-01-30T10:26:19.115651"}
        data["tracking"].append(tracking_dict)

        courier = [row for row in couriers if row["courier_id"] == courier_id]
        courier[0]["tracking_ids"].append(tracking_id)

        return json.dumps(tracking_dict)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_tracking",
                "description": "Create a new tracking entry for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to create tracking for."},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "List of item IDs associated with the tracking."},
                        "courier_id": {"type": "string", "description": "The delivery carrier for the tracking."},
                        "delivery_options": {"type": "string", "description": "Delivery options for the tracking."}
                    },
                    "required": ["order_id", "item_ids"]
                }
            }
        }
