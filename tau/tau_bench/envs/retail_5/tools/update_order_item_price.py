from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class UpdateOrderItemPrice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, item_id: str = None, new_price: float = None) -> str:
        if not all([order_id, item_id, new_price]):
            payload = {"error": "order_id, item_id, and new_price are required"}
            out = json.dumps(
                payload)
            return out

        order = next((o for o in data["orders"] if o["order_id"] == order_id), None)
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out

        if order["status"] != "pending":
            payload = {"error": "Can only update prices on pending orders."}
            out = json.dumps(payload)
            return out

        item_to_update = next(
            (item for item in order["items"] if item["item_id"] == item_id), None
        )
        if not item_to_update:
            payload = {"error": f"Item {item_id} not in order."}
            out = json.dumps(payload)
            return out

        item_to_update["price"] = new_price
        payload = {
                "success": True,
                "order_id": order_id,
                "item_id": item_id,
                "new_price": new_price,
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
                "name": "updateOrderItemPrice",
                "description": "Manually update the price of an item in a pending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "new_price": {"type": "number"},
                    },
                    "required": ["order_id", "item_id", "new_price"],
                },
            },
        }
