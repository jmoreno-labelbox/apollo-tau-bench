from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class CreatePendingOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, item_details: list[dict[str, Any]] = None) -> str:
        if not user_id or not item_details:
            payload = {"error": "user_id and item_details are required"}
            out = json.dumps(payload)
            return out

        user = next((u for u in data["users"].values() if u["user_id"] == user_id), None)
        if not user:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out

        order_items, total_amount = [], 0.0
        order_string = ""
        for detail in item_details:
            item_id, quantity = detail["item_id"], detail.get("quantity", 1)
            found_item = None
            for p in data["products"].values():
                if item_id in p["variants"]:
                    variant = p["variants"][item_id]
                    if variant["available"]:
                        price = variant["price"] * quantity
                        found_item = {
                            "name": p["name"],
                            "product_id": p["product_id"],
                            "item_id": item_id,
                            "price": price,
                            "options": variant["options"],
                        }
                        total_amount += price
                        order_string += f"{item_id}"
                    break
            if not found_item:
                payload = {"error": f"Item {item_id} is not available"}
                out = json.dumps(payload)
                return out
            order_items.append(found_item)

        order_id = f"#W{generate_unique_id()}_{order_string}"
        new_order = {
            "order_id": order_id,
            "user_id": user_id,
            "address": None,
            "items": order_items,
            "fulfillments": [],
            "status": "pending",
            "payment_history": [],
            "timestamp": get_current_timestamp(),
        }

        existing_order_index = next(
            (i for i, o in enumerate(data["orders"]) if o["order_id"] == order_id), None
        )
        if existing_order_index is not None:
            data["orders"][existing_order_index] = new_order
        else:
            data["orders"][order_id] = new_order
        payload = {"success": True, "order_id": order_id, "total_amount": total_amount}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createPendingOrder",
                "description": 'Creates a new order with a "pending" status without payment or shipping.',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "item_details": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                            },
                        },
                    },
                    "required": ["user_id", "item_details"],
                },
            },
        }
