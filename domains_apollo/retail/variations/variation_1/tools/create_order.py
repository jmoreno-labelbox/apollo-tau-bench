from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, item_ids: list[str], payment_method_id: str
    ) -> str:
        pass
        users = data["users"]
        orders = data["orders"]
        products = data["products"]

        items = []

        for product in products:
            for item_id, item in product["variants"].items():
                if item_id in item_ids:
                    item_info = {
                        "item_id": item_id,
                        "product_id": product["product_id"],
                        "name": product["name"],
                        "price": item["price"],
                        "options": item["options"],
                    }
                    items.append(item_info)

        #Verify if the user is present
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        if len(user) == 0:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out
        user = user[0]

        #Verify if the payment method is available
        if payment_method_id not in user["payment_methods"]:
            payload = {"error": "Payment method not found"}
            out = json.dumps(payload)
            return out

        #Compute the total cost of the items
        total_price = 0
        for item in items:
            total_price += item["price"]

        #Verify if the payment method is a gift card and has sufficient balance
        payment_method = user["payment_methods"][payment_method_id]
        if payment_method["source"] == "gift_card":
            if payment_method["balance"] < total_price:
                payload = {"error": "insufficient gift card balance to pay for the order"}
                out = json.dumps(
                    payload)
                return out
            else:
                payment_method["balance"] -= total_price
                payment_method["balance"] = round(payment_method["balance"], 2)

        payment = {
            "transaction_type": "payment",
            "amount": total_price,
            "payment_method_id": payment_method_id,
        }

        #Initiate a new order
        order_id = f"#W{len(orders) + 1:07d}"
        order = {
            "order_id": order_id,
            "user_id": user_id,
            "items": items,
            "address": user.get("address", {}),
            "fulfilments": [],
            "status": "pending",
            "payment_history": [payment],
            "timestamp": "2025-07-15T03:35:22.797102",  #Constant timestamp for consistency
        }

        #Include the order in the user's orders and the overall orders list
        orders.append(order)
        user.setdefault("orders", []).append(order_id)
        payload = order
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrder",
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
                                "type": "string",
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
