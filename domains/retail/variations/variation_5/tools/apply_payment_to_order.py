from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class ApplyPaymentToOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, payment_method_id: str = None, shipping_address: str = None) -> str:
        if not all([order_id, payment_method_id, shipping_address]):
            payload = {
                    "error": "order_id, payment_method_id, and shipping_address are required"
                }
            out = json.dumps(
                payload)
            return out

        order = next((o for o in data["orders"] if o["order_id"] == order_id), None)
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        if order["status"] != "pending":
            payload = {"error": f'Order status is not pending, but {order["status"]}'}
            out = json.dumps(
                payload)
            return out

        user = next(
            (u for u in data["users"] if u["user_id"] == order["user_id"]), None
        )
        if not user or payment_method_id not in user["payment_methods"]:
            payload = {"error": "Invalid payment method for user"}
            out = json.dumps(payload)
            return out

        total_amount = sum(item["price"] for item in order["items"])

        #Process gift card payments independently
        if payment_method_id.startswith("gift_card"):
            #Retrieve details of the gift card payment method
            gift_card = user["payment_methods"][payment_method_id]
            gift_card_balance = gift_card.get("balance", 0)

            if gift_card_balance >= total_amount:
                #Adequate balance - subtract the amount and proceed as usual
                gift_card["balance"] = gift_card_balance - total_amount
                order["payment_history"].append(
                    {
                        "transaction_type": "payment",
                        "amount": total_amount,
                        "payment_method_id": payment_method_id,
                        "timestamp": get_current_timestamp(),
                    }
                )
                order["address"] = shipping_address
                order["status"] = "processing"
                payload = {"success": True, "order_id": order_id, "new_status": "processing"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            else:
                #Insufficient balance - utilize the entire available balance and maintain the order in pending status
                if gift_card_balance > 0:
                    order["payment_history"].append(
                        {
                            "transaction_type": "partial_payment",
                            "amount": gift_card_balance,
                            "payment_method_id": payment_method_id,
                            "timestamp": get_current_timestamp(),
                        }
                    )
                    order["address"] = shipping_address
                    order["status"] = "pending"
                    gift_card["balance"] = 0
                payload = {
                        "success": False,
                        "reason": "Insufficient gift card balance",
                        "order_id": order_id,
                        "status": "pending",
                        "remaining_amount": total_amount - gift_card_balance,
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        else:
            #Standard payment method handling
            order["payment_history"].append(
                {
                    "transaction_type": "payment",
                    "amount": total_amount,
                    "payment_method_id": payment_method_id,
                    "timestamp": get_current_timestamp(),
                }
            )
            order["address"] = shipping_address
            order["status"] = "processing"
            payload = {"success": True, "order_id": order_id, "new_status": "processing"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applyPaymentToOrder",
                "description": "Applies a payment method and shipping address to a pending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "payment_method_id": {"type": "string"},
                        "shipping_address": {"type": "object"},
                    },
                    "required": ["order_id", "payment_method_id", "shipping_address"],
                },
            },
        }
