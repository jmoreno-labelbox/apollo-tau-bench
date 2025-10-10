# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProcessItemExchange(Tool): # CREATE
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, item_ids: list[str], new_item_ids: list[str], payment_method_id: str) -> str:
        orders = data["orders"]
        order = [row for row in orders if row["order_id"] == order_id]


        if len(order) > 1:
            return json.dumps({"error": "Multiple orders found"})
        if not order:
            return json.dumps({"error": "Order not found"})
        order = order[0]

        # Verify the presence of the item in the order.
        items = order.get("items", [])

        removed_price = 0.0
        for item in items:
            if item["item_id"] in item_ids:
                removed_price += item["price"]

        for item in items:
            if item["item_id"] in item_ids:
                items.remove(item)

        products = data["products"]

        added_price = 0.0
        for product in products:
            for item_id, item in product["variants"].items():
                if item_id in new_item_ids:
                    item_info = {
                        "item_id": item_id,
                        "product_id": product["product_id"],
                        "name": product["name"],
                        "price": item["price"],
                        "options": item["options"],
                    }
                    added_price += item["price"]
                    items.append(item_info)

        exchange_cost = added_price - removed_price

        # Verify if the gift card balance is sufficient.
        user_id = order["user_id"]
        users = data["users"]
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        if not user:
            return json.dumps({"error": "User not found"})
        user = user[0]

        payment_method = user["payment_methods"].get(payment_method_id)
        if not payment_method:
            return json.dumps({"error": "Payment method not found"})

        if payment_method_id[:9] == "gift_card":
            if payment_method["balance"] < exchange_cost:
                return json.dumps({"error": "Insufficient gift card balance to pay for the exchange"})

            payment_method["balance"] -= exchange_cost
            payment_method["balance"] = round(payment_method["balance"], 2)

        payment_info = {
            "transaction_type": "exchange_payment" if exchange_cost > 0 else "exchange_refund",
            "amount": abs(exchange_cost),
            "payment_method_id": payment_method_id,
        }
        order["payment_history"].append(payment_info)



        return json.dumps(payment_info)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_item_exchange",
                "description": "Process an item exchange for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to process the exchange for."},
                        "item_id": {"type": "string", "description": "The ID of the item to be exchanged."},
                        "reason": {"type": "string", "description": "The reason for the exchange."}
                    },
                    "required": ["order_id", "item_id", "reason"]
                }
            }
        }
