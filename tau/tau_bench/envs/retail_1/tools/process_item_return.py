from tau_bench.envs.tool import Tool
import json
from typing import Any

class ProcessItemReturn(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any], order_id: str, item_ids: list[str], payment_method_id: str
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

        refund_amount = 0.0
        for item in items:
            if item["item_id"] in item_ids:
                refund_amount += item["price"]

        for item in items:
            if item["item_id"] in item_ids:
                items.remove(item)

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

        if payment_method["source"] == "gift_card":
            payment_method["balance"] += refund_amount
            payment_method["balance"] = round(payment_method["balance"], 2)

        #Insert a return record into the payment history
        payment_info = {
            "transaction_type": "return",
            "amount": refund_amount,
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
                "name": "ProcessItemReturn",
                "description": "Process an item return for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to process the return for.",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item IDs to be returned.",
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "The payment method ID to refund the return amount.",
                        },
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"],
                },
            },
        }
