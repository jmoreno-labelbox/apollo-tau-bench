from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class CancelOrderItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, item_id: str = None) -> str:
        if not order_id or not item_id:
            payload = {"error": "order_id and item_id are required"}
            out = json.dumps(payload)
            return out

        order = next((o for o in data["orders"] if o["order_id"] == order_id), None)
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out

        if order["status"] not in ["pending", "processing", "processed"]:
            payload = {
                    "error": f"Cannot cancel items from an order with status '{order['status']}'"
                }
            out = json.dumps(
                payload)
            return out

        #Identify the item for cancellation and compute the refund amount
        cancelled_item = next(
            (item for item in order["items"] if item["item_id"] == item_id), None
        )
        if not cancelled_item:
            payload = {"error": f"Item {item_id} not found in order {order_id}"}
            out = json.dumps(
                payload)
            return out

        refund_amount = cancelled_item["price"]

        #Eliminate the item from the order
        len(order["items"])
        order["items"] = [item for item in order["items"] if item["item_id"] != item_id]

        if not order["items"]:
            order["status"] = "cancelled"

        #Verify if gift card payments were made for this order and process the refund
        user = next(
            (u for u in data["users"] if u["user_id"] == order["user_id"]), None
        )
        gift_card_refund_processed = False

        if user and "payment_history" in order:
            #Search for gift card payments within the payment history
            for payment in order["payment_history"]:
                if payment.get("transaction_type") in [
                    "payment",
                    "partial_payment",
                ] and payment.get("payment_method_id", "").startswith("gift_card"):

                    payment_method_id = payment["payment_method_id"]
                    if payment_method_id in user["payment_methods"]:
                        #Reinstate the refund amount to the gift card balance
                        gift_card = user["payment_methods"][payment_method_id]
                        current_balance = gift_card.get("balance", 0)
                        gift_card["balance"] = current_balance + refund_amount
                        gift_card_refund_processed = True

                        #Record the refund in the payment history
                        order["payment_history"].append(
                            {
                                "transaction_type": "refund",
                                "amount": -refund_amount,
                                "payment_method_id": payment_method_id,
                                "reason": f"Item cancellation: {item_id}",
                                "timestamp": get_current_timestamp(),
                            }
                        )
                        break

        #If no gift card payment is detected, still document the refund in the payment history
        if not gift_card_refund_processed:
            if "payment_history" not in order:
                order["payment_history"] = []
            order["payment_history"].append(
                {
                    "transaction_type": "refund",
                    "amount": -refund_amount,
                    "reason": f"Item cancellation: {item_id}",
                    "timestamp": get_current_timestamp(),
                }
            )
        payload = {
                "success": True,
                "order_id": order_id,
                "new_status": order["status"],
                "refund_amount": refund_amount,
                "gift_card_refund_processed": gift_card_refund_processed,
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
                "name": "cancelOrderItem",
                "description": "Remove a specific item from a pending or processing order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to modify.",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "The ID of the item to remove.",
                        },
                    },
                    "required": ["order_id", "item_id"],
                },
            },
        }
