from tau_bench.envs.tool import Tool
import json
from typing import Any

class ProcessItemExchange(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        item_ids: list[str],
        new_item_ids: list[str],
        payment_method_id: str,
    ) -> str:
        pass
        orders = data["orders"]
        order = [row for row in orders if row["order_id"] == order_id]

        if len(order) > 1:
            payload = {"error": "Multiple orders found"}
            out = json.dumps(payload)
            return out
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        order = order[0]

        #Verify if the item is present in the order
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

        #Verify if the gift card has sufficient balance
        user_id = order["user_id"]
        users = data["users"]
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        if not user:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out
        user = user[0]

        payment_method = user["payment_methods"].get(payment_method_id)
        if not payment_method:
            payload = {"error": "Payment method not found"}
            out = json.dumps(payload)
            return out

        if payment_method_id[:9] == "gift_card":
            if payment_method["balance"] < exchange_cost:
                payload = {"error": "Insufficient gift card balance to pay for the exchange"}
                out = json.dumps(
                    payload)
                return out

            payment_method["balance"] -= exchange_cost
            payment_method["balance"] = round(payment_method["balance"], 2)

        payment_info = {
            "transaction_type": (
                "exchange_payment" if exchange_cost > 0 else "exchange_refund"
            ),
            "amount": abs(exchange_cost),
            "payment_method_id": payment_method_id,
        }
        order["payment_history"].append(payment_info)
        payload = payment_info
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessItemExchange",
                "description": "Process an item exchange for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to process the exchange for.",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "The ID of the item to be exchanged.",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the exchange.",
                        },
                    },
                    "required": ["order_id", "item_id", "reason"],
                },
            },
        }
