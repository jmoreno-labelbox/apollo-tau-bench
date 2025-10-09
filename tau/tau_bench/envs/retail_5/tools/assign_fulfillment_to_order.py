from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class AssignFulfillmentToOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, courier_id: str = None, delivery_options: str = "standard") -> str:
        if not order_id or not courier_id:
            payload = {"error": "order_id and courier_id are required"}
            out = json.dumps(payload)
            return out

        order = next((o for o in data["orders"].values() if o["order_id"] == order_id), None)
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        if order["status"] != "processing":
            payload = {"error": f'Order status is not processing, but {order["status"]}'}
            out = json.dumps(
                payload)
            return out

        ord_split = order_id.split("_")

        tracking_id = ord_split[1] if len(ord_split) > 1 else f"{generate_unique_id()}"
        item_ids = [item["item_id"] for item in order["items"]]

        fulfillment = {"tracking_id": [tracking_id], "item_ids": item_ids}
        order["fulfillments"].append(fulfillment)

        new_tracking_record = {
            "tracking_id": [tracking_id],
            "item_ids": item_ids,
            "address": order["address"],
            "delivery_carrier": courier_id,
            "delivery_options": delivery_options,
            "order_id": order_id,
            "tracking_history": {"received": get_current_timestamp()},
        }
        data["tracking"][tracking_id] = new_tracking_record

        courier = next(
            (c for c in data["couriers"].values() if c["courier_id"] == courier_id), None
        )
        if courier:
            courier["tracking_ids"].append(tracking_id)

        order["status"] = "processed"
        payload = {
                "success": True,
                "order_id": order_id,
                "tracking_id": tracking_id,
                "new_status": "processed",
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
                "name": "assignFulfillmentToOrder",
                "description": "Assigns a courier and creates tracking for a processed order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "courier_id": {"type": "string"},
                        "delivery_options": {"type": "string"},
                    },
                    "required": ["order_id", "courier_id"],
                },
            },
        }
