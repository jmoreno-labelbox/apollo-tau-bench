# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProcessPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, payment_method_source: str, amount: float) -> str:
        """
        Process payment for a customer order following retail rules validation
        """
        # Rule: Validate user identity exists before processing any user requests
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Rule: Payment methods must be valid type: credit_card, paypal, or gift_card with sufficient balance
        payment_methods = user.get("payment_methods", {})
        pay_keys = list(payment_methods.keys())
        for key in pay_keys:
            if payment_method_source in key:
                payment_method = payment_methods[key]

        if not payment_method:
            return json.dumps({"error": f"Payment method {payment_method_source} not found for user", "status": "failed"})

        payment_source = payment_method.get("source")
        if payment_source not in ["credit_card", "paypal", "gift_card"]:
            return json.dumps({"error": f"Invalid payment method type: {payment_source}", "status": "failed"})

        # Rule: Gift card payments cannot exceed available balance - verify balance sufficiency before processing
        if payment_source == "gift_card":
            available_balance = payment_method.get("balance", 0)
            if amount > available_balance:
                print(f"Insufficient gift card balance: {available_balance} for amount: {amount}")
                return json.dumps({
                    "error": f"Insufficient gift card balance. Available: ${available_balance}, Required: ${amount}",
                    "status": "failed"
                })

        # Rule: Credit card payments must validate last_four digits and brand type match user's stored payment methods
        if payment_source == "credit_card":
            brand = payment_method.get("brand")
            last_four = payment_method.get("last_four")
            if not brand or not last_four:
                return json.dumps({"error": "Invalid credit card information", "status": "failed"})

        # Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        verification_required = amount > 1000.0

        # Process payment successfully
        result = {
            "status": "success",
            "user_id": user_id,
            "payment_method_id": payment_method_source,
            "payment_source": payment_source,
            "amount": amount,
            "verification_required": verification_required,
            "transaction_id": f"TXN_{user_id}_{payment_method_source}_{int(amount)}"
        }

        # Add specific details based on payment type
        if payment_source == "gift_card":
            new_balance = payment_method.get("balance", 0) - amount
            result["remaining_gift_card_balance"] = new_balance
        elif payment_source == "credit_card":
            result["card_brand"] = payment_method.get("brand")
            result["card_last_four"] = payment_method.get("last_four")

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_payment",
                "description": "Process customer payment with validation according to retail business rules",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier"},
                        "payment_method_source": {"type": "string", "description": "Payment method identifier from customer's stored methods"},
                        "amount": {"type": "number", "description": "Payment amount in dollars"},

                    },
                    "required": ["user_id", "payment_method_source", "amount"]
                }
            }
        }
