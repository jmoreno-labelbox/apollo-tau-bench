from tau_bench.envs.tool import Tool
import json
from typing import Any

class SplitOrderFulfillment(Tool):
    """Establish a new tracking record and fulfillment for a selection of items, based on the given tracking_id and courier_id."""

    @staticmethod
    def invoke(
        data, 
        order_id: str, 
        item_ids: list = [], 
        tracking_id: str = None, 
        courier_id: str = None, 
        delivery_options: str = "Standard", 
        address: str = None
    ) -> str:
        if not order_id or not item_ids or not tracking_id or not courier_id:
            payload = {"error": "order_id, item_ids, tracking_id, courier_id are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        order = _find_order(data, order_id)
        if not order:
            payload = {"error": f"order_id {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        # Establish or replace tracking record
        tr_list = data.setdefault("tracking", [])
        tr = _find_tracking(data, tracking_id)
        if not tr:
            tr = {
                "tracking_id": [tracking_id],
                "item_ids": item_ids,
                "address": address or order.get("address"),
                "delivery_carrier": courier_id,
                "delivery_options": delivery_options,
                "order_id": order_id,
                "tracking_history": {},
            }
            data["tracking"][tr["tracking_id"]] = tr
        else:
            tr["item_ids"] = item_ids
            tr["delivery_carrier"] = courier_id
            tr["delivery_options"] = delivery_options
            tr["order_id"] = order_id
            tr["address"] = address or order.get("address")
        # Connect to order fulfillments
        fl = _ensure_list(order, "fulfillments")
        payload = {"tracking_id": [tracking_id], "item_ids": item_ids}
        if payload not in fl:
            fl.append(payload)
        payload = {
            "success": True,
            "order_id": order_id,
            "tracking_id": tracking_id,
            "courier_id": courier_id,
            "item_ids": item_ids,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "splitOrderFulfillment",
                "description": "Create a tracking record and link a subset of items to it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "tracking_id": {"type": "string"},
                        "courier_id": {"type": "string"},
                        "delivery_options": {"type": "string"},
                        "address": {"type": "object"},
                    },
                    "required": ["order_id", "item_ids", "tracking_id", "courier_id"],
                },
            },
        }
