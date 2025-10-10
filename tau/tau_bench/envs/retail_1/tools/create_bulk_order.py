# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateBulkOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, item_ids: List[Dict[str, Any]], payment_method_id: str) -> str:
        users = data["users"]
        orders = data["orders"]
        products = data["products"]

        items = []

        for product in products:
            for item_id, item in product["variants"].items():
                if item_id in item_ids.keys():
                    item_info = {
                        "item_id": item_id,
                        "product_id": product["product_id"],
                        "name": product["name"],
                        "price": item["price"],
                        "options": item["options"],
                    }
                    for _ in range(item_ids[item_id]):  # Insert the item repeatedly according to the specified quantity.
                        items.append(item_info)

        # Verify the existence of the user.
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        if len(user) == 0:
            return json.dumps({"error": "User not found"})
        user = user[0]

        # Verify the existence of the payment method.
        if payment_method_id not in user["payment_methods"]:
            return json.dumps({"error": "Payment method not found"})

        # Determine the overall cost of the items.
        total_price = 0
        for item in items:
            total_price += item["price"]

        # Verify if the payment method is a gift card and if it contains sufficient balance.
        payment_method = user["payment_methods"][payment_method_id]
        if payment_method["source"] == "gift_card":
            if payment_method["balance"] < total_price:
                return json.dumps({"error": "insufficient gift card balance to pay for the order"})
            else:
                payment_method["balance"] -= total_price
                payment_method["balance"] = round(payment_method["balance"], 2)

        payment = {
            "transaction_type": "payment",
            "amount": total_price,
            "payment_method_id": payment_method_id,
        }

        # Initiate a new order.
        order_id = f"#W{len(orders) + 1:07d}"
        order = {
            "order_id": order_id,
            "user_id": user_id,
            "items": items,
            "address": user.get("address", {}),
            "fulfilments": [],
            "status": "pending",
            "payment_history": [payment],
            "timestamp": "2025-07-15T03:35:22.797102" # Set a fixed timestamp to ensure consistency.
        }

        # Include the order in both the user's order list and the global orders array.
        orders.append(order)
        user.setdefault("orders", []).append(order_id)

        return json.dumps(order)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_bulk_order",
                "description": "Create a new order for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user id, such as 'sara_doe_496'.",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {
                                "type": "dictionary",
                                "keys": {
                                    "item_id": {"type": "string", "description": "The item id, such as 'item_0001'."},
                                },
                                "values": {
                                    "quantity": {"type": "integer", "description": "The quantity of the item to be included in the order."}
                                }
                            },
                            "description": (
                                "The item ids to be included in the order."
                            ),
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": (
                                "The payment method id to pay for the order, such as 'gift_card_0000000' or 'credit_card_0000000'. "
                                "These can be looked up from the user details."
                            ),
                        },
                    },
                    "required": ["user_id", "items", "payment_method_id"],
                },
            },
        }
