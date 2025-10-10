# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProcessItemReturn(Tool): # WRITE
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, item_ids: list[str], payment_method_id: str) -> str:
        orders = data["orders"]
        order = [row for row in orders if row["order_id"] == order_id]

        if len(order) > 1:
            return json.dumps({"error": "Multiple orders found"})
        if not order:
            return json.dumps({"error": "Order not found"})
        order = order[0]

        # Check if the item exists in the order
        items = order.get("items", [])

        refund_amount = 0.0
        for item in items:
            if item["item_id"] in item_ids:
                refund_amount += item["price"]

        for item in items:
            if item["item_id"] in item_ids:
                items.remove(item)

        # Check if the gift card has enough balance
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

        if payment_method["source"] == "gift_card":
            payment_method["balance"] += refund_amount
            payment_method["balance"] = round(payment_method["balance"], 2)

        # Add a return entry to the payment history
        payment_info = {
            "transaction_type": "return",
            "amount": refund_amount,
            "payment_method_id": payment_method_id,
        }
        order["payment_history"].append(payment_info)

        return json.dumps(payment_info)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_item_return",
                "description": "Process an item return for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to process the return for."},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "List of item IDs to be returned."},
                        "payment_method_id": {"type": "string", "description": "The payment method ID to refund the return amount."}
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"]
                }
            }
        }
