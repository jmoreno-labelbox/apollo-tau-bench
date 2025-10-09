from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class AdjustOrderPayment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, payment_method_id: str = None) -> str:
        if not order_id or not payment_method_id:
            payload = {"error": "order_id and payment_method_id are required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        users = data["users"]

        order = next((o for o in orders if o["order_id"] == order_id), None)
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out

        # Determine the current total of items within the order
        current_total = sum(item["price"] for item in order["items"])

        # Compute the total amount that has been paid so far
        paid_amount = 0.0
        if "payment_history" in order:
            for transaction in order["payment_history"]:
                if (
                    transaction.get("transaction_type") == "payment"
                    or transaction.get("transaction_type") == "partial_payment"
                ):
                    paid_amount += transaction.get("amount", 0.0)
                elif transaction.get("transaction_type") == "refund":
                    paid_amount += transaction.get(
                        "amount", 0.0
                    )  # refund amounts are less than zero
                elif transaction.get("transaction_type") == "charge":
                    paid_amount += transaction.get("amount", 0.0)

        # Determine the difference
        payment_difference = current_total - paid_amount

        # Retrieve the user and verify the payment method
        user = next((u for u in users if u["user_id"] == order["user_id"]), None)
        if not user:
            payload = {"error": "User not found for this order"}
            out = json.dumps(payload)
            return out

        if payment_method_id not in user.get("payment_methods", {}):
            payload = {"error": "Payment method not found for this user"}
            out = json.dumps(payload)
            return out

        # Set up payment_history if it is not already present
        if "payment_history" not in order:
            order["payment_history"] = []

        transaction_type = None
        amount = 0.0
        message = ""

        if (
            abs(payment_difference) < 0.01
        ):  # Practically equal (considering floating point precision)
            message = f"Order total ({current_total:.2f}) matches paid amount ({paid_amount:.2f}). No adjustment needed."
            payload = {
                "success": True,
                "order_id": order_id,
                "current_total": current_total,
                "paid_amount": paid_amount,
                "payment_difference": payment_difference,
                "action": "no_action_needed",
                "message": message,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        elif payment_difference < 0:  # Amount paid exceeds total, requires a refund
            refund_amount = abs(payment_difference)
            transaction_type = "refund"
            amount = -refund_amount  # Negative indicates a refund
            message = f"Refund of ${refund_amount:.2f} processed to payment method {payment_method_id}"

        else:  # payment_difference is greater than 0, requires additional charge
            charge_amount = payment_difference
            transaction_type = "charge"
            amount = charge_amount  # Positive indicates a need for extra charge
            order["status"] = "processing"
            message = f"Additional charge of ${charge_amount:.2f} processed to payment method {payment_method_id}"

        # Generate the transaction record
        transaction = {
            "transaction_type": transaction_type,
            "amount": amount,
            "payment_method_id": payment_method_id,
            "reason": "Order total adjustment",
            "timestamp": get_current_timestamp(),
        }

        # Include the transaction in the payment history
        order["payment_history"].append(transaction)
        payload = {
            "success": True,
            "order_id": order_id,
            "current_total": current_total,
            "paid_amount": paid_amount,
            "payment_difference": payment_difference,
            "action": transaction_type,
            "transaction_amount": amount,
            "payment_method_id": payment_method_id,
            "message": message,
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
                "name": "adjustOrderPayment",
                "description": "Automatically adjusts payment for an order by comparing current order total with paid amount. Creates refund if overpaid or charges additional amount if underpaid.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID to adjust payment for",
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "Payment method ID to use for refund or additional charge",
                        },
                    },
                    "required": ["order_id", "payment_method_id"],
                },
            },
        }
